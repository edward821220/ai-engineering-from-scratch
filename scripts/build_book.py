#!/usr/bin/env python3
"""Assemble course lessons into book volumes and render them with pandoc.

Usage:
    python3 scripts/build_book.py                 # assemble + epub for all volumes
    python3 scripts/build_book.py --volume language
    python3 scripts/build_book.py --pdf           # also render PDF (xelatex)
    python3 scripts/build_book.py --assemble-only # markdown only, no pandoc

The book is deliberately a companion to the repo and the website, not a
replacement. Interactive figures, quizzes, and runnable code stay online;
every chapter ends with the links that take the reader there.
"""

import argparse
import functools
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_catalog import LESSON_DIR_RE, read_h1, slug_to_title  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PHASES = ROOT / "phases"
BUILD = ROOT / "book" / "_build"
DIST = ROOT / "dist" / "book"

CONFIG = json.loads((ROOT / "book" / "volumes.json").read_text(encoding="utf-8"))
SITE = CONFIG["site"].rstrip("/")
REPO = CONFIG["repo"].rstrip("/")

FENCE = re.compile(r"^```")
ASSET_IMG = re.compile(r"\]\(\.\./assets/")
HEADING2 = re.compile(r"^## ")

MERMAID_OK = shutil.which("mmdc") is not None
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]


def lesson_dirs(phase):
    base = PHASES / phase
    if not base.is_dir():
        return []
    return [
        d
        for d in sorted(base.iterdir())
        if d.is_dir() and LESSON_DIR_RE.match(d.name) and (d / "docs" / "en.md").is_file()
    ]


def phase_title(phase):
    title = read_h1(PHASES / phase / "README.md") or slug_to_title(phase.split("-", 1)[-1])
    if BOOK_LANG == "en":
        return title
    return book_text(f"phase.{phase}", clean_phase_title(title))


def urls_for(phase, lesson):
    rel = f"phases/{phase}/{lesson}"
    return {
        "web": f"{SITE}/lesson?path={rel}",
        "code": f"{REPO}/tree/main/{rel}/code",
        "repo": f"{REPO}/tree/main/{rel}",
    }


def fenced_div(cls, *lines):
    return ["", "::: {." + cls + "}", *lines, ":::", ""]


def continue_box(u, has_quiz):
    lines = [
        book_text(
            "continue.heading",
            "**Continue online.** The living edition of this chapter has more than the page can hold:",
        ),
        "",
        book_text(
            "continue.figures", "- Animated, interactive figures and the web text: <{web}>",
            web=u["web"],
        ),
        book_text("continue.code", "- Runnable code for every step: <{code}>", code=u["code"]),
    ]
    if has_quiz:
        lines.append(book_text("continue.quiz", "- The chapter quiz, graded in the browser: <{web}>", web=u["web"]))
    lines += [
        "",
        book_text(
            "continue.repo-note",
            "The repository moves faster than any printing. When the book and the repo disagree, trust the repo.",
        ),
    ]
    return fenced_div("continue-online", *lines)


def fence_end(src, i):
    """Index of the line that closes the fence opened at src[i] (len(src) if unclosed)."""
    j = i + 1
    while j < len(src) and src[j].strip() != "```":
        j += 1
    return j


BOOK_LANG = "en"
BOOK_STRINGS = {}
MISSING_BOOK_KEYS = set()
ENGLISH_FALLBACKS = []


def load_book_strings(lang):
    if lang == "en":
        return {}
    path = ROOT / "book" / "i18n" / f"{lang}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def book_text(key, default, **values):
    value = BOOK_STRINGS.get(key) if BOOK_LANG != "en" else default
    if not isinstance(value, str):
        if BOOK_LANG != "en":
            MISSING_BOOK_KEYS.add(key)
        value = default
    return value.format(**values) if values else value


def series_title():
    return book_text("series.title", CONFIG["series"])


def volume_title(vol):
    return book_text(f"volume.{vol['slug']}.title", vol["title"])


def volume_subtitle(vol):
    return book_text(f"volume.{vol['slug']}.subtitle", vol["subtitle"])


