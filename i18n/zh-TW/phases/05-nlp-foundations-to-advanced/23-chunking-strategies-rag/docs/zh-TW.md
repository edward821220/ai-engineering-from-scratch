# RAG 的切塊策略

> 切塊的設定對檢索品質的影響，和選哪個 embedding 模型一樣大（Vectara，NAACL 2025）。切塊切錯，再多的重排（reranking）也救不了你。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 5 · 14 (Information Retrieval), Phase 5 · 22 (Embedding Models)
**Time:** ~60 minutes

## The Problem｜問題

你把一份 50 頁的合約放進 RAG 系統。使用者問：「What is the termination clause?」。檢索器回傳封面。為什麼？因為模型是在 512 token 的區塊上訓練的，終止條款在 20 頁之後，被換頁切開，附近沒有局部關鍵字把它和查詢綁在一起。

修法不是「買一個更好的 embedding 模型」。修法是切塊。多大？重疊多少？在哪裡切開？要不要帶周圍的脈絡？

2026 年 2 月的評測給出令人意外的結果：

- Vectara 2026 的研究：遞迴的 512 token 切塊，以 69% 的準確率（accuracy）贏過語意切塊的 54%。
- SPLADE 加 Mistral-8B 在 Natural Questions 上：重疊測不到任何好處。
- 脈絡斷崖：回應品質在大約 2,500 個 token 的脈絡附近陡掉。

「看起來明顯」的答案（語意切塊、20% 重疊、1000 個 token）常常是錯的。這一課為六種策略建立直覺，並告訴你何時該伸手拿哪一種。

## The Concept｜核心概念

![Six chunking strategies visualized on one passage](../assets/chunking.svg)

**固定切塊。** 每 N 個字元或 token 切一次。最簡單的基準模型（baseline）。會從句子中間切開。壓縮好，連貫差。

**遞迴。** LangChain 的 `RecursiveCharacterTextSplitter`。先試 `\n\n`，再 `\n`，再 `.`，再空白。退得乾淨。2026 年的預設。

**語意。** 把每個句子做成 embedding。算相鄰句子的餘弦（cosine）相似度。相似度掉到閾值（threshold）以下就切開。保住主題連貫。較慢；有時產出 40 個 token 的小碎片，傷檢索。

**句子。** 在句子邊界切開。一塊一句，或 N 句的視窗。到大約 5000 個 token 為止，和語意切塊不相上下，成本只是一小部分。

**父文件。** 檢索存小的子區塊，*並且*為脈絡存較大的父區塊。用子區塊檢索；回傳父區塊。壞掉時退得穩：子區塊不好，回傳的父區塊仍合理。

**晚切塊（2024）。** 先在 token 層級把整份文件做成 embedding，再把 token 的 embedding 聚成區塊的 embedding。保住跨區塊的脈絡。搭配長脈絡的 embedder（BGE-M3、Jina v3）。計算量較高。

**脈絡式檢索（Anthropic，2024）。** 在每個區塊前面加上 LLM 生成的、說明它在文件裡位置的摘要（「This chunk is section 3.2 of the termination clauses...」）。在 Anthropic 自己的評測裡，檢索改善 35% 到 50%。建索引很貴。

### 贏過每個預設的那條規則

區塊大小要配問句類型：

| 問句類型 | 區塊大小 |
|------------|-----------|
| 事實題（「執行長叫什麼名字？」） | 256 到 512 個 token |
| 分析／多跳 | 512 到 1024 個 token |
| 整節理解 | 1024 到 2048 個 token |

NVIDIA 2026 的評測。區塊要大到裝得下答案加上局部脈絡，小到檢索器的前 K 名聚焦在答案上，而不是脈絡雜訊。

```figure
n5-chunk-cuts
```

## Build It｜動手實作

### 步驟 1：固定切塊和遞迴切塊

