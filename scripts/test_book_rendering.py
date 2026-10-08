import hashlib
import io
import re
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

import build_book


ROOT = Path(__file__).resolve().parents[1]
FILTER = ROOT / "book" / "literal-tokens.lua"
PDF_SOURCE_FORMAT = "markdown+fenced_divs+autolink_bare_uris"
LONG_LINES = """# Wrapping regression

```python
message = "Every sample in the batch must be pre-padded with the same number of image placeholders before replacing them with projected image embeddings."
identifier = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
```

```text
This plain-text code block must also wrap its long lines without losing the final marker: PLAIN_TEXT_END.
```

Further reading: (http://neuralnetworksanddeeplearning.com/). Keep the URL clickable.

- PaddleOCR is mature, fast, and multilingual. One-line usage: `paddleocr.PaddleOCR(lang="en").ocr(image_path)`.
- A long MCP identifier: `params._meta.io.modelcontextprotocol/protocolVersion`.

| Leaderboard | Tracks | URL |
| --- | --- | --- |
| Open ASR Leaderboard | English and multilingual | `huggingface.co/spaces/hf-audio/open_asr_leaderboard` |
| TTS Arena | English TTS | `huggingface.co/spaces/TTS-AGI/TTS-Arena` |
| Escaping | Literal symbols | `{value}#100%_ok` |
| Unicode | Literal multiplication | `k × sr / N` |

| Mistake | Why it is bad | Fix |
| --- | --- | --- |
| Fitting on full data before splitting | Data leakage | Use Pipeline with cross_val_score |
| Feature engineering outside the pipeline | Different transforms at train vs serve | Put all transforms in the Pipeline |
| Not handling unknown categories | Production crash on new values | OneHotEncoder(handle_unknown="ignore") |
| Hardcoded column names | Breaks when features change | Use column lists from config |
| No data validation | Silently wrong predictions | Add schema checks before prediction |
| Training/serving skew | Model sees different features in prod | One Pipeline object for both |
| A long plain identifier | Must remain readable in a narrow table cell | Abcdefghijklmnopqrstuvwxyz0123456789Abcdefghijklmnopqrstuvwxyz0123456789 |
"""


def fixture_book(root, *, localized=False, translated=False):
    phase = "00-setup-and-tooling" if localized else "00-fixture"
    phase_name = "Setup & Tooling" if localized else "Fixture Phase"
    slug = "foundations" if localized else "fixture"
    subtitle = "Math, Tooling, and Classical Machine Learning" if localized else "Math and ML"
    lesson = "01-example"
    phase_dir = root / "phases" / phase
    lesson_docs = phase_dir / lesson / "docs"
    lesson_docs.mkdir(parents=True)
    (phase_dir / "README.md").write_text(f"# Phase 00: {phase_name}\n", encoding="utf-8")
    source = "# Example\n\n## Ship It\n\nThis artifact is reusable.\n\n## Exercises\n\nTry it.\n"
    (lesson_docs / "en.md").write_text(source, encoding="utf-8")
    if translated:
        translated_docs = root / "i18n" / "zh-TW" / "phases" / phase / lesson / "docs"
        translated_docs.mkdir(parents=True)
        (translated_docs / "zh-TW.md").write_text(
            "# 範例\n\n## Ship It｜交付成果\n\n本課的成果。\n\n## Exercises｜練習\n\n試試看。\n",
            encoding="utf-8",
        )
    vol = {
        "slug": slug, "number": 1, "title": "Foundations", "subtitle": subtitle,
        "phases": [phase],
    }
    config = dict(build_book.CONFIG)
    config.update(
        series="AI Engineering from Scratch", site="https://course.test",
        repo="https://repo.test", volumes=[vol],
    )
    return vol, config, phase, lesson, phase_dir / lesson


def render(source, output="html", lua_filter=FILTER):
    return subprocess.run(
        ["pandoc", "--from", "markdown+fenced_divs", "--to", output,
         "--lua-filter", str(lua_filter)],
        input=source, text=True, capture_output=True, check=True,
    ).stdout