def validate_build_inputs(lang, volume, translations_ref):
    languages = json.loads((ROOT / "languages.json").read_text(encoding="utf-8"))
    language_codes = {entry["code"] for entry in languages["languages"]}
    volume_slugs = {entry["slug"] for entry in CONFIG["volumes"]}
    if lang not in language_codes:
        raise ValueError(f"unknown language: {lang}")
    if volume != "all" and volume not in volume_slugs:
        raise ValueError(f"unknown volume: {volume}")
    if (not translations_ref or len(translations_ref) > 255 or translations_ref.startswith("refs/")
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", translations_ref)):
        raise ValueError("translations_ref must be a short branch name")
    checked = subprocess.run(
        ["git", "check-ref-format", "--branch", translations_ref],
        capture_output=True, text=True,
    )
    if checked.returncode:
        raise ValueError("translations_ref is not a valid Git branch name")


def _lesson_source(phase, lesson):
    en = ROOT / "phases" / phase / lesson / "docs" / "en.md"
    if BOOK_LANG != "en":
        tr = ROOT / "i18n" / BOOK_LANG / "phases" / phase / lesson / "docs" / f"{BOOK_LANG}.md"
        if tr.is_file():
            return tr
        ENGLISH_FALLBACKS.append(f"phases/{phase}/{lesson}")
    return en


def transform_lesson(phase, lesson_dir):
    lesson = lesson_dir.name
    u = urls_for(phase, lesson)
    has_quiz = (lesson_dir / "quiz.json").is_file()
    src = _lesson_source(phase, lesson).read_text(encoding="utf-8").splitlines()

    out = []
    balanced = True
    i = 0
    while i < len(src):
        line = src[i]

        if FENCE.match(line):
            end = fence_end(src, i)
            if end >= len(src):
                balanced = False
            info = line[3:].strip()
            block = src[i + 1 : end]
            if info == "figure":
                fig_id = block[0].strip() if block else "figure"
                out += fenced_div(
                    "interactive-figure",
                    book_text(
                        "figure.interactive",
                        "**Interactive figure: `{id}`.** This one moves. Watch it animate and drag its controls in the web edition: <{web}>",
                        id=fig_id, web=u["web"],
                    ),
                )
            elif info == "mermaid":
                rendered = render_mermaid(block)
                if rendered:
                    out += ["", f"![{book_text('figure.alt', 'diagram')}]({rendered})", ""]
                else:
                    out += fenced_div(
                        "interactive-figure",
                        book_text(
                            "figure.mermaid", "**Diagram.** Rendered live in the web edition: <{web}>",
                            web=u["web"],
                        ),
                    )
            else:
                out += src[i : end + 1]
            i = end + 1
            continue

        if line.startswith("## Ship It"):
            out += fenced_div(
                "continue-online",
                book_text(
                    "ship-it.box",
                    "**This chapter ships an artifact.** The course version of this lesson produces a reusable prompt or agent skill. It lives in the repository, ready to install: <{repo}>",
                    repo=u["repo"],
                ),
            )
            i += 1
            while i < len(src):
                if FENCE.match(src[i]):
                    end = fence_end(src, i)
                    if end >= len(src):
                        balanced = False
                    i = end + 1
                    continue
                if HEADING2.match(src[i]):
                    break
                i += 1
            continue

        if line.startswith("## Exercises"):
            out.append(line)
            out.append("")
            out.append(book_text(
                "exercises.starter", "Starter code and the lesson's working implementation: <{code}>",
                code=u["code"],
            ))
            i += 1
            continue

        out.append(ASSET_IMG.sub(f"](phases/{phase}/{lesson}/assets/", line))
        i += 1

    if not balanced:
        raise ValueError(f"unbalanced code fence in {lesson_dir / 'docs' / 'en.md'}")

    out += continue_box(u, has_quiz)
    return out


@functools.lru_cache(maxsize=None)
def font_families():
    if not shutil.which("fc-list"):
        return frozenset()
    r = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True)
    return frozenset(
        fam.strip() for fam_line in r.stdout.splitlines() for fam in fam_line.split(",")
    )


def pick_font(candidates):
    families = font_families()
    for c in candidates:
        if c in families:
            return c
    return None