```python
def chunk_fixed(text, size=512, overlap=0):
    step = size - overlap
    return [text[i:i + size] for i in range(0, len(text), step)]


def chunk_recursive(text, size=512, seps=("\n\n", "\n", ". ", " ")):
    if len(text) <= size:
        return [text]
    for sep in seps:
        if sep not in text:
            continue
        parts = text.split(sep)
        chunks = []
        buf = ""
        for p in parts:
            if len(p) > size:
                if buf:
                    chunks.append(buf)
                    buf = ""
                chunks.extend(chunk_recursive(p, size=size, seps=seps[1:] or (" ",)))
                continue
            candidate = buf + sep + p if buf else p
            if len(candidate) <= size:
                buf = candidate
            else:
                if buf:
                    chunks.append(buf)
                buf = p
        if buf:
            chunks.append(buf)
        return [c for c in chunks if c.strip()]
    return chunk_fixed(text, size)
```

### 步驟 2：語意切塊

```python
def chunk_semantic(text, encoder, threshold=0.6, min_chars=200, max_chars=2048):
    sentences = split_sentences(text)
    if not sentences:
        return []
    embs = encoder.encode(sentences, normalize_embeddings=True)
    chunks = [[sentences[0]]]
    for i in range(1, len(sentences)):
        sim = float(embs[i] @ embs[i - 1])
        current_len = sum(len(s) for s in chunks[-1])
        if sim < threshold and current_len >= min_chars:
            chunks.append([sentences[i]])
        else:
            chunks[-1].append(sentences[i])

    result = []
    for group in chunks:
        text_group = " ".join(group)
        if len(text_group) > max_chars:
            result.extend(chunk_recursive(text_group, size=max_chars))
        else:
            result.append(text_group)
    return result
```

在你的領域上調校 `threshold`。太高，就碎掉。太低，就變成一大塊。

### 步驟 3：父文件

```python
def chunk_parent_child(text, parent_size=2048, child_size=256):
    parents = chunk_recursive(text, size=parent_size)
    mapping = []
    for p_idx, parent in enumerate(parents):
        children = chunk_recursive(parent, size=child_size)
        for child in children:
            mapping.append({"child": child, "parent_idx": p_idx, "parent": parent})
    return mapping


def retrieve_parent(child_query, mapping, encoder, top_k=3):
    child_embs = encoder.encode([m["child"] for m in mapping], normalize_embeddings=True)
    q_emb = encoder.encode([child_query], normalize_embeddings=True)[0]
    scores = child_embs @ q_emb
    top = np.argsort(-scores)[:top_k]
    seen, parents = set(), []
    for i in top:
        if mapping[i]["parent_idx"] not in seen:
            parents.append(mapping[i]["parent"])
            seen.add(mapping[i]["parent_idx"])
    return parents
```

關鍵洞見：父區塊要去重。多個子區塊可以對到同一個父區塊；全部回傳會浪費脈絡。

### 步驟 4：脈絡式檢索（Anthropic 的模式）

```python
def contextualize_chunks(document, chunks, llm):
    context_prompts = [
        f"""<document>{document}</document>
Here is the chunk to situate: <chunk>{c}</chunk>
Write 50-100 words placing this chunk in the document's context."""
        for c in chunks
    ]
    contexts = llm.batch(context_prompts)
    return [f"{ctx}\n\n{c}" for ctx, c in zip(contexts, chunks)]
```

為加上脈絡的區塊建索引。查詢時，檢索受惠於額外的周圍訊號。

### 步驟 5：評估

```python
def recall_at_k(queries, corpus_chunks, encoder, k=5):
    chunk_embs = encoder.encode(corpus_chunks, normalize_embeddings=True)
    hits = 0
    for q_text, gold_idxs in queries:
        q_emb = encoder.encode([q_text], normalize_embeddings=True)[0]
        top = np.argsort(-(chunk_embs @ q_emb))[:k]
        if any(i in gold_idxs for i in top):
            hits += 1
    return hits / len(queries)
```

永遠要評測。對你的語料庫（corpus）最好的策略，可能和任何部落格文章都不一樣。

## 坑

- **只在事實問句上評估切塊。** 多跳問句會露出很不一樣的贏家。用按問句類型分層的評估集。
- **語意切塊沒有最小大小。** 會產出 40 個 token 的碎片，傷檢索。永遠強制 `min_tokens`。
- **把重疊當迷信。** 2026 年的研究發現，重疊常常沒有好處，還把索引成本加倍。要量，不要假設。
- **沒有最小和最大。** 5 個 token 或 5000 個 token 的區塊都會弄壞檢索。要夾住。
- **跨文件切塊。** 永遠不要讓一個區塊跨兩份文件。先按文件切，再合併。

