# 對話狀態追蹤（dialogue state tracking）

> 「我想要北邊一家便宜的餐廳……改成中等價……再加義大利菜。」三輪，三次狀態更新。DST 讓槽位–值（slot-value）的字典和訂位保持同步。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 5 · 17 (Chatbots), Phase 5 · 20 (Structured Outputs)
**Time:** ~75 minutes

## The Problem｜問題

在任務導向的對話系統裡，使用者的目標編成一組槽位–值：`{cuisine: italian, area: north, price: moderate}`。每一輪使用者都可以新增、改、或拿掉一個槽位。系統必須讀完整段對話，正確輸出目前的狀態。

一個槽位錯了，系統就訂錯餐廳、排錯航班、或刷錯卡。DST 是使用者說的話和後端執行之間的鉸鏈。

2026 年就算有 LLM，它仍然要緊：

- 合規敏感的領域（銀行、醫療、機票訂位）要的是確定的槽位值，不是自由生成。
- 工具呼叫的代理在打 API 之前，仍要先把槽位解析出來。
- 多輪修正比看起來難：「其實不要，改成星期四。」

現代管線（pipeline）：傳統 DST 概念，加 LLM 抽取器，加結構化輸出的護欄。

## The Concept｜核心概念

![DST: dialog history → slot-value state](../assets/dst.svg)

**任務結構。** schema 定義領域（domain）（餐廳、旅館、計程車）和它們的槽位（菜系、區域、價位、人數）。每個槽位可以是空的、從封閉集合填一個值（價位：{cheap, moderate, expensive}），或自由形式的值（名稱："The Copper Kettle"）。

**兩種 DST 表述。**

- **分類。** 對每個（槽位，候選值）預測是／否。封閉詞彙的槽位做得到。2020 年以前的標準。
- **生成。** 給定對話，把槽位值生成為自由文字。開放詞彙的槽位做得到。現代的預設。

**指標。** 聯合目標準確率（Joint Goal Accuracy，JGA）——每一輪裡，每個槽位都對的比例。全有或全無。MultiWOZ 2.4 排行榜在 2026 年頂端大約 83%。

**架構。**

1. **規則式（槽位 regex 加關鍵字）。** 窄領域的強基準模型（baseline）。可以除錯。
2. **TripPy／BERT-DST。** 以 BERT 編碼的複製式生成。LLM 之前的標準。
3. **LDST（LLaMA 加 LoRA）。** instruction-tuned 的 LLM，用領域–槽位的 prompt。在 MultiWOZ 2.4 上達到 ChatGPT 等級的品質。
4. **沒有本體（ontology）的做法（2024–26）。** 跳過 schema，直接生成槽位名稱和值。處理開放領域。
5. **Prompt 加結構化輸出（2024–26）。** LLM 配 Pydantic schema，加約束解碼（constrained decoding）。5 行程式碼，正式環境（production）就緒。

### 經典的失敗模式

- **跨輪共指（coreference）。** 「就維持第一個選項。」要解析是哪一個選項。
- **覆寫還是附加。** 使用者說「加義大利菜。」你是換掉菜系，還是附加？
- **隱含確認。** 「OK 酷」——那算接受了提出的訂位嗎？
- **修正。** 「其實改成晚上 7 點。」必須更新時間，不能清掉其他槽位。
- **對上一句系統話的共指。** 「對，那個。」哪個「那個」？

```figure
n5-slot-tracker
```

## Build It｜動手實作

### 步驟 1：規則式槽位抽取器

見 `code/main.py`。regex 加同義詞字典，在窄領域蓋住 70% 的制式話：

```python
CUISINE_SYNONYMS = {
    "italian": ["italian", "pasta", "pizza", "italy"],
    "chinese": ["chinese", "chow mein", "noodles"],
}


def extract_cuisine(utterance):
    for canonical, synonyms in CUISINE_SYNONYMS.items():
        if any(syn in utterance.lower() for syn in synonyms):
            return canonical
    return None
```

在制式詞彙之外很脆。確定性的槽位確認做得到。

### 步驟 2：狀態更新迴圈

```python
def update_state(state, utterance):
    new_state = dict(state)
    for slot, extractor in SLOT_EXTRACTORS.items():
        value = extractor(utterance)
        if value is not None:
            new_state[slot] = value
    for slot in NEGATION_CLEARS:
        if is_negated(utterance, slot):
            new_state[slot] = None
    return new_state
```

三條不變量：

- 使用者沒碰到的槽位，永遠不要重設。
- 明確的否定（「菜系算了」）必須清掉。
- 使用者的修正（「其實……」）必須覆寫，不要附加。

### 步驟 3：用結構化輸出做 LLM 驅動的 DST

```python
from pydantic import BaseModel
from typing import Literal, Optional
import instructor

class RestaurantState(BaseModel):
    cuisine: Optional[Literal["italian", "chinese", "indian", "thai", "any"]] = None
    area: Optional[Literal["north", "south", "east", "west", "center"]] = None
    price: Optional[Literal["cheap", "moderate", "expensive"]] = None
    people: Optional[int] = None
    day: Optional[str] = None


def llm_dst(history, llm):
    prompt = f"""You track the slot values of a restaurant booking across turns.
Dialogue so far:
{render(history)}

Update the state based on the latest user turn. Output only the JSON state."""
    return llm(prompt, response_model=RestaurantState)
```

Instructor 加 Pydantic 保證一個合法的狀態物件。沒有 regex、沒有 schema 對不上、沒有幻覺（hallucination）出來的槽位。

### 步驟 4：JGA 評估