def render_mermaid(block):
    if not MERMAID_OK:
        return None
    assets = BUILD / "diagrams"
    assets.mkdir(parents=True, exist_ok=True)
    stem = hashlib.sha1("\n".join(block).encode()).hexdigest()[:16]
    svg = assets / f"{stem}.svg"
    if svg.is_file():
        return str(svg.relative_to(ROOT))
    mmd = assets / f"{stem}.mmd"
    mmd.write_text("\n".join(block), encoding="utf-8")
    try:
        subprocess.run(
            ["mmdc", "-i", str(mmd), "-o", str(svg), "-b", "transparent", "--quiet"],
            check=True, capture_output=True, timeout=60,
        )
        return str(svg.relative_to(ROOT))
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or b"").decode(errors="replace").strip()[:300]
        print(f"warning: mermaid render failed for {mmd.name}: {detail}", file=sys.stderr)
        return None
    except subprocess.TimeoutExpired:
        print(f"warning: mermaid render timed out for {mmd.name}", file=sys.stderr)
        return None


@functools.lru_cache(maxsize=None)
def git_date():
    return subprocess.run(
        ["git", "log", "-1", "--format=%cs"], capture_output=True, text=True, cwd=ROOT
    ).stdout.strip()


@functools.lru_cache(maxsize=None)
def git_edition():
    return subprocess.run(
        ["git", "log", "-1", "--format=%cd", "--date=format:%Y.%m"],
        capture_output=True, text=True, cwd=ROOT,
    ).stdout.strip() or "0000.00"


@functools.lru_cache(maxsize=None)
def titlepage_template():
    return (ROOT / "book" / "titlepage.tex").read_text(encoding="utf-8")


def titlepage_content(vol, chapters):
    number = f"{vol['number']:03d}"
    replacements = {
        "@VOLMARK@": book_text("titlepage.volume-mark", "VOL\\_{number}", number=number),
        "@REFERENCE_MANUAL@": book_text("titlepage.reference-manual", "REFERENCE\\ MANUAL"),
        "@SERIES_TITLE_TOP@": book_text("series.title.top", "AI\\ ENGINEERING"),
        "@SERIES_TITLE_BOTTOM@": book_text("series.title.bottom", "FROM\\ SCRATCH."),
        "@OPEN_SOURCE@": book_text("titlepage.open-source", "OPEN\\ SOURCE"),
        "@MIT_LICENSE@": book_text("titlepage.mit-license", "MIT\\ LICENSE"),
        "@VOLUME_PREFIX@": book_text("titlepage.volume-prefix", "VOLUME"),
        "@VOLUME_SUFFIX@": book_text("titlepage.volume-suffix", ""),
        "@CHAPTERS_LABEL@": book_text("titlepage.chapters-label", "CHAPTERS"),
        "@PHASES_LABEL@": book_text("titlepage.phases-label", "PHASES"),
        "@EDITION_LABEL@": book_text("titlepage.edition-label", "EDITION"),
        "@LIVING_COURSE_LABEL@": book_text("titlepage.living-course-label", "A SNAPSHOT OF A LIVING COURSE"),
        "@NEWEST_BUILD_LABEL@": book_text("titlepage.newest-build-label", "NEWEST BUILD ALWAYS AT THE LINK BELOW"),
        "@ROMAN@": ROMAN[vol["number"] - 1],
        "@TOTALVOL@": ROMAN[len(CONFIG["volumes"]) - 1],
        "@CHAPTERS@": str(chapters),
        "@PHASES@": "\\ \\textperiodcentered\\ ".join(p.split("-")[0] for p in vol["phases"]),
        "@EDITION@": git_edition(),
        "@TITLE@": volume_title(vol),
        "@SUBTITLE@": volume_subtitle(vol),
    }
    template = titlepage_template()
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    return template