class BookRenderingTest(unittest.TestCase):
    def test_literal_tokens_remain_text_in_valid_xhtml(self):
        source = 'Prompt: "<image A> caption <image B>". Replace a name with "<PERSON>".\n\n'
        source += '| Token | Meaning |\n| --- | --- |\n| <image> | Image |\n| <doc A> | Context |\n'
        root = ET.fromstring("<div>" + render(source) + "</div>")
        text = "".join(root.itertext())
        for token in ("<image>", "<image A>", "<image B>", "<PERSON>", "<doc A>"):
            self.assertIn(token, text)

    def test_code_and_real_html_are_unchanged(self):
        source = 'Keep `<image>` and <em>emphasis</em>.\n\n```text\n<PERSON> <doc A>\n```\n'
        result = render(source)
        root = ET.fromstring("<div>" + result + "</div>")
        self.assertEqual(root.find("p/code").text, "<image>")
        self.assertEqual(root.find("p/em").text, "emphasis")
        self.assertEqual(root.find("pre/code").text.strip(), "<PERSON> <doc A>")

    def test_pdf_input_retains_literal_tokens(self):
        result = render('"<image A>" "<PERSON>" "<doc A>"', "latex")
        for token in ("image A", "PERSON", "doc A"):
            self.assertIn(token, result)
        self.assertEqual(result.count(r"\textless"), 3)
        self.assertEqual(result.count(r"\textgreater"), 3)

    def test_table_breaks_only_long_ascii_tokens(self):
        layout = ROOT / "book" / "pdf-layout.lua"
        for token in ("Abcdefghijklmnopqrstuvwxyz0123456789", "package.module.LongIdentifier123"):
            with self.subTest(token=token):
                source = f"| Value |\n| --- |\n| {token} |\n"
                result = render(source, "latex", layout)
                self.assertIn(r"\allowbreak{}", result)
                self.assertIn(token, result.replace(r"\allowbreak{}", ""))
                self.assertEqual(render(source, "html", layout), render(source, "html"))
        for token in ("short/path", "prefix_" + "e\u0301" * 12,
                      "prefix_" + "👩\u200d💻" * 4, "prefix_" + "x\ufe0f" * 12):
            with self.subTest(token=token):
                source = f"| Value |\n| --- |\n| {token} |\n"
                self.assertEqual(render(source, "latex", layout), render(source, "latex"))

    def test_requested_pdf_failure_fails_the_build(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.multiple(build_book, BUILD=Path(directory), DIST=Path(directory)), \
                 patch.object(build_book, "git_date", return_value="2026-09-07"), \
                 patch.object(build_book, "git_edition", return_value="2026.09"), \
                 patch.object(build_book, "pick_font", return_value=None), \
                 patch.object(build_book.subprocess, "run", side_effect=[
                     None, subprocess.CalledProcessError(43, "pandoc"),
                 ]):
                with self.assertRaises(subprocess.CalledProcessError):
                    build_book.render(build_book.CONFIG["volumes"][0], Path("fixture.md"), 1, pdf=True)

    @unittest.skipUnless(shutil.which("xelatex") and shutil.which("pdftotext"),
                         "PDF layout check requires xelatex and pdftotext")
    def test_pdf_long_code_and_urls_stay_inside_margins(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "wrapping.pdf"
            result = subprocess.run(
                ["pandoc", "--from", PDF_SOURCE_FORMAT, "--pdf-engine=xelatex",
                 "--lua-filter", str(ROOT / "book" / "pdf-layout.lua"),
                 "--include-in-header", str(ROOT / "book" / "theme.tex"),
                 "-V", "documentclass=book", "-V", "geometry=margin=1in",
                 "-o", str(pdf)],
                input=LONG_LINES, text=True, capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            bbox = subprocess.check_output(["pdftotext", "-bbox", str(pdf), "-"], text=True)
        root = ET.fromstring(bbox)
        ns = {"x": "http://www.w3.org/1999/xhtml"}
        for page in root.findall(".//x:page", ns):
            right = float(page.attrib["width"]) - 72
            for word in page.findall(".//x:word", ns):
                self.assertGreaterEqual(float(word.attrib["xMin"]), 71, word.text)
                self.assertLessEqual(float(word.attrib["xMax"]), right + 1, word.text)
        text = "".join(word.text or "" for word in root.findall(".//x:word", ns))
        for marker in ("embeddings.", "PLAIN_TEXT_END.", "neuralnetworksanddeeplearning.com",
                       "open_asr_leaderboard", "TTS-Arena", "{value}#100%_ok", "k×sr/N",
                       'paddleocr.PaddleOCR(lang="en").ocr(image_path)', "protocolVersion"):
            self.assertIn(marker, text)
        self.assertIn("OneHotEncoder(handle_unknown=", text)
        self.assertIn("Abcdefghijklmnopqrstuvwxyz0123456789" * 2, text)

    def test_english_assembly_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vol, config, _, _, _ = fixture_book(root)
            build_book.MISSING_BOOK_KEYS.clear()
            build_book.ENGLISH_FALLBACKS.clear()
            with patch.multiple(
                build_book, ROOT=root, PHASES=root / "phases", BUILD=root / "build",
                CONFIG=config, SITE=config["site"], REPO=config["repo"],
                BOOK_LANG="en", BOOK_STRINGS={},
            ):
                md, chapters, _ = build_book.assemble(vol)
            self.assertEqual(chapters, 1)
            self.assertEqual(
                hashlib.sha256(md.read_bytes()).hexdigest(),
                "95e3437e38b7819f34f4cab25ae11eeb89b2c9d3f8027550eaa50f79ad7b5584",
            )

    def test_zh_tw_assembly_and_metadata_are_localized(self):
        strings = build_book.load_book_strings("zh-TW")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vol, config, _, _, _ = fixture_book(root, localized=True, translated=True)
            build_book.MISSING_BOOK_KEYS.clear()
            build_book.ENGLISH_FALLBACKS.clear()
            with patch.multiple(
                build_book, ROOT=root, PHASES=root / "phases", BUILD=root / "build",
                CONFIG=config, SITE=config["site"], REPO=config["repo"],
                BOOK_LANG="zh-TW", BOOK_STRINGS=strings,
            ):
                md, chapters, _ = build_book.assemble(vol)
                metadata = build_book.metadata(vol).read_text(encoding="utf-8")
            text = md.read_text(encoding="utf-8")
            for phrase in (
                "# 關於本卷", "| 卷 | 書名 | 課程階段 |", "# 第 I 部：環境設定與工具",
                "本課交付的成果", "起始程式碼和本課的完整實作", "線上繼續學習",
            ):
                self.assertIn(phrase, text)
            self.assertEqual(chapters, 1)
            self.assertIn('title: "從零打造 AI 工程"', metadata)
            self.assertIn("lang: zh-TW", metadata)
            self.assertIn("toc-title: 目錄", metadata)
            self.assertEqual(build_book.MISSING_BOOK_KEYS, set())
            self.assertEqual(build_book.ENGLISH_FALLBACKS, [])

    def test_build_input_validation_uses_registry_and_git_ref_rules(self):
        build_book.validate_build_inputs("zh-TW", "foundations", "zh-tw/validation")
        invalid = [
            ("xx", "foundations", "translations"),
            ("zh-TW", "missing-volume", "translations"),
            ("zh-TW", "foundations", "../../main"),
            ("zh-TW", "foundations", "bad..ref"),
            ("zh-TW", "foundations", "-option"),
            ("zh-TW", "foundations", "refs/heads/translations"),
            ("zh-TW", "foundations", "branch;echo"),
            ("zh-TW", "foundations", "branch with space"),
            ("zh-TW", "foundations", "branch\\\\name"),
            ("zh-TW", "foundations", "a" * 256),
        ]
        for values in invalid:
            with self.subTest(values=values), self.assertRaises(ValueError):
                build_book.validate_build_inputs(*values)

    def test_book_workflow_validates_env_inputs_without_shell_interpolation(self):
        workflow = (ROOT / ".github" / "workflows" / "build-book.yml").read_text(encoding="utf-8")
        lines = workflow.splitlines()
        run_lines = []
        for index, line in enumerate(lines):
            if not re.match(r"^\s+run:", line):
                continue
            indent = len(line) - len(line.lstrip())
            run_lines.append(line)
            for following in lines[index + 1:]:
                if following.strip() and len(following) - len(following.lstrip()) <= indent:
                    break
                run_lines.append(following)
        self.assertNotIn("${{", "\n".join(run_lines))
        self.assertIn("BOOK_LANG: ${{ github.event.inputs.lang || (github.ref_name == 'zh-tw/validation' && 'zh-TW') || 'en' }}", workflow)
        self.assertIn("BOOK_VOLUME: ${{ github.event.inputs.volume || (github.ref_name == 'zh-tw/validation' && 'foundations') || 'all' }}", workflow)
        self.assertIn("TRANSLATIONS_REF: ${{ github.event.inputs.translations_ref || (github.ref_name == 'zh-tw/validation' && github.ref_name) || 'translations' }}", workflow)
        self.assertIn("--validate-inputs", workflow)
        self.assertIn('git archive FETCH_HEAD "i18n/$BOOK_LANG" | tar -x', workflow)
        self.assertIn("BUILD_PDF: ${{ github.event_name != 'push' || github.ref_name == 'zh-tw/validation' }}", workflow)
        self.assertIn("branches: [main, zh-tw/validation]", workflow)
        self.assertIn('"i18n/zh-TW/**"', workflow)
        self.assertIn("env.BOOK_LANG == 'zh-TW'", workflow)
        self.assertIn("args+=(--pdf)", workflow)
        self.assertIn("name: book-epub-${{ env.BOOK_LANG }}", workflow)
        self.assertIn("name: book-pdf-${{ env.BOOK_LANG }}", workflow)

    def test_missing_translation_is_listed_as_english_fallback(self):
        strings = build_book.load_book_strings("zh-TW")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, config, phase, lesson, lesson_dir = fixture_book(root, localized=True)
            build_book.ENGLISH_FALLBACKS.clear()
            with patch.multiple(
                build_book, ROOT=root, BOOK_LANG="zh-TW", BOOK_STRINGS=strings,
            ):
                source = build_book._lesson_source(phase, lesson)
            self.assertEqual(source, lesson_dir / "docs" / "en.md")
            self.assertEqual(build_book.ENGLISH_FALLBACKS, [f"phases/{phase}/{lesson}"])

    def test_missing_book_string_falls_back_and_is_reported(self):
        vol = {"slug": "foundations"}
        build_book.MISSING_BOOK_KEYS.clear()
        build_book.ENGLISH_FALLBACKS.clear()
        with patch.multiple(build_book, BOOK_LANG="zh-TW", BOOK_STRINGS={}):
            self.assertEqual(build_book.book_text("missing.key", "English default"), "English default")
            output = io.StringIO()
            with redirect_stderr(output):
                build_book.report_fallbacks(vol)
        self.assertIn("missing.key", output.getvalue())

    def test_english_titlepage_is_byte_identical(self):
        with patch.multiple(build_book, BOOK_LANG="en", BOOK_STRINGS={}):
            with patch.object(build_book, "git_edition", return_value="2026.10"):
                titlepage = build_book.titlepage_content(build_book.CONFIG["volumes"][0], 3)
        self.assertEqual(
            hashlib.sha256(titlepage.encode("utf-8")).hexdigest(),
            "faf0924ca7570026d3205a2a21afaebda3ddb53f23a3dae974d4aac4e58a14c9",
        )

    def test_zh_tw_pdf_localizes_cover_and_chapter_and_sets_cjk_mono_font(self):
        strings = build_book.load_book_strings("zh-TW")
        vol = build_book.CONFIG["volumes"][0]
        build_book.MISSING_BOOK_KEYS.clear()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "build").mkdir()
            with patch.multiple(
                build_book, BUILD=root / "build", DIST=root / "dist",
                BOOK_LANG="zh-TW", BOOK_STRINGS=strings,
            ), patch.object(build_book, "git_date", return_value="2026-10-07"), \
                 patch.object(build_book, "git_edition", return_value="2026.10"), \
                 patch.object(build_book, "pick_font", return_value="Noto Sans CJK TC"), \
                 patch.object(build_book.subprocess, "run") as run:
                build_book.render(vol, Path("fixture.md"), 3, pdf=True)
            titlepage = (root / "build" / "foundations-titlepage.tex").read_text(encoding="utf-8")
            theme = (root / "build" / "foundations-theme.tex").read_text(encoding="utf-8")
            pdf_command = run.call_args_list[1].args[0]
            self.assertIn("參考手冊", titlepage)
            self.assertIn("從零打造", titlepage)
            self.assertIn("第 001 卷", titlepage)
            self.assertNotIn("@REFERENCE_MANUAL@", titlepage)
            self.assertIn(r"\newcommand{\bookchapterprefix}{第 }", theme)
            self.assertIn(r"\bookchapterprefix\thechapter\bookchaptersuffix", theme)
            self.assertIn("CJKmonofont=Noto Sans CJK TC", pdf_command)
            self.assertIn("lang=zh-TW", pdf_command)
            self.assertEqual(build_book.MISSING_BOOK_KEYS, set())


if __name__ == "__main__":
    unittest.main()
