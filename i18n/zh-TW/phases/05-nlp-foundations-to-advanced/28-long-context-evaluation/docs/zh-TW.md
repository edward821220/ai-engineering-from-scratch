# 長脈絡評估——NIAH、RULER、LongBench、MRCR

> Gemini 3 Pro 標榜 1000 萬個 token 的脈絡。在 100 萬個 token 時，8 針的 MRCR 掉到 26.3%。標榜的不等於用得上。長脈絡評估告訴你，你要交付的那個模型實際容量是多少。

**Type:** Learn
**Languages:** Python
**Prerequisites:** Phase 5 · 13 (Question Answering), Phase 5 · 23 (Chunking Strategies)
**Time:** ~60 minutes

## The Problem｜問題

你有一份 200 頁的合約。模型宣稱脈絡是 100 萬個 token。你把合約貼進去，問：「終止條款是什麼？」模型有回答——但答案來自封面，因為終止條款深到 12 萬個 token，超過模型的注意力（attention）真正顧得到的地方。

這就是 2026 年的脈絡容量落差。規格表寫 100 萬或 1000 萬。現實是其中 60% 到 70% 用得上，而「用得上」取決於任務。

- **檢索（retrieval）：乾草堆裡的單針。** 在前沿模型上，一直到標榜的上限都接近完美。
- **多跳／聚合。** 大多數模型過了大約 12.8 萬就陡掉。
- **分散事實上的推理。** 最先失敗的任務。

長脈絡評估量的就是這些軸。這一課點出這些評測、各自實際量什麼，以及怎麼為你的領域做自訂的針測試。

## The Concept｜核心概念

![NIAH baseline, RULER multi-task, LongBench holistic](../assets/long-context-eval.svg)

**乾草堆裡的針（NIAH，2023）。** 把一個事實（「魔法詞是 pineapple」）放在長脈絡裡受控的深度。請模型把它找回來。掃過深度 × 長度。這是最早的長脈絡評測。前沿模型現在把它做滿了；它是必要但不充分的基準模型（baseline）。

**RULER（Nvidia，2024）。** 4 類共 13 種任務：檢索（單鍵／多鍵／多值）、多跳追蹤（變數追蹤）、聚合（常見詞頻率）、問答。脈絡長度可設定（4000 到 12.8 萬以上）。它露出那些 NIAH 做滿、多跳卻失敗的模型。2024 年發布時，17 個宣稱 3.2 萬以上脈絡的模型裡，只有一半在 3.2 萬時還維持品質。

**LongBench v2（2024）。** 503 題選擇題，脈絡從 8000 到 200 萬個詞，六類任務：單文件問答、多文件問答、長的脈絡內學習、長對話、程式碼儲存庫、長的結構化資料。這是真實世界長脈絡行為的正式環境（production）評測。

**MRCR（Multi-Round Coreference Resolution）。** 大規模的多輪共指（coreference）。有 8 針、24 針、100 針的變體。露出模型在注意力開始掉之前，能同時記住多少事實。

**NoLiMa。** 「非詞彙的針。」針和查詢沒有字面重疊；檢索需要一步語意推理。比 NIAH 難。

**HELMET。** 把很多文件接在一起，問題來自其中任何一份。測的是選擇性注意力。

**BABILong。** 把 bAbI 的推理鏈嵌進不相干的乾草堆。測的是乾草堆裡的推理，不只是檢索。

### 實際要報告什麼

- **標榜的脈絡視窗（context window）。** 規格表上的那個數字。
- **有效檢索長度。** NIAH 在某個閾值（threshold）通過，例如 90%。
- **有效推理長度。** 多跳或聚合在那個閾值通過。
- **衰退曲線。** 準確率（accuracy）對上脈絡長度，依任務類型畫出來。

規格表要兩個數字：檢索有效、推理有效。推理有效長度通常是標榜視窗的 25% 到 50%。

```figure
gx-niah-decay
```

## Build It｜動手實作

### 步驟 1：為你的領域做自訂 NIAH

見 `code/main.py`。骨架是：

```python
def build_haystack(filler_text, needle, depth_ratio, total_tokens):
    if not (0.0 <= depth_ratio <= 1.0):
        raise ValueError(f"depth_ratio must be in [0, 1], got {depth_ratio}")
    if total_tokens <= 0:
        raise ValueError(f"total_tokens must be positive, got {total_tokens}")

    filler_tokens = tokenize(filler_text)
    needle_tokens = tokenize(needle)
    if not filler_tokens:
        raise ValueError("filler_text produced no tokens")

    # Repeat filler until long enough to fill the haystack body.
    body_len = max(total_tokens - len(needle_tokens), 0)
    while len(filler_tokens) < body_len:
        filler_tokens = filler_tokens + filler_tokens
    filler_tokens = filler_tokens[:body_len]

    insert_at = min(int(body_len * depth_ratio), body_len)
    haystack = filler_tokens[:insert_at] + needle_tokens + filler_tokens[insert_at:]
    return " ".join(haystack)


def score_niah(model, haystack, question, expected):
    answer = model.complete(f"Context: {haystack}\nQ: {question}\nA:", max_tokens=50)
    return 1 if expected.lower() in answer.lower() else 0
```

掃 `depth_ratio` ∈ {0, 0.25, 0.5, 0.75, 1.0} × `total_tokens` ∈ {1k, 4k, 16k, 64k}。畫熱圖。那就是你目標模型的 NIAH 卡片。

### 步驟 2：多針變體

```python
def build_multi_needle(filler, needles, total_tokens):
    depths = [0.1, 0.4, 0.7]
    chunks = [filler[:int(total_tokens * 0.1)]]
    for depth, needle in zip(depths, needles):
        chunks.append(needle)
        next_chunk = filler[int(total_tokens * depth): int(total_tokens * (depth + 0.3))]
        chunks.append(next_chunk)
    return " ".join(chunks)
```