def theme_file(vol):
    BUILD.mkdir(parents=True, exist_ok=True)
    theme = (ROOT / "book" / "theme.tex").read_text(encoding="utf-8")
    prefix = book_text("chapter.prefix", "CHAPTER ")
    suffix = book_text("chapter.suffix", "")
    theme = theme.replace(
        r"\newcommand{\bookchapterprefix}{CHAPTER }",
        "\\newcommand{\\bookchapterprefix}{" + prefix + "}",
    )
    theme = theme.replace(
        r"\newcommand{\bookchaptersuffix}{}",
        "\\newcommand{\\bookchaptersuffix}{" + suffix + "}",
    )
    path = BUILD / f"{vol['slug']}-theme.tex"
    path.write_text(theme, encoding="utf-8")
    return path


def clean_phase_title(raw):
    return re.sub(r"^Phase\s+\d+\s*[:—-]\s*", "", raw).strip()


def series_map(vol):
    rows = []
    for v in CONFIG["volumes"]:
        marker = "**" if v["slug"] == vol["slug"] else ""
        phases = ", ".join(p.split("-")[0] for p in v["phases"])
        title, subtitle = volume_title(v), volume_subtitle(v)
        rows.append(
            f"| {marker}{v['number']}{marker} | {marker}{title}{marker} — {subtitle} | {phases} |"
        )
    headers = [
        book_text("front.series-map.volume", "Vol"),
        book_text("front.series-map.title", "Title"),
        book_text("front.series-map.phases", "Course phases"),
    ]
    return "\n".join(["| " + " | ".join(headers) + " |", "|-----|-------|---------------|"] + rows)


def how_to_use(vol):
    series = series_title()
    title = volume_title(vol)
    number = vol["number"]
    phases = ", ".join(p.split("-")[0] for p in vol["phases"])
    index = f"{SITE}/llms.txt"
    return f"""# {book_text('front.about-volume.heading', 'About This Volume')} {{.unnumbered}}

{book_text(
    'front.about-volume.body',
    'This is Volume {number} of *{series}*, a six-volume compilation of the open course of the same name. Each volume stands alone; cross-references cite course phase numbers, which map to volumes like this:',
    number=number, series=series,
)}

{series_map(vol)}

{book_text(
    'front.chapters.body',
    'The chapters in this volume come from course phases {phases}. Chapter prerequisites name phases, not volumes; use the table above to translate.',
    phases=phases,
)}

# {book_text('front.how-to-use.heading', 'How to Use This Book')} {{.unnumbered}}

{book_text('front.how-to-use.intro', 'This volume is one loop of a larger machine, and it works best when you run the whole loop:')}

1. {book_text(
    'front.how-to-use.read',
    '**Read the chapter here.** The prose, the derivations, and the code walkthroughs are complete on the page.',
)}
2. {book_text(
    'front.how-to-use.run',
    '**Run the code from the repository.** Every chapter has a `code/` directory with a working implementation you can run and break: <{repo}>',
    repo=REPO,
)}
3. {book_text(
    'front.how-to-use.web',
    '**Open the web edition for what paper cannot do.** Animated figures you can watch and drag, and a quiz per chapter that grades itself: <{site}>',
    site=SITE,
)}

{book_text(
    'front.repository.note',
    'The repository is the living edition. Lessons are updated as the field moves; the book is a snapshot with a version number. When they disagree, the repo is right.',
)}

## {book_text('front.learning-with-ai.heading', 'Learning with an AI')} {{.unnumbered}}

{book_text(
    'front.learning-with-ai.body',
    'This course is built to be read by agents as well as people. The machine-readable index of every lesson lives at <{index}>. If you learn with an AI assistant, paste this and go:',
    index=index,
)}

> {book_text(
    'front.learning-with-ai.prompt',
    'I am working through *{series}, Volume {number}: {title}*. Fetch {index}, find the lesson I name, and act as my tutor: quiz me on its Key Terms, review my solutions to its Exercises, and walk me through its code from the repository.',
    series=series, number=number, title=title, index=index,
)}
"""


