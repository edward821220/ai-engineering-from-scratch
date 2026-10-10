# 完整的 transformer——編碼器加解碼器

> 注意力是主角。其他一切——殘差（residual）、正規化、前饋、交叉注意力（cross-attention）——是讓你能把它疊深的鷹架。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 7 · 02 (Self-Attention), Phase 7 · 03 (Multi-Head Attention), Phase 7 · 04 (Positional Encoding)
**Time:** ~75 minutes

## The Problem｜問題

單一注意力層是特徵（feature）抽取器，不是一個模型。每一層一次矩陣乘法，對語言的容量不夠。你需要深度——深度沒有正確的接法就會壞。

2017 年 Vaswani 論文把六個設計決定包成一塊，把一層注意力變成可以疊的區塊。之後每一個 transformer——只有編碼器（encoder）的（BERT）、只有解碼器（decoder）的（GPT）、編碼器–解碼器的（T5）——繼承同一副骨架。2026 年的區塊被修過（RMSNorm、SwiGLU、pre-norm、RoPE），骨架還是同一個。

這一課是骨架。後面的課把它專門化——06 是編碼器，07 是解碼器，08 是編碼器–解碼器。

## The Concept｜核心概念

![Encoder and decoder block internals, wired](../assets/full-transformer.svg)

### 六個零件

1. **Embedding 加位置訊號。** Token 變成向量。位置用 RoPE（現代）或正弦（經典）注入。
2. **自注意力。** 每個位置注意其他每個位置。解碼器裡要遮罩。
3. **前饋網路（FFN）。** 位置上的兩層 MLP：`W_2 · activation(W_1 · x)`。預設展開倍率 4 倍。
4. **殘差連接。** `x + sublayer(x)`。沒有它，大約 6 層之後梯度就消失（vanishing gradient）。
5. **層正規化（layer normalization）。** `LayerNorm` 或 `RMSNorm`（現代）。穩住殘差流。
6. **交叉注意力，只有解碼器有。** 查詢來自解碼器，鍵和值來自編碼器的輸出。

看一個向量流過一個區塊：注意力在位置之間混合，殘差把它往前帶，前饋把它變換，正規化讓這條流保持穩定。

```figure
transformer-block
```

### 編碼器區塊（BERT、T5 的編碼器用）

```
x → LN → MHA(self) → + → LN → FFN → + → out
                     ^              ^
                     |              |
                     └── residual ──┘
```

編碼器是雙向的。沒有遮罩。所有位置都看得到所有位置。

### 解碼器區塊（GPT、T5 的解碼器用）

```
x → LN → MHA(masked self) → + → LN → MHA(cross to encoder) → + → LN → FFN → + → out
```

解碼器每個區塊有三個子層。中間那個——交叉注意力——是資訊從編碼器流到解碼器的唯一地方。在純解碼器架構（GPT）裡，交叉注意力被拿掉，只剩遮罩過的自注意力加前饋。

### Pre-norm 對 post-norm

原始論文：`x + sublayer(LN(x))` 對 `LN(x + sublayer(x))`。Post-norm 大約在 2019 年失寵——沒有小心的暖身，很難訓練得很深。Pre-norm（子層之前先做 `LN`）是 2026 年的預設：Llama、Qwen、GPT-3 以後、Mistral 都用它。

### 2026 年現代化的區塊

Vaswani 2017 交付的是 LayerNorm 加 ReLU。現代的堆疊兩個都換了。正式環境（production）的區塊實際長這樣：

| 元件 | 2017 | 2026 |
|-----------|------|------|
| 正規化 | LayerNorm | RMSNorm |
| 前饋的活化（activation） | ReLU | SwiGLU |
| 前饋展開 | 4 倍 | 2.6 倍（SwiGLU 用三個矩陣，總參數對得上） |
| 位置 | 絕對正弦 | RoPE |
| 注意力 | 完整 MHA | GQA（或 MLA） |
| 偏置（bias）項 | 有 | 沒有 |

RMSNorm 拿掉 LayerNorm 的減平均數（mean），少一次減法，省計算，經驗上至少一樣穩。SwiGLU（`Swish(W1 x) ⊙ W3 x`）在 Llama、PaLM、Qwen 的論文裡，困惑度（perplexity）穩定比 ReLU／GELU 的前饋好大約 0.5 點。

### 參數數量

一個區塊，`d_model = d`、前饋展開 `r`：

- MHA：`4 · d²`（Q、K、V、O 投影）
- 前饋（SwiGLU）：`3 · d · (r · d)` ≈ `3rd²`
- 正規化：可忽略

在 `d = 4096, r = 2.6, layers = 32`（大約 Llama 3 8B），總共：`32 · (4·4096² + 3·2.6·4096²) ≈ 32 · (16 + 32) M = ~1.5B parameters per layer × 32 ≈ 7B`（再加上 embedding 和輸出頭）。和公開的數字相符。

## Build It｜動手實作

### 步驟 1：積木

用第 3 課那個很小的 `Matrix` 類別（為了獨立，複製到這個檔案）：

- `layer_norm(x, eps=1e-5)`——減平均數，除以標準差。
- `rms_norm(x, eps=1e-6)`——除以 RMS。不減平均數。
- `gelu(x)` 和 `silu(x) * W3 x`（SwiGLU）。
- `ffn_swiglu(x, W1, W2, W3)`。
- `encoder_block(x, params)` 和 `decoder_block(x, enc_out, params)`。

