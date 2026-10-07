#!/usr/bin/env python3
"""Contract tests for the local zh-TW translation checker."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_translation.py"
sys.path.insert(0, str(ROOT / "scripts"))
from check_translation import check_document, parse_glossary, parse_glossary_rows

SOURCE = """# Demo Lesson

> A short hook.

**Type:** Learn
**Languages:** Python
**Prerequisites:** None
**Time:** ~30 minutes

## Learning Objectives

- Explain `token` use.

## The Problem

A plain source paragraph.

```python
print(1)
```

## Build It

Use $x + y$ and [the guide](https://example.com/guide).

| Term | Meaning |
| --- | --- |
| token | A unit |

```mermaid
graph TD
    A[Source label] --> B[Target label]
```

```figure
figure-id
```
"""

TRANSLATION = """# 示範課程

> 簡短引言。

**Type:** Learn
**Languages:** Python
**Prerequisites:** None
**Time:** ~30 minutes

## Learning Objectives｜學習目標

- 說明 `token` 的用途。

## The Problem｜問題

一段原始文字。

```python
print(1)
```

## Build It｜動手實作

使用 $x + y$ 和 [指南](https://example.com/guide)。

| 術語 | 意義 |
| --- | --- |
| token | 一個單位 |

```mermaid
graph TD
    A[來源標籤] --> B[目標標籤]
```

```figure
figure-id
```
"""


class TranslationDocumentTest(unittest.TestCase):
    def test_aligned_translation_passes_and_returns_no_findings(self) -> None:
        self.assertEqual([], check_document(SOURCE, TRANSLATION))

    def test_code_fence_must_match_verbatim(self) -> None:
        altered = TRANSLATION.replace("print(1)", "print(2)")
        self.assert_has_finding(check_document(SOURCE, altered), "fence")

    def test_inline_code_and_math_must_match(self) -> None:
        altered_code = TRANSLATION.replace("`token`", "`tokens`")
        self.assert_has_finding(check_document(SOURCE, altered_code), "protected")
        altered_math = TRANSLATION.replace("$x + y$", "$x - y$")
        self.assert_has_finding(check_document(SOURCE, altered_math), "protected")

    def test_link_text_may_translate_but_target_must_not_change(self) -> None:
        self.assertEqual([], check_document(SOURCE, TRANSLATION))
        altered = TRANSLATION.replace("https://example.com/guide", "https://example.com/other")
        self.assert_has_finding(check_document(SOURCE, altered), "protected")

    def test_metadata_header_must_remain_exact(self) -> None:
        altered = TRANSLATION.replace("**Time:** ~30 minutes", "**Time:** 約 30 分鐘")
        self.assert_has_finding(check_document(SOURCE, altered), "metadata")

    def test_mermaid_labels_may_translate_but_node_ids_and_edges_must_match(self) -> None:
        translated_labels = TRANSLATION.replace("A[來源標籤] --> B[目標標籤]", "A[起點] --> B[終點]")
        self.assertEqual([], check_document(SOURCE, translated_labels))
        altered_node = TRANSLATION.replace("B[目標標籤]", "C[目標標籤]")
        self.assert_has_finding(check_document(SOURCE, altered_node), "mermaid")
        altered_edge = TRANSLATION.replace("A[來源標籤] --> B", "A[來源標籤] -.-> B")
        self.assert_has_finding(check_document(SOURCE, altered_edge), "mermaid")

    def test_figure_block_must_remain_verbatim(self) -> None:
        altered = TRANSLATION.replace("figure-id", "different-figure")
        self.assert_has_finding(check_document(SOURCE, altered), "figure")

    def test_fixed_heading_requires_original_english_prefix_and_chinese_label(self) -> None:
        valid = TRANSLATION.replace("## Build It｜動手實作", "## Build It｜實作")
        self.assertEqual([], check_document(SOURCE, valid))
        invalid = TRANSLATION.replace("## Build It｜動手實作", "## 動手實作")
        self.assert_has_finding(check_document(SOURCE, invalid), "heading")
        empty = TRANSLATION.replace("## Build It｜動手實作", "## Build It｜")
        self.assert_has_finding(check_document(SOURCE, empty), "heading")

    def test_heading_levels_and_paragraph_counts_must_match(self) -> None:
        changed_level = TRANSLATION.replace("## The Problem｜問題", "### The Problem｜問題")
        self.assert_has_finding(check_document(SOURCE, changed_level), "structure")
        removed_paragraph = TRANSLATION.replace("\n一段原始文字。\n", "\n")
        self.assert_has_finding(check_document(SOURCE, removed_paragraph), "structure")

    def test_list_item_count_and_table_shape_must_match(self) -> None:
        extra_list_item = TRANSLATION.replace("- 說明 `token` 的用途。", "- 說明 `token` 的用途。\n- 另一項。")
        self.assert_has_finding(check_document(SOURCE, extra_list_item), "structure")
        extra_table_cell = TRANSLATION.replace("| 術語 | 意義 |", "| 術語 | 意義 | 備註 |")
        self.assert_has_finding(check_document(SOURCE, extra_table_cell), "structure")

    def test_simplified_only_characters_are_checked_outside_protected_spans(self) -> None:
        simplified = TRANSLATION.replace("一段原始文字。", "这段原始文字。")
        self.assert_has_finding(check_document(SOURCE, simplified), "simplified")
        source_with_code = SOURCE.replace("`token`", "`这`", 1)
        target_with_code = TRANSLATION.replace("`token`", "`这`", 1)
        self.assertEqual([], check_document(source_with_code, target_with_code))

    def test_high_confidence_mainland_terms_fail_but_ambiguous_terms_do_not(self) -> None:
        mainland = TRANSLATION.replace("一段原始文字。", "這段數據需要處理。")
        self.assert_has_finding(check_document(SOURCE, mainland), "mainland")
        ambiguous = TRANSLATION.replace("一段原始文字。", "這段配置很清楚。")
        self.assertEqual([], check_document(SOURCE, ambiguous))
        shared_traditional = TRANSLATION.replace("一段原始文字。", "皇后就在 3 公里外，只有一個人；兩者互相呼應。")
        self.assertEqual([], check_document(SOURCE, shared_traditional))

    def test_glossary_forbidden_variants_are_reported_with_lesson_path(self) -> None:
        glossary = """| English | 譯法 | 保留英文 | 禁用 | 備註 |
| --- | --- | --- | --- | --- |
| token | token | 是 | 詞元、令牌 | keep English |
"""
        findings = check_document(
            SOURCE,
            TRANSLATION.replace("一段原始文字。", "這個詞元很重要。"),
            glossary_text=glossary,
            lesson="phases/00-demo/01-example",
        )
        self.assert_has_finding(findings, "詞元")
        self.assertTrue(any("phases/00-demo/01-example" in finding for finding in findings))

    def test_glossary_parser_reads_forbidden_columns(self) -> None:
        glossary = """| English | 譯法 | 保留英文 | 禁用 | 備註 |
| --- | --- | --- | --- | --- |
| token | token | 是 | 詞元、令牌 | keep English |
| data | 資料 | 否 | — | no forbidden variant |
"""
        entries = parse_glossary(glossary)
        self.assertEqual([("token", "詞元"), ("token", "令牌")], entries)
        self.assertEqual(2, len(parse_glossary_rows(glossary)))

    def assert_has_finding(self, findings: list[str], phrase: str) -> None:
        self.assertTrue(findings, "expected a finding")
        self.assertTrue(any(phrase.lower() in finding.lower() for finding in findings), findings)


class TranslationCacheTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source_root = self.root / "source"
        self.translation_root = self.root / "translation"
        self.rel = Path("phases/00-demo/01-example/docs/en.md")
        self.source = self.source_root / self.rel
        self.destination = self.translation_root / "i18n/zh-TW/phases/00-demo/01-example/docs/zh-TW.md"
        self.cache = self.translation_root / "i18n/zh-TW/.cache/00-demo.json"
        self.source.parent.mkdir(parents=True)
        self.source.write_text(SOURCE, encoding="utf-8")
        self.destination.parent.mkdir(parents=True)
        self.destination.write_text(TRANSLATION, encoding="utf-8")
        glossary = self.translation_root / "i18n/zh-TW/GLOSSARY.md"
        glossary.parent.mkdir(parents=True, exist_ok=True)
        glossary.write_text("| English | 譯法 | 保留英文 | 禁用 | 備註 |\n| --- | --- | --- | --- | --- |\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_checker(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--lang", "zh-TW", "--source-root", str(self.source_root),
             "--translations-root", str(self.translation_root), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_write_cache_uses_upstream_key_and_source_sha256(self) -> None:
        result = self.run_checker("--phase", "00-demo", "--write-cache")
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(self.cache.read_text(encoding="utf-8"))
        self.assertEqual(hashlib.sha256(SOURCE.encode()).hexdigest(), payload[self.rel.as_posix()])

    def test_only_filters_by_lesson_directory(self) -> None:
        result = self.run_checker("--only", "phases/00-demo/01-example")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn(self.rel.as_posix(), result.stdout)

    def test_write_cache_does_not_pin_invalid_translation(self) -> None:
        self.destination.write_text(TRANSLATION.replace("print(1)", "print(9)"), encoding="utf-8")
        result = self.run_checker("--only", "phases/00-demo/01-example", "--write-cache")
        self.assertNotEqual(0, result.returncode)
        self.assertFalse(self.cache.exists())

    def test_language_code_cannot_escape_the_translation_root(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--lang", "../outside", "--source-root", str(self.source_root),
             "--translations-root", str(self.translation_root), "--write-cache"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("--lang must be a language code", result.stderr)

    def test_stale_lists_missing_translation_and_source_hash_mismatch(self) -> None:
        self.destination.unlink()
        result = self.run_checker("--stale")
        self.assertNotEqual(0, result.returncode)
        self.assertIn("missing translation", result.stdout.lower())
        self.destination.parent.mkdir(parents=True, exist_ok=True)
        self.destination.write_text(TRANSLATION, encoding="utf-8")
        self.cache.parent.mkdir(parents=True, exist_ok=True)
        self.cache.write_text(json.dumps({self.rel.as_posix(): "old-hash"}), encoding="utf-8")
        result = self.run_checker("--stale")
        self.assertNotEqual(0, result.returncode)
        self.assertIn("stale", result.stdout.lower())
        self.assertIn(self.rel.as_posix(), result.stdout)


if __name__ == "__main__":
    unittest.main()
