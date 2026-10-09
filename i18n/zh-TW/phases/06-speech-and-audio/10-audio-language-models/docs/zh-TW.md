# 音訊語言模型：Qwen2.5-Omni、Audio Flamingo、GPT-4o Audio

> 2026 年的音訊語言模型，對語音、環境聲、音樂一起推理。Qwen2.5-Omni-7B 在 MMAU-Pro 上打平 GPT-4o Audio。Audio Flamingo Next 在 LongAudioBench 上超過 Gemini 2.5 Pro。開放和封閉的差距基本上合上了。多音訊任務除外，那裡大家都接近亂猜。

**Type:** Learn
**Languages:** Python
**Prerequisites:** Phase 6 · 04 (ASR), Phase 12 · 03 (Vision-Language Models), Phase 7 · 10 (Audio Transformers)
**Time:** ~45 minutes

## The Problem｜問題

你有 5 秒音訊：狗叫，有人喊「stop!」，然後靜音。有用的問題跨好幾個軸：

- **轉錄。** 「說了什麼？」這是 ASR 的地盤。
- **語意推理。** 「這個人有危險嗎？」得同時懂狗叫、喊聲和靜音。
- **音樂推理。** 「旋律是哪些樂器在奏？」
- **長音訊檢索。** 「這 90 分鐘的課，講師在哪裡解釋梯度下降法？」

一個模型、一個 prompt，把這些都答出來，就是**音訊語言模型**（LALM／ALM）。和純 ASR 分開：LALM 產出自由形式的自然語言答案，不只是逐字稿。

## The Concept｜核心概念

![Audio-language model: audio encoder + projector + LLM decoder](../assets/alm-architecture.svg)

### 三元件模板

2026 年每一個 LALM 都是同一個骨架：

1. **音訊編碼器。** Whisper 編碼器、BEATs、CLAP、WavLM，或各模型自己的編碼器。
2. **投影器。** 線性層或 MLP，把音訊編碼器的特徵（feature）接到 LLM 的 token embedding 空間。
3. **LLM。** 以 Llama、Qwen、Gemma 為基礎的解碼器。吃交錯的文字和音訊 token，再生成文字。

訓練：

- **第 1 階段。** 凍結編碼器和 LLM。只用 ASR 或說明文字資料訓練投影器。
- **第 2 階段。** 在遵循指令的音訊任務上做完整或 LoRA fine-tune（問答、推理、音樂理解）。
- **第 3 階段（可選）。** 語音進、語音出，加上語音解碼器。Qwen2.5-Omni 和 AF3-Chat 做這個。

### 2026 年的模型版圖

| 模型 | 骨幹 | 音訊編碼器 | 輸出模態 | 取用 |
|-------|----------|---------------|-----------------|--------|
| Qwen2.5-Omni-7B | Qwen2.5-7B | 自訂加 Whisper | 文字加語音 | Apache-2.0 |
| Qwen3-Omni | Qwen3 | 自訂 | 文字加語音 | Apache-2.0 |
| Audio Flamingo 3 | Qwen2 | AF-CLAP | 文字 | NVIDIA 非商業 |
| Audio Flamingo Next | Qwen2 | AF-CLAP v2 | 文字 | NVIDIA 非商業 |
| SALMONN | Vicuna | Whisper 加 BEATs | 文字 | Apache-2.0 |
| LTU／LTU-AS | Llama | CAV-MAE | 文字 | Apache-2.0 |
| GAMA | Llama | AST 加 Q-Former | 文字 | Apache-2.0 |
| Gemini 2.5 Flash／Pro（不公開） | Gemini | 專有 | 文字加語音 | API |
| GPT-4o Audio（不公開） | GPT-4o | 專有 | 文字加語音 | API |

### 基準的現實檢查（2026）

**MMAU-Pro。** 1800 組問答，涵蓋語音、聲音、音樂、混合。含多音訊子集。

| 模型 | 整體 | 語音 | 聲音 | 音樂 | 多音訊 |
|-------|---------|--------|-------|-------|-------------|
| Gemini 2.5 Pro | 約 60% | 73.4% | 51.9% | 64.9% | 約 22% |
| Gemini 2.5 Flash | 約 57% | 73.4% | 50.5% | 64.9% | 21.2% |
| GPT-4o Audio | 52.5% | — | — | — | 26.5% |
| Qwen2.5-Omni-7B | 52.2% | 57.4% | 47.6% | 61.5% | 約 20% |
| Audio Flamingo 3 | 約 54% | — | — | — | — |
| Audio Flamingo Next | LongAudioBench 上目前最好 | — | — | — | — |

**多音訊那一欄對所有人都難堪。** 四選一的隨機是 25%。大多數模型就在那附近。LALM 比兩段片段仍然吃力。

### 2026 年 LALM 有用的地方

- **客服錄音的合規稽核。** 「客服有沒有說到必須揭露的那句？」
- **無障礙。** 向聽障使用者描述聲音事件（不只是轉錄）。
- **內容審核。** 偵測暴力語言、威脅的語氣，以及背景脈絡。
- **Podcast 或會議分章。** 語意摘要，不只是說話人輪次。
- **音樂曲庫分析。** 「找出所有 B 段轉調的曲目。」

### 它們還沒有用的地方

- 細的樂理（和弦層級以下）。
- 長對話裡按說話人歸因的推理（超過 10 分鐘就變差）。
- 多音訊比較（22% 到 26% 只比亂猜高一點）。
- 即時串流推理（大多數是離線批次推論）。

```figure
v4-alm-tokens
```

## Build It｜動手實作

### 步驟 1：查詢 Qwen2.5-Omni

