# zh-TW 終態複審（v3-final-audit）：phases 05 / 07（45 課）

- 範圍：05-nlp-foundations-to-advanced（29 課）、07-transformers-deep-dive（16 課）。唯讀複審，未修改任何譯稿或 repo 檔案。
- 來源：審閱報告 `/Users/edward/Desktop/ai-engineering-from-scratch/docs/reviews/zh-tw/r2.md`（05）與 `r3.md`（07）；誤駁回稽核 `v2-kept-audit.md`（05 段）與 `v3-kept-audit.md`（07 段）；修復日誌 `f2-changelog.md`（05，60 筆）、`f3-changelog.md`（07，94 筆）、`f4-changelog.md`（05/09 L199、07/13 L137）。`/private/tmp/zh-tw-review/r2.md`、`r3.md` 為較舊版本，未採用。
- 譯稿：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`；原文：`/private/tmp/aiefs-main-source/phases/<phase>/<lesson>/docs/en.md`；術語：`i18n/zh-TW/GLOSSARY.md`；風格：`i18n/zh-TW/STYLE.md`。行號為審查時現況。

## 判定類別

- `[verified]`：報告註記已修復（或稽核 miss 已由修復日誌補上），現況確認改好且未改錯。
- `[not-fixed]`：註記已修復，但現況仍有問題（部分套用、假修復，或修法本身造成錯誤）。
- `[kept-ok]`：維持原樣，複審同意（含稽核判 ok／borderline 且無明確錯誤者）。
- `[kept-wrong]`：維持原樣，但複審認為仍該修（含稽核判 miss 而現況未修）。
- `[new-issue]`：報告未提、現況有明確錯誤（疊字、錯亂句、英文殘留、GLOSSARY 違規、增譯／漏譯）。

## 方法與限制

- 逐條依報告章節定位現況（grep／關鍵字），再對照英文原稿判定；改錯判定均以 en.md 對照。
- 官方結構檢查器（預設檢查模式，唯讀，未用 `--write-cache`）於審查開始時執行：05 為 29 passed／0 failed，07 為 16 passed／0 failed。此閘門不驗譯法、首見英文與語意，故不作為通過證據。
- 全域掃描：疊字、中英之間半形空格、GLOSSARY 禁用詞（標記器、嵌入、詞元、提示詞、微調、智慧體、代理程式、報酬、政策、分支、基準測試等，05/07 皆無殘留）、生成語境「抽樣」、「代理」、「黃金」、「前向」殘留。
- 限制：（a）審查中途一次 bash 呼叫被自動審查拒絕（審查服務不可用），之後改用 Read／Grep 唯讀核對，未重試被拒指令；（b）未對 05/07 全課做「首見英文」完整掃描，首見判定以報告與稽核列舉者為主；（c）f4 日誌於審查期間仍在增長，05/09 與 07/13 已對照其紀錄，05/19 的 f4 紀錄為 D4「保留」L26「可以抽樣（sampling）不同的切分」；f4 之後若再改動，相關判定需重查。
- 圖片替代文字（alt）維持英文：`check_translation.py` 將整段 `![alt](src)` 列為受保護跨度，且 STYLE 規定「圖片參照」原樣保留；判 `[kept-ok]`，但無障礙缺口屬 supervisor 決策 A，此處不擅自決定。

---

## 05-nlp-foundations-to-advanced/01-text-processing
- 05-01.1 [verified] r2 P1 L24「子詞」首見 → L24「子詞（subword）」。
- 05-01.2 [verified] r2 P1 L135「詞性標記器」（維持原樣；稽核 #50 miss；f2 已修）→ L135「詞性標註器（POS tagger）」。
- 05-01.3 [verified] r2 P2 L209「準確率安靜地變差」→ L209「準確率在不知不覺中下降」。
- 05-01.4 [new-issue] P2 L250 表格「NOUN、VERB、ADJ 這類類別」疊字「這類類別」。

## 05-nlp-foundations-to-advanced/02-bag-of-words-tfidf
- 05-02.1 [verified] r2 P1 L189「詞彙表外詞（out-of-vocabulary word）」已附英文。
- 05-02.2 [verified] r2 P1 L189「子詞 embedding（subword embedding）」已附英文。
- 05-02.3 [verified] r2 P2 L178「係數最高的正向詞就是模型做出該預測的依據」（原「正向最高的詞」誤讀已消除）。
- 05-02.4 [verified] r2 P2 L182「語意理解不足的問題」。
- 05-02.5 [verified] r2 P2 L176「資料量較少的情境」。

## 05-nlp-foundations-to-advanced/03-word-embeddings-word2vec
- 05-03.1 [verified] r2 P1 L220「詞彙表外」首見 → L204 首見「詞彙表外（out-of-vocabulary，OOV）」，L220 同。
- 05-03.2 [not-fixed] r2 P1 L204、220「子詞組合」→ 現況 L204「用subword composition處理詞彙表外…」、L220「fastText 用subword composition修這件事」：中文譯名遭刪、英文裸露、中英間缺半形空格。應為「子詞組合（subword composition）」。
- 05-03.3 [verified] r2 P2 L203「50、100、200、300 維的檢查點」→ L203「…預訓練向量版本」。
- 05-03.4 [verified] r2 P2 L201「真正做事時」→ L201「實際應用時」。

## 05-nlp-foundations-to-advanced/04-glove-fasttext-subword
- 05-04.1 [kept-ok] r2 P2 L3「把共現矩陣做了矩陣分解」（維持原樣；稽核 #51 ok）。
- 05-04.2 [verified] r2 P2 L14「有一條並行的研究」→ L14「另有一支研究方向」。
- 05-04.3 [kept-ok] r2 P2 L28「數語料庫裡每一對相鄰的配對」（維持原樣；稽核 #52 borderline；可讀，不列為錯）。
- 05-04.4 [verified] r2 P2 L28「每個句子都能切成某個東西」→ L28「每個句子都能切分成 token 序列」。
- 05-04.5 [verified] r2 P2 L210「不需要容忍 OOV」→ L210「不必處理 OOV」。

## 05-nlp-foundations-to-advanced/05-sentiment-analysis
- 05-05.1 [verified] r2 P1 L170 AUROC／AUPRC 僅縮寫 → L170 附 ROC 曲線下面積（area under the ROC curve）與精確率－召回率曲線下面積（area under the precision-recall curve）全名。
- 05-05.2 [verified] r2 P2 L164–172「巨觀平均／巨觀 F1」→ 全篇「宏平均／宏平均 F1」（無「巨觀」殘留）。
- 05-05.3 [verified] r2 P2 L244「多數第一次嘗試會落在那裡」→ L244「多數初次嘗試的結果也會落在這個水準」。

## 05-nlp-foundations-to-advanced/06-named-entity-recognition
- 05-06.1 [verified] r2 P0 L254「F1 拉高 11 到 12 個百分點」→ L254「F1 提升 11% 到 12%」（與原文一致）。
- 05-06.2 [verified] r2 P1 L42「發射機率、轉移機率、維特比解碼」（維持原樣；稽核 #53 miss；f2 已修）→ L42 附 emission／transition probability、Viterbi decoding。
- 05-06.3 [verified] r2 P2 L250「標註資料稀少時更是好上非常多」→ L250「標註資料稀少時，表現往往更好」。
- 05-06.4 [verified] r2 P2 L228「對產品實體涵蓋很弱」→ L228「對產品實體的辨識涵蓋率不佳」。
- 05-06.5 [verified] r2 P2 L273「稀疏類型」→ L273「低頻實體類別」。
- 05-06.6 [new-issue] P2 L250「現在在很多領域和 fine-tune 過的模型不相上下」疊字「現在在」。

## 05-nlp-foundations-to-advanced/07-pos-tagging-parsing
- 05-07.1 [verified] r2 P1 L87「轉移機率、發射機率、維特比解碼」（維持原樣；稽核 #54 miss；f2 已修）→ L87 三者皆附英文。
- 05-07.2 [verified] r2 P2 L166「最大生成樹」→ L166「最大權重生成樹（maximum spanning tree）」。
- 05-07.3 [verified] r2 P2 L196「Stanford 接在 CoreNLP 之後的後繼」→ L196「Stanford 推出的 CoreNLP 後繼系統」。
- 05-07.4 [verified] r2 P2 L196「60 種以上語言目前最好」→ L196「在 60 多種語言上達到最先進水準」。
- 05-07.5 [verified] r2 P2 L206「跨語言轉移」→ L206「跨語言遷移」。

## 05-nlp-foundations-to-advanced/08-cnns-rnns-for-text
- 05-08.1 [verified] r2 P1 L24「全域最大池化」→ L24「全域最大池化（global max-pooling）」。
- 05-08.2 [verified] r2 P1 L32「雙向 RNN」→ L32「雙向 RNN（bidirectional RNN）」。
- 05-08.3 [kept-wrong] r2 P2 L30、108、192–193「閘」（維持原樣；稽核 #55 borderline）。稽核條件「若保留『閘』，首見 L30 應附 gate」未滿足：L30「LSTM 加上閘」首見無英文，全篇僅用「閘」。建議首見「閘門（gate）」並統一。
- 05-08.4 [verified] r2 P2 L30「普通 RNN 會梯度消失」→ L30「普通 RNN 會遇到梯度消失問題（vanishing gradient）」。
- 05-08.5 [verified] r2 P2 L151「這就是那一疊」→ L151「這就是適合的技術組合」。

## 05-nlp-foundations-to-advanced/09-sequence-to-sequence
- 05-09.1 [not-fixed] r2 P1 L26、208「標準結果 token」（GLOSSARY ground truth＝真實標籤）。L208 已改「用真的 token」，但 L26 仍為「…的*標準結果（ground truth）* token」。原文 en L26 為 "*ground-truth* token"。應改「真實標籤（ground truth）」或「真實 token」。
- 05-09.2 [verified] r2 P1 L16、22、167「排程抽樣／抽樣」→ L16「排程取樣」、L22「用取樣或 argmax」、L167「排程取樣（scheduled sampling）」；全課無「抽樣」殘留。
- 05-09.3 [verified] r2 P1 L125「貪婪解碼」→ L125「貪婪解碼（greedy decoding）」。
- 05-09.4 [verified] r2 P2 L53「把暴露偏差的落差收起來」→ L104「縮小暴露偏差造成的落差」。
- 註 f4：L199「和基礎模型在留出輸入上」→「和基模型在留出輸入上」已套用（全課無「基礎模型」殘留）。

## 05-nlp-foundations-to-advanced/10-attention-mechanism
- 05-10.1 [kept-ok] r2 P1 L20 圖片 alt「Bahdanau attention: decoder queries all encoder states」（維持原樣；稽核 #56 borderline；checker 保護 alt，見決策 A）。
- 05-10.2 [verified] r2 P1 L44、51「加法分數／乘法分數」（維持原樣；稽核 #57 miss；f2 已修）→ L44「Bahdanau（加法注意力，additive attention）分數」、L51「Luong（乘法注意力，multiplicative attention）分數」。
- 05-10.3 [verified] r2 P1 L139「縮放點積注意力」→ L139「縮放點積注意力（scaled dot-product attention）」。
- 05-10.4 [not-fixed] r2 P2 L105「Luong 的論文能落地」→ 修法造成錯亂句。現況 L105「這就是 這正是 Luong 方法受到採用的原因的原因。」（en：「This is why Luong's paper landed.」）。應為「這正是 Luong 方法受到採用的原因。」。
- 05-10.5 [verified] r2 P2 L107「一個算過的數字例子」→ L107「完整數值範例」。

## 05-nlp-foundations-to-advanced/11-machine-translation
- 05-11.1 [verified] r2 P1 L89「充分」（adequacy）→ L89「流暢、適切度、語氣、文化恰當」。
- 05-11.2 [verified] r2 P2 L3「養了自然語言處理研究三十年、現在還在養」→ L3「支撐自然語言處理研究三十年，至今仍持續推動研究」。
- 05-11.3 [verified] r2 P2 L14「人和機器之間的差距一直很頑固」→ L14「人機之間的品質差距始終難以縮小」。
- 05-11.4 [verified] r2 P2 L62「用哪種文字和切分」→ L62「使用哪種文字系統與切分方式」。
- 05-11.5 [verified] r2 P2 L66、186「簡短懲罰」→ L66、L186「過短懲罰」。
- 05-11.6 [verified] r2 P2 L66「例外地好」→ L66「50 是『非常出色』」。
- 05-11.7 [verified] r2 P2 L102「給客戶看的內容通常會錯」→ L102「這種語體通常不適合客戶溝通」。
- 05-11.8 [kept-ok] r2 P2 L146「短程」（維持原樣；稽核 #58 borderline）。原文 "Short runs" 本身模糊，譯文忠實，不列為錯。

## 05-nlp-foundations-to-advanced/12-text-summarization
- 05-12.1 [verified] r2 P0 L26、207「空句預訓練目標／空句目標」→ L26「Pegasus 特別用缺句生成預訓練目標（gap-sentence generation objective）」，L207 參考文獻改「缺句生成目標」。
- 05-12.2 [kept-ok] r2 P1 L26「空句預訓練目標」首見未附英文（維持原樣；稽核 #59 borderline）。首見英文已由 05-12.1 補上；括註 generation 與原文 pretraining 不逐字一致，屬 borderline，不阻擋。
- 05-12.3 [kept-ok] r2 P1 L20 圖片 alt「Extractive TextRank vs abstractive transformer」（維持原樣；稽核 #60 borderline；checker 保護 alt）。
- 05-12.4 [verified] r2 P2 L28「例外地好」→ L28「40 的 ROUGE-L 是『好』，50 是『非常出色』」。
- 05-12.5 [verified] r2 P2 L131「靠近合規的內容」→ L131「與法規遵循相關的內容」。
- 05-12.6 [verified] r2 P2 L143「問一個問答模型那些答案在來源裡的問題」→ L143「向問答模型提出答案可在來源中找到的問題」。
- 05-12.7 [verified] r2 P2 L198「參考譯文」→ L198「系統輸出和參考摘要之間的 n-gram」。

## 05-nlp-foundations-to-advanced/13-question-answering
- 05-13.1 [verified] r2 P1 L177「量答案多久是對的」→ L177「計算答案答對的次數／比例」。
- 05-13.2 [kept-ok] r2 P1 L24 圖片 alt「QA architectures: extractive, retrieval-augmented, generative」（維持原樣；稽核 #61 borderline；checker 保護 alt）。
- 05-13.3 [kept-ok] r2 P2 L28、122「前 `k` 段」（維持原樣；稽核 #62 borderline）。top-k 常見譯法，不列為錯。
- 05-13.4 [verified] r2 P2 L115「序數打破正規化」→ L115「序數後綴未經正規化處理」。
- 05-13.5 [not-fixed] r2 P2 L126、133「黃金參考／黃金答案」。L126 已改「標準參考答案」；L133「讓你在沒有整理過的人工整理的參考答案時」為修法錯誤（重複、錯亂；en「without curated gold answers」）。應為「在沒有人工整理的參考答案時」。
- 05-13.6 [verified] r2 P2 L149「高度事實」→ L147「高度重視事實正確性的受管制領域、受管制的領域」（修法已套用）。
- 05-13.7 [new-issue] P2 L147 同列「受管制的領域」與前段語意重複（en 為 "highly factual, regulated domains" 兩項）。
- 05-13.8 [verified] r2 P2 L178「餘弦（cosine）0.3」→ L178「餘弦相似度 0.3」。
- 05-13.9 [verified] r2 P2 L179「量有沒有混合這一步的答案準確率」→ L179「比較加入與未加入混合檢索時的答案準確率」。

## 05-nlp-foundations-to-advanced/14-information-retrieval-search
- 05-14.1 [verified] r2 P1 L170、234「延遲互動」→ L170「ColBERT late-interaction」、L234「晚期互動」。
- 05-14.2 [verified] r2 P2 L3「BM25 精準但脆」→ L3「精準但脆弱」。
- 05-14.3 [verified] r2 P2 L112「餘弦（cosine）」→ L112「餘弦相似度（cosine similarity）」。

## 05-nlp-foundations-to-advanced/15-topic-modeling
- 05-15.1 [kept-ok] r2 P1 L35「句子 transformer」（維持原樣；稽核 #63 borderline）。中英拼接可讀，與程式庫名 sentence-transformers 一致，不列為錯。
- 05-15.2 [kept-ok] r2 P1 L24 圖片 alt「LDA mixture model vs BERTopic clustering」（維持原樣；稽核 #64 borderline）。
- 05-15.3 [verified] r2 P2 L12「1 萬張客服單」→ L12「1 萬件客服工單」。
- 05-15.4 [verified] r2 P2 L14「主題模型不靠監督」→ L14「主題模型以無監督方式……回答這件事」。
- 05-15.5 [verified] r2 P2 L16、174「混合成員」→ L16「多重主題歸屬」、L174「多重主題歸屬」。
- 05-15.6 [verified] r2 P2 L38、109、111「前幾個詞」→ L38、L109、L110、L111「排名前幾的詞」。

## 05-nlp-foundations-to-advanced/16-text-generation-pre-transformer
- 05-16.1 [verified] r2 P1 L157、181「抽樣」→ L157「### 步驟 4：用取樣生成文字」、L181「依機率取樣（sampling）」。
- 05-16.2 [verified] r2 P1 L61「負對數概似（likelihood）」→ L61「負對數概似（negative log-likelihood）」。
- 05-16.3 [kept-ok] r2 P1 L20 圖片 alt「N-gram model: count, smooth, generate」（維持原樣；稽核 #65 borderline；checker 保護 alt）。
- 05-16.4 [verified] r2 P1 L34、42「三元模型／三元」（維持原樣；稽核 #66 miss；f2 已修）→ L34「三元模型（trigram model）」。
- 05-16.5 [verified] r2 P2 L28「英文大約有四分之三是被迫的走法」→ L28「英文中字母約有四分之三可由脈絡大致預測」。
- 05-16.6 [verified] r2 P2 L33「仍面對的分岔因子」（維持原樣；稽核 #67 miss；f2 已修）→ L33「模型猜完之後仍需面對的選項數（branching factor）」。f2 以「選項數」取代稽核建議「分支數」，因 GLOSSARY 禁用「分支」，可接受。
- 05-16.7 [verified] r2 P2 L155「三個活動零件」→ L155「三個關鍵組成部分」。
- 05-16.8 [kept-ok] r2 P2 L181「小的隨機旋鈕（溫度）」（維持原樣；稽核 #68 ok）→ 現況 L181「小的隨機旋鈕（溫度，temperature）」。
- 05-16.9 [verified] r2 P2 L205「最清楚的接觸」→ L205「最清楚的入門教材」。

## 05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural
- 05-17.1 [not-fixed] r2 P1「LLM 代理／代理迴圈／程式代理」→ agent。標題與多數處已統一，但 AI agent 語境殘留「代理」（GLOSSARY agent＝保留英文）：L163「自動檢查代理行為」、L203「藏在代理會讀的文件」、L207「代理先規劃」、L210「代理就離題」、L211「代理一直呼叫同一個工具」、L266「有寫入權限的代理需要執行期防禦」。
- 05-17.2 [new-issue] P2 中英間缺半形空格（代理→agent 修法引入）：L52「agent處理」、L131「### 步驟 4：agent迴圈」、L202「agent宣稱」、L242「上面的LLM agent」、L260「就在 agent接手之前」、L261「為LLM agent模式命名」。
- 05-17.3 [kept-ok] r2 P1 L20 圖片 alt「Chatbot evolution: rule-based → retrieval → neural → agent」（維持原樣；稽核 #69 borderline；checker 保護 alt）。
- 05-17.4 [verified] r2 P2 L24「知道它的弧線要緊」→ L24「了解它的發展歷程很重要」。
- 05-17.5 [not-fixed] r2 P2 L28「名字到了／為實質進展編了兩個月」。已補「人工智慧一詞由達特茅斯夏季研討會提出；提案預期兩個月內能取得重大進展」，但仍保留原直譯「那份提案為實質進展編了兩個月。」，重複且生硬。應刪除殘句。
- 05-17.6 [verified] r2 P2 L30「這麼少的機器就能做到」→ L30「只靠這麼少的機制就能做到」。
- 05-17.7 [verified] r2 P2 L32「決定下一支腳本哪一個會觸發」→ L32「決定下一輪觸發哪支腳本」。
- 05-17.8 [verified] r2 P2 L48「從不可靠地扣題」→ L48「也無法穩定切合主題」。
- 05-17.9 [verified] r2 P2 L50、163「檢索接地」（維持原樣；稽核 #70 miss；f2 已修）→ L50「先檢索、再以檢索到的文件作為依據（grounding，即 RAG）」、L163「以檢索到的文件作為依據（grounding）」。
- 05-17.10 [verified] r2 P2 L116「最佳相符不夠近」→ L116「最佳結果的相似度未達門檻」。
- 05-17.11 [verified] r2 P2 L210「範圍蔓延」→ L210「任務範圍失控」（同行「代理就離題」見 05-17.1）。

## 05-nlp-foundations-to-advanced/18-multilingual-nlp
- 05-18.1 [verified] r2 P1 L3、14、48、210、220「跨語言遷移」→ L3 首見已附「（cross-lingual transfer）」；其餘處亦附英文（超額標註，非錯）。
- 05-18.2 [verified] r2 P1 L24「遮罩語言建模」→ L24「遮罩語言建模（masked language modeling）」。
- 05-18.3 [verified] r2 P1 L85「NLI 資料」→ L85「自然語言推論（natural language inference，NLI）」。
- 05-18.4 [kept-ok] r2 P1 L20 圖片 alt「Cross-lingual transfer via shared multilingual embedding space」（維持原樣；稽核 #71 borderline；checker 保護 alt）。
- 05-18.5 [verified] r2 P2 L14「改寫了 NLP 怎麼交付到世界上」→ L14「改變了 NLP 推向全球使用者的方式」。
- 05-18.6 [verified] r2 P2 L26「類型上相近的語言」→ L26「語言類型學上相近的語言」。
- 05-18.7 [verified] r2 P2 L28「最划算的那一根槓桿」→ L28「最具成本效益的做法」。
- 05-18.8 [verified] r2 P2 L42「叫 mT5 或 NLLB」→ L42「應選用 mT5 或 NLLB」。
- 05-18.9 [verified] r2 P2 L145「離拉丁字母很遠的文字」→ L145「非拉丁字母系統的文字」。
- 05-18.10 [kept-ok] r2 P2 L167「切分倍率稅（fertility）」（維持原樣；稽核 #72 borderline）。附英文且後句有釋義，GLOSSARY fertility 保留英文，可保留。
- 05-18.11 [new-issue] P2 L34「第一個實用的多語語言模型」、L213「第一個多語語言模型」：「語語」疊字；建議「多語言模型」。

## 05-nlp-foundations-to-advanced/19-subword-tokenization
- 05-19.1 [kept-ok] r2 P1 L20 圖片 alt「BPE vs Unigram vs WordPiece, character-by-character」（維持原樣；稽核 #73 borderline；checker 保護 alt）。
- 05-19.2 [verified] r2 P2 L3「每個現代大型語言模型都靠其中一種交付」→ L3「每個現代 LLM 都使用其中一種 tokenizer」。
- 05-19.3 [verified] r2 P2 L26「數每一對相鄰的」→ L22「統計每一組相鄰字元對的出現次數」（BPE 段）。
- 05-19.4 [verified] r2 P2 L38「不做前 tokenization」→ L34「不需預先分詞」。
- 05-19.5 [verified] r2 P2 L40「一個函式庫，訓練加服務」→ L36「同一個函式庫即可支援訓練與推論服務」。
- 05-19.6 [kept-ok] f4 D4 保留 L26「可以抽樣（sampling）不同的切分」（不列為問題；原文 can sample tokenizations，屬統計抽樣語境）。

## 05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding
- 05-20.1 [verified] r2 P1 L3「抽樣」→ L3「在取樣（sampling）之前改 logit」。
- 05-20.2 [kept-ok] r2 P1 L26 圖片 alt「Constrained decoding masking invalid tokens at each step」（維持原樣；稽核 #74 borderline；checker 保護 alt）。
- 05-20.3 [verified] r2 P2 L28「抽樣器」→ L28「logit 處理器坐在模型和取樣器之間」。
- 05-20.4 [verified] r2 P2 L35「基於 Pydantic、包住任何 LLM 的包裝」→ L35「以 Pydantic 為基礎，為各種 LLM 提供包裝層」。
- 05-20.5 [verified] r2 P2 L39「這種鷹架」→ L39「這類固定格式片段」。
- 05-20.6 [verified] r2 P2 L171「忍受得了重試」→ L171「可接受重試造成的延遲與成本」。

## 05-nlp-foundations-to-advanced/21-nli-textual-entailment
- 05-21.1 [not-fixed] r2 P1 L1、3「自然語言推論（NLI）」首見英文。L3 無展開問題已解；但標題 L1 現為「自然語言推論（natural language inference，NLI）（natural language inference）」，修法造成重複括註。
- 05-21.2 [kept-ok] r2 P1 L20 圖片 alt「NLI: three-way classification, premise vs hypothesis」（維持原樣；稽核 #75 borderline；checker 保護 alt）。
- 05-21.3 [verified] r2 P1 L233「RTE」（維持原樣；稽核 #76 miss；f2 已修）→ L165「RTE｜辨識文本蘊涵（Recognizing Textual Entailment）」。
- 05-21.4 [verified] r2 P2 L3「在正式環境裡卻是承重的」（維持原樣；稽核 #77 miss；f2 已修）→ L3「在正式環境（production）裡卻是不可或缺的基礎」。
- 05-21.5 [verified] r2 P2 L17「說成話的標籤」→ L22「轉述成自然語句的標籤」。
- 05-21.6 [verified] r2 P2 L49「開放的預設」→ L74「常用開源預設模型」。
- 05-21.7 [verified] r2 P2 L111「每個主張對上檢索到的脈絡」→ L101「逐一檢查每項主張是否受到檢索脈絡蘊涵」。
- 05-21.8 [verified] r2 P2 L145「NLI 是文字理解的膠帶」→ L128「NLI 是文字理解的萬用補強工具」。
- 05-21.9 [verified] r2 P2 L212「看它會不會壞」→ L156「觀察模型是否因此失效」。
- 05-21.10 [verified] r2 P2 L225「有黃金脈絡的」→ L158「有人工標註參考脈絡的」。

## 05-nlp-foundations-to-advanced/22-embedding-models-deep-dive
- 05-22.1 [verified] r2 P1 L32、211「延遲互動」→ L32「多向量（晚期互動）」、L211「正式環境裡的晚期互動」。
- 05-22.2 [verified] r2 P1 L36「Matryoshka 表示學習」→ L36「Matryoshka 表示學習（Matryoshka Representation Learning）」。
- 05-22.3 [verified] r2 P1 L38–40「MTEB」（維持原樣；稽核 #78 miss；f2 已修）→ L40「大規模文本 embedding 評測（Massive Text Embedding Benchmark，MTEB）」。
- 05-22.4 [kept-ok] r2 P1 L26 圖片 alt「Dense, sparse, and multi-vector embeddings」（維持原樣；稽核 #79 borderline；checker 保護 alt）。
- 05-22.5 [verified] r2 P2 L91「前幾層這樣做幾乎無損」→ L91「在前幾個截斷層級幾乎不會損失品質」。
- 05-22.6 [verified] r2 P2 L134「從零手寫餘弦」→ L134「### 步驟 5：從零實作餘弦相似度」。
- 05-22.7 [kept-ok] r2 P2 L144「不理延遲（latency）的尾端」（維持原樣；稽核 #80 borderline）。可讀；建議「延遲長尾」但不列為錯。
- 05-22.8 [verified] r2 P2 L191「挑帕累托意義上划算的那一個」→ L191「選出帕累托最佳解」。

## 05-nlp-foundations-to-advanced/23-chunking-strategies-rag
- 05-23.1 [kept-ok] r2 P1 L26 圖片 alt「Six chunking strategies visualized on one passage」（維持原樣；稽核 #81 borderline；checker 保護 alt）。
- 05-23.2 [verified] r2 P1 L28–40「固定切塊、遞迴、語意、句子、父文件、延遲切塊、脈絡化檢索」首見英文（維持原樣；稽核 #82 miss；f2 已修）→ L28「固定切塊（fixed chunking）」、L30「遞迴（recursive chunking）」、L32「語意（semantic chunking）」、L34「句子（sentence chunking）」、L36「父文件（parent-document）」、L38「後置切塊（late chunking，2024）」、L40「脈絡化檢索（contextual retrieval，Anthropic，2024）」。
- 05-23.3 [verified] r2 P1 L38、203、248、256「延遲切塊」→ 全篇改「後置切塊」；全課無「延遲切塊」殘留。
- 05-23.4 [verified] r2 P2 L30「退回得很乾淨」→ L30「可順利退回較低層級的分隔符」。
- 05-23.5 [verified] r2 P2 L52、207「前 K 筆／前 5 的召回率」→ L52「top-K 結果」、L207「recall@5（前 5 名召回率）」已改；其餘殘留見 05-23.7。
- 05-23.6 [verified] r2 P2 L40「This chunk is section 3.2 of the termination clauses…」→ L40「這個區塊是終止條款第 3.2 節……」。
- 05-23.7 [new-issue] P2 L207「recall@5（前 5 名召回率）（recall）」多餘英文括註「（recall）」，且「量recall@5」缺半形空格；L52「檢索器的top-K 結果」缺空格。

## 05-nlp-foundations-to-advanced/24-coreference-resolution
- 05-24.1 [kept-ok] r2 P1 L25 圖片 alt「Coreference clustering: mentions → entities」（維持原樣；稽核 #83 borderline；checker 保護 alt）。
- 05-24.2 [verified] r2 P1 L39–41「提及配對分類器」「提及排序」「基於 span 的端到端」（維持原樣；稽核 #84 miss；f2 已修）→ L39「提及配對分類器（mention-pair classifier）」、L40「提及排序（mention-ranking）」、L41「基於 span 的端到端（span-based end-to-end，Lee 等人，2017）」。
- 05-24.3 [verified] r2 P1 L150「標準結果（ground truth）」→ L150「真實標註資料（ground truth）」。
- 05-24.4 [verified] r2 P2 L3「…lunch.」。引號後句號重複（維持原樣；稽核 #85 miss；f2 已修）→ L3「…at lunch.」三個指稱，已無重複句號。
- 05-24.5 [kept-ok] r2 P2 L14「表面 NLP……之間的黏合」（維持原樣；稽核 #86 borderline）。可讀；建議「表層」與「橋樑」但不列為錯。
- 05-24.6 [verified] r2 P2 L32「名詞性」→ L32「名詞性提及」。
- 05-24.7 [verified] r2 P2 L105「單例爆炸」→ L105「單一提及群集過多」。
- 05-24.8 [verified] r2 P2 L42「簡單情況很好，長文件和罕見所指會掙扎」→ L42「簡單案例表現良好，但處理長文件和罕見所指時仍有困難」。

## 05-nlp-foundations-to-advanced/25-entity-linking
- 05-25.1 [verified] r2 P1 L1、22「消歧」→ L1 標題「實體連結與消歧（entity linking and disambiguation）」（唯一附英文）；L23「實體連結與消歧。」；E1 重複括註已移除。
- 05-25.2 [kept-ok] r2 P1 L29 圖片 alt「Entity linking pipeline: mention → candidates → disambiguated entity」（維持原樣；稽核 #87 borderline；checker 保護 alt）。
- 05-25.3 [verified] r2 P1 L21–23、43「候選生成、消歧、提及召回率」（維持原樣；稽核 #88 miss；f2 已修）→ L22「候選生成（candidate generation）」、L43「提及召回率（mention recall，候選生成）」。
- 05-25.4 [not-fixed] r2 P2 L43「黃金提及」、L184「黃金實體連結」。L43 已改「人工標註的提及」；但 L184 表格「1,393 篇帶黃金實體連結的 Reuters 文章」仍在。
- 05-25.5 [verified] r2 P2 L12「Jordan beat the press.」。引號後句號重複（維持原樣；稽核 #89 miss；f2 已修）→ L12 無重複句號。
- 05-25.6 [verified] r2 P2 L39「端到端對上管線」→ L39「端到端架構與管線式架構」。
- 05-25.7 [verified] r2 P2 L124「熱門偏差」→ L124「流行度偏差」。
- 05-25.8 [verified] r2 P1 L36「取餘弦（cosine）最大的」→ L36「取餘弦相似度（cosine similarity）最大的」。

## 05-nlp-foundations-to-advanced/26-relation-extraction-kg
- 05-26.1 [kept-ok] r2 P1 L25 圖片 alt「Text → triples → knowledge graph」（維持原樣；稽核 #90 borderline；checker 保護 alt）。
- 05-26.2 [verified] r2 P1 L19「關係抽取（RE）」→ L19「關係抽取（relation extraction，RE）」。
- 05-26.3 [verified] r2 P1 L20、46「脈絡精確率（precision）、脈絡召回率（recall）」。定位錯誤：05/26 現況無此字串（稽核 #91 已指出）；實質對應 05/27 L20、L45–47，已由 f2 修為附英文（見 05-27.3）。
- 05-26.4 [verified] r2 P1 L35「AEVS（錨定–抽取–驗證–補充）」首見未附英文（維持原樣；稽核 #92 miss；f2 已修）→ L21、L35 皆附 Anchor-Extraction-Verification-Supplement。
- 05-26.5 [verified] r2 P1 L86「遠距監督資料」→ L84「在遠距監督（distant supervision）資料上 fine-tune」。
- 05-26.6 [kept-ok] r2 P2 L3、21、207「出處（provenance）」（維持原樣；稽核 #93 ok）。已附英文，L207 表格有釋義。
- 05-26.7 [verified] r2 P2 L3、19「加總」→ L3「彙整」、L19「在語料庫上彙整」。
- 05-26.8 [verified] r2 P2 L31「脆、準、說得清楚」→ L31「脆弱、精確且可解釋」。
- 05-26.9 [not-fixed] r2 P2 L49「開放資訊抽取出來發現」。現況 L49「先用開放資訊抽取探索關係，再將其標準化到封閉本體，再把關係標準化到封閉本體上，才併進主圖」，修法後重複「標準化到封閉本體」子句。應合併為「先用開放資訊抽取探索關係，再把關係標準化到封閉本體，才併進主圖」。
- 05-26.10 [verified] r2 P2 L68「仍在領域管線裡交付」→ L68「Hearst 模式仍用於特定領域的正式管線」。
- 05-26.11 [verified] r2 P2 L150「很多關係有時間界」→ L149「許多關係只在特定時間範圍內成立」。

## 05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks
- 05-27.1 [kept-ok] r2 P1 L28 圖片 alt「Four evaluation dimensions, LLM-as-judge architecture」（維持原樣；稽核 #94 borderline；checker 保護 alt）。
- 05-27.2 [verified] r2 P1 L20、30「LLM 當評審」→ L3、L24、L30「LLM-as-judge（LLM 當評審）」首見已附英文。
- 05-27.3 [verified] r2 P1 L20、45–46「答案相關性、脈絡精確率、脈絡召回率」（維持原樣；稽核 #95 miss；f2 已修）→ L20 與表格 L45–47 皆附 answer relevance、context precision、context recall。
- 05-27.4 [verified] r2 P1 L32「GPT-4o-mini $0.003 per scored case enables …」整句英文殘留（維持原樣；稽核 #96 P0 miss；f2 已修）→ L32「GPT-4o-mini 每個已評分案例約 0.003 美元，1000 個樣本的回歸評測不到 5 美元。」英文整句已刪。
- 05-27.5 [verified] r2 P2 L3「人工審查擴不了規模」→ L3「人工審查無法因應如此大的評估規模」。
- 05-27.6 [verified] r2 P2 L20「有研究撐著，很輕」→ L20「有研究支持，且輕量」。
- 05-27.7 [not-fixed] r2 P2 L51「在對上人類標籤有相關之前」「畫評審對人」。「畫評審對人」已改「繪製評審與人工分數的比較圖」；但 L51 仍有「在對上人類標籤（label）有相關之前，不要信原始的評審分數」（逐字直譯未改）。
- 05-27.8 [verified] r2 P2 L175「原始加總藏起失敗」→ L175「整體平均分數會掩蓋失敗案例」。
- 05-27.9 [verified] r2 P2 L176「黃金資料集（dataset）腐壞」→ L176「評估資料集逐漸失效」。
- 05-27.10 [not-fixed] r2 P2 L175「最底下的分位數」。L175 已改「最低分位數」；但 L223「加上最底下分位數的警報」仍存（同類未修）。
- 05-27.11 [new-issue] P2「黃金」直譯殘留（同 05/13 已修之「黃金參考／黃金答案」類）：L13「黃金參考是：『June 29, 2007.』」、L47「對上黃金答案的 LLM 評審」、L233「黃金答案的主張裡」。

## 05-nlp-foundations-to-advanced/28-long-context-evaluation
- 05-28.1 [kept-ok] r2 P1 L24 圖片 alt「NIAH baseline, RULER multi-task, LongBench holistic」（維持原樣；稽核 #97 borderline；checker 保護 alt）。
- 05-28.2 [verified] r2 P1 L3、26「長脈絡評估」→ L3「長脈絡評估（long-context evaluation）告訴你」首見已附英文；標題保留英文原題。
- 05-28.3 [verified] r2 P2 L3「Gemini 3 Pro 廣告……廣告上的 ≠ 用得上的」（維持原樣；稽核 #98 miss；f2 已修）→ L3「Gemini 3 Pro 宣稱支援 1000 萬個 token 的脈絡……宣稱的容量 ≠ 用得上的容量」；L16、L42、L47 的「廣告」同步改「宣稱」。
- 05-28.4 [verified] r2 P2 L26「前沿模型現在把它做飽和了」→ L26「前沿模型目前在這項基準上已接近滿分」。
- 05-28.5 [verified] r2 P2 L28「揭露出 NIAH 飽和、多跳卻失敗的模型」→ L28「能在 NIAH 上接近滿分、卻無法勝任多跳任務的模型」。
- 05-28.6 [verified] r2 P2 L30「長的上下文學習（in-context learning）」→ L30「長脈絡內學習（long in-context learning）」。
- 05-28.7 [verified] r2 P2 L45「準確率（accuracy）對脈絡長度，按任務類型畫」→ L45「按任務類型繪製準確率隨脈絡長度變化的曲線」。
- 05-28.8 [verified] r2 P2 L135、183、189「填充文」→ 統一「填充文字」。
- 05-28.9 [verified] r2 P2 L145「快速健全檢查」→ L145「快速初步檢查」。

## 05-nlp-foundations-to-advanced/29-dialogue-state-tracking
- 05-29.1 [kept-ok] r2 P1 L26 圖片 alt「DST: dialog history → slot-value state」（維持原樣；稽核 #99 borderline；checker 保護 alt）。
- 05-29.2 [verified] r2 P1 L19「會用工具的代理」→ L19「會使用工具的 agent」。
- 05-29.3 [verified] r2 P1 L14、32「DST」「封閉詞彙的槽位」→ 標題 L1「對話狀態追蹤（dialogue state tracking）」；L32「封閉詞彙表槽位（closed-vocabulary slot）」。
- 05-29.4 [verified] r2 P1 L134「校準：系統在多少比例的輪次把所有槽位都做對？」→ L134「計算／評估：系統有多少比例的輪次能讓所有槽位都正確？」。
- 05-29.5 [kept-wrong] r2 P2 L14「DST 是……之間的轉折」（維持原樣；稽核 #100 borderline）。現況仍為「DST 是使用者說的話、和後端執行的事之間的轉折」。hinge 指連接兩端的關鍵樞紐，「轉折」易被讀成事件轉折，語意偏移風險。建議「樞紐」或「關鍵橋樑」。
- 05-29.6 [verified] r2 P2 L41「領域–槽位的 prompting」→ L41「依領域與槽位設計 prompt」。
- 05-29.7 [verified] r2 P2 L61「蓋住 70% 的制式說法」→ L61「在窄領域可涵蓋窄領域中 70% 的常見固定表達」（修法可；「窄領域」重複見 05-29.9）。
- 05-29.8 [verified] r2 P2 L77「脆在制式詞彙之外。確定性的槽位確認行得通。」→ L77「超出標準詞彙範圍就容易失效；適合用於確定性高的槽位確認」。
- 05-29.9 [new-issue] P2 L61「在窄領域可涵蓋窄領域中 70%」：「窄領域」重複。
- 05-29.10 [verified] r2 P2 L153「隱含繼承」→ L153「槽位值延續」。
- 05-29.11 [verified] r2 P2 L150「把較舊的輪次摘要掉」→ L150「摘要較早的對話輪次」。
- 05-29.12 [new-issue] P2 L33「把槽位值生成成自由文字」：疊字「生成成」；建議「生成為自由文字」。

---

## 07-transformers-deep-dive/01-why-transformers
- 07-01.1 [verified] r3 P1 首見「序列模型」（維持原樣；稽核 K022 miss；f3 已修）→ L12「最前沿的序列模型（sequence model）」。
- 07-01.2 [not-fixed] r3 P2 多處直譯：已套用 L3「架構選擇」；未套用：L16「把這股擠壓放軟」（建議「緩解資訊壓縮」）、L28「這浪費了 99% 的矽」（建議「浪費 99% 的運算資源」）、L30「注意力是廣播」（建議「注意力可平行傳播資訊」）、L32、L99「串列深度」（建議「循序計算深度」）、L48「編成一串加法」、L82「循環沒死，它是一個元件」（建議「循環架構並未消失，而是成為組成元件之一」）。

## 07-transformers-deep-dive/02-self-attention-from-scratch
- 07-02.1 [kept-wrong] r3 P1 L39–41、L310–312 空行（維持原樣；稽核 K023 borderline）。en L39「Every token generates three vectors:」與清單同段無空行，en L309「This lesson produces:」同；譯稿於引導句後插入空行（prose block 69→71），違反 STYLE「段落一一對應」。官方檢查器未攔截。建議移除空行。
- 07-02.2 [verified] r3 P1「加權和」→「加權總和」（維持原樣；稽核 K024 miss；f3 已修）→ L12、L45、L135、L137、L156 皆為「加權總和」。
- 07-02.3 [verified] r3 P1 首見「查詢、投影、注意力矩陣、注意力分數」（維持原樣；稽核 K025 miss；f3 已修）→ L3「查詢（query）表」、L12「投影（projection）」、L14「注意力矩陣（attention matrix）」、L45「注意力分數（attention score）」。
- 07-02.4 [not-fixed] r3 P2 多處直譯（部分套用：「查找表→查詢表」「加權總和」）。未套用：L21「給出修法」、L21「但它仍然栓在 RNN 上」、L23「在單一個平行步驟裡注意到其他每個位置」、L29「把注意力想成一次軟的資料庫查找」、L45「那些分數拿來加權值」、L229「為一句話做出假的 embedding」。

## 07-transformers-deep-dive/03-multi-head-attention
- 07-03.1 [verified] r3 P1 首見「注意力頭、投影、子空間、鍵、潛在空間」（維持原樣；稽核 K026 miss；f3 已修）→ L3「注意力頭（attention head）」、L14「投影（projection）」「子空間（subspace）」、L16「鍵（key）」、L39「潛在空間（latent space）」。
- 07-03.2 [not-fixed] r3 P2 多處直譯（已套用：L12「混在同一個 softmax 分布」、L24「進行注意力計算時彼此獨立」、L28「基礎機制」、L62「一次重塑操作」）。未套用：L3「頭是免費的。多拿幾個。」、L16「2026 年每個交付出去的 transformer 的預設」（建議「所有 transformer 的預設架構」）、L39「把 KV 快取的記憶體（memory）砍到 N/G 分之一」（建議「降至」）。

## 07-transformers-deep-dive/04-positional-encoding
- 07-04.1 [verified] r3 P1 L18「RoPE——旋轉位置 embedding」→ L19「RoPE（Rotary Position Embedding）」。
- 07-04.2 [verified] r3 P1 首見「位置編碼、外推、注意力分數、相對位置」（維持原樣；稽核 K027 miss；f3 已修）→ L1「位置編碼（positional encoding）」、L18「外推（extrapolation）」、L20「注意力分數（attention score）」、L74「相對位置（relative position）」。
- 07-04.3 [not-fixed] r3 P2 多處直譯（已套用：L3「注意力具有排列不變性」、L149「重縮放」、L18「外推很差」）。未套用：L12「縮放點積注意力是順序盲的」（建議「不感知順序」）、L16「修法是想辦法把位置注入 embedding」（建議「將位置資訊注入 embedding」）、L50「漂亮的手法」（建議「巧妙的作法」）、L56「直接偏置注意力分數」（建議「為注意力分數加入偏置」）、L62「較近的 token 被抬高」（建議「提高較近 token 的注意力分數」）。
- 07-04.4 [observation] 全篇用「外推」；GLOSSARY「extrapolation｜外插（機器學習預測語境）」。未列為錯，請 supervisor 確認沿用「外推」（LLM 位置外推慣用語）或統一為 GLOSSARY 譯法。

## 07-transformers-deep-dive/05-full-transformer
- 07-05.1 [verified] r3 P1 L58、159「暖機」→ L58「沒有小心的預熱（warmup）」、L161「不用預熱的花招也能訓練得更深」。
- 07-05.2 [verified] r3 P1 首見「位置訊號、殘差連接、層正規化、殘差流、參數數量」（維持原樣；稽核 K028 miss；f3 已修）→ L24「位置訊號（position signal）」、L27「殘差連接（residual connection）」、L28「層正規化（layer normalization）」「殘差流（residual stream）」、L75「參數數量（parameter count）」。
- 07-05.3 [not-fixed] r3 P2 多處直譯（僅套用「鷹架→支架」L3）。未套用：L12「沒有對的配管，深度會壞掉」（建議「沒有適當的架構支援，模型就難以加深」）、L16「這一課是骨架」（建議「本課介紹整體架構」）、L31「殘差把它往前帶」（建議「殘差連接將資訊向前傳遞」）、L58「Post-norm 大約在 2019 年失寵」（建議「逐漸不再採用」）、L62「Vaswani 2017 交付的是 LayerNorm 加 ReLU」（建議「原始論文採用…」）、L68、L123「對得上」（建議「相符」）、L130「標準函式庫的參考裡」（建議「標準函式庫的實作範例」）、L143「仍然最好」（建議「表現最佳」）。

## 07-transformers-deep-dive/06-bert-masked-language-modeling
- 07-06.1 [verified] r3 P1 首見「預訓練、分布偏移」（維持原樣；稽核 K029 miss；f3 已修）→ L12「預訓練（pretraining）好」、L45「分布偏移（distribution shift）」。
- 07-06.2 [not-fixed] r3 P2 多處直譯（已套用約 7 項，如 L14「參數效率帶來重大啟發」、L45「避免模型只依賴遮罩 token」、L64「推論比 DeBERTa-v3 快 2 到 3 倍」、L108「兩種情況都應產生合理的 token 分布」、L127「經對比損失訓練的 BERT」、L129「查詢與文件間的雙向注意力」、L131「以較小解碼器的彈性達到相近品質」）。未套用：L3「差一句話——以及之後五年裡，所有長得像 embedding 的東西」（建議「兩者只差一個預測任務，卻影響了此後五年的 embedding 技術」）、L16「地球上每一個搜尋引擎、內容審核管線、語意搜尋系統裡面都有一個 BERT」（建議「各大搜尋引擎……都採用 BERT」）。

## 07-transformers-deep-dive/07-gpt-causal-language-modeling
- 07-07.1 [verified] r3 P0 L69「遮罩從來不是加到注意力上的」→ L65「`-inf` 遮罩不是新機制。它是第 1 階段的那些零，搬進 softmax 的輸入域。」（修正；與 en 相符）。
- 07-07.2 [verified] r3 P1 首見「next-token prediction、因果遮罩、前綴平均、列隨機矩陣、溫度」（維持原樣；稽核 K030 miss；f3 已修）→ L12、L16 next-token prediction（保留英文）、L16「因果遮罩（causal mask）」、L39「前綴平均（prefix averaging）」、L65「列隨機矩陣（row-stochastic matrix）」、L99「溫度（temperature）」。
- 07-07.3 [new-issue] P1 GLOSSARY 違規：生成語境「抽樣」應為「取樣」（GLOSSARY「sampling」註記生成模型用「取樣」；「temperature sampling＝溫度取樣」）。L94「抽樣的選擇比大家想的更要緊」、L99「logits 除以 T，再抽樣」、L142「### 步驟 4：抽樣」、L144「一個抽樣函式是 10 行」、L173「挑抽樣參數」、L188「抽樣發生在這些分數上」。報告未列；屬同類殘留。
- 07-07.4 [not-fixed] r3 P2 多處直譯（已套用：L3「影響最深遠的一行程式碼」、L65「新機制」）。未套用：L18「架構上的修煉」（建議「架構上的改良」）、L39「反方向把推導跑一遍」（建議「從反方向推導」）、L41「一條序列最笨的因果摘要」（建議「最簡單的因果摘要」）、L79「自迴歸（autoregressive）稅」（建議「自迴歸帶來的代價」）、L105「是任何正式環境（production）推論堆疊的基本配備」（建議「基本功能」）。

## 07-transformers-deep-dive/08-t5-bart-encoder-decoder
- 07-08.1 [verified] r3 P1 首見「編碼器–解碼器、稠密表示、遮罩區段預測、去噪自編碼器、文字填空」（維持原樣；稽核 K031 miss；f3 已修）→ L1「編碼器–解碼器（encoder–decoder）模型」、L19「稠密表示（dense representation）」、L23「遮罩區段預測（masked span prediction，…）」、L24「去噪自編碼器（denoising autoencoder）」、L71「文字填空（text infilling，…）」。「哨兵」首見 L56 已附「（sentinel）」，L113 為非首見。
- 07-08.2 [verified] r3 P1 L79、94「top-p 抽樣／抽樣」→ L79「貪婪／集束／top-p 取樣都適用」；全課無「抽樣」殘留。
- 07-08.3 [not-fixed] r3 P2 多處直譯（已套用：L3、L12「輸入到輸出」、L23「遮罩區段預測」、L63「表現相近」、L75「下游表現最佳」、L100「最重要的單一元件」、L137「執行數十種任務」）。未套用：L12「各自為了不同目標把 2017 年的架構削薄」（建議「簡化 2017 年的架構」）、L33「只有解碼器搶走了鎂光燈」（建議「純解碼器模型成為焦點」）。

## 07-transformers-deep-dive/09-vision-transformers
- 07-09.1 [verified] r3 P1 首見「圖塊」「線性投影」（維持原樣；稽核 K032 miss；f3 已修）→ L3「圖塊（patch）」、L14「線性投影（linear projection）」。「監督式預訓練」「自監督特徵」於現況不存在。
- 07-09.2 [new-issue] P1 L12「2020 年以前，電腦電腦視覺主要依賴卷積」：修 r3「視覺就是卷積」時產生疊字「電腦電腦」。
- 07-09.3 [not-fixed] r3 P2 多處直譯（已套用：L36「只需兩行程式碼」、L66「在相同計算量下」、L74「僅用標準函式庫切分圖塊」、L59「自監督（self-supervised，沒有標籤）」）。未套用：L3「同一個 transformer 兩邊都吃」（建議「transformer 可處理兩者」）、L14「原味的 transformer 編碼器」（建議「標準 transformer」）。

## 07-transformers-deep-dive/10-audio-transformers-whisper
- 07-10.1 [verified] r3 P1 mel 譯名統一（維持原樣；稽核 K033 miss；f3 已修）→ L3「梅爾頻譜圖（mel-spectrogram）」、L18「對數梅爾頻譜圖（log-mel spectrogram）」、L28「80 個梅爾頻率槽」、L104、L173、L180–181 皆統一。
- 07-10.2 [verified] r3 P1 首見（語音活動偵測、語言辨識、時間戳記、編碼器–解碼器、步幅、前處理）（維持原樣；稽核 K034 miss；f3 已修）→ L17、L18、L32、L168。
- 07-10.3 [not-fixed] r3 P1「80 個 mel 頻帶、10 毫秒步幅」「hop = 10 毫秒」。L28、L173 已改「梅爾頻率槽、10 毫秒跳躍長度（stride）」；但 L116「hop = 10 毫秒」、L172「10 毫秒 hop」仍用 hop（GLOSSARY hop size＝跳躍長度）；L182 音框列「以 10 毫秒步幅重疊」與跳躍長度不一致。
- 07-10.4 [not-fixed] r3 P2 多處直譯（已套用：L3「以梅爾頻譜圖為輸入並產生語音」）。未套用：L12「換領域就脆」（建議「跨領域泛化能力弱」）、L30「### 步驟 2——卷積的莖」（建議「卷積 stem」）、L40「從一個 BPE 詞彙產出 token」（建議「從 BPE 詞彙表產生 token」）、L79「用 VAD 加重疊把串流接上去」（建議「以重疊視窗拼接串流」）、L80「沒有外部切塊」（建議「外部切分」）。
- 07-10.5 [observation] 「影像」（L3、L28）：GLOSSARY「image｜映像」列註為 Docker 語境；ML 語境已有「影像分類」「影像壓縮」先例；未列為錯。

## 07-transformers-deep-dive/11-mixture-of-experts
- 07-11.1 [kept-wrong] r3 P1 L131–139「When to pick MoE」「When NOT to pick MoE」後空行（維持原樣）。en L131、L136 與清單同段無空行；譯稿多 2 行（prose block 55→57）。同 07-02.1 段落結構問題。
- 07-11.2 [verified] r3 P1「評測」→「效能基準測試」（L3、L75 等）；全課無「評測」殘留。
- 07-11.3 [verified] r3 P1 首見（路由器、活躍參數、負載平衡、專家容量、共用專家、細粒度專家、專家平行）（維持原樣；稽核 K036 miss；f3 已修）→ L14「路由器（router）」「活躍參數（active parameters）」、L44「負載平衡（load balancing）」、L49「專家容量（expert capacity）」、L54「共用專家（shared experts）」、L58「細粒度專家（fine-grained experts）」、L79「專家平行（expert parallelism）」。
- 07-11.4 [verified] r3 P2 L3「每個評測都打贏它」→ L3「在所有效能基準測試中都勝過它」。
- 07-11.5 [verified] r3 P2 L12「推論時的 FLOPs 等於參數數量」：r3 建議「約等於參數量的兩倍」會改義；現況 L12「等於它的參數數量（前向再乘 2）」與 en 一致（"equal its parameter count (times 2 for forward pass)"），採現況。
- 07-11.6 [not-fixed] r3 P2 多處直譯（已套用：L129「最快的專家平行處理路徑」）。未套用：L14「把這條鏈拆開」（建議「將兩者拆開」）、L46「其他專家就挨餓」（建議「其他專家則可能閒置」）、L56「共用專家抓住共同知識」（建議「學習共通知識」）、L62「組合縮放快非常多」（建議「可用的專家組合數增加得更快」）、L79「全部專家都住在 GPU 上」（建議「所有專家都必須常駐 GPU」）、L118「參數總數看了會嚇到」（建議「參數總量相當驚人」）、L140「延遲要緊的單人服務」（建議「對延遲敏感的單使用者服務」）、L145「共用專家的布局」（建議「配置」）。

## 07-transformers-deep-dive/12-kv-cache-flash-attention
- 07-12.1 [kept-wrong] r3 P1 L106–108「2026 defaults」後空行（維持原樣）。en L106 與清單同段無空行；譯稿多 1 行（prose block 66→67）。同 07-02.1。
- 07-12.2 [verified] r3 P1「加速／加速比、前向、位元相同」→「加速比」：L93 表頭、L108、L109、L213；「前向傳遞」：L87、L98、L100、L104、L213；「完全相同」：L89。
- 07-12.3 [verified] r3 P1 首見（隱藏狀態、分塊、工作集、前綴快取）（維持原樣；稽核 K039 miss；f3 已修）→ L12「隱藏狀態（hidden state）」、L19「分塊（tiling）」、L174「工作集（working set）」、L204「前綴快取（prefix caching）」；HBM／SRAM 原文即英文。
- 07-12.4 [new-issue] P1 L21「都都以這些技術為前提」疊字；「每個前沿模型發布時都啟用 Flash Attention Flash Attention」英文重複。二者皆為 r3 P2 修法（「假設它們在」「出貨時都開著」）引入（en L21：Every frontier model ships with Flash Attention enabled.）。
- 07-12.5 [not-fixed] r3 P2 多處直譯（已套用：L14「需要搬移大量資料」、L56「調整維度」、L87「反向傳播時重新計算部分前向傳遞的值」、L104「一次大模型前向傳遞」、L114「GPU 閒置」、L120「vLLM 的代表功能」）。未套用：L54「GQA 是 KV cache 的大勝利」（建議「GQA 大幅降低 KV cache 成本」）、L16「把前沿推論從『慢』推到『快』」（建議「讓前沿推論從……提升至……」，僅部分套用）、L12「單純（naive）的自迴歸解碼器」（建議「樸素解碼器」，可接受）。
- 07-12.6 [verified] r3 P2 L116、L204「吞吐量」：現況「多 5 到 10 倍」「5 倍吞吐量」與 en（5–10× throughput gain、5× throughput gain）一致；r3 建議「吞吐量常可提升至 5 倍」非必要。

## 07-transformers-deep-dive/13-scaling-laws
- 07-13.1 [not-fixed] r3 P1「評測」→「效能基準測試」（L21）：現況「在每個每項效能基準測試上打贏 GPT-3」為修法造成的疊字「每個每項」（en：beat GPT-3 on every benchmark）。應為「在每項效能基準測試上打贏 GPT-3」。L71「每項效能基準測試上的跳躍」正確。
- 07-13.2 [verified] r3 P1「減不掉的損失」→「不可約損失」：L40「不可約損失天花板（loss floor）」。
- 07-13.3 [verified] r3 P1「基礎模型」→「基模型」：L120「基模型每個參數 20 個 token」；全課無「基礎模型」殘留。
- 07-13.4 [verified] r3 P1 首見（訓練運算、損失天花板、運算最佳、運算最佳前緣、資料策展、漸近線、突現能力）（維持原樣；稽核 K040 miss；f3 已修）→ L12「訓練運算（training compute）」、L40「不可約損失天花板（loss floor）」、L51「運算最佳（compute-optimal）」、L104「運算最佳的前緣（compute-optimal frontier）」、L127「資料策展（data curation）」「漸近線（asymptote）」、L150「突現能力（emergent abilities）」。
- 07-13.5 [verified] f4 E3 L137「前緣（compute-optimal frontier）」→「前緣」去重已套用；L137 現為「對運算最佳前緣，畫損失對 log10(C)」，首見 L104 保留英文，無問題。
- 07-13.6 [not-fixed] r3 P2 多處直譯（已套用：L3「運算分成兩部分」、L14「模型更大，容量（capacity）更高」）。未套用：L21「訓練一小族叫 Chinchilla 的模型」（建議「一系列 Chinchilla 模型」）、L23「換更小且部署（deployment）得了的足跡」（建議「換成較小且可部署的模型」）、L55「訓練成本付一次；推論成本付到永遠」（建議「訓練成本只支付一次，推論成本則會持續累積」）、L60「延遲（latency）是 Chinchilla 最佳的 700 億的一小段」（建議「延遲僅為……的一小部分」）、L63「看服務量」（建議「依服務量而定」）、L71「評分器的假象」（建議「評分方式造成的假象」）、L83「有效運算可以複利」（建議「有效運算量能複利成長」）、L85「有大約 2 倍的有效運算增益」（建議「有效運算量提升約 2 倍」）、L85、L127「絕對常數」（建議「乘數常數」）、L102「把 L 畫成 (N, D) 的等高線」（建議「繪製 L 的等高線」）、L120「在某個損失地板飽和」（建議「某個損失下限」）。

## 07-transformers-deep-dive/14-build-a-transformer-capstone
- 07-14.1 [not-fixed] r3 P1「梯度裁切」→「梯度裁剪」（L60、L170）：L171 已改「梯度裁剪（gradient clipping）」；但 L60「梯度（gradient）裁切」仍為舊譯名（GLOSSARY gradient clipping＝梯度裁剪）。
- 07-14.2 [verified] r3 P1「暖身（warmup）」→「預熱」：L172「學習率先線性爬升，這段叫預熱」。
- 07-14.3 [verified] r3 P1 首見（端到端、訓練迴圈、驗證損失、位元組級、梯度裁剪、學習率排程）（維持原樣；稽核 K041 miss；f3 已修）→ L14「端到端（end-to-end）」、L60「訓練迴圈（training loop）」、L76「驗證損失（validation loss，…）」、L87「位元組級（byte-level）」、L171「梯度裁剪（gradient clipping）」、L172「餘弦學習率排程（learning-rate schedule）」。
- 07-14.4 [not-fixed] r3 P2 多處直譯（已套用：L14「真正的語言模型」）。未套用：L76「驗證損失……緊跟著訓練損失」（建議「與訓練損失相近」）、L103「沒有 tokenizer 的戲」（建議「也不需要複雜的 tokenizer」）、L111「挪一位的交叉熵」（建議「將目標序列向後位移一格後計算交叉熵」）、L126「從 top-p 的 logits 取樣，接上去，繼續」（建議「從 logits 取樣並接續生成」）、L139「這是清楚的勝利」（建議「這是明確的成果」）、L143「要把它做成真的東西」（建議「要把它發展成實際應用」）、L149「最後會是一個 1.25 億參數的 GPT」（建議「最終會得到一個……」）、L170「2021 年以來的標準」（建議「自 2021 年以來的標準做法」）、L16「借它的形狀，再依我們講過的東西改裝」（建議「沿用其架構並依本課內容調整」）、L74「訓練損失從大約 4.2（隨機）降到大約 1.5，大約 6 分鐘」（建議「耗時約 6 分鐘」）、L84「腳本處理：」（建議「腳本會執行以下工作：」）。

## 07-transformers-deep-dive/15-attention-variants
- 07-15.1 [verified] r3 P1 首見（滑動視窗、稀疏、差分、拓樸、區塊注意力、差分注意力、稀疏模式）（維持原樣；稽核 K042 miss；f3 已修）→ L1 標題「滑動視窗（sliding window）、稀疏（sparse）、差分（differential）」、L14「拓樸（topology）」、L17「稀疏／區塊注意力（block attention）」、L18「差分注意力（differential attention）」、L50「稀疏模式（sparse pattern）」。
- 07-15.2 [not-fixed] r3 P2 多處直譯（已套用：L3「完整注意力的矩陣形狀是正方形」、L91「因果遮罩比較器」）。未套用：L3「記憶體（memory）付這個代價」（建議「記憶體需求也隨之增加」）、L12「序列長度上要 O(N²) 的記憶體」（建議「序列長度為 N 時需…」）、L12「每個 token 仍然注意每一個別的 token」（建議「所有其他 token」）、L26「視窗外的 token 在分數矩陣裡拿到 -inf」（建議「視窗外的位置在分數矩陣中設為 -inf」）、L42「非零項目——少到 8 分之一」（建議「非零項目數約為完整矩陣的八分之一」）、L53「品質對上時，脈絡經驗上有 2 倍」（建議「品質相當時可支援約兩倍長的脈絡」）、L56「讓自訂稀疏模式在 PyTorch 裡是一等公民」（建議「PyTorch 的一級功能」）、L60「就把權重倒在第一個 token」（建議「集中到第一個 token」）、L72「大海撈針的檢索更尖」（建議「檢索結果更精確」）、L100「下三角；對角線上方權重為零」（建議「下三角矩陣，對角線上方的權重為零」）、L130「往序列起點每隔一個 token」（建議「每隔 stride 個 token 取一個」）、L145「有意識地付記憶體的帳」（建議「明確衡量記憶體成本」）、L177「注意力匯的污染會傷到的工作負載」（建議「容易受注意力匯影響的工作負載」）。

## 07-transformers-deep-dive/16-speculative-decoding
- 07-16.1 [not-fixed] r3 P1 術語與 GLOSSARY：「前向」殘留（GLOSSARY forward pass＝前向傳遞）：L3「貴的模型一次前向驗證全部 N 個」、L79「驗證一次前向把 N 個草稿 token 餵進驗證器」、L146「一次驗證器前向產出六個 token」、L194「每個大模型前向的 token 數」；「抽樣」殘留（生成語境應為取樣）：L38「從頭抽樣的數學洞見」、L67「從每個頭抽樣」。L154「卡方檢定確認落在抽樣誤差裡」屬統計語境，不列為錯。加速比（L40、L174）與取樣（L14、L89）已統一。
- 07-16.2 [not-fixed] r3 P2 多處直譯（已套用：L3「每個 token 都得等待前一個 token」、L57「用驗證器上額外的輸出頭取代草稿模型」、L73「驗證器最後一層的隱藏狀態」）。未套用：L3「貴的模型」（建議「大型模型」）、L12「這就是推測解碼的全部賣點」（建議「核心價值」）、L16「由四族草稿加驗證器主導」（建議「四類草稿－驗證器組合主導推論」）、L40「什麼決定加速比」（建議「哪些因素決定加速比」）、L42「草稿對驗證器的成本比」（建議「草稿模型相對驗證器的成本」）、L51「草稿多接近驗證器。同一族、同一份訓練資料會明顯拉高 α」（建議「使用相同模型家族與訓練資料」）、L52「比較難對上」（建議「較難匹配」）、L79「把 N 個草稿 token 餵進驗證器」（建議「一次送入驗證器」）、L154「經驗上」（建議「實際上」）、L211「暫用 KV 緩衝」（建議「暫存 KV 緩衝區」）。

---

## Summary

- 總計 264 條（05：206 條；07：58 條），另有 2 條觀察（07-04.4、07-10.5，未計入類別）。
- 類別統計（05 ／ 07 ／ 合計）：verified 154 ／ 30 ／ 184；kept-ok 30 ／ 0 ／ 30；not-fixed 11 ／ 20 ／ 31；kept-wrong 2 ／ 3 ／ 5；new-issue 9 ／ 3 ／ 12。

### 優先清單（先修）

P1（錯誤、GLOSSARY 違規、修法引入的錯誤）：
1. 05-10.4 [not-fixed]：L105 錯亂句「這就是 這正是 Luong 方法受到採用的原因的原因。」
2. 05-13.5 [not-fixed]：L133 錯亂句「在沒有整理過的人工整理的參考答案時」。
3. 07-13.1 [not-fixed]：L21 疊字「在每個每項效能基準測試上」。
4. 07-12.4 [new-issue]：L21「都都以這些技術為前提」；「Flash Attention Flash Attention」。
5. 07-09.2 [new-issue]：L12「電腦電腦視覺」。
6. 05-21.1 [not-fixed]：L1 標題重複括註「（natural language inference）」。
7. 05-09.1 [not-fixed]：L26「標準結果（ground truth）」違反 GLOSSARY（ground truth＝真實標籤）。
8. 05-17.1 [not-fixed]：AI agent 語境殘留「代理」：L163、L203、L207、L210、L211、L266。
9. 07-07.3 [new-issue]：生成語境「抽樣」殘留：L94、L99、L142、L144、L173、L188（GLOSSARY 取樣）。
10. 07-14.1 [not-fixed]：L60「梯度裁切」殘留（GLOSSARY＝梯度裁剪）。
11. 07-16.1 [not-fixed]：「前向」殘留（L3、L79、L146、L194）與「抽樣」殘留（L38、L67）。
12. 07-10.3 [not-fixed]：hop／步幅殘留（L116、L172、L182；GLOSSARY hop size＝跳躍長度）。
13. 05-03.2 [not-fixed]：「子詞組合」中文譯名遭刪、英文裸露（L204、L220）。
14. 05-26.9 [not-fixed]：L49 重複子句。
15. 05-25.4 [not-fixed]：L184「黃金實體連結」殘留。
16. 05-27.11 [new-issue]：「黃金」直譯殘留（L13、L47、L233；與 05/13 已修之同類）。
17. 05-17.2 [new-issue]：中英缺半形空格（L52、L131、L202、L242、L260、L261）。
18. 05-17.5 [not-fixed]：L28 殘句「那份提案為實質進展編了兩個月」。
19. 05-27.7、05-27.10 [not-fixed]：L51「在對上人類標籤有相關之前」殘留；L223「最底下分位數」殘留。

P2（kept-wrong、部分套用、小型疊字）：
- kept-wrong：05-29.5（L14「轉折」，hinge 語意偏移）、05-08.3（「閘」首見 L30 無英文，全篇未統一閘門）、段落空行 07-02.1、07-11.1、07-12.1（與 en 段落結構不一致）。
- not-fixed 部分套用（直譯建議未全數套用）：07-01.2、07-02.4、07-03.2、07-04.3、07-05.3、07-06.2、07-07.4、07-08.3、07-09.3、07-10.4、07-11.6、07-12.5、07-13.6、07-14.4、07-15.2、07-16.2。
- 小型疊字／重複（new-issue）：05-01.4「這類類別」、05-06.6「現在在」、05-13.7「受管制的領域」重複、05-18.11「多語語言模型」、05-23.7 重複括註與缺空格、05-29.9「窄領域」重複、05-29.12「生成成」。

### 需要 supervisor 決策（未擅自決定）
1. 決策 A：圖片 alt 維持英文（05 段約 18 條 kept-ok）。無障礙缺口 vs checker 保護與 STYLE「圖片參照」原樣規定。
2. 07-04.4：「外推」全篇使用，GLOSSARY extrapolation＝外插；需確認沿用或統一。
3. 07-02.1、07-11.1、07-12.1：引導句後空行是否依 STYLE「段落一一對應」修正（官方檢查器未攔截）。
4. 05-29.5、05-08.3：低優先，是否列入修正。

### 推薦下一步
先修 P1 清單 1–19（優先 1–5、7–11）；修正後重跑 `scripts/check_translation.py --phase 05-…／07-…` 與本報告的 grep 清單。07 的 P2 直譯批次修可延後。若 f4 仍在執行，05/09 與 07/13 的 f4 變動需重查。

### 工具與限制
- 審查中途一次 bash 呼叫被自動審查拒絕；之後所有核對改用 Read／Grep／find（唯讀）。未重試被拒指令。
- 本審查未修改任何譯稿、未執行 git 操作（無 staged 變更）。