#!/usr/bin/env python3
"""Check Traditional Chinese lesson fidelity and source freshness.

See docs/plans/2026-10-07-2037-feat-zh-tw-translation-plan.md (U1).
This stdlib-first checker reuses the upstream translation hash and Markdown spans.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_catalog import LESSON_DIR_RE, PHASE_DIR_RE  # noqa: E402
from translate_lessons import BARE_URL, IMAGE, INLINE_CODE, INLINE_MATH, source_hash  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
META_CANDIDATE_RE = re.compile(r"^\s*\*\*[^*\n]+:\*\*")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-+*]|\d+[.)])\s+(.+)$")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")
LINK_TARGET_RE = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
LANG_CODE_RE = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*$")
REFERENCE_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\[([^\]\n]*)\]")

# Curated high-confidence characters: these occur in Simplified Chinese but
# have distinct Traditional forms. Shared characters are intentionally omitted.
SIMPLIFIED_ONLY = set(
    "这为与专门业东丝丢两严丧个丰临为么义乌乐乔习乡书买乱争于亏云互亚产亲亿仅从仓仪们价众优会伞伟传伤伦伪体余佣侠侣侥侦侧侨俩俭债倾偿儿兑党兰兴养兽内冈册写军农冲决况冻净凉减凑几凤凭凯击凿剂剑剥剧劝办务动励劳势勋匀区医华协单卖卢卫却厂厌历厉压厕县参双发变叙叠只叶号叹叽后吏吕吗吨听启吴呐呒呓呕园困围国圆图团圣场坏块坚坛坞坟坠垄垒垦垫埙埚堑墙壮声壳壶处备复够头夸夺奋奖妇妈妩娄娱娅婴孙学宁宝实宠审宪宫宽宾寝对寻导寿将尔尘尝尧尸尽层届属岚岛岁岂岖岗岩岭峡峦币帅师帐帘带帮庄庆库应庙废开异弃张弥弯弹强归当录彻径忆忧怀态怂怃怄怅怆总恋恶恼惊惧惨惩惫惯愤战户扑执扩扫扬扰抚抛抢护报拟拢拣拥拦拨择挛挝挟挠挡挣挤挥捞损捡换据掳掷掸掺揽搀搁搂携摄摆摇摊撵攒数斋断无旧时旷昼显晒晓暂朴机杀杂权条杨极构枢枪枫柜柠标栈栋栖样桢桦桥桨桩梦检椭楼榄槛橱欢歼殴毁毕毙气汇汉汤沟没沣沧沪泞泪泻泽洁洒浊测济浏浑浓涛涝涡涣涤润涧涨涩淀渊渗温湾湿溃溅滚滞满滤滥滨滩渐浆潇潜澜灭灯灵灾灿炉点炼烟烦烧烂热爱爷牵犹狱状独狭狮猎猪献玛环现琐琼瑶电画畅疗疯痪瘫皱盏盐监盖盘着睁瞒矫矿码砖砚硕确碍祷祸离种积称稳穷窃窑窜窝窥竖竞笔笺笼筑筛签简篱篮类粪粮紧纠纪约级红纤纲纳纵纷纸纹纺纽线练组绅细织终绍经绑绒结绕绘给绝统绢绣继绩绪续缓编缘缚缝缩缴网罗罚罢翘耸职联聪肃肠肤肾肿胀胁胆胜胶脉脏脐脑脚脱脸腊腻腾舆舱舰艺节芜芦苏苇苍茧荆荫药莱莲获莹莺萝萤营葱蒋蓬蔷蔽蕴虏虑虫虽虾蚀蚁蚂蚕蛮蛰蜡蝇蝉补袄装裆裤见观规觅视览觉触计订认讥许设访证评识诉诊词译试诗诚话诞诡询该详诫语误诱说请诸读课谁调谈谋谎谜谢谣谦谨谬谱贝负贡财责贤败账货质贩贪贫贯贱贴贵贷贸费贺贻贼赂赃资赋赌赎赏赐赔赖赘赚赛赞赠赵赶趋跃践踪踊车轨轩转轮软轰轴轻载较辅辆辈辉辐辑输辖辙辞辩边辽达迁过迈运还这进远违连迟选逊递逻遗邮邻郑酝酱采释钉针钓钙钝钞钟钢钦钧钩钮钱钳钻铁铃铅银铺链销锁锅锈锋锐错锚锤锥锦锭键锯锻镀镁镇镜长门闪闭问闯闲间闷闸阁阅阀队阳阴阵阶际陆陈险陪随隐难雏雾韦韧项顺须顽顾顿预领颁颂颇颈频颗题颜额风飞饥饭饮饱饰饺饼饿馋馆马驭驮驰驱驳驴驶驻驼驾骂骄骆骏骑骗骤鱼鲁鲍鲜鲤鲫鲸鸟鸡鸭鸳鸯鸿鹃鹅鹉鹊鹏鹤麦黄齐齿龄龙龟"
)
# 只/后/里/余/互 are shared; 困 is valid Traditional in 困難/困惑 (only the
# sleepy sense should be 睏). Removing them avoids false positives on correct text.
SIMPLIFIED_ONLY -= set("只后里余互困")
MAINLAND_TERMS = (
    "数据", "軟件", "软件", "硬件", "服務器", "服务器", "客戶端", "客户端",
    "信息", "數據", "視頻", "视频", "網絡", "网络", "鏈接", "链接", "默認", "默认",
    "激活", "獲取", "获取", "數據庫", "数据库", "應用程序", "應用軟件", "操作系統",
    "內存", "内存", "硬盤", "硬盘", "打印機", "打印机", "鼠標", "鼠标", "二維碼",
    "項目組", "項目經理", "視頻會議", "視頻文件", "后验", "后端", "后处理", "后面",
    "后续", "之后", "然后", "后来", "最后", "余弦", "余数", "剩余", "厘米",
)
FIXED_HEADINGS = {
    "Learning Objectives": "學習目標",
    "The Problem": "問題",
    "The Concept": "核心概念",
    "Build It": "動手實作",
    "Use It": "實際應用",
    "Ship It": "交付成果",
    "Exercises": "練習",
    "Key Terms": "關鍵術語",
    "Further Reading": "延伸閱讀",
    "Learning objectives": "學習目標",
    "Problem": "問題",
    "Concept": "核心概念",
}


@dataclass(frozen=True)
class Block:
    kind: str
    shape: tuple[object, ...] = ()
    raw: str = ""


def _raw(raw_lines: list[str], start: int, end: int) -> str:
    return "".join(raw_lines[start:end])


def _table_cells(line: str) -> list[str]:
    cells = re.split(r"(?<!\\)\|", line.strip())
    if cells and not cells[0].strip():
        cells.pop(0)
    if cells and not cells[-1].strip():
        cells.pop()
    return [cell.strip() for cell in cells]


def _is_table_row(line: str) -> bool:
    return line.lstrip().startswith("|") and line.count("|") >= 2


def _is_block_start(lines: list[str], index: int, in_intro: bool) -> bool:
    line = lines[index]
    return bool(
        HEADING_RE.match(line)
        or FENCE_RE.match(line)
        or line.lstrip().startswith("$$")
        or line.lstrip().startswith(">")
        or LIST_RE.match(line)
        or _is_table_row(line)
        or (in_intro and META_CANDIDATE_RE.match(line))
        or re.match(r"^ {0,3}(?:<!--|</?[A-Za-z][\w:-]*(?:\s|>|/))", line)
        or re.match(r"^ {0,3}(?:\*\s*){3,}$|^ {0,3}(?:-\s*){3,}$|^ {0,3}(?:_\s*){3,}$", line)
    )


def parse_blocks(text: str) -> list[Block]:
    raw_lines = text.splitlines(keepends=True)
    lines = [line.rstrip("\r\n") for line in raw_lines]
    blocks: list[Block] = []
    i = 0
    in_intro = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        heading = HEADING_RE.match(line)
        if heading:
            blocks.append(Block("heading", (len(heading.group(1)),), line))
            if len(heading.group(1)) == 2:
                in_intro = False
            i += 1
            continue

        fence = FENCE_RE.match(line)
        if fence:
            marker, info = fence.groups()
            info = info.strip().split(maxsplit=1)[0].lower() if info.strip() else ""
            start = i
            i += 1
            close_re = re.compile(r"^\s{0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*$")
            while i < len(lines) and not close_re.match(lines[i]):
                i += 1
            if i < len(lines):
                i += 1
            kind = "figure" if info == "figure" else "mermaid" if info == "mermaid" else "fence"
            blocks.append(Block(kind, (info, marker[0], len(marker)), _raw(raw_lines, start, i)))
            continue

        if stripped.startswith("$$"):
            start = i
            if stripped.count("$$") < 2:
                i += 1
                while i < len(lines) and "$$" not in lines[i]:
                    i += 1
                if i < len(lines):
                    i += 1
            else:
                i += 1
            blocks.append(Block("math", (), _raw(raw_lines, start, i)))
            continue

        if in_intro and META_CANDIDATE_RE.match(line):
            blocks.append(Block("metadata", (), _raw(raw_lines, i, i + 1)))
            i += 1
            continue

        if _is_table_row(line):
            start = i
            rows: list[list[str]] = []
            while i < len(lines) and _is_table_row(lines[i]):
                cells = _table_cells(lines[i])
                if not all(TABLE_SEPARATOR_RE.fullmatch(cell.replace(" ", "")) for cell in cells):
                    rows.append(cells)
                i += 1
            blocks.append(Block("table", (len(rows), tuple(len(row) for row in rows)), _raw(raw_lines, start, i)))
            continue

        list_match = LIST_RE.match(line)
        if list_match:
            indent, marker, _ = list_match.groups()
            blocks.append(Block("list_item", (len(indent.expandtabs(4)), bool(re.match(r"\d", marker)), marker.rstrip(".)")), line))
            i += 1
            continue

        if line.lstrip().startswith(">"):
            start = i
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                i += 1
            blocks.append(Block("blockquote", (), _raw(raw_lines, start, i)))
            continue

        if re.match(r"^ {0,3}(?:<!--|</?[A-Za-z][\w:-]*(?:\s|>|/))", line):
            start = i
            i += 1
            while i < len(lines) and lines[i].strip() and not _is_block_start(lines, i, in_intro):
                i += 1
            blocks.append(Block("html", (), _raw(raw_lines, start, i)))
            continue

        if re.match(r"^ {0,3}(?:\*\s*){3,}$|^ {0,3}(?:-\s*){3,}$|^ {0,3}(?:_\s*){3,}$", line):
            blocks.append(Block("rule", (), line))
            i += 1
            continue

        start = i
        i += 1
        while i < len(lines) and lines[i].strip() and not _is_block_start(lines, i, in_intro):
            i += 1
        blocks.append(Block("paragraph", (), _raw(raw_lines, start, i)))

    return blocks


def _mermaid_syntax(raw: str) -> str:
    lines = raw.splitlines()
    if len(lines) >= 2:
        lines = lines[1:-1]
    body = "\n".join(lines)
    # Replace sequence participant labels but retain participant kind and identifier.
    body = re.sub(
        r"(?m)^(\s*(?:participant|actor)\s+[\w.-]+\s+as\s+).*$",
        r"\1<participant-label>",
        body,
    )
    # Quoted labels may contain bracket/paren characters (e.g. `id["[1, 0] (x)"]`).
    # Strip the whole quoted span first so the inner delimiters cannot confuse the
    # per-shape loop below.
    body = re.sub(r'(\b[\w.-]+\s*[\[({])"[^"\n]*"', r'\1""', body)
    # Replace node labels but retain each node identifier and shape delimiter.
    for opening, closing in (("[", "]"), ("(", ")"), ("{", "}")):
        pattern = re.compile(r"(\b[\w.-]+\s*" + re.escape(opening) + r")[^\n" + re.escape(closing) + r"]*" + re.escape(closing))
        body = pattern.sub(lambda match: match.group(1) + closing, body)
    return "\n".join(line.rstrip() for line in body.splitlines() if line.strip())


def _protected_spans(text: str) -> Counter[tuple[str, str]]:
    spans: list[tuple[int, int, str, str]] = []
    for kind, pattern in (("image", IMAGE), ("inline code", INLINE_CODE), ("math", INLINE_MATH)):
        spans.extend((match.start(), match.end(), kind, match.group(0)) for match in pattern.finditer(text))

    occupied = [(start, end) for start, end, _, _ in spans]
    for match in LINK_TARGET_RE.finditer(text):
        if not any(match.start() < end and match.end() > start for start, end in occupied):
            spans.append((match.start(1), match.end(1), "link target", match.group(1).strip()))
            occupied.append((match.start(), match.end()))
    for match in REFERENCE_LINK_RE.finditer(text):
        if not any(match.start() < end and match.end() > start for start, end in occupied):
            spans.append((match.start(1), match.end(1), "link target", match.group(1).strip()))
            occupied.append((match.start(), match.end()))
    for match in BARE_URL.finditer(text):
        if not any(match.start() < end and match.end() > start for start, end in occupied):
            spans.append((match.start(), match.end(), "URL", match.group(0)))
            occupied.append((match.start(), match.end()))
    return Counter((kind, value) for _, _, kind, value in spans)


def _prose(block: Block) -> str:
    if block.kind in {"paragraph", "heading", "list_item", "blockquote", "table"}:
        text = block.raw
        for pattern in (IMAGE, INLINE_CODE, INLINE_MATH):
            text = pattern.sub(" ", text)
        text = LINK_TARGET_RE.sub(")", text)
        text = REFERENCE_LINK_RE.sub("]", text)
        return BARE_URL.sub(" ", text)
    return ""


def parse_glossary_rows(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    header_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith("|")), None)
    if header_index is None:
        return []
    headers = [cell.strip().lower() for cell in _table_cells(lines[header_index])]
    forbidden_headers = {"禁用", "禁用譯法", "forbidden", "forbidden variants"}
    if "english" not in headers or not forbidden_headers.intersection(headers):
        return []
    indexes = {
        "english": headers.index("english"),
        "preferred": next(
            (i for i, value in enumerate(headers) if value in {"譯法", "taiwan translation", "translation"}), -1
        ),
        "keep_english": next(
            (i for i, value in enumerate(headers) if value in {"保留英文", "keep english"}), -1
        ),
        "forbidden": next(i for i, value in enumerate(headers) if value in forbidden_headers),
        "notes": next((i for i, value in enumerate(headers) if value in {"備註", "notes"}), -1),
    }
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 1:]:
        if not _is_table_row(line):
            if rows:
                break
            continue
        cells = _table_cells(line)
        if all(TABLE_SEPARATOR_RE.fullmatch(cell.replace(" ", "")) for cell in cells):
            continue
        if len(cells) != len(headers):
            continue
        rows.append({
            key: cells[index] if index >= 0 else ""
            for key, index in indexes.items()
        })
    return rows


def parse_glossary(text: str) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for row in parse_glossary_rows(text):
        for variant in re.split(r"[、,;；]+", row["forbidden"]):
            variant = variant.strip().strip("`*_ ")
            if row["english"] and variant and variant not in {"—", "-", "無", "none"}:
                entries.append((row["english"], variant))
    return entries


def check_document(source: str, translation: str, *, glossary_text: str = "", lesson: str = "") -> list[str]:
    findings: list[str] = []
    prefix = f"{lesson}: " if lesson else ""
    source_blocks = parse_blocks(source)
    target_blocks = parse_blocks(translation)
    source_shape = [(block.kind, block.shape) for block in source_blocks]
    target_shape = [(block.kind, block.shape) for block in target_blocks]

    if source_shape != target_shape:
        mismatch = next((i for i, (left, right) in enumerate(zip(source_shape, target_shape), 1) if left != right), None)
        if mismatch is None:
            mismatch = min(len(source_shape), len(target_shape)) + 1
        findings.append(f"{prefix}structure differs at block {mismatch} (source {len(source_shape)} blocks, translation {len(target_shape)} blocks)")

    for index, (original, translated) in enumerate(zip(source_blocks, target_blocks), 1):
        if original.kind == "metadata" and original.raw != translated.raw:
            findings.append(f"{prefix}metadata differs at block {index}")
        elif original.kind == "fence" and original.raw != translated.raw:
            findings.append(f"{prefix}fence differs at block {index}")
        elif original.kind == "figure" and original.raw != translated.raw:
            findings.append(f"{prefix}figure block differs at block {index}")
        elif original.kind == "mermaid" and _mermaid_syntax(original.raw) != _mermaid_syntax(translated.raw):
            findings.append(f"{prefix}mermaid node ids or edges differ at block {index}")
        elif original.kind == "heading":
            original_match = HEADING_RE.match(original.raw)
            translated_match = HEADING_RE.match(translated.raw)
            if original_match and translated_match:
                original_title, translated_title = original_match.group(2), translated_match.group(2)
                if original_title in FIXED_HEADINGS:
                    expected = original_title + "｜" + FIXED_HEADINGS[original_title]
                    if translated_title != expected:
                        findings.append(f"{prefix}fixed heading must be {expected!r}, got {translated_title!r}")

    source_spans = Counter()
    target_spans = Counter()
    target_prose: list[str] = []
    for block in source_blocks:
        if block.kind in {"paragraph", "heading", "list_item", "blockquote", "table"}:
            source_spans.update(_protected_spans(block.raw))
    for block in target_blocks:
        if block.kind in {"paragraph", "heading", "list_item", "blockquote", "table"}:
            target_spans.update(_protected_spans(block.raw))
            target_prose.append(_prose(block))
    if source_spans != target_spans:
        missing = list((source_spans - target_spans).elements())
        added = list((target_spans - source_spans).elements())
        findings.append(f"{prefix}protected spans differ (missing={missing[:3]!r}, added={added[:3]!r})")

    prose = "\n".join(target_prose)
    simplified = sorted(set(prose) & SIMPLIFIED_ONLY)
    if simplified:
        findings.append(f"{prefix}simplified-only characters: {''.join(simplified)}")
    for term in MAINLAND_TERMS:
        if term in prose:
            findings.append(f"{prefix}mainland wording: {term}")
    for english, variant in parse_glossary(glossary_text):
        if variant and variant in prose:
            findings.append(f"{prefix}glossary forbidden variant for {english!r}: {variant}")
    return findings


def _phase_docs(source_root: Path):
    phases_dir = source_root / "phases"
    if not phases_dir.is_dir():
        return
    for phase in sorted(phases_dir.iterdir()):
        if not phase.is_dir() or not PHASE_DIR_RE.fullmatch(phase.name):
            continue
        for lesson in sorted(phase.iterdir()):
            doc = lesson / "docs" / "en.md"
            if lesson.is_dir() and LESSON_DIR_RE.fullmatch(lesson.name) and doc.is_file():
                yield doc


def _selected_docs(source_root: Path, phase: str | None, only: str | None):
    for doc in _phase_docs(source_root):
        rel = doc.relative_to(source_root).as_posix()
        if phase and PurePosixPath(rel).parts[1] != phase:
            continue
        if only and not (rel == only or rel.startswith(only + "/")):
            continue
        yield doc, rel


def _translation_path(root: Path, lang: str, rel: str) -> Path:
    source = PurePosixPath(rel)
    return root / "i18n" / lang / source.parent / f"{lang}.md"


def _cache_path(root: Path, lang: str, phase: str) -> Path:
    root = root.resolve()
    path = root / "i18n" / lang / ".cache" / f"{phase}.json"
    if path.is_symlink() or not path.resolve().is_relative_to(root):
        raise ValueError(f"cache path escapes translations root: {path}")
    return path


def _load_cache(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in value.items()):
        raise ValueError(f"invalid cache schema: {path}")
    return value


def _write_caches(root: Path, lang: str, records: list[tuple[str, str, str]]) -> None:
    grouped: dict[str, dict[str, str]] = {}
    for rel, source_digest, _ in records:
        phase = PurePosixPath(rel).parts[1]
        path = _cache_path(root, lang, phase)
        cache = grouped.setdefault(phase, _load_cache(path))
        cache[rel] = source_digest
    for phase, cache in grouped.items():
        path = _cache_path(root, lang, phase)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _validate_only(value: str) -> str:
    path = PurePosixPath(value.strip("/"))
    if path.is_absolute() or ".." in path.parts or len(path.parts) != 3 or path.parts[0] != "phases":
        raise argparse.ArgumentTypeError("--only must be phases/<phase>/<lesson>")
    return path.as_posix()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT, help="checkout containing canonical phases/<phase>/<lesson>/docs/en.md")
    parser.add_argument("--translations-root", type=Path, default=ROOT, help="checkout containing i18n/<lang>")
    parser.add_argument("--phase", help="limit to one phase directory, such as 00-setup-and-tooling")
    parser.add_argument("--only", type=_validate_only, help="limit to phases/<phase>/<lesson>")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--stale", action="store_true", help="list missing translations, missing cache entries, and source-hash mismatches")
    mode.add_argument("--write-cache", action="store_true", help="pin source hashes only after every selected translation passes")
    args = parser.parse_args(argv)
    if not LANG_CODE_RE.fullmatch(args.lang):
        parser.error("--lang must be a language code such as zh-TW")

    source_root = args.source_root.resolve()
    translations_root = args.translations_root.resolve()
    glossary_path = translations_root / "i18n" / args.lang / "GLOSSARY.md"
    glossary_text = glossary_path.read_text(encoding="utf-8") if glossary_path.is_file() else ""
    docs = list(_selected_docs(source_root, args.phase, args.only))
    if not docs:
        print("no matching lessons", file=sys.stderr)
        return 2

    if args.stale:
        stale_count = 0
        caches: dict[str, dict[str, str]] = {}
        for doc, rel in docs:
            phase = PurePosixPath(rel).parts[1]
            cache_path = _cache_path(translations_root, args.lang, phase)
            try:
                cache = caches.setdefault(phase, _load_cache(cache_path))
            except (OSError, json.JSONDecodeError, ValueError) as error:
                print(f"invalid cache {cache_path}: {error}")
                stale_count += 1
                continue
            translation_path = _translation_path(translations_root, args.lang, rel)
            if not translation_path.is_file():
                print(f"missing translation: {rel}")
                stale_count += 1
            elif rel not in cache:
                print(f"missing cache: {rel}")
                stale_count += 1
            elif cache[rel] != source_hash(doc.read_text(encoding="utf-8")):
                print(f"stale source hash: {rel} cached={cache[rel]} current={source_hash(doc.read_text(encoding='utf-8'))}")
                stale_count += 1
        print(f"{args.lang}: {stale_count} stale or missing lesson(s)")
        return 1 if stale_count else 0

    records: list[tuple[str, str, str]] = []
    failures = 0
    for doc, rel in docs:
        source = doc.read_text(encoding="utf-8")
        translated_path = _translation_path(translations_root, args.lang, rel)
        if not translated_path.is_file():
            print(f"FAIL missing translation: {rel}")
            failures += 1
            continue
        translation = translated_path.read_text(encoding="utf-8")
        findings = check_document(source, translation, glossary_text=glossary_text, lesson=rel.rsplit("/docs/en.md", 1)[0])
        if findings:
            for finding in findings:
                print(f"FAIL {finding}")
            failures += 1
        else:
            source_digest = source_hash(source)
            translation_digest = source_hash(translation)
            print(f"OK {rel} source={source_digest} translation={translation_digest}")
            records.append((rel, source_digest, translation_digest))

    print(f"{args.lang}: {len(records)} passed, {failures} failed")
    if failures:
        return 1
    if args.write_cache:
        _write_caches(translations_root, args.lang, records)
        print(f"wrote {len(records)} source hash(es) to {translations_root / 'i18n' / args.lang / '.cache'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
