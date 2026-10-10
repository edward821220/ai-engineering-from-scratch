# 多頭注意力（multi-head attention）

> 一個注意力頭一次學一種關係。八個頭學八種。頭是免費的。多拿幾個。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 7 · 02 (Self-Attention from Scratch)
**Time:** ~75 minutes

## The Problem｜問題

單一自注意力（self-attention）頭算出一張注意力矩陣。那張矩陣抓住一種關係——通常是訓練訊號要它把損失（loss）壓到最低的那一種。若你的資料把主詞動詞一致、共指（coreference）、長程語篇、句法切塊纏在一起，單一頭把它們糊進同一個 softmax 分布，一半的訊號就沒了。

2017 年 Vaswani 論文的修法：平行跑好幾個注意力函式，各自有自己的 Q、K、V 投影，再把輸出接起來。每個頭在較小的子空間裡運作，維度（dimension）是 `d_model / n_heads`。總參數（parameter）數量不變。表達力上升。

多頭注意力是 2026 年每個 transformer 交付時的預設。唯一要爭的是頭要幾個，以及鍵和值是否共用投影：Grouped-Query Attention、Multi-Query Attention、Multi-head Latent Attention。

## The Concept｜核心概念

![Multi-head attention splits, attends, concatenates](../assets/multi-head-attention.svg)

**拆開。** 取形狀 `(N, d_model)` 的 `X`。投影成 Q、K、V，各自形狀 `(N, d_model)`。重排成 `(N, n_heads, d_head)`，其中 `d_head = d_model / n_heads`。轉置成 `(n_heads, N, d_head)`。

**平行注意。** 在每個頭裡跑縮放後的內積注意力。每個頭產出 `(N, d_head)`。這些頭在 embedding 的不同子空間上運作，注意力計算本身的期間彼此不交談。

**接起來再投影。** 把頭疊回 `(N, d_model)`，乘上一個學來的輸出矩陣 `W_o`，形狀 `(d_model, d_model)`。`W_o` 是頭開始混合的地方。

**為什麼行得通。** 每個頭可以專精，不必和其他頭搶表示預算。2019 到 2024 的探查研究顯示頭的角色不同：位置頭、注意前一個 token 的頭、複製頭、命名實體（named entity）頭、歸納頭（它們撐起脈絡內學習）。

**2026 年的變體譜系：**

| 變體 | Q 頭數 | K/V 頭數 | 誰在用 |
|---------|---------|-----------|---------|
| 多頭（MHA） | N | N | GPT-2、BERT、T5 |
| 多查詢（MQA） | N | 1 | PaLM、Falcon |
| 分組查詢（GQA） | N | G（例如 N/8） | Llama 2 70B、Llama 3+、Qwen 2+、Mistral |
| 多頭潛在（MLA） | N | 壓成低秩 | DeepSeek-V2、V3 |

GQA 是現代的預設，因為它把 KV 快取的記憶體（memory）砍成 `N/G` 分之一，品質幾乎不變。MLA 再進一步，把 K/V 壓進潛在空間，計算時再投影回來——多花 FLOPs，省下更多記憶體。

```figure
multihead-split
```

## Build It｜動手實作

### 步驟 1：從我們已有的單頭注意力拆頭

拿第 2 課的 `SelfAttention`，用一對拆開／接上把它包起來。NumPy 實作見 `code/main.py`；邏輯是：

```python
def split_heads(X, n_heads):
    n, d = X.shape
    d_head = d // n_heads
    return X.reshape(n, n_heads, d_head).transpose(1, 0, 2)  # (heads, n, d_head)

def combine_heads(H):
    h, n, d_head = H.shape
    return H.transpose(1, 0, 2).reshape(n, h * d_head)
```

一次重排、一次轉置。沒有迴圈。PyTorch 在 `nn.MultiheadAttention` 底下做的就是這個。

### 步驟 2：每個頭跑縮放後的內積注意力

每個頭拿到自己那一片 Q、K、V。注意力變成一次批次（batch）矩陣乘法：

```python
def mha_forward(X, W_q, W_k, W_v, W_o, n_heads):
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    Qh = split_heads(Q, n_heads)         # (heads, n, d_head)
    Kh = split_heads(K, n_heads)
    Vh = split_heads(V, n_heads)
    scores = Qh @ Kh.transpose(0, 2, 1) / np.sqrt(Qh.shape[-1])
    weights = softmax(scores, axis=-1)
    out = weights @ Vh                    # (heads, n, d_head)
    concat = combine_heads(out)
    return concat @ W_o, weights
```

在真實硬體上，`Qh @ Kh.transpose(...)` 是一次 `bmm`。GPU 看到的是單一次批次矩陣乘法，形狀 `(heads, N, d_head) × (heads, d_head, N) -> (heads, N, N)`。加頭是免費的。

### 步驟 3：分組查詢注意力的變體

只有鍵和值的投影變了。Q 有 `n_heads` 組；K 和 V 有 `n_kv_heads < n_heads` 組，再重複到對得上：

