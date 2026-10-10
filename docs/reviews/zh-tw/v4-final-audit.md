# zh-TW 終態複審（v4-final-audit）：phases 08 / 09 / 10 / 11（共 68 課）

- 譯稿：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`；原文：同路徑 `en.md`（`/private/tmp/aiefs-main-source/phases/`）。
- 依據：`docs/reviews/zh-tw/r1.md`（phase 10，含處置標注）、`docs/reviews/zh-tw/r3.md`（08/09/11，含處置標注；與 /private/tmp 舊版不同，採 docs 版，與 v3 稽核一致）、`v1-kept-audit.md`（phase 10 kept 稽核）、`v3-kept-audit.md`（08/09/11 kept 稽核 K042–K133）、`f1-changelog.md`、`f3-changelog.md`、`f4-changelog.md`、`f4-before/` 快照、`GLOSSARY.md`、`STYLE.md`。
- 唯讀：未編輯任何譯稿或 repo 檔案。輔助腳本與掃描輸出位於 `/private/tmp/zh-tw-review/v4-scratch/`。
- 行號：一律為現況 zh-TW.md 行號（以關鍵字定位）。

## 判定類別

- `[verified]`：註記已修復，現況確實改好且未改錯；或 kept 項已由 kept 稽核判 miss 並於 f1/f3 修好。
- `[not-fixed]`：註記已修復（或 kept 項經稽核判 miss），現況仍有問題，含假修復、修錯、疊註、疊字、殘句、占位符殘留。
- `[kept-ok]`：維持原樣，複審同意（含 borderline 且語意可接受者）。
- `[kept-wrong]`：維持原樣，但複審認為仍應修。
- `[new-issue]`：r1/r3 未提，現況有明確錯誤。
- `[存疑]`：本輪無法逐字核對（見下方「覆蓋與限制」），未以推測定案，需後續補查。

## 覆蓋與限制（必讀）

1. phase 10（24 課、206 條 finding）：逐條以腳本（坏文字／好文字存在性、首見英文附註）加 Grep／Read 行文核對判定。
2. 全卷 68 課機械掃描：疊字、疊註、三連字、英文殘留、GLOSSARY 禁用／譯法殘留、字串存在性；f1/f3/f4 變更日誌 828 條逐條核對「新文是否仍在現況」——腳本於 bash 權限中斷前完成。
3. 08 課（42 條）：腳本＋Grep 核對，可判定者已判定。
4. 09、11 課（127 條）：GLOSSARY 殘留（政策、報酬、提供者、噪聲、基底、門檻、叢集等）與 kept 稽核點名句以 Grep 核對；首見附英文與 P2 風格列表項未逐條核對，標 `[存疑]`（09：27 條；11：51 條）。
5. 執行中 bash 工具曾被權限層要求審批而阻斷（python3 呼叫被擋），之後改以 Grep／Read 續查；未能再執行腳本的項目一律標 `[存疑]`，不以推測定案。
6. 不計入判定：程式碼、行內碼、數學式、URL、參考文獻英文標題、圖片 alt（已定策保留英文）、Mermaid timeline、受保護內容的英文。

---

## phases/10-llms-from-scratch/01-tokenizers
- [verified] P0 「每秒處理數百萬次請求」→ z186「對於服務數百萬次請求的模型而言」，增譯「每秒」已移除。
- [kept-ok] P1 模型比較表整表英文（kept）→ z190–197 表頭已譯為繁中、模型名與數值保留；kept-audit 判 ok，問題已不存在。
- [verified] P1 「推論」首見 → z25「推論（inference）」已附英文。
- [verified] P1 「注意力容量」（kept，kept-audit miss）→ z35「注意力（attention）容量」已附英文（f1 已修）。
- [kept-ok] P1 「壓縮演算法」（kept）→ z55 通用 CS 詞，判準 5 可不加註；kept-audit ok。
- [verified] P1 「訓練語料庫」→ z57「訓練語料庫（training corpus）」。
- [verified] P1 「參數」→ 首見 z13「參數（parameter）」已附英文，全課 4 處皆附。
- [verified] P1 「壓縮比」「分布」（kept，kept-audit miss）→ z320、z471「壓縮率（compression ratio）」，GLOSSARY 一致；「分布」kept-ok。
- [verified] P2 「乘載著意義」→ z3「承載意義」。
- [verified] P2 「在何處崩潰」→ z14「在哪些情況下失效」。
- [verified] P2 「被重新挪用在 tokenization 上」→ z55「後來改用於 tokenization」，句內無疊字。
- [verified] P2 「產詞率（Fertility）」（kept，kept-audit miss）→ z467 表格改為保留「Fertility」並定義為「每個字詞的平均 token 數」；GLOSSARY 禁用「產詞率」已遵守。

## phases/10-llms-from-scratch/02-building-a-tokenizer
- [verified] P1 「效能瓶頸」→ z23「效能瓶頸（bottleneck）」。
- [verified] P1 「位元組」→ 首見 z13「位元組（byte）層級回退（byte-level fallback）」。
- [verified] P1 「正規化」→ z12「正規化（normalization）」。
- [verified] P1 「256 個項目」→ z65「256 個位元組值」，GLOSSARY 相容。
- [verified] P1 「分布」→ z139「訓練分布（distribution）」已附英文。
- [verified] P2 「它會崩潰」→ z21「它就失效了」。
- [verified] P2 「預先切分與子詞切分串接在一起」→ z23「把預先切分與子詞切分串成一條管線」。
- [kept-ok] P2 「剛好就是 256 個項目」（kept）→ z65 已改為「位元組值」，kept-audit ok。
- [verified] P2 字元映射 `G` 改為 `Ġ`（kept，kept-audit miss）→ z67 現況已恢復為源文「G」，未見自行修正痕跡（kept-audit miss 已解）。

## phases/10-llms-from-scratch/03-data-pipelines
- [not-fixed] P1 「準確率與召回率」→ 修法已改為「精確率」，但 z287 現為「參數控制了精確率與召回率之間的權衡之間的權衡」，「之間的權衡」疊寫（new-issue 合併於此）。
- [verified] P1 「移除無關文字內容」→ z190「移除非文字內容」。
- [verified] P1 「壓縮比」→ z347、z387「壓縮率（compression ratio）」。
- [verified] P1 「模型／資料管線」（kept，kept-audit miss）→ z1 標題「預訓練資料管線（pipeline）」、z3「模型（model）」首見已附英文。
- [verified] P1 「串流」→ z12「串流（streaming）」。
- [verified] P2 「不是一個小型資料集」→ z21「不是一個資料集」。
- [verified] P2 「刪除所有標記語言」→ z83「移除所有標記」。
- [verified] P2 「它在推理上就會崩潰」→ z47「它就無法勝任推理」。
- [verified] P2 「較小的模型在日後的所有服務中都更加便宜」→ z180「較小的模型長期提供推論服務的成本更低」。
- [verified] P2 「訓練迴圈所消耗的資料輸入」→ z319「訓練迴圈會從這裡取得資料」。
- [not-fixed] P2 「有多少是真實資料，相對於填充內容的比例」→ 修法為「打包序列中實際資料所占的比例」，但 z389 現為「打包後的序列中打包序列中實際資料所占的比例」，「打包序列中」疊寫（new-issue）。

## phases/10-llms-from-scratch/04-pre-training-mini-gpt
- [verified] P1 「偏差參數」→ z527「偏置參數」，依 GLOSSARY bias=偏置。
- [verified] P1 「下一個 token 預測任務」→ z13 保留「next-token prediction」（GLOSSARY 保留英文）；附註：「的next-token prediction，」與中文間缺半形空格（格式，低）。
- [verified] P1 「反向傳播」→ z23、z201「反向傳遞（backward pass）」，GLOSSARY 一致。
- [verified] P1 「模型」「推論」首見（kept，kept-audit miss）→ z3「模型（model）」、z146「推論（inference）」已附英文。
- [verified] P2 「我乘載什麼資訊？」→ z94「我承載什麼資訊？」。
- [verified] P2 「通過 12 個 transformer 區塊」→ z41「經過 12 個 transformer 區塊」。
- [verified] P2 「因為記憶體頻寬才是限制瓶頸」→ z160「因為瓶頸在記憶體頻寬」。
- [verified] P2 「高原期」→ z513「平台期」。

## phases/10-llms-from-scratch/05-scaling-distributed
- [verified] P0 「每張 GPU 產生不同區塊的行」→ z308「每張 GPU 產生不同區塊的欄」，方向已更正。
- [verified] P0 「行平行／列平行」→ z310「欄平行（column-parallel）」「列平行（row-parallel）」，與輸入／輸出維度說明一致。
- [kept-ok] P1 英文殘句（27、217、546）（kept）→ 現況已譯為中文，無英文整句殘留（kept-audit ok）。
- [verified] P1 「規約（求和）」→ z561「歸約（求和）」，GLOSSARY reduction 一致。
- [verified] P1 「梯度同步」「模型狀態」首見（kept，kept-audit miss）→ z13「梯度同步（gradient synchronization）」、z15「模型狀態（model states）」。
- [not-fixed] P1 「滑動平均／滑動變異數」「前向傳遞／反向傳播」首見附英文 → z44「一個滑動平均（m）與一個滑動變異數（v）」仍未附 moving mean/variance；z19「反向傳播」、z23「前向傳遞」首見仍未附英文，且「反向傳播」未依 GLOSSARY 統一為「反向傳遞」。
- [verified] P2 「Meta 使用 16,384 張 GPU 並非炫耀，而是迫不得已」→ z46「不是因為想用，而是因為不得不用」。
- [verified] P2 「徹底掌握其底層機制」→ z29「了解各策略的運作機制」。
- [verified] P2 「初期階段閒置而後期階段正在計算」→ z314「前段階段閒置、後段階段仍在計算」（用語略生硬，非錯誤）。

## phases/10-llms-from-scratch/06-instruction-tuning-sft
- [verified] P1 「基底模型」→ 全課已改「基模型」（z3、z21、z393 等），無「基底模型」殘留。
- [verified] P1 「Total cost: $600...」英文殘句（kept，kept-audit miss）→ z25 已完整譯為「總成本僅 600 美元，訓練數小時即產出能遵循指令、回答問題並進行對話的聊天機器人……」，英文已移除。
- [verified] P1 「監督式 fine-tuning」首見附全稱 → z12「監督式 fine-tuning（Supervised Fine-Tuning）（SFT）」正確；但同一修法使 z33、z589 疊註，見下方 new-issue。
- [verified] P2 「產生相應的成果」→ z43「產生續寫內容」。
- [verified] P2 「Vicuna 就是在…上訓練出來的」→ z77「Vicuna 使用從使用者分享的 ChatGPT 對話記錄中蒐集的 70,000 段 ShareGPT 對話進行訓練」。
- [verified] P2 「預測序列中的每一個下一個 token」→ z106「預測序列中的每個後續 token」。
- [kept-wrong] P2 「整整小了 15 倍／低了 15 倍」（kept，borderline）→ z391 仍為「相較於預訓練中使用的 3e-4，整整小了 15 倍」；en 為「15x smaller」，「整整」為原文沒有的強調，且「小了 15 倍」易被讀成減去（低）。z132「SFT 的學習率低了 15 倍」同理。
- [verified] P2 「更小的更新步伐」→ z142「更小的更新幅度」。
- [kept-ok] P2 「擊敗了……範例」（kept，borderline）→ z27 仍為「擊敗了」，屬臺灣科技媒體常見用法，語意可接受。

## phases/10-llms-from-scratch/07-rlhf
- [verified] P1 Response A／Response B 全文英文（kept，kept-audit miss）→ z21、z23 已逐段譯為繁中，量子運算說明亦已對照。
- [verified] P1 「基底模型」→ z37「基模型」。
- [verified] P1 「訓練範例」→ z27「訓練樣本」。
- [verified] P1 「邊界差距（margin）」→ z605「分數間隔」，GLOSSARY margin 指間隔；此處依 r1 採分數間隔。
- [verified] P1 「獎勵模型」首見 → z1「獎勵模型（reward model）」。
- [verified] P2 「被挪用作為評分器」→ z75「改作評分器」。
- [verified] P2 「專挑這些盲點進行攻擊」→ z105「利用這些盲點」。
- [verified] P2 「單純在模式比對上湊合『高品質』的假象」（kept，kept-audit miss）→ z108「產生冗長、語氣正式卻空洞的回應，只在表面模式上貼近「高品質」」，已去除「湊合」「假象」的增義。
- [verified] P2 「它具有對整個（prompt，回應）序列最完整的語意表示」→ z266「它對整個（prompt，回應）序列的表示最完整」。
- [verified] P2 「在帶有 KL 懲罰下更新策略」→ z352「加入 KL 懲罰來更新策略」。

## phases/10-llms-from-scratch/08-dpo
- [verified] P1 「基底模型」→ z165、z169、z635、z639 已統一「基模型」（全課無「基底模型」殘留）。
- [verified] P1 「邊界差距（margin）」→ z310「分數間隔」。
- [verified] P1 「下一個 token 預測」→ z153 保留「next-token prediction」（附註：「標準next-token prediction損失」與中文間缺半形空格，低）。
- [verified] P1 「偏好配對」「策略模型」首見（kept，kept-audit miss）→ z3「偏好配對（preference pair）」「策略模型（policy model）」已附英文。
- [verified] P2 「參數量大其 10 倍模型」→ z169「參數量是其 10 倍的模型」。
- [verified] P2 「在線上迴圈中重新訓練」→ z145「在持續迭代的迴圈中重新訓練」。
- [not-fixed] P2 「不再分先做 SFT 再做 DPO」→ 修法為「ORPO 不必先做 SFT 再做 DPO」，但 z153 現為「ORPO ORPO 不必先做 SFT 再做 DPO」（疊字，new-issue）。
- [verified] P2 「正持續暴跌」→ z165「持續降低」。
- [verified] P2 「DPO 直接消耗此資料」→ z183「DPO 可直接使用這些資料」。
- [verified] P2 「訓練迴圈極其乾淨」→ z398「訓練迴圈簡潔許多」。
- [verified] P2 「beta 參數是 DPO 對應於 RLHF 中 KL 係數的等價物」→ z457「DPO 的 beta 參數對應於 RLHF 的 KL 係數」。

## phases/10-llms-from-scratch/09-constitutional-ai-self-improvement
- [kept-wrong] P1 「群組相對策略最佳化」（kept，borderline）→ 憲法式 AI 首見 z3 已附英文（verified）；但 z13「推導 GRPO 目標函數（DeepSeek-R1 的群組相對策略最佳化）」首見仍無英文全稱 group-relative policy optimization，依 STYLE 首見附英文，仍應補（低）。
- [verified] P2 「將大多數人類工作替換為模型本身」→ z3「以模型本身取代大部分人類參與」。
- [not-fixed] P2 「具有基於規則結果獎勵的可驗證推理軌跡」→ 修法為「產生可驗證的推理軌跡…」，但 z14 現為「產生產生可驗證的推理軌跡」（疊字）。
- [verified] P2 「同組兄弟樣本」→ z89「同組其他樣本」。
- [verified] P2 「評論者（critic）模型／批判器」→ z95「評論模型」、z187「批判模型」，統一完成。
- [verified] P2 「處理對其他方法抗拒的殘餘行為」→ z162「處理其他方法仍無法解決的殘餘行為」。
- [verified] P2 「手寫規則」→ z187「手寫評分規準」。
- [not-fixed] P2 「歷史年份」→ 修法為「首都、日期」，但 z310 現為「（首都、首都、日期）」（疊字，new-issue）。

## phases/10-llms-from-scratch/10-evaluation
- [verified] P1 「per judgment」→ z37「每次評判（$0.10–$2.00）」。
- [verified] P1 「真實性（faithfulness）」（kept，kept-audit miss）→ z113「忠實度（faithfulness，答案是否忠於檢索到的脈絡？）」。
- [verified] P1 「對多個模型提供者執行」→ z115「對多個模型執行」。
- [kept-ok] P2 「200 多萬張人類偏好選票」（kept，borderline）→ z37、z512、z519 仍為「張」「選票」用語；語意可解，kept-audit borderline（低）。
- [verified] P2 「訓練語料庫爬取整個網路」→ z60「訓練語料庫收錄了從網路爬取的內容」。
- [verified] P2 「數萬次此類比較」→ z88「數千次此類比較」。
- [verified] P2 「與人類之一致性」→ z131「與人類的一致性」。
- [verified] P2 「輸入文字」→ z35「輸入」。

## phases/10-llms-from-scratch/11-quantization
- [not-fixed] P1 「一列有較大數值而另一列有較小數值」→ 修法為「一欄／另一欄」，但 z106 現為「如果一欄／另一欄，較小數值的列就會失去大部分精度」：漏掉「有較大數值」「有較小數值」的條件子句，且「列」仍誤用（en 為 column／small values，應為「較小數值的欄」或「小值」）（new-issue：句意不完整）。同段 z529「GPTQ 一次量化一個列」亦為 column 誤作 row，修法未落實（同一 finding）。
- [verified] P1 「四捨五入誤差」→ z104「捨入誤差」，GLOSSARY rounding error 一致。
- [verified] P1 「權重」首見 → z3「模型權重（model weights）」已附英文（f4 C 亦已處理）。
- [verified] P2 「品質衝擊會隨序列長度等比擴大」→ z118「品質影響會隨序列長度增加而加重」。
- [verified] P2 「完美平衡了品質與體積」→ z163「在品質與檔案大小之間取得平衡」。
- [verified] P2 「輸出盲測對比」→ z196「輸出比較」。
- [kept-ok] P2 「記憶體減少 2／4／8 倍」（kept，borderline）→ z214、z216、z220 仍為「記憶體減少 2／4／8 倍」（z218 為 3.5 倍，與 en 一致）；kept-audit borderline，語意可讀（低）。

## phases/10-llms-from-scratch/12-inference-optimization
- [verified] P1 「a $25k/month inference bill from a $5k/month」英文片語（kept，kept-audit miss）→ z23「每月 2.5 萬美元的推論帳單…每月僅 5,000 美元的帳單」，英文已刪。
- [verified] P1 「Further Reading」五筆英文說明（kept，kept-audit miss）→ z777 起各篇說明已譯為繁中，保留作者與篇名。
- [verified] P1 「受限解碼」→ 全課無「受限解碼」殘留；z205「約束解碼與工具呼叫」。
- [not-fixed] P1 「Profiler」「記憶體分析器」→ 修法為「KV 快取記憶體效能分析器」，但 z626 標題現為「### 步驟 6：KV 快取KV 快取記憶體效能分析器」（疊字，new-issue）。
- [verified] P2 「載入每個權重複本」→ z58「每載入一個權重」。
- [verified] P2 「相當於直接省下一整張高階 GPU 的負載」→ z194 含修法句「每秒省下相當於 40 秒 GPU 運算的工作量」；但同句前段仍有「這每秒能省下 40 秒的 GPU 運算時間」，句意重複（new-issue，低）。
- [kept-ok] P2 「草稿與目標模型在位置 j 出現歧異」（kept）→ z161「若在位置 j 出現歧異，則接受前 j-1 個 token」，「歧異」精確（kept-audit ok）。

## phases/10-llms-from-scratch/13-building-complete-llm-pipeline
- [verified] P0 「一次 eval 指標回歸…數百萬美元的 GPU 預算」→ z21「可能讓團隊損失整整一週的實際耗時，以及一個月的 GPU 預算」，數字與時間單位已依原文；「整整」為輕度強調（低）。
- [verified] P1 「DeepSeek-V3 reported $5.6M」英文殘句 → z147「DeepSeek-V3 據報僅花費約 560 萬美元」，英文已移除。
- [verified] P1 「compile-time failures」→ z95「強型別產物與強型別簽章讓這些失誤在編譯期錯誤」。
- [verified] P1 「基底模型」→ z177「保留基模型」。
- [verified] P1 「對精度要求嚴格的安全評估採用 8 位元」→ z191「在精度差異會影響判斷的安全評估中採用 8 位元」。
- [verified] P2 「一週的時鐘時間」→ z21「一週的實際耗時」。
- [verified] P2 「背後的工程紀律卻極其宏大」→ z23「背後的工程紀律要求卻很高」。
- [verified] P2 「管線的純粹與強健」→ z117「維持管線流程可靠」。
- [verified] P2 「所節省的時鐘時間」→ z241「所節省的實際耗時」。

## phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs
- [verified] P1 「沒有偏差項（bias）」→ z59「沒有偏置項」。
- [verified] P1 「該腳本／腳本內建」→ z240「該程式檔」、z246「程式檔內建」。
- [verified] P1 「NTK-aware 插值」→ z67「內插（interpolation）」已附英文。
- [verified] P2 「這在業界早已定論，毫無爭議」→ z139 已刪除「業界定論」增譯，改為「因此較容易訓練深層模型」；但同句仍保留「顯然」且「更容易訓練……因此較容易訓練深層模型」重複（new-issue，低；en 為 strictly easier to train at depth）。
- [verified] P2 「完全沒有改變」→ z19「架構骨幹保持不變」。

## phases/10-llms-from-scratch/15-speculative-decoding-eagle3
- [not-fixed] P1 「回滾的開銷僅僅是重設指針」→ 修法為「回滾需處理每層、每頭的 KV 位元組，但…仍可忽略」，但 z59 現為錯亂句：「維護實體 KV 快取搭配維護實體 KV 快取與邏輯長度，拒絕時截斷邏輯長度，在拒絕時直接截斷邏輯長度。無論哪種方式，…但相較於前向傳遞成本仍可忽略，相對於前向傳遞而言微不足道」（new-issue：疊句、自相矛盾）。
- [kept-wrong] P1 「加速比」「接受率」「殘差分布」首見（kept）→ z15「加速比（speedup）」「殘差分布（residual distribution）」已附英文；但 z14「根據接受率 `α`」首見仍未附 acceptance rate（低）。
- [verified] P2 「能帶來 2 倍以上的額外加速」→ z25「加速效果可達廉價草稿模型的 2 倍」（數值依 en；同句又以「粗糙的草稿模型」指 cheap draft，用詞與 z25 後文「廉價」不一致，低）。
- [not-fixed] P2 「時鐘時間」→ 修法為「實際耗時」，z43「預期總實際耗時」已改；但 z155 現為「每個 token 的實際實際耗時」（疊字，new-issue）。
- [not-fixed] P2 「邏輯長度指針」→ 修法為「維護實體 KV 快取與邏輯長度，拒絕時截斷邏輯長度」，但 z59 同 P1 錯亂句，新文本身已重複（不能視為修正）。
- [verified] P2 「推測解碼相較於樸素解碼」→ z133「EAGLE-3 推測解碼相較於批次 64 的樸素解碼」。

## phases/10-llms-from-scratch/16-differential-attention-v2
- [kept-ok] P1 「雜訊底限會隨著脈絡長度線性增長」（kept）→ z12「為何該底限會隨著脈絡長度增長」，已無「線性」增譯（kept-audit ok）。
- [not-fixed] P1 「長脈絡精度／檢索精度」→ 修法為「長脈絡準確率」，但 z21「超過 32k 後大海撈針基準測試上的微幅精度衰退」仍以「精度」指基準準確率（r1 所指的同類用語，未改；en 為 accuracy）。
- [verified] P1 「差分注意力」首見 → z1「差分注意力（Differential Attention）（V2）」已附英文。
- [verified] P2 「隨著脈絡長度等比放大／等比擴大」→ z19「會隨脈絡長度增加而累積」、z84「其價值隨脈絡長度加重」。
- [verified] P2 「三個致命問題」→ z23「三個問題」。
- [verified] P2 「帶有數值穩定性減去最大值的 softmax」→ z108「先減去最大值以維持數值穩定的 softmax」。
- [verified] P2 「僅在維度記錄上記帳方式不同」→ z120「差別只在維度與形狀的記錄方式」。

## phases/10-llms-from-scratch/17-native-sparse-attention
- [verified] P1 「大跨度回想任務／長程回想能力」→ z21「長距離檢索任務上慘遭滑鐵盧」、z75「長程召回能力」（用詞已修；「慘遭滑鐵盧」為原文沒有的渲染，見 new-issue）。
- [verified] P2 「稀疏注意力顯然是唯一的答案」（kept，kept-audit miss）→ z21「稀疏注意力（Sparse attention）顯然是最直接的答案」。
- [verified] P2 「在未來的幾年內」→ z23「兩年後」。
- [not-fixed] P2 「加速比隨著序列長度線性擴大」及「效益隨序列長度等比擴大」→ z57 已修為「加速效果會隨序列長度增加而提升」，但 z71「效益隨序列長度等比擴大」仍在（r1 點名之一未改）。
- [verified] P2 「平均池化基準」→ z93「平均池化基準」，全課統一。

## phases/10-llms-from-scratch/18-multi-token-prediction
- [not-fixed] P1 「必須從頭訓練」→ 修法為「否（需重新訓練）」，但 z103 現為「否（否（需重新訓練））」（疊括號，new-issue）。
- [verified] P1 「主幹模型」→ z21「骨幹模型」，與 GLOSSARY backbone 一致。
- [verified] P1 「生成吞吐量」首見（kept，kept-audit miss）→ z3「生成吞吐量（throughput）」已附英文。
- [verified] P2 「被直接挪用為推測解碼草稿模型」→ z3「直接改作推測解碼的草稿模型」。
- [verified] P2 「預測下下個 token」→ z3「預測再下一個 token」。
- [not-fixed] P2 「位移偏移量 `k`」→ 修法為「位移 `k` 的真實 token」，但 z142 現為「相對於位移 `k` 的真實 token 的真實 token 的交叉熵」（疊句，new-issue）。
- [verified] P2 「將訓練好的 MTP 模組挪用為 EAGLE 風格的草稿模型」→ z181「改作 EAGLE 風格的草稿模型」。

## phases/10-llms-from-scratch/19-dualpipe-parallelism
- [verified] P1 「叢集」→ z3「群集」，GLOSSARY cluster 一致。
- [kept-wrong] P1 「記憶體」「瓶頸」「裝置」「前向傳遞／反向傳遞」首見（kept）→ 前向傳遞（z23）、瓶頸（z84）首見已附英文；但 z33「反向傳播（backward pass）」譯名與 GLOSSARY backward pass=「反向傳遞」不符（低）。
- [not-fixed] P2 「與它們所觸發的 all-to-all 通訊完美重疊」→ 修法為刪「完美」，但 z3 現為「能將前向與反向計算完美。」——「與…通訊重疊」整段被刪、「完美」仍在，句子殘缺（new-issue）。
- [not-fixed] P2 「三個相互疊加的致命瓶頸」→ 修法為刪「致命」，但 z19 現為「會遭遇致命：」——「三個相互疊加的瓶頸」整段被刪，「致命」仍在，句子殘缺（new-issue）。
- [verified] P2 「已是不可或缺的標配」→ z103「實務上幾乎不可或缺」。
- [verified] P2 「緊縮那些最落後的落後節點」→ z126「縮小落後 rank 造成的差距」。

## phases/10-llms-from-scratch/20-deepseek-v3-walkthrough
- [verified] P1 「偏差項／偏差張量」→ z56「偏置項」、z113「偏置張量」、z182「逐專家偏置項」，GLOSSARY 一致。
- [verified] P1 「無任何可測量的副作用」→ z58「未觀察到對主損失的可測量影響」。
- [verified] P1 「疊加了 D=1 個 MTP 模組」→ z62「加入 D = 1 的 MTP 模組」。
- [verified] P1 「低秩」「無輔助損失負載平衡」「隱藏狀態」首見（kept，kept-audit miss）→ z31「低秩（low-rank）」、z3「無輔助損失負載平衡（auxiliary-loss-free load balancing）」、z15「無輔助損失路由（Auxiliary-loss-free routing）」已附英文。
- [not-fixed] P2 「並在此之上加入了重大創新」→ 修法為刪「重大」，但 z3 現為「並在此之上加入了重大：多頭潛在注意力（MLA）…」——「重大」仍在，且「加入了重大：」句子殘缺（new-issue）。
- [verified] P2 「不可或缺的必備技能」→ z21「基本要求」。
- [not-fixed] P2 「在底層骨骼上完全一致」→ 修法為「基本架構與 Llama 或 Mistral 相同」，但 z27 現為「這與每一款 Llama 或 Mistral 基本架構與 Llama 或 Mistral 相同。」（重複，new-issue）。
- [not-fixed] P2 「巨額記憶體頻寬」「絕對的淨勝局」→ z50 「相較於所節省的所節省的記憶體頻寬」（疊字，new-issue），「這是絕對的淨勝局」仍在（未依修法改為「整體有利」）。
- [not-fixed] P2 「完美重疊」→ 修法為刪「完美」，但 z68 現為「能將前向與反向運算區塊與跨節點 all-to-all 通訊完美。」（殘句，「完美」仍在）（new-issue）。
- [not-fixed] P2 「延續……成功基石」（標註「已修復：現有譯文已採正確用語」）→ z140 現為「預期將延續 MLA + MoE + MTP 的成功基石」，評價用語仍在；標註與現況不符。

## phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer
- [verified] P1 「歷經三年的規模擴展依然歷久彌新…」→ z3「解釋為何這套混合配方能歷經三年擴展仍持續發展，而純 SSM 與純 Transformer 的長脈絡嘗試則未能延續」，對比已保留（「能…仍持續」略贅，低）。
- [not-fixed] P1 「長期經驗評估」→ 修法為「依據長脈絡實證評估所做的後續改進」，但 z72 現為「根據依據長脈絡實證評估所做的後續改進做出的後期改進」（疊詞「根據依據」，句子拗口，new-issue）。
- [verified] P1 Mamba-3 術語首見（kept，kept-audit miss）→ z3「複數值狀態空間（complex-valued state spaces）」「MIMO（multi-input multi-output）」、z15「指數梯形離散化（exponential-trapezoidal discretization）」「複數值狀態更新（complex-valued state update）」已附英文。
- [not-fixed] P2 「頻頻失守」→ 修法為「在某些類別的脈絡內檢索任務上表現不佳」，但 z21 現為「在某些類別的脈絡內檢索（in-context retrieval）上在某些類別的脈絡內檢索任務上表現不佳」（疊句，new-issue）。
- [verified] P2 「純 Transformer 完全勝任」→ z109「純 Transformer 即可」。
- [not-fixed] P2 「隨著 Mamba-3 修復了狀態追蹤能力」→ 修法為「Mamba-3 在狀態追蹤上的進展可能使…」，但 z123 現為「隨著 Mamba-3 修復了狀態追蹤能力，Mamba-3 在狀態追蹤上的進展可能使下一代混合架構進一步降低注意力比例」（保留原斷言且疊寫）。
- [not-fixed] P2 「嚴謹外推」→ 修法為刪「嚴謹」，但 z143 現為「並對各類假設變體進行了嚴謹。」（「嚴謹」仍在，句子殘缺，new-issue）。
- [verified] P2 「做出權威推薦」→ z153「提出建議」。

## phases/10-llms-from-scratch/22-async-hogwild-inference
- [verified] P1 「尚未被商業正式環境廣泛採用」（kept，kept-audit miss）→ z97「尚未進入商業正式環境」，語意已對齊原文。
- [verified] P1 「多代理」→ z3、z25、z163「多 agent（Multi-agent）」，與前文統一。
- [not-fixed] P1 「非嚴格線性依賴的比例」→ 修法為「總工作量中可平行處理的比例」，但 z185 現為「總工作量中總工作量中可平行處理的比例」（疊句，new-issue）。
- [kept-ok] P1 「推測解碼、投票集成、思維樹、行程」首見（kept）→ z3「推測解碼（speculative decoding）」、z25「投票集成（voting ensemble）」「思維樹（tree of thought）」已附英文；「行程」為通用 CS 詞。
- [verified] P2 「時鐘時間」（多處）→ 全課已改「實際耗時」（z14、z167 等），無「時鐘」殘留。
- [verified] P2 「每秒 35 個 token 的 decode 速度」→ z19「每秒 35 個 token 的解碼速度（decode speed）」。
- [verified] P2 「這使即時互動完全淪為空談」→ z19「模型仍不適合即時互動」。
- [not-fixed] P2 「沉重的顯式協調機制」→ 修法為刪「沉重的」，但 z25 現為「無一例外都引入了沉重的——投票規則、分岔與剪枝邏輯、agent 間的訊息傳遞協議」：「顯式協調機制」整詞被刪，「沉重的」懸空，句子殘缺（new-issue）。
- [not-fixed] P2 「雖然並非絕對，但頻率極高」→ 修法為「通常會……，但並非每次都會」，但 z41 現為「自發（通常會……，但並非每次都會）」——保留修法範本中的占位符「……」，動詞未補完（new-issue）。
- [verified] P2 「c 相對於單步 decode 時間必須極其微小」（kept，kept-audit miss）→ z70「`c` 相對於單步 decode 時間必須夠小」。
- [verified] P2 「節點內頻寬充足」→ z93「節點內同步可行」。
- [verified] P2 「具備極高的系統工程門檻」→ z97「需要不少系統工程工作」。
- [verified] P2 「相對於推測解碼已能穩定交付的加速幅度」→ z97「穩定」已刪除。
- [not-fixed] P2 「顯著高於」及「大獲全勝／嚴重虧損」→ 「顯著高於」已改「多於」（z167，verified）；但 z171 仍為「解釋為何一個是大獲全勝，另一個卻是嚴重虧損」，修法「有利／不利」未落實。
- [not-fixed] P2 「官方唯一真實開源程式碼庫」→ 修法為「論文實驗的參考實作」，但 z198 現為「該論文實驗的論文實驗的參考實作」（疊字，new-issue）。

## phases/10-llms-from-scratch/25-speculative-decoding
- [verified] P1 「測試期模擬（training-time test）」→ z88「測試期模擬（test-time simulation）」。
- [verified] P1 「推測解碼、拒絕抽樣、殘差分布、知識蒸餾」首見（kept，kept-audit miss）→ z3「推測解碼（speculative decoding，Leviathan 等人，2023 年）」、z29「拒絕取樣（rejection sampling）」、z30「殘差分布（residual distribution）」、z64「知識蒸餾（knowledge distillation）」已附英文，「拒絕抽樣」已依 GLOSSARY 改「拒絕取樣」。
- [verified] P2 「時鐘時間加速」→ z115「實際耗時加速」。
- [verified] P2 「顯著拉升了實質接受率」→ z86「提高有效接受率 α_effective」。
- [verified] P2 「拓撲遮罩僅消耗微不足道的額外 KV 條目」→ z92「只增加少量 KV 條目」。
- [verified] P2 「結構化輸出（JSON、SQL）」（kept，kept-audit miss）→ z107 已刪除 JSON、SQL 示例。
- [verified] P2 「一流通推測解碼」→ z165「原生提供完整的推測解碼支援」。
- [not-fixed] P2 「消除誤差累積」→ 修法為刪除，但 z200 現仍為「…訓練草稿模型去匹配目標模型測試期分布而非教師強制，消除誤差累積」（未刪）。
- [not-fixed] P2 「包含優雅證明」→ 修法為刪除，但 z205 現仍為「DeepMind 同期獨立發布、包含優雅證明的推測抽樣論文」（未刪）。

## phases/10-llms-from-scratch/34-gradient-checkpointing
- [kept-ok] P1 標題「梯度檢查點與活化值重算」首見英文（kept，borderline）→ z1 標題無英文，正文 z16 首見已附 Gradient checkpointing／activation recomputation；標題慣例可接受。
- [not-fixed] P1 「正在傳輸中最內層的層級（它們橫豎都必須立刻完成）」→ 修法為「管線階段中已在執行的最內層（這些運算本來就得完成）」，但 z91 現為「管線平行階段中管線階段中已在執行的最內層…」（疊句，new-issue）。
- [verified] P1 「參數梯度的誤差必須在機器精度層級嚴格為零」→ z272「參數梯度應在機器精度範圍內一致」。
- [not-fixed] P2 「記憶體崩潰（OOM）的深淵」「記憶體佔用……大幅暴跌」→ OOM 比喻已改為「活化值會把你推過這個上限」（z16）；但「記憶體佔用依檢查點分段與總層數的比例大幅暴跌」仍保留戲劇化「暴跌」，且「依比例」的歧義未說明（低）。
- [verified] P2 「天真全量檢查點」→ z31「簡單的全量檢查點做法」。
- [not-fixed] P2 「softmax 絕對主導了記憶體佔用」→ 修法為刪「絕對」，但 z44 現為「…僅隨長度呈線性增長。對於長序列，絕對。」（殘句：「絕對」懸空，主語與謂語缺失，new-issue）。
- [verified] P2 「2024 年後的幾乎所有前沿訓練執行作業」→ z48「2024 年以來多數前沿訓練作業」。
- [verified] P2 「一流通選項」→ z54「完整支援選項」。
- [not-fixed] P2 「權威包裝器」→ 修法為「PyTorch 的標準包裝器」，但 z261 現為「PyTorch 中的PyTorch 的標準包裝器」（疊字，new-issue）。
- [not-fixed] P2 「將活化值分片搬運至 CPU」→ 修法為刪「分片」，但 z263 現為「FSDP2 具備 `module.to_empty(device="cpu")` 與 `offload_policy`，分片 而非重算」——「分片」仍在，且句意與原文「卸載活化值而非重算」不符（new-issue）。
## phases/08-generative-ai/01-generative-models-taxonomy-history
- [not-fixed] P1（kept，K043）GLOSSARY：forward pass 應為「前向傳遞」、noise schedule 應為「雜訊排程」。GLOSSARY 部分已修（z26「一次前向傳遞」、z127「雜訊排程」）；但首見「前向傳遞」（z26）仍未附 forward pass（低）。
- [not-fixed] P2（已修復）風格：「瞇著眼看」「乾淨地疊在你腦子裡」「把界調高」「主力骨幹」等 8 條中仍有 4 條原樣殘留（低）。

## phases/08-generative-ai/02-autoencoders-vae
- [not-fixed] P1（kept，K044）首見附英文：「編碼空間」z12、「KL 懲罰」z16、「潛在空間」z113 已附英文（kept-audit miss 已修）；但「像素」z12、「後驗」z97 首見仍未附英文（低）。
- [not-fixed] P2（已修復）風格：16 條中仍有 11 條原文字句殘留，例如「逼編碼看起來像高斯」「打扮過的壓縮模型」「三個目標，一個架構，一個損失」「VAE 很少單獨出貨」「被擴散比下去」「無緣無故慢 3 倍」（中）。

## phases/08-generative-ai/03-gans-generator-discriminator
- [verified] P1（kept，K045）首見附英文：標題「產生器對鑑別器」、z30「純量」、z37「訓練迴圈」已附英文（kept-audit miss 已修）。
- [verified] P2（已修復）風格：17 條原句全部不再出現（已抽驗改寫句）。

## phases/08-generative-ai/04-conditional-gans-pix2pix
- [verified] P1（已修復）「取樣」統一、「訊號」統一：全文無「損失信號」「很強的信號」殘留。
- [verified] P1（kept，K046）首見附英文：「配對資料」z14、「感受野」z26、「吞吐量」z142 已附英文（kept-audit miss 已修）。
- [not-fixed] P2（已修復）風格：18 條中 6 條仍在，例如 z14「你正好有需要的信號」、z24「高頻細節會消失」、z117「說明沒有配對資料，它也學得到兩者之間的映射」（低）。

## phases/08-generative-ai/05-stylegan
- [not-fixed] P1（已修復）首見附英文：「轉置卷積」z12、「映射網路」z22、「仿射投影」z14、「領域調適」z48 首見仍未附英文；「潛在空間」「自適應實例正規化」「權重解調」「路徑長度正則」「等變核」等已附英文（低）。
- [verified] P2（已修復）風格：17 條中實際殘留為 0（命中字串「換風格」「一次前向」為「交換風格」「一次前向傳遞」的子字串，非殘留）。

## phases/08-generative-ai/06-diffusion-ddpm-from-scratch
- [not-fixed] P1（已修復）GLOSSARY：noise schedule 應為「雜訊排程」，但 z122 仍為「餘弦排程」、z156 仍為「β 排程」（低）。
- [kept-ok] P1（kept，borderline）「三個直覺」三項之間空行：格式差異，內容不變（K047）。
- [verified] P1（kept，K048）首見附英文：「鞍點」z12、「馬可夫鏈」z14、「後驗」z34、「證據下界」z52、「反向取樣」z95、「時間條件」z111 已附英文（kept-audit miss 已修）。
- [not-fixed] P2（已修復）風格：19 條中仍有 12 條殘留，例如「高斯解碼器吐出糊掉的樣本」「把數學收拾乾淨」「閉式之所以讓數學算得出來」「式子醜」「瑣碎問題」「喬裝過的」（中）。

## phases/08-generative-ai/07-latent-diffusion-stable-diffusion
- [kept-ok] P1（kept，borderline）Stage 1／Stage 2 空行：格式差異（K049）。
- [not-fixed] P1（已修復）首見附英文：「像素空間擴散」z3、「U-Net」z12、「對抗損失」z24、「文字條件」z27、「CPU 卸載」z136 首見仍未附英文（低）。
- [not-fixed] P2（已修復）風格：20 條中仍有 13 條殘留，例如「運算帳單荒謬」「像素是 16 分之一」「兩階段底層」「把它們混進去」「prompt 貼合上贏過 CLIP」（中）。

## phases/08-generative-ai/08-controlnet-lora-conditioning
- [kept-ok] P1（kept，borderline）LoRA 與 ControlNet-lite 空行：格式差異（K050）。
- [verified] P1（已修復）「控制信號／條件信號」已全篇統一為「訊號」（殘留 0）。
- [verified] P1（kept，K051）基底模型→基模型（08 全課殘留 0）；首見「跳躍連接」「恆等」「線性層」「交叉注意力」「影像條件配接器」「執行時縮放」「條件」已附英文。殘留「差值」z16、「多租戶」z142 未附英文（低）。
- [not-fixed] P2（已修復）風格：22 條中仍有 10 條殘留，例如「釘住你要指定一張影像所需的 10%」「貴到做不起來」「去讀條件，再讓它推一下骨幹」「教模型新概念，你的臉」「不會搞砸」「小的旁路模型出貨」（中）。

## phases/08-generative-ai/09-inpainting-outpainting-editing
- [verified] P1（kept，K052）「噪聲」→「雜訊」：08 全課「噪聲」殘留 0；「條件訊號」統一。
- [verified] P1（kept，K053）首見：「前向擴散」「條件訊號」「邊界假影」「反向過程」「遮罩膨脹」已附英文；殘留「9 通道 U-Net」z136、「前向傳遞」z149 首見未附英文（低）。
- [verified] P2（已修復）風格：19 條原句全部不再出現。

## phases/08-generative-ai/10-video-generation
- [verified] P1（kept，K054）首見：「時空壓縮」z14、「時間一致性」z15 已附英文；殘留「像素」z12 首見未附英文（低）。
- [存疑] P2（已修復）風格：18 條中約 9 條字串仍命中，其中含子字串誤判（如「完整 3D 注意力」被「完整 3D 注意力計算」命中）；「幀與幀不一致」「成本從 2024 到 2026 降到 20 分之一」「鏡頭計畫」需逐句覆核，本輪未完成。

## phases/08-generative-ai/11-audio-generation
- [not-fixed] P1（已修復）首見附英文：「一維訊號」z3、「音素結構」z14、「和弦進行」z15、「聲音設計」z16、「神經音訊編解碼器」z18、「時間步」z26、「偏移」z39 首見仍未附英文（中）。
- [verified] P2（已修復）風格：18 條中 16 條不再出現；命中的「預測器」為合法用詞、「一次前向」為「一次前向傳遞」的子字串。
- [new-issue] 中：z39「將 RVQ token 攤平成一條序列一條序列」疊字。
- [new-issue] 中：z132「伺服器必須為每位使用者伺服器必須為每位使用者每秒產生至少 75 個 token」疊句。

## phases/08-generative-ai/12-3d-generation
- [kept-ok] P1（kept，borderline）z31–33 標題後空行：格式差異。
- [verified] P1（kept，K056）runtime→「執行環境」（z151）、optimizer→「最佳化器」（z157）。
- [存疑] P1（kept，K057）首見：「可微分」「密度」等未逐一核對；「基礎模型」已無殘留。
- [存疑] P1（kept）其餘首見附英文項目與 P2 風格項目：本輪未逐條核對。

## phases/08-generative-ai/13-flow-matching-rectified-flows
- [verified] P1（kept，K058）首見：「隨機遊走」（random walk，z12）、「部署配方」（deployment recipe，z161）已附英文；標題「整流流」「反向過程」「蒸餾」首見未逐一核對。
- [存疑] P2（已修復）風格：本輪未逐條核對。

## phases/08-generative-ai/14-evaluation-fid-clip-score
- [kept-ok] P1（kept，borderline）「Failure modes」標題後空行：格式差異（K059）。
- [verified] P1（已修復）「算平均」→「算平均數」（z28）。
- [存疑] P1（kept，K060）首見：「人類偏好」「樣本品質」「多變量高斯」「特徵抽取器」「質性檢視」「特徵向量」「樣本數」未逐一核對。
- [存疑] P2（已修復）風格：本輪未逐條核對。

## phases/08-generative-ai/19-visual-autoregressive-var
- [kept-ok] P1（kept，borderline）「Three structural wins」與子步驟引言空行：格式差異（K061）。
- [verified] P1（kept，K062）首見：標題「下一尺度預測（next-scale prediction）」、「尺度內平行生成（intra-scale parallel generation）」、「條件分布（conditional distribution）」已附英文；「自迴歸生成」「注意力遮罩」「尺度數量」未逐一核對。
- [存疑] P2（已修復）風格：本輪未逐條核對。

## phases/09-reinforcement-learning/01-mdps-states-actions-rewards
- [verified] P1（已修復）「政策」→「策略」、「隨機政策」→「隨機策略」：09 全課「政策」殘留 0。
- [存疑] P1（已修復）首見附英文（狀態、動作、轉移……）：本輪未逐條核對。
- [new-issue] 中：z3 與 z16 出現「都都可用同一個數學框架描述」疊字。
- [存疑] P2（已修復）風格：本輪未逐條核對。

## phases/09-reinforcement-learning/02-dynamic-programming
- [verified] P1（kept，K063）「政策」→「策略」（09 全課政策殘留 0）。
- [存疑] P1（kept，K064）首見附英文（模型式 RL、不動點迭代、終止狀態、隨機變體、平手規則、同步更新）：本輪未逐條核對。
- [存疑] P2（已修復）風格：本輪未逐條核對。

## phases/09-reinforcement-learning/03-monte-carlo-methods
- [verified] P1（kept，K065）「政策」→「策略」、「重要性抽樣」→「重要性取樣」、「估計器」→「估計量」、「報酬」→「獎勵」：09 全課殘留皆為 0。
- [存疑] P1（kept，K066）首見附英文：未逐條核對。
- [存疑] 其餘 P1 項目：本輪未逐條核對。

## phases/09-reinforcement-learning/04-q-learning-sarsa
- [verified] P1（kept，K067）「政策」→「策略」、「報酬」→「獎勵」（09 全課殘留皆為 0）。
- [存疑] P1（kept，K068）首見附英文：未逐條核對。
- [存疑] P2（已修復）風格：未逐條核對。

## phases/09-reinforcement-learning/05-dqn
- [verified] P1（kept，K069）「報酬」→「獎勵」、「政策」→「策略」（09 全課殘留皆為 0）。
- [存疑] P1（kept，K070）首見附英文：未逐條核對。
- [存疑] P2（已修復）風格：未逐條核對。

## phases/09-reinforcement-learning/06-policy-gradients-reinforce
- [not-fixed] P1（kept，K071）首見附英文（熵獎勵、權重向量、對數機率、展開、熵崩塌、樣本效率、功勞分配、優勢）：全課 policy 譯名系統性錯誤（見下條）使首見判定不成立，列為 not-fixed。
- [new-issue] **P0（嚴重語意錯誤）**：全課把 policy（策略）誤譯為「變異數／變異數減少」，包括標題 z1「變異數／變異數減少梯度（policy gradient）」、導語 z3「直接把變異數／變異數減少參數化」、z12、z14、z24（「變異數／變異數減少梯度定理」）、z43、z51、z53、z61、z74、z122、z131、z133、z134、z143、z144、z179、z181、z187、z188、z192、z193、z199 等，至少 23 處。09 其他課無此串，判定為本課獨有的批次替換錯誤。
- [存疑] P2（已修復）風格：因上條錯誤已達全課語意失真，本輪未逐條核對。

## phases/09-reinforcement-learning/07-actor-critic-a2c-a3c
- [存疑] P1（kept，K072）首見附英文（評論者、行動者、蒙地卡羅回報、內插、平行環境、非同步、參數伺服器、價值回歸、共享主幹、重要性抽樣修正、聯賽訓練、模仿預訓練）：未逐條核對。
- [存疑] 其餘 2 條（P1／P2）：未逐條核對。

## phases/09-reinforcement-learning/08-ppo
- [verified] P1（kept，K073）「政策」→「策略」（09 殘留 0）；TRPO 譯名已改為「信賴域策略最佳化」（「信賴域政策」殘留 0）。
- [存疑] 同條「約束」→「限制條件」、「程式」→「程式碼」：未逐條核對。
- [存疑] P1（kept，K074）首見附英文：未逐條核對。

## phases/09-reinforcement-learning/09-reward-modeling-rlhf
- [verified] P1（kept，K075）「報酬」→「獎勵」（09 全課「報酬」殘留 0）。
- [存疑] 首見附英文（K075 所列 25 項以上）與「策略」首見 policy 附英文：未逐條核對。

## phases/09-reinforcement-learning/10-multi-agent-rl
- [verified] P1（kept，K076）「政策」→「策略」、「報酬」→「獎勵」（09 殘留 0）。
- [kept-ok] P2（kept，borderline）CTDE 段與「例子：」清單之間空行：格式差異（K077）。
- [存疑] P1（kept，K076）首見附英文（馬可夫性質、非定態、集中訓練、聯合動作、功勞分配、學習曲線等）：未逐條核對。

## phases/09-reinforcement-learning/11-sim-to-real-transfer
- [存疑] P1（kept，K078）首見附英文（真實落差、飽和、分布偏移、條件分布、模型誤差、殘差模擬器、觀測適應、特權學習、教師、學生、蒸餾）：未逐條核對。
- [存疑] 其餘 2 條：未逐條核對。

## phases/09-reinforcement-learning/12-rl-for-games
- [verified] P1（kept，K079）GLOSSARY：「政策」→「策略」、「報酬」→「獎勵」、「基底模型」→「基模型」（09 全課殘留皆為 0）；「拒絕抽樣」殘留 0。
- [存疑] P1（kept，K080）首見附英文（遊戲上的強化學習標題、訊號、訓練迴圈、潛在空間、組內相對基準、思維鏈、軌跡、完美資訊、獎勵操弄、消融、完整序列）：未逐條核對（z1、z63 已見英文）。
- [存疑] P2（已修復）風格：未逐條核對。

## phases/11-llm-engineering/01-prompt-engineering
- [verified] P1（kept，K081）「提供者」→「服務供應商」（11 全課「提供者」殘留 0）。
- [new-issue] 低：z134「一口氣排除了大片不需要的輸出空間」屬直譯式渲染，原文未強調（低）。
- [存疑] 其餘 3 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/02-few-shot-cot
- [verified] P1（kept，K082）「原文 five words 譯成『七個字』」已改為「五個英文單字」（z21）。
- [kept-ok] K083：「生成式 sampling」與「組基準變異」所引段落已不存在，駁回合理。
- [verified] P1 前向傳播→前向傳遞：11 全課「前向傳播」殘留 0（02 無殘留）；首見附英文（K084 其餘項）：未逐條核對。
- [存疑] 其餘 1 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/03-structured-outputs
- [verified] P1（kept，K085）「提供者」→「服務供應商」（殘留 0）。
- [存疑] P1（kept，K086）首見附英文（受限解碼、幻覺、型別化資料、擷取、工具呼叫、解碼器、詞彙表、型別合規、信心分數）：未逐條核對。
- [存疑] 其餘 1 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/04-embeddings
- [存疑] P1（kept，K087）首見附英文（餘弦相似度、隱藏層、群集、內積、召回率、分塊、閾值、雙編碼器、交叉編碼器、向量索引、正交）：未逐條核對；「提供者」已改「服務供應商」（殘留 0）。
- [new-issue] 中：z131「當前目前最常用的演算法的演算法是 HNSW」錯亂句（疊字）。
- [new-issue] 中：z216「在數百萬向量向量庫中進行超高速初篩」疊字。
- [存疑] 其餘 2 條 r3 項目：未逐條核對（f3 疊字「向量表示的向量表示」已修，z38 確認）。

## phases/11-llm-engineering/05-context-engineering
- [存疑] P1（kept，K088）首見附英文（脈絡工程、少樣本、工具定義、生成緩衝、滑動視窗、動態脈絡組裝、動態工具挑選、餘弦相似度、語意去重、脈絡回放、脈絡壓縮器）：未逐條核對。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/06-rag
- [verified] P1（kept，K089）「提供者」→「服務供應商」（殘留 0）；「歐氏距離」改寫之殘留：未逐條核對。
- [存疑] P1（kept，K090）首見附英文：未逐條核對。
- [new-issue] 中：z119「能確保句子不會在不會在不適當的位置切斷句子被強行截斷」錯亂疊字。
- [new-issue] 中：z131「Anthropic 的 RAG Anthropic 的 RAG 指引也建議此範圍此區間」疊字。
- [new-issue] 中：z172「多數多數正式環境 RAG 系統採用以下參數」疊字。
- [存疑] 其餘 1 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/07-advanced-rag
- [verified] P1（kept，K091）英文例句已譯為繁中（z22），無整句英文殘留。
- [存疑] P1（kept，K092）首見附英文（近似最近鄰、骨幹、詞頻、逆文件頻率、文件頻率、飽和、社群偵測、多重查詢）：未逐條核對。
- [new-issue] 中：z3「只能在 10 份文件上只能在 10 份文件上運作的示範」疊句。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/08-fine-tuning-lora
- [verified] P1（kept，K093）英文殘句「on cloud providers」已整併為繁中段落（z24）。
- [verified] P1（kept，K095）「大致符合常態分布」「保留的資訊比 4 位元更多」，「被證明」「顯著低於」已移除（殘留 0）。
- [verified] P2（kept，K096）渲染詞（黃金甜蜜點、徹底重構、權威經典、一站式全能、徹底消除）本課已無殘留。
- [存疑] P1（kept，K094）GLOSSARY 基模型已統一（11 全課「基礎模型」殘留 0）；首見附英文（預訓練、注意力層、最佳化器、線性層、參數縮減比例、初始化、縮放因子、目標層、適應能力、常態分布、資料型別、顯存、相關性係數）：未逐條核對。
- [new-issue] 低：z173 Unsloth 列「改寫前向與反向傳播」，backward pass 依 GLOSSARY 應為「反向傳遞」。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。
- [verified] f4「積少成多」（z136）對照 en「Small but it adds up.」，語意保真。

## phases/11-llm-engineering/09-function-calling
- [verified] P1（kept，K097）「凌亂履歷」已改為「從文字中擷取產品資訊」（殘留 0）。
- [verified] P2（kept，K099）風格：「實體操作」「免責聲明之下」「真實溫度」「陋習」「平行並行」殘留 0。
- [存疑] P1（kept，K098）首見附英文（函式呼叫迴圈、平行函式呼叫、結構化輸出、速率限制、工具註冊表）：未逐條核對；「提供者」已改「服務供應商」（殘留 0）。
- [new-issue] 中：z24「包裝在帶有免責聲明的幻覺的幻覺」疊字錯亂。
- [new-issue] 中：z124「你的程式碼能平行執行執行兩者」疊字。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/10-evaluation
- [存疑] P1（kept，K100）首見附英文（評估資料集、邊界情況、確定性斷言、回歸測試、品質衰退、格式遵循度、幻覺率、基準測試、信賴區間、語意相似度、語意品質、人工評審、統計顯著性、樣本規模、少樣本、可觀測性、評分函式）：未逐條核對；「模型提供者」已改「服務供應商」（11 殘留 0）。
- [not-fixed] P2（kept，K101）渲染詞殘留：z203「單看一個孤立的 4.2/5 分毫無意義」為原文沒有的強調（低）。
- [存疑] 其餘 5 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/11-caching-cost
- [verified] P1（kept，K102）英文殘句「$0.005 normally costs…」已譯為繁中（z73）。
- [verified] P1（kept，K103）增譯「高達」「系統保證」「無條件」已移除（z153、z835 殘留 0）。
- [verified] P1（kept，K104）「平價平價模型」重複字已刪；「拒絕新請求」已補（z884）。
- [verified] P1（kept，K105）「門檻」→「閾值」（11/11 殘留 0）；「提供者」→「服務供應商」（殘留 0）。
- [存疑] P1（kept，K106）首見附英文（語意快取、前綴快取、精確快取、配額、成本追蹤、批次處理、快取命中率、向量資料庫、移動平均、分類準確率、確定性呼叫）：未逐條核對。
- [verified] P2（kept，K107）渲染詞（殘酷算數、毫無意義、表現完美、關乎生死存亡、虛擬水桶、最為燒錢）於本課已無殘留。
- [存疑] 其餘 1 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/12-guardrails
- [verified] P1（kept，K108）「若要求一句摘要卻收到 8,000 字文章，就截斷或重新生成」已補回（z96）。
- [verified] P1（kept，K109）NeMo「可與任何 LLM 整合」、「針對參考文字的幻覺檢驗」、Presidio「可同時處理輸入與輸出」已補回／更正（z124、z126、z128）。
- [verified] P1（kept，K110）「類別分數」（z773）取代「機率評分」。
- [verified] P1（kept，K111）「金融服務、醫療與政府」（z178）。
- [存疑] P1（kept，K112）首見附英文與「資料洩漏」統一：未逐條核對。
- [verified] P2（kept，K113）絕對化用語（瞬間繳械投降、固若金湯、完全無法區分、毫無例外、不可攻破）本課已無殘留。
- [new-issue] 低至中：z3「問題從來不是是否有人會嘗試」「不是是」疊字。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/13-production-app
- [verified] P1（kept，K114）英文括號殘句「with caching saving」已刪（z236）。
- [not-fixed] P1（kept，K115）檢核項目「具備隨機抖動的指數退避重試」仍含 jitter（z276），原文僅為「Exponential backoff on all LLM API calls」（低）。
- [verified] P1（kept，K116）「保證響應」已刪、「完全無感」改為「對使用者無感」（z136）、「瞬間秒級回滾」改為「瞬間回滾」（z175）。
- [存疑] P1（kept，K117）首見附英文（語意快取、分塊、百分位數、負載平衡器、快取命中率、優雅降級、健康檢查）：未逐條核對。
- [verified] P2（kept，K118）渲染詞（陽春 Demo、模型智商、擠爆、飆破、總結集大成、緊密咬合）本課已無殘留。
- [new-issue] 中：z9 metadata 區的「**Related:**」整句仍為英文（en.md:9 亦為英文原句），譯文未翻譯。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/14-model-context-protocol
- [存疑] P1（kept，K119）首見附英文（能力宣告、支援版本、授權、工具引數、快取範疇、遙測、狀態代號、背壓）：未逐條核對。
- [kept-ok] P2（kept，K120）圖說替代文字英文：受 check_translation.py 保護（alt 維持英文，已定策）。
- [verified] P2（kept，K121）渲染詞（統一通用、徹底無狀態化、大幅收斂、完全無需、徹底廢除、嚴禁採納）本課已無殘留。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/15-prompt-caching
- [verified] P1（kept，K122）「提供者」→「服務供應商」（11 殘留 0）。
- [存疑] P1（kept，K123）首見附英文（端點、快取中斷點、佈局最佳化器、預熱、前綴、命中率、寫入溢價、讀取折扣、快取鍵、快取標記）：未逐條核對。
- [verified] P2（kept，K124）渲染詞（全額付費、永遠無法命中、淨省錢、粉碎每一次快取命中、四大關鍵支點）本課已無殘留。
- [new-issue] 中：z227 TTL 列「快取快取保持有效的秒數」疊字。
- [new-issue] 低：z26「最低快取門檻」（threshold 應為「閾值」）、z171「低於門檻」。
- [存疑] 其餘 2 條 r3 項目：未逐條核對。

## phases/11-llm-engineering/16-langgraph-state-machines
- [kept-ok] P1（kept，K125）「merge／branch／fork」以合併、分支、分岔譯名（圖操作語境，borderline）。
- [存疑] P1（kept，K126）首見附英文（條件邊、檢查點快照、狀態增量、子圖、函式簽章、中斷）：未逐條核對。
- [kept-ok] P2（kept，K127）圖說替代文字英文：受保護（已定策）。
- [存疑] 其餘 3 條 r3 項目（含 P2 風格）：未逐條核對；z152「極速重現」為殘留渲染詞（低）。

## phases/11-llm-engineering/17-agent-framework-tradeoffs
- [verified] P1（kept，K128）「以 pickle 序列化的對話紀錄」已取代「序列化的對話紀錄字典」（字典殘留 0）。
- [verified] P1（kept，K129）「每日數千次」「優先採用」已取代「數萬次」「一律堅持」（數萬次殘留 0）。
- [verified] P1（kept，K130）「不想被特定框架綁定」（技術債已刪）、「服務供應商原廠 SDK」、「編排（orchestration）」（z117）。
- [verified] P2（kept，K131）「節點（node）」首見已附英文（z26）。
- [存疑] P2（kept，K132）渲染詞（兜售著相同的展示 Demo、抽象層開始到處漏水、挑選地表最強框架、最不適用的災難場景、永遠是速度最快、最透明的終極框架）：未逐條核對。
- [kept-ok] P2（kept，K133）圖說替代文字英文：受保護（已定策）。
- [存疑] 其餘 3 條 r3 項目：未逐條核對。