完整接線見 `code/main.py`。

### 步驟 2：接一個 2 層編碼器和一個 2 層解碼器

把它們疊起來。把編碼器輸出送進解碼器的每一次交叉注意力。輸出投影之前加一層最後的 LN。

```python
def encode(tokens, params):
    x = embed(tokens, params.emb) + sinusoidal(len(tokens), params.d)
    for block in params.encoder_blocks:
        x = encoder_block(x, block)
    return x

def decode(target_tokens, encoder_out, params):
    x = embed(target_tokens, params.emb) + sinusoidal(len(target_tokens), params.d)
    for block in params.decoder_blocks:
        x = decoder_block(x, encoder_out, block)
    return x
```

### 步驟 3：在一個玩具例子上跑前向

送進 6 個 token 的來源和 5 個 token 的目標。確認輸出形狀是 `(5, vocab)`。不訓練——這一課講的是架構，不是損失（loss）。

### 步驟 4：換成 RMSNorm 加 SwiGLU

把 LayerNorm 和 ReLU 前饋換成 RMSNorm 和 SwiGLU。確認形狀仍然相符。這就是 2026 年的現代化，換一個函式。

## Use It｜實際應用

PyTorch／TF 的參考實作：`nn.TransformerEncoderLayer`、`nn.TransformerDecoderLayer`。但 2026 年大多數正式環境程式碼自己寫區塊，因為：

- Flash Attention 是在注意力裡面呼叫，不經 `nn.MultiheadAttention`。
- GQA／MLA 不在標準函式庫（library）的參考實作裡。
- RoPE、RMSNorm、SwiGLU 不是 PyTorch 的預設。

HF `transformers` 有乾淨的參考區塊，你應該讀：`modeling_llama.py` 是 2026 年標準的純解碼器區塊。大約 500 行，值得走一次。

**編碼器、解碼器、編碼器–解碼器——何時選哪個：**

| 需求 | 選 | 例子 |
|------|------|---------|
| 分類、embedding、文字上的問答 | 只有編碼器 | BERT、DeBERTa、ModernBERT |
| 文字生成、聊天、程式碼、推理 | 只有解碼器 | GPT、Llama、Claude、Qwen |
| 結構化輸入到結構化輸出（翻譯、摘要） | 編碼器–解碼器 | T5、BART、Whisper |

只有解碼器贏了語言，因為它縮放最乾淨，理解和生成都做得到。當輸入有清楚的「來源序列」身份時（翻譯、語音辨識、結構化任務），編碼器–解碼器仍然最好。

## Ship It｜交付成果

見 `outputs/skill-transformer-block-reviewer.md`。這個 skill 用 2026 年的預設審查一個新的 transformer 區塊實作，並標出缺的零件（pre-norm、RoPE、RMSNorm、GQA、前饋展開倍率）。

## Exercises｜練習

1. **簡單。** 數你的 encoder_block 在 `d_model=512, n_heads=8, ffn_expansion=4, swiglu=True` 的參數。實作這個區塊，用 `sum(p.numel() for p in block.parameters())` 驗證。
2. **中等。** 從 post-norm 換成 pre-norm。兩邊都初始化，在隨機輸入上量疊了 12 層之後的活化範數。Post-norm 的活化應該爆掉；pre-norm 的應該保持有界。
3. **困難。** 在玩具複製任務上實作 4 層編碼器–解碼器（把 `x` 反過來複製）。訓練 100 步。報告損失。換成 RMSNorm 加 SwiGLU 加 RoPE——損失會不會下降？

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 區塊 | 「一層 transformer」 | 正規化加注意力加正規化加前饋的一疊，用殘差連接包起來。 |
| 殘差 | 「跳接」 | 輸出 `x + f(x)`；讓梯度能流過很深的堆疊。 |
| Pre-norm | 「先正規化，不是事後」 | 現代寫法：`x + sublayer(LN(x))`。不用暖身的花招也能訓練得更深。 |
| RMSNorm | 「沒有平均數的 LayerNorm」 | 除以 RMS；少一次運算，經驗上的穩定性一樣。 |
| SwiGLU | 「大家都換過去的前饋」 | `Swish(W1 x) ⊙ W3 x → W2`。在語言模型困惑度上贏過 ReLU／GELU。 |
| 交叉注意力 | 「解碼器怎麼看見編碼器」 | Q 來自解碼器、K／V 來自編碼器輸出的 MHA。 |
| 前饋展開 | 「中間的 MLP 有多寬」 | 隱藏寬度對 d_model 的倍率，通常是 4（LayerNorm）或 2.6（SwiGLU）。 |
| 無偏置 | 「丟掉 +b 項」 | 現代堆疊在線性層省掉偏置；困惑度略好，模型略小。 |

## Further Reading｜延伸閱讀

- [Vaswani et al. (2017). Attention Is All You Need](https://arxiv.org/abs/1706.03762) ——原始的區塊規格。
- [Xiong et al. (2020). On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745) ——為什麼深了以後 pre-norm 贏過 post-norm。
- [Zhang, Sennrich (2019). Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467) ——RMSNorm。
- [Shazeer (2020). GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) ——SwiGLU 論文。
- [HuggingFace `modeling_llama.py`](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py) ——2026 年標準的純解碼器區塊。