def assemble(vol):
    BUILD.mkdir(parents=True, exist_ok=True)
    parts = [how_to_use(vol)]
    chapters = 0
    for part_idx, phase in enumerate(vol["phases"]):
        title = clean_phase_title(phase_title(phase))
        parts.append(
            f"\n# {book_text('part.heading', 'Part {roman} — {title}', roman=ROMAN[part_idx], title=title)} {{.unnumbered .part}}\n\n"
            f"*{book_text('phase.intro', 'Course phase {number}. Live edition with animated figures and quizzes: <{catalog}>', number=phase.split('-')[0], catalog=f'{SITE}/catalog.html')}*\n"
        )
        for lesson_dir in lesson_dirs(phase):
            parts.append("\n".join(transform_lesson(phase, lesson_dir)))
            chapters += 1
    text = "\n\n".join(parts)
    md = BUILD / f"{vol['slug']}.md"
    md.write_text(text, encoding="utf-8")
    return md, chapters, len(text.split())


def metadata(vol):
    meta = BUILD / f"{vol['slug']}-meta.yaml"
    subtitle = book_text(
        "metadata.subtitle",
        "Volume {number} — {title}: {subtitle}",
        number=vol["number"], title=volume_title(vol), subtitle=volume_subtitle(vol),
    )
    meta.write_text(
        "---\n"
        f"title: \"{series_title()}\"\n"
        f"subtitle: \"{subtitle}\"\n"
        f"author: \"{CONFIG['author']}\"\n"
        f"lang: {BOOK_LANG}\n"
        f"toc-title: {book_text('toc.title', 'Contents')}\n"
        "---\n",
        encoding="utf-8",
    )
    return meta


def render(vol, md, chapters, pdf=False):
    DIST.mkdir(parents=True, exist_ok=True)
    meta = metadata(vol)
    suffix = "" if BOOK_LANG == "en" else f"-{BOOK_LANG}"
    epub = DIST / f"aiefs-vol{vol['number']}-{vol['slug']}{suffix}.epub"
    cmd = [
        "pandoc", str(meta), str(md),
        "-o", str(epub),
        "--from", "markdown+fenced_divs",
        "--lua-filter", str(ROOT / "book" / "literal-tokens.lua"),
        "--toc", "--toc-depth=1",
        "--top-level-division=chapter",
        "--css", str(ROOT / "book" / "epub.css"),
        "--resource-path", str(ROOT),
        "--metadata", f"date={git_date()}",
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)
    results = [epub]
    if pdf and BOOK_LANG in ("ar", "fa", "ur", "he"):
        # right-to-left scripts need a bidi engine + Arabic/Hebrew fonts that the
        # xelatex theme does not ship; the EPUB (above) handles RTL natively, so
        # skip the PDF rather than emit a broken left-to-right one.
        print(f"note: skipping {BOOK_LANG} PDF for {vol['slug']} (RTL not wired for PDF); EPUB produced", file=sys.stderr)
        pdf = False
    if pdf:
        titlepage = BUILD / f"{vol['slug']}-titlepage.tex"
        titlepage.write_text(titlepage_content(vol, chapters), encoding="utf-8")
        pdf_out = DIST / f"aiefs-vol{vol['number']}-{vol['slug']}{suffix}.pdf"
        cmd_pdf = [
            "pandoc", str(md),
            "-o", str(pdf_out),
            "--from", "markdown+fenced_divs+autolink_bare_uris",
            "--lua-filter", str(ROOT / "book" / "literal-tokens.lua"),
            "--lua-filter", str(ROOT / "book" / "pdf-layout.lua"),
            "--toc", "--toc-depth=1",
            "--top-level-division=chapter",
            "--pdf-engine=xelatex",
            "--columns=40",
            "--resource-path", str(ROOT),
            "--include-in-header", str(theme_file(vol)),
            "--include-before-body", str(titlepage),
            "-M", f"title-meta={book_text('metadata.pdf-title', '{series} Volume {number}: {title}', series=series_title(), number=vol['number'], title=volume_title(vol))}",
            "-M", "author-meta=aiengineeringfromscratch.com",
            "-M", f"lang={BOOK_LANG}",
            "-V", f"toc-title={book_text('toc.title', 'Contents')}",
            "-V", "documentclass=book",
            "-V", "classoption=oneside,openany",
            "-V", "geometry=margin=1in",
            "-V", "fontsize=10pt",
        ]
        serif = pick_font(["DejaVu Serif", "STIX Two Text", "Georgia"])
        mono = pick_font(["DejaVu Sans Mono", "Menlo", "Consolas"])
        if serif:
            cmd_pdf += ["-V", f"mainfont={serif}"]
        if mono:
            cmd_pdf += ["-V", f"monofont={mono}"]
        # CJK scripts need a matching font; DejaVu already covers
        # Latin/Cyrillic/Greek/Devanagari for the other languages.
        cjk_candidates = {
            "zh": ["Noto Sans CJK SC", "Noto Serif CJK SC", "Source Han Serif SC"],
            "zh-TW": ["Noto Sans CJK TC", "Noto Serif CJK TC", "Source Han Serif TC"],
            "ja": ["Noto Sans CJK JP", "Noto Serif CJK JP", "Source Han Serif JP"],
            "ko": ["Noto Sans CJK KR", "Noto Serif CJK KR", "Source Han Serif KR"],
        }
        if BOOK_LANG in cjk_candidates:
            cjk = pick_font(cjk_candidates[BOOK_LANG])
            if cjk:
                cmd_pdf += ["-V", f"CJKmainfont={cjk}", "-V", f"CJKmonofont={cjk}"]
        subprocess.run(cmd_pdf, check=True, cwd=ROOT)
        results.append(pdf_out)
    return results