```python
from transformers import AutoModelForCausalLM, AutoProcessor

processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-Omni-7B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-Omni-7B", torch_dtype="auto")

audio, sr = load_wav("clip.wav", sr=16000)
messages = [{
    "role": "user",
    "content": [
        {"type": "audio", "audio": audio},
        {"type": "text", "text": "What sounds do you hear, and what's happening?"},
    ],
}]
inputs = processor.apply_chat_template(messages, tokenize=True, return_tensors="pt")
output = model.generate(**inputs, max_new_tokens=200)
print(processor.decode(output[0], skip_special_tokens=True))
```

### 步驟 2：投影器模式

```python
import torch.nn as nn

class AudioProjector(nn.Module):
    def __init__(self, audio_dim=1280, llm_dim=4096):
        super().__init__()
        self.down = nn.Linear(audio_dim, llm_dim)
        self.act = nn.GELU()
        self.up = nn.Linear(llm_dim, llm_dim)

    def forward(self, audio_features):
        return self.up(self.act(self.down(audio_features)))
```

就是這樣。投影器通常是 1 到 3 層線性層。在 ASR 配對上訓練它（音訊到逐字稿），是第 1 階段的前置任務。

### 步驟 3：對 MMAU／LongAudioBench 做基準

```python
from datasets import load_dataset
mmau = load_dataset("gamma-lab-umd/MMAU-Pro", split="test")
mcq = mmau.filter(lambda item: len(item["choices"] or []) > 1)

correct = 0
for item in mcq:
    answer = call_model(item["audio_path"], item["question"], item["choices"])
    if answer == item["answer"]:
        correct += 1
print(f"Accuracy: {correct / len(mcq):.3f}")
```

`audio_path` 指向資料集儲存庫裡的 `data.zip`（大約 47 GB），評分前要先下載並解壓。這個完全比對的迴圈是健全檢查，不是基準的計分器，所以數字不能和公開的 MMAU-Pro 結果比。官方評估器用 embedding 相似度（NV-Embed-v2）對多選題，用 LLM 裁判給開放題評分，用正規表示式規則檢查遵循指令的答案：把預測寫進 `model_output` 欄，再跑 [MMAU-Pro repo](https://github.com/sonalkum/MMAUPro) 的 `evaluate_mmau_pro_comprehensive.py`。每個 `category`（語音、聲音、音樂、多音訊，以及其他）分開回報。加總的數字會把模型失敗的地方藏起來。

## Use It｜實際應用

| 任務 | 2026 年的選擇 |
|------|-----------|
| 自由形式的音訊問答（開放） | Qwen2.5-Omni-7B |
| 長音訊上最好的開放模型 | Audio Flamingo Next |
| 最好的封閉模型 | Gemini 2.5 Pro |
| 語音進、語音出的代理 | Qwen2.5-Omni 或 GPT-4o Audio |
| 音樂推理 | Audio Flamingo 3 或 2（專做音樂的 AF-CLAP） |
| 客服稽核 | 經 API 用 Gemini 2.5 Pro，並對你的政策文件做 RAG |

## Pitfalls｜容易踩的坑

- **多音訊上過度信任。** 如果你的任務是「哪一段有 X」，接近亂猜是真的。
- **長音訊變差。** 超過 10 分鐘，大多數模型的說話人歸因就破。先做說話人分離（第 6 課），再摘要。
- **靜音上的幻覺。** 用 Whisper 編碼器的 LALM 繼承了同一個問題。用 VAD 當閘。
- **挑基準。** 廠商部落格只亮最好看的類別。多音訊子集要自己跑 MMAU-Pro。

## Ship It｜交付成果

存成 `outputs/skill-alm-picker.md`。依給定的音訊理解任務，挑 LALM、基準子集，以及輸出模態（文字或語音）。

## Exercises｜練習

1. **簡單。** 跑 `code/main.py`，看玩具投影器，以及假的 LALM 怎麼把（音訊 embedding、文字 token）路由到輸出 token。
2. **中等。** 在 100 題 MMAU-Pro 語音題上給 Qwen2.5-Omni-7B 評分。和論文報的數字比。
3. **困難。** 做一個最小的音訊說明文字基準模型：BEATs 編碼器加 2 層投影器加凍結的 Llama-3.2-1B。只在 AudioCaps 上 fine-tune 投影器。和 SALMONN 在 Clotho-AQA 上比。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| LALM | 音訊版的 ChatGPT | 音訊編碼器加投影器加 LLM 解碼器。 |
| 投影器 | 轉接器 | 小 MLP，把音訊特徵映到 LLM 的 embedding 空間。 |
| MMAU | 那個基準 | 1 萬組音訊問答，跨語音、聲音、音樂。 |
| MMAU-Pro | 更難的 MMAU | 1800 題，多音訊、推理很重。 |
| LongAudioBench | 長音訊評估 | 多分鐘片段，用語意查詢。 |
| 語音進／語音出 | 語音原生 | 模型吃語音、出語音，不繞文字。 |

## Further Reading｜延伸閱讀

- [Chu et al. (2024). Qwen2-Audio](https://arxiv.org/abs/2407.10759) ——參考架構。
- [Alibaba (2025). Qwen2.5-Omni](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) ——語音進、語音出。
- [NVIDIA (2025). Audio Flamingo 3](https://arxiv.org/abs/2507.08128) ——開放的長音訊領先者。
- [NVIDIA (2026). Audio Flamingo Next](https://arxiv.org/abs/2604.10905) ——LongAudioBench 上目前最好。
- [Tang et al. (2023). SALMONN](https://arxiv.org/abs/2310.13289) ——雙編碼器的先行者。
- [MMAU-Pro leaderboard](https://sonalkum.github.io/mmau-pro/) ——2026 年的即時排名。