```python
def gqa_project(X, W, n_kv_heads, n_heads):
    kv = split_heads(X @ W, n_kv_heads)       # (kv_heads, n, d_head)
    repeat = n_heads // n_kv_heads
    return np.repeat(kv, repeat, axis=0)      # (n_heads, n, d_head)
```

推論（inference）時這省記憶體，因為 KV 快取裡活著的是 `n_kv_heads` 份，不是 `n_heads` 份。Llama 3 70B 用 64 個查詢頭、8 個 KV 頭——快取縮到八分之一。

### 步驟 4：探查每個頭學到什麼

在一個短句子上用 4 個頭跑 MHA。每個頭印出 `(N, N)` 的注意力矩陣。就算是隨機初始化，你也會看到不同的頭抓出不同的結構——一部分是訊號，一部分是子空間裡的旋轉對稱。

## Use It｜實際應用

在 PyTorch 裡，一行版本：

```python
import torch.nn as nn

mha = nn.MultiheadAttention(embed_dim=512, num_heads=8, batch_first=True)
```

PyTorch 2.5 以後的 GQA：

```python
from torch.nn.functional import scaled_dot_product_attention

# scaled_dot_product_attention auto-dispatches Flash Attention on CUDA.
# For GQA, pass Q of shape (B, n_heads, N, d_head) and K,V of shape
# (B, n_kv_heads, N, d_head). PyTorch handles the repeat.
out = scaled_dot_product_attention(q, k, v, is_causal=True, enable_gqa=True)
```

**頭要幾個？** 2026 年正式環境（production）模型的經驗法則：

| 模型大小 | d_model | n_heads | d_head |
|------------|---------|---------|--------|
| 小型（約 1.25 億） | 768 | 12 | 64 |
| 基礎（約 3.5 億） | 1024 | 16 | 64 |
| 大型（約 10 億） | 2048 | 16 | 128 |
| 前沿（約 700 億） | 8192 | 64 | 128 |

`d_head` 幾乎總是落在 64 或 128。它是一個頭能「看到」多少的單位。低於 32，頭就開始和縮放因子 `sqrt(d_head)` 打架；高過 256，你就失去「很多小專家」的好處。

## Ship It｜交付成果

見 `outputs/skill-mha-configurator.md`。這個 skill 依參數預算、序列長度、部署（deployment）目標，為新的 transformer 建議頭數、kv 頭數和投影策略。

## Exercises｜練習

1. **簡單。** 從 `code/main.py` 拿 MHA，把 `n_heads` 從 1 改到 16，`d_model=64` 固定。畫一個小小的一層模型在合成複製任務上的損失。頭變多是有幫助、持平，還是有害？
2. **中等。** 實作 MQA（所有查詢頭共用一個 KV 頭）。量參數數量相對完整 MHA 掉多少。算 N=2048 時，推論的 KV 快取縮多少。
3. **困難。** 實作一個小型的多頭潛在注意力：把 K、V 壓成秩 `r` 的潛在向量，存在 KV 快取裡，注意時再解壓。`r` 要到多少，快取記憶體才降到完整 MHA 的 1/8 以下，而品質仍在驗證困惑度（perplexity）的 1 bit 以內？

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 頭 | 「一個注意力電路」 | 一個維度 `d_head = d_model / n_heads` 的 Q/K/V 投影，有自己的注意力矩陣。 |
| d_head | 「頭的維度」 | 每個頭的隱藏寬度；正式環境裡幾乎總是 64 或 128。 |
| 拆開／接上 | 「重排的技巧」 | 注意力前後做 `(N, d_model) ↔ (n_heads, N, d_head)` 的重排加轉置。 |
| W_o | 「輸出投影」 | 把頭接起來之後乘上的 `(d_model, d_model)` 矩陣；頭在這裡混合。 |
| MQA | 「一個 KV 頭」 | 多查詢注意力：共用單一的 K/V 投影。KV 快取最小，品質有些損失。 |
| GQA | 「Llama 2 之後的預設」 | 分組查詢注意力，`n_kv_heads < n_heads`；重複到和 Q 對上。 |
| MLA | 「DeepSeek 的手法」 | 多頭潛在注意力：K、V 壓成低秩潛在向量，注意時再解壓。 |
| 歸納頭 | 「脈絡內學習背後的電路」 | 一對頭，偵測先前出現過的地方，並複製後面跟著的東西。 |

## Further Reading｜延伸閱讀

- [Vaswani et al. (2017). Attention Is All You Need §3.2.2](https://arxiv.org/abs/1706.03762) ——原始的多頭規格。
- [Shazeer (2019). Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) ——MQA 論文。
- [Ainslie et al. (2023). GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) ——訓練之後怎麼把 MHA 轉成 GQA。
- [DeepSeek-AI (2024). DeepSeek-V2 Technical Report](https://arxiv.org/abs/2405.04434) ——MLA，以及為什麼它在快取記憶體上贏過 MHA／GQA。
- [Olsson et al. (2022). In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) ——從機制看頭實際在做什麼。