def check_phases():
    claimed = set()
    for vol in CONFIG["volumes"]:
        for phase in vol["phases"]:
            claimed.add(phase)
            if not (PHASES / phase).is_dir() or not lesson_dirs(phase):
                sys.exit(f"volume {vol['slug']}: phase {phase} is missing or has no lessons")
    for d in sorted(PHASES.iterdir()):
        if d.is_dir() and d.name not in claimed:
            print(f"warning: phase directory {d.name} is not claimed by any volume", file=sys.stderr)


def report_fallbacks(vol):
    if BOOK_LANG == "en":
        return
    if MISSING_BOOK_KEYS:
        print(
            f"warning: missing {BOOK_LANG} book strings for {vol['slug']}; using English: "
            + ", ".join(sorted(MISSING_BOOK_KEYS)),
            file=sys.stderr,
        )
    if ENGLISH_FALLBACKS:
        print(f"warning: {BOOK_LANG} lessons fell back to English for {vol['slug']}:", file=sys.stderr)
        for lesson in ENGLISH_FALLBACKS:
            print(f"  {lesson}", file=sys.stderr)
    else:
        print(f"{BOOK_LANG} English lesson fallbacks for {vol['slug']}: none", file=sys.stderr)


def main():
    global BOOK_LANG, BOOK_STRINGS
    ap = argparse.ArgumentParser()
    ap.add_argument("--volume", help="build one volume by slug")
    ap.add_argument("--pdf", action="store_true", help="also render PDF via xelatex")
    ap.add_argument("--assemble-only", action="store_true", help="skip pandoc")
    ap.add_argument("--lang", default="en",
                    help="build a translated edition from i18n/<lang>/ (English fallback per lesson)")
    ap.add_argument("--validate-inputs", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--translations-ref", default="translations", help=argparse.SUPPRESS)
    args = ap.parse_args()
    try:
        validate_build_inputs(args.lang, args.volume or "all", args.translations_ref)
    except ValueError as exc:
        sys.exit(str(exc))
    BOOK_LANG = args.lang
    BOOK_STRINGS = load_book_strings(BOOK_LANG)

    if args.validate_inputs:
        print("build inputs valid")
        return

    check_phases()

    vols = CONFIG["volumes"]
    if args.volume:
        vols = [v for v in vols if v["slug"] == args.volume]
        if not vols:
            sys.exit(f"unknown volume: {args.volume}")

    for vol in vols:
        MISSING_BOOK_KEYS.clear()
        ENGLISH_FALLBACKS.clear()
        md, chapters, words = assemble(vol)
        print(f"vol {vol['number']} {vol['slug']}: {chapters} chapters, {words:,} words -> {md}")
        if not args.assemble_only:
            for artifact in render(vol, md, chapters, pdf=args.pdf):
                size = artifact.stat().st_size // 1024
                print(f"  {artifact} ({size} KB)")
        report_fallbacks(vol)


if __name__ == "__main__":
    main()