```python
def joint_goal_accuracy(predicted_states, gold_states):
    correct = sum(1 for p, g in zip(predicted_states, gold_states) if p == g)
    return correct / len(predicted_states)
```

校準：系統在多少比例的輪次把所有槽位都做對？MultiWOZ 2.4 上，2026 年頂尖系統是 80% 到 83%。你的領域內系統在你的窄詞彙上應該超過那個，否則 LLM 基準模型會贏過你。

### 步驟 5：處理修正

```python
CORRECTION_CUES = {"actually", "no wait", "on second thought", "change that to"}


def is_correction(utterance):
    return any(cue in utterance.lower() for cue in CORRECTION_CUES)
```

偵測到修正時，覆寫最近更新的槽位，不要附加。沒有 LLM 幫忙很難做對。現代的模式：永遠讓 LLM 從歷史重新生成整個狀態，而不是漸進更新——這自然就處理了修正。

## 坑

- **整段歷史重新生成的成本。** 每輪讓 LLM 重算狀態，總 token 是 O(n²)。把歷史加上限，或摘要較舊的輪次。
- **schema 漂移。** 事後加新槽位會弄壞舊的訓練資料。給 schema 做版本管理。
- **大小寫。** 「Italian」對「italian」對「ITALIAN」——到處正規化（normalize）。
- **隱含繼承。** 若使用者先前指定「4 個人」，換一個時間的新請求不該清掉人數。永遠傳入完整歷史。
- **自由形式對封閉集合。** 名稱、時間、地址要自由形式的槽位；菜系和區域是封閉的。schema 裡兩種都要。

## Use It｜實際應用

2026 年的組合：

| 情境 | 做法 |
|-----------|----------|
| 窄領域（一或兩個意圖） | 規則式加 regex |
| 寬領域，有標籤（label）的資料 | LDST（在 MultiWOZ 風格的資料上用 LLaMA 加 LoRA） |
| 寬領域，沒有標籤，正式環境就緒 | LLM 加 Instructor 加 Pydantic schema |
| 語音 | ASR 加正規化器加 LLM-DST |
| 多領域訂位流程 | schema 引導的 LLM，每個領域一個 Pydantic 模型 |
| 合規敏感 | 規則式為主，LLM 後援加確認流程 |

## Ship It｜交付成果

存成 `outputs/skill-dst-designer.md`：

```markdown
---
name: dst-designer
description: Design a dialogue state tracker — schema, extractor, update policy, evaluation.
version: 1.0.0
phase: 5
lesson: 29
tags: [nlp, dialogue, task-oriented]
---

Given a use case (domain, languages, vocab openness, compliance needs), output:

1. Schema. Domain list, slots per domain, open vs closed vocabulary per slot.
2. Extractor. Rule-based / seq2seq / LLM-with-Pydantic. Reason.
3. Update policy. Regenerate-whole-state / incremental; correction handling; negation handling.
4. Evaluation. Joint Goal Accuracy on a held-out dialogue set, slot-level precision/recall, confusion on the hardest slot.
5. Confirmation flow. When to explicitly ask the user to confirm (destructive actions, low-confidence extractions).

Refuse LLM-only DST for compliance-sensitive slots without a rule-based secondary check. Refuse any DST that cannot roll back a slot on user correction. Flag schemas without version tags.
```

## Exercises｜練習

1. **簡單。** 在 `code/main.py` 為 3 個槽位（菜系、區域、價位）做規則式狀態追蹤器。在 10 段手寫對話上測。量 JGA。
2. **中等。** 同一份資料集（dataset），用 Instructor 加 Pydantic 加一個小 LLM。比較 JGA。檢查最難的輪次。
3. **困難。** 兩個都做，然後路由：規則式為主；規則式有信心地抽出的槽位少於 2 個時，改用 LLM 後援。量合併後的 JGA，以及每輪的推論（inference）成本。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| DST | 對話狀態追蹤 | 跨對話輪次維持槽位–值的字典。 |
| 槽位 | 使用者意圖的單位 | 後端需要的具名參數（菜系、日期）。 |
| 領域 | 任務範圍 | 餐廳、旅館、計程車——各是一組槽位。 |
| JGA | 聯合目標準確率 | 每一輪裡每個槽位都對的比例。全有或全無。 |
| MultiWOZ | 那個評測 | 多領域的 WOZ 資料集；標準的 DST 評估。 |
| 沒有本體的 DST | 沒有 schema | 直接生成槽位名稱和值，沒有固定清單。 |
| 修正 | 「其實……」 | 覆寫先前已填槽位的那一輪。 |

## Further Reading｜延伸閱讀

- [Budzianowski et al. (2018). MultiWOZ — A Large-Scale Multi-Domain Wizard-of-Oz](https://arxiv.org/abs/1810.00278) ——標準評測。
- [Feng et al. (2023). Towards LLM-driven Dialogue State Tracking (LDST)](https://arxiv.org/abs/2310.14970) ——用 LLaMA 加 LoRA 的 instruction tuning 做 DST。
- [Heck et al. (2020). TripPy — A Triple Copy Strategy for Value Independent Neural Dialog State Tracking](https://arxiv.org/abs/2005.02877) ——複製式 DST 的主力。
- [King, Flanigan (2024). Unsupervised End-to-End Task-Oriented Dialogue with LLMs](https://arxiv.org/abs/2404.10753) ——以 EM 為基礎的無監督任務導向對話。
- [MultiWOZ leaderboard](https://github.com/budzianowski/multiwoz) ——標準的 DST 結果。