「三個魔法詞是什麼？」這種問題要三個都找回來。單針成功預測不了多針成功。

### 步驟 3：多跳變數追蹤（RULER 風格）

```python
haystack = """X1 = 42. ... (filler) ... X2 = X1 + 10. ... (filler) ... X3 = X2 * 2."""
question = "What is X3?"
```

答案要串起三次賦值。前沿模型在 12.8 萬時，這裡的準確率常常掉到 50% 到 70%。

### 步驟 4：在你的組合上跑 LongBench v2

```python
from datasets import load_dataset
longbench = load_dataset("THUDM/LongBench-v2")

def eval_model_on_longbench(model, subset="single-doc-qa"):
    tasks = [x for x in longbench["test"] if x["task"] == subset]
    correct = 0
    for x in tasks:
        answer = model.complete(x["context"] + "\n\nQ: " + x["question"], max_tokens=20)
        if normalize(answer) == normalize(x["answer"]):
            correct += 1
    return correct / len(tasks)
```

依類別報告準確率。加總分數會藏起任務層級的大差異。

## 坑

- **只做 NIAH。** 在 100 萬個 token 通過 NIAH，對多跳什麼都沒說。永遠跑 RULER，或自訂的多跳測試。
- **均勻的深度抽樣。** 很多實作只測深度 0.5。要測 0、0.25、0.5、0.75、1.0——「迷失在中間」是真的。
- **和填充文有詞彙重疊。** 針和填充文共用關鍵字，檢索就變得太容易。用 NoLiMa 風格、不重疊的針。
- **忽略延遲（latency）。** 100 萬個 token 的 prompt 預填要 30 到 120 秒。準確率旁邊也要量第一個 token 的時間。
- **廠商自己報的數字。** OpenAI、Google、Anthropic 都發自己的分數。永遠在你的用途上獨立重跑。

## Use It｜實際應用

2026 年的組合：

| 情境 | 評測 |
|-----------|-----------|
| 快速健全檢查 | 自訂 NIAH，3 個深度 × 3 個長度 |
| 為正式環境挑模型 | 在你的目標長度上跑 RULER（13 種任務） |
| 真實世界的問答品質 | LongBench v2 的單文件問答子集 |
| 多跳推理 | BABILong，或自訂的變數追蹤 |
| 對話 | 在你的目標長度上跑 MRCR 8 針 |
| 模型升級的退步 | 固定的內部 NIAH 加 RULER 測試架，每個新模型都跑 |

正式環境的經驗法則：在你預定的長度上有 NIAH 加 1 個推理任務之前，永遠不要信脈絡視窗。

## Ship It｜交付成果

存成 `outputs/skill-long-context-eval.md`：

```markdown
---
name: long-context-eval
description: Design a long-context evaluation battery for a given model and use case.
version: 1.0.0
phase: 5
lesson: 28
tags: [nlp, long-context, evaluation]
---

Given a target model, target context length, and use case, output:

1. Tests. NIAH depth × length grid; RULER multi-hop; custom domain task.
2. Sampling. Depths 0, 0.25, 0.5, 0.75, 1.0 at each length.
3. Metrics. Retrieval pass rate; reasoning pass rate; time-to-first-token; cost-per-query.
4. Cutoff. Effective retrieval length (90% pass) and effective reasoning length (70% pass). Report both.
5. Regression. Fixed harness, rerun on every model upgrade, surface deltas.

Refuse to trust a context window from the model card alone. Refuse NIAH-only evaluation for any multi-hop workload. Refuse vendor self-reported long-context scores as independent evidence.
```

## Exercises｜練習

1. **簡單。** 做一個 NIAH：3 個深度（0.25、0.5、0.75）× 3 個長度（1000、4000、1.6 萬）。在任何模型上跑。把通過率畫成 3×3 的熱圖。
2. **中等。** 加上 3 針變體。在每個長度量「三個都找回來」。和同一長度的單針通過率比。
3. **困難。** 做一個變數追蹤任務（X1 → X2 → X3，3 跳），嵌進 6.4 萬的填充文。在 3 個前沿模型上量準確率。每個模型報告有效推理長度。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| NIAH | 乾草堆裡的針 | 把一個事實種進填充文，請模型把它找回來。 |
| RULER | 加強版的 NIAH | 13 種任務，跨檢索／多跳／聚合／問答。 |
| 有效脈絡 | 真正的容量 | 準確率還維持在閾值以上的那個長度。 |
| 迷失在中間 | 深度偏差 | 模型對長輸入中段的內容注意不夠。 |
| 多針 | 一次很多事實 | 種進多個事實；測的是注意力能不能同時顧，不只是檢索。 |
| MRCR | 多輪共指 | 8、24 或 100 針的共指；露出注意力飽和。 |
| NoLiMa | 非詞彙的針 | 針和查詢沒有共用的字面 token；需要推理。 |

## Further Reading｜延伸閱讀

- [Kamradt (2023). Needle in a Haystack analysis](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) ——最早的 NIAH 儲存庫。
- [Hsieh et al. (2024). RULER: What's the Real Context Size of Your Long-Context LMs?](https://arxiv.org/abs/2404.06654) ——多任務評測。
- [Bai et al. (2024). LongBench v2](https://arxiv.org/abs/2412.15204) ——真實世界的長脈絡評估。
- [Modarressi et al. (2024). NoLiMa: Non-lexical needles](https://arxiv.org/abs/2404.06666) ——更難的針。
- [Kuratov et al. (2024). BABILong](https://arxiv.org/abs/2406.10149) ——乾草堆裡的推理。
- [Liu et al. (2024). Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) ——深度偏差那篇論文。