## Use It｜實際應用

2026 年的組合：

| 情況 | 策略 |
|-----------|----------|
| 第一次做、語料庫未知 | 遞迴，512 個 token，不重疊 |
| 事實問答 | 遞迴，256 到 512 個 token |
| 分析／多跳 | 遞迴，512 到 1024 個 token，加父文件 |
| 交叉參照很多（合約、論文） | 晚切塊或脈絡式檢索 |
| 對話語料庫 | 以輪次為單位的區塊，加說話者的後設資料 |
| 短語（推文、評論） | 一份文件就是一個區塊 |

從遞迴 512 開始。在 50 個查詢的評估集上量前 5 的召回率（recall）。再從那裡調校。

## Ship It｜交付成果

存成 `outputs/skill-chunker.md`：

```markdown
---
name: chunker
description: Pick a chunking strategy, size, and overlap for a given corpus and query distribution.
version: 1.0.0
phase: 5
lesson: 23
tags: [nlp, rag, chunking]
---

Given a corpus (document types, avg length, domain) and query distribution (factoid / analytical / multi-hop), output:

1. Strategy. Recursive / sentence / semantic / parent-document / late / contextual. Reason.
2. Chunk size. Token count. Reason tied to query type.
3. Overlap. Default 0; justify if >0.
4. Min/max enforcement. `min_tokens`, `max_tokens` guards.
5. Evaluation plan. Recall@5 on 50-query stratified eval set (factoid, analytical, multi-hop).

Refuse any chunking strategy without min/max chunk size enforcement. Refuse overlap above 20% without an ablation showing it helps. Flag semantic chunking recommendations without a min-token floor.
```

## Exercises｜練習

1. **簡單。** 用固定（512，0）、遞迴（512，0）、遞迴（512，100）切一份 20 頁的文件。比較區塊數和邊界品質。
2. **中等。** 在 5 份文件上做 30 個查詢的評估集。量遞迴、語意、父文件的前 5 召回率。誰贏？和部落格文章一樣嗎？
3. **困難。** 實作脈絡式檢索。量相對基準遞迴切塊的 MRR 改善。報告索引成本（LLM 呼叫次數）對上準確率增益。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 區塊 | 文件的一塊 | 被做成 embedding、建索引、再被檢索的次文件單位。 |
| 重疊 | 安全邊際 | 相鄰區塊共享的 N 個 token；在 2026 年的評測裡常常沒用。 |
| 語意切塊 | 聰明的切塊 | 在相鄰句子的 embedding 相似度下跌處切開。 |
| 父文件 | 兩層檢索 | 檢索小的子區塊，回傳較大的父區塊。 |
| 晚切塊 | 先做 embedding 再切 | 在 token 層級為整份文件做 embedding，再聚成區塊向量。 |
| 脈絡式檢索 | Anthropic 的那一招 | 索引前，把 LLM 生成的摘要加在每個區塊前面。 |
| 脈絡斷崖 | 2500 token 的牆 | RAG 裡、大約 2,500 個脈絡 token 觀察到的品質下跌（2026 年 1 月）。 |

## Further Reading｜延伸閱讀

- [Yepes et al. / LangChain — Recursive Character Splitting docs](https://python.langchain.com/docs/how_to/recursive_text_splitter/) ——正式環境（production）的預設。
- [Vectara (2024, NAACL 2025). Chunking configurations analysis](https://arxiv.org/abs/2410.13070) ——切塊和選 embedding 一樣要緊。
- [Jina AI — Late Chunking in Long-Context Embedding Models (2024)](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) ——晚切塊論文。
- [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) ——用 LLM 生成的脈絡前綴，檢索改善 35% 到 50%。
- [NVIDIA 2026 chunk-size benchmark — Premai summary](https://blog.premai.io/rag-chunking-strategies-the-2026-benchmark-guide/) ——依問句類型決定區塊大小。
