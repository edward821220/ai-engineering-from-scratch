# v1 「維持原樣」條目複審報告（kept-audit）

- 審閱報告：`docs/reviews/zh-tw/r1.md`，共抽出 **97 條**含「維持原樣」的條目（以 awk 逐行抽出，清單見 `/private/tmp/zh-tw-review/kept-list.tsv`），分屬 **54 課**。
- 譯稿：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`（最新版）。
- 原稿：`/private/tmp/aiefs-main-source/phases/<phase>/<lesson>/docs/en.md`。
- 術語依據：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/GLOSSARY.md`；風格依據：`STYLE.md`（專門術語首見須附英文）。
- 行號：一律為**現況** zh-TW.md 行號（原報告行號已因修復而偏移）；以關鍵字定位。
- 判準：(1) 資訊保真（增譯／漏譯／語意改變）；(2) 英文整句殘留；(3) GLOSSARY 違規；(4) 受保護內容；(5) 專門術語首見未附英文 → miss，通用 CS 詞（程式碼、記憶體、終端機、網路、套件、伺服器、日誌檔、行程、陣列、類別、裝置等）→ ok；(6) 語氣與風格。
- 嚴重度僅標在 miss 行末：高／中／低。「低」表示僅缺首見英文等版面性問題。
- 條目順序與原報告一致；每條一行判定。

---

## phases/00-setup-and-tooling/07-docker-for-ai
- [borderline] 「同事的環境……你的模型在他的電腦上崩潰」性別指涉 → zh-TW.md:19「結果你的模型在他的電腦上崩潰」；EN:19「Your model crashes on their machine.」（their 為中性） → 「他」將同事預設為男性，臺灣口語「他」可泛指，影響小。建議改「同事的電腦上」（零成本）。

## phases/00-setup-and-tooling/09-data-management
- [miss] 「文字分類」「影像分類」表格首見未附英文 → zh-TW.md:216「文字分類基礎」、:220「影像分類基礎」（表格首見；EN「Text classification basics」「Image classification fundamentals」）；GLOSSARY 收 text/image classification 為 ML 專門術語 → 首見改「文字分類（text classification）基礎」「影像分類（image classification）基礎」。（嚴重度：低）

## phases/00-setup-and-tooling/11-linux-for-ai
- [ok] 「訓練日誌」 → 本課 zh-TW.md 無此詞，為誤置條目；該句實際在 00-10 zh-TW.md:12「訓練（training）日誌」，已附英文。本課無殘留。建議報告端更正歸屬。

## phases/00-setup-and-tooling/12-debugging-and-profiling
- [ok] 「日誌檔」「終端機輸出」 → zh-TW.md:106「一份日誌檔，而不是……終端機輸出」；通用 CS 詞（GLOSSARY log file、terminal），依判準 5 可不加註。
- [miss] 「前向傳遞」「反向傳遞」首見未附英文 → zh-TW.md:379「分別測量資料載入、前向傳遞和反向傳遞的時間」（本課首見，位於練習段）；GLOSSARY forward pass／backward pass 為 DL 專門術語 → 首見改「前向傳遞（forward pass）」「反向傳遞（backward pass）」。（嚴重度：低）

## phases/01-math-foundations/02-vectors-matrices-operations
- [miss] 「像素」「模型」首見未附英文 → zh-TW.md:27「模型處理的每張影像都是一個像素值矩陣」（本課首見）；GLOSSARY 像素、模型為專門術語 → 首見附 pixel、model。（嚴重度：低）
- [miss] 「純量」「學習率」「初始化」「殘差連接」首見未附英文 → zh-TW.md:73 表格「純量乘法 | … | 學習率 × 梯度」、:78「初始化、殘差連接」（表格首見）；GLOSSARY scalar／learning rate／initialization／residual connection 皆為專門術語 → 首見附英文。（嚴重度：低）
- [miss] 「陣列」「偏置向量」首見未附英文 → zh-TW.md:102「當你把偏置向量加進一個輸出矩陣時……較小的陣列」；「陣列」屬通用程式詞可接受，但「偏置向量」（bias vector，GLOSSARY bias→偏置）未附英文 → 「偏置向量（bias vector）」。（嚴重度：低）

## phases/01-math-foundations/03-matrix-transformations
- [miss] 「特徵值」「特徵向量」首見未附英文 → zh-TW.md:14「用特徵方程式（characteristic equation）計算 2x2 矩陣的特徵值與特徵向量」（學習目標首見）；GLOSSARY 特徵值／特徵向量 → 附 eigenvalue／eigenvector。（嚴重度：低）
- [miss] 「神經網路」「權重」首見未附英文 → zh-TW.md:21「神經網路對資料做的每個變換……」（神經網路首見）；「權重」首見於 :436「神經網路權重分析」 → 附 neural network／weight。（嚴重度：低）
- [miss] 「變異數」「降維」首見未附英文 → zh-TW.md:213「PCA。……特徵值告訴你每個成分捕捉到多少變異數……就完成降維」（首見）；GLOSSARY variance、dimensionality reduction → 附英文。（嚴重度：低）

## phases/01-math-foundations/04-calculus-for-ml
- [miss] 「特徵值」首見未附英文 → zh-TW.md:209 表格「正定（所有特徵值 > 0）」（首見；EN「eigenvalues」） → 附 eigenvalues。（嚴重度：低）
- [miss] 「預設最佳化器」「變異數」首見未附英文 → zh-TW.md:257「Adam 是深度學習的預設最佳化器。它透過追蹤……移動平均數與變異數」（首見）；GLOSSARY default→預設、variance→變異數 → 附 variance（default 屬一般用語，可併附）。（嚴重度：低）

## phases/01-math-foundations/05-chain-rule-and-autodiff
- [miss] 「Value 類別」「自動微分引擎」 → 「Value 類別」（class）屬通用程式詞可接受；「自動微分」首見於標題 zh-TW.md:1「連鎖律與自動微分」及 :12「反向模式自動微分（reverse-mode autodiff）」，未附 automatic differentiation（GLOSSARY 自動微分） → 首見附「自動微分（automatic differentiation）」。（嚴重度：低）
- [miss] 「前向傳遞」「反向傳遞」首見未附英文 → zh-TW.md:13「用拓撲排序（topological sort）在計算圖中實作前向傳遞與反向傳遞」（學習目標首見）；GLOSSARY 專門術語 → 附 forward／backward pass。（嚴重度：低）
- [miss] 「訓練迴圈」「深度學習」首見未附英文 → zh-TW.md:384「一個用純 Python 加自動微分寫成的完整神經網路（neural network）訓練迴圈。所有商業深度學習框架……」（首見）；GLOSSARY training loop、deep learning → 附英文。（嚴重度：低）

## phases/01-math-foundations/06-probability-and-distributions
- [miss] 「數值穩定技巧」「常態分布」「變異數」首見未附英文 → zh-TW.md:12「從零實作伯努利、類別、卜瓦松、均勻與常態分布的……」、:13「計算期望值與變異數」、:14「用數值穩定技巧（減去最大 logit）」（學習目標首見）；GLOSSARY normal distribution、variance、numerical stability（數值穩定性） → 附英文，並建議「數值穩定技巧」與 GLOSSARY「數值穩定性」對齊。（嚴重度：低）
- [miss] 「分類器」「語言模型」首見未附英文 → zh-TW.md:19「一個分類器輸出 `[0.03, 0.91, 0.06]`；一個語言模型從 50,000 個候選中挑選下一個詞」（首見）；GLOSSARY classifier、language model → 附英文。（嚴重度：低）
- [miss] 「機率分布」「損失函數」首見未附英文 → zh-TW.md:21「模型做的每個預測都是一個機率分布；每個損失函數都在衡量……」（首見）；GLOSSARY probability distribution、loss function → 附英文。（嚴重度：低）
- [miss] 「條件機率」「獨立性」首見未附英文 → zh-TW.md:46「### 條件機率與獨立性」（首見，標題）；GLOSSARY conditional probability → 附英文。（嚴重度：低）
- [miss] 「二元分類」「多類別分類」首見未附英文 → zh-TW.md:99「為二元分類建模」、:107「為多類別分類建模」（首見）；GLOSSARY → 附英文。（嚴重度：低）
- [miss] 「聯合分布」「邊際分布」首見未附英文 → zh-TW.md:157「### 聯合分布與邊際分布」（首見，標題）；GLOSSARY → 附英文。（嚴重度：低）

## phases/01-math-foundations/07-bayes-theorem
- [miss] 「信賴區間」「可信度區間」首見未附英文 → zh-TW.md:180 表格「不確定性 | 信賴區間（關於程序） | 可信度區間（關於參數）」（首見；EN「Confidence intervals」「Credible intervals」）；GLOSSARY 收錄兩詞（頻率學派／貝氏語境） → 附英文。（嚴重度：低）
- [miss] 「垃圾郵件篩選器」「機器學習」首見未附英文 → zh-TW.md:23「每個垃圾郵件篩選器、每個醫學診斷、每個量化不確定性的機器學習模型」（首見）；GLOSSARY spam filter、machine learning → 附英文。（嚴重度：低）
- [miss] 「懲罰」「正則化」首見未附英文 → zh-TW.md:14「說明 MAP 如何對應到 L2 正則化」（學習目標首見）；:162「一個懲罰大參數值的先驗」 → 附 regularization、penalty。（嚴重度：低）

## phases/01-math-foundations/08-optimization
- [miss] 「一階動差」「二階動差」 → zh-TW.md:127「1. 一階動差（m）」、:128「2. 二階動差（v）：梯度平方的移動平均數」（EN:128「Second moment (v)」）；GLOSSARY 規定 second moment 譯為「二階矩」，譯文「動差」違反 GLOSSARY，且首見未附英文 → 改「一階矩（first moment）」「二階矩（second moment）」。（嚴重度：中）
- [miss] 「學習率排程」「損失地景」首見未附英文 → zh-TW.md:14「分辨凸與非凸損失地景」、:15「設定學習率排程（步進衰減、餘弦退火、預熱）」（學習目標首見）；GLOSSARY learning rate schedule、loss landscape → 附英文。（嚴重度：低）

## phases/01-math-foundations/09-information-theory
- [miss] 「條件熵」「聯合熵」首見未附英文 → zh-TW.md:110「### 條件熵」、:130「### 聯合熵」（標題首見）；GLOSSARY → 附 conditional entropy、joint entropy。（嚴重度：低）
- [ok] 「把正確的標籤，透過……傳送出去」 → zh-TW.md:21「模型試著把正確的標籤，透過一個由學到的權重構成的雜訊通道傳送出去」；逗點略拗但語意完整、與 EN 一致，屬風格。

## phases/01-math-foundations/10-dimensionality-reduction
- [miss] 「使相同的機率分布成立」 → zh-TW.md:97「然後找出一個 2D 排列，使相同的機率分布成立」（EN「find a 2D arrangement where the same probability distribution holds」）；「使……成立」為翻譯腔，「排列」易被讀成順序而非配置。建議「找出一個 2D 配置，使其點對機率分布與原空間一致」。（嚴重度：低）

## phases/01-math-foundations/13-numerical-stability
- [miss] 「捨入誤差」（現況譯為「捨入雜訊」） → zh-TW.md:21「32 位元浮點運算中累積的捨入雜訊，悄悄拉低了準確率，悄悄吃掉了你的準確率」（EN:21「Thirty-two bits of accumulated rounding error quietly ate your accuracy.」）；(a) 原文是 rounding error，GLOSSARY 指定「捨入誤差」，「捨入雜訊」對應的是 rounding noise（zh:50、:85 另有用）；(b)「悄悄」重複，「拉低了準確率」為重複的增譯。建議「32 位元浮點運算累積的捨入誤差，悄悄吃掉了你的準確率」。（嚴重度：中）
- [ok] 「Welford 演算法」 → zh-TW.md:103「可用 Welford 演算法」；人名已為英文，與 GLOSSARY 譯法「Welford 演算法」一致。

## phases/01-math-foundations/15-statistics-for-ml
- [miss] 「常態分布」首見未附英文 → zh-TW.md:103「皮爾森相關係數假設……兩個變數大致符合常態分布」（首見；GLOSSARY normal distribution） → 附英文。（嚴重度：低）

## phases/01-math-foundations/16-sampling-methods
- [miss] 「你需要一種方法，將簡單分布的樣本變換成目標分布的樣本」 → zh-TW.md:41「……其他情況下，你需要一種方法，將簡單分布的樣本變換成目標分布（target distribution）（target distribution）的樣本」。句意與 EN 一致、語句可接受（維持原樣的理由成立），但修復後出現同一英文註解連續重複兩次的排版錯誤。建議刪除重複的「（target distribution）」。（嚴重度：低）

## phases/01-math-foundations/17-linear-systems
- [borderline] 「浮點運算」首見未附英文 → zh-TW.md:114「約需十億次浮點運算」（首見；EN「floating-point operations」）；GLOSSARY「浮點運算」為數值計算通用詞，接近 CS 通用詞，可不加註；但同課 :135 已附「浮點運算（floating-point arithmetic）」。建議首見補「（floating-point operations）」以與全課一致。

## phases/01-math-foundations/19-complex-numbers
- [miss] 「正交基底」首見未附英文 → zh-TW.md:385「單位根構成頻域（frequency domain）的一組正交基底」；「頻域」已附英文，「正交基底」未附（EN「orthogonal basis」），屬線性代數專門術語（GLOSSARY basis→基底） → 「正交基底（orthogonal basis）」。（嚴重度：低）

## phases/01-math-foundations/20-fourier-transform
- [miss] 「座標系統」首見未附英文 → zh-TW.md:69「DFT 是基底變換（change of basis）——它只是用另一種座標系統重新表示相同的資訊」（首見；EN「coordinate system」）；GLOSSARY coordinate system→座標系統 → 首見附 coordinate system。（嚴重度：低）

## phases/01-math-foundations/21-graph-theory
- [ok] 「正規化相鄰矩陣」 → zh-TW.md:14「實作為正規化相鄰矩陣（normalized adjacency matrix）乘法」，首見已附英文；現況已修。
- [ok] 「透過 FFT 乘法進行卷積」 → 誤置：此句實際在 01-20 zh-TW.md:14「套用卷積定理（convolution theorem），透過 FFT 乘法進行卷積（convolution）」，01-21 無此句。語意與 EN「perform convolution via FFT multiplication」一致；「進行卷積」為可接受的一般用語。

## phases/01-math-foundations/22-stochastic-processes
- [ok] 「變異數」「標準常態分布」 → zh-TW.md:56「每一步的變異數（variance）為 1……標準常態分布（standard normal distribution）」，首見已附英文；現況已修。

## phases/02-ml-fundamentals/01-what-is-machine-learning
- [ok] 「偏差過高」「變異很高」 → zh-TW.md:235「**偏差（bias）**：……偏差過高會造成欠擬合」、:237「**變異（variance）**：……若模型的變異很高」；首見（Mermaid :187「偏差過高（bias）」）已附英文；現況已修。

## phases/02-ml-fundamentals/03-logistic-regression
- [ok] 「預測腫瘤」 → zh-TW.md:19「你想根據腫瘤大小預測腫瘤是惡性還是良性」；EN 為動詞「predict」，非 prediction 術語，屬一般用語。
- [miss] 「非線性」首見未附英文 → zh-TW.md:100「sigmoid 引入了非線性，但梯度更新規則仍相同」（首見；EN「nonlinearity」）；GLOSSARY nonlinearity→非線性 → 附英文。（嚴重度：低）

## phases/02-ml-fundamentals/04-decision-trees
- [miss] 「分段常數預測」首見未附英文 → zh-TW.md:447「將樹的分段常數預測畫在真實曲線上比較」（本課唯一出現，位於練習）；GLOSSARY piecewise-constant→分段常數 → 附 piecewise-constant。（嚴重度：低）

## phases/02-ml-fundamentals/08-feature-engineering
- [miss] 「分布」首見未附英文 → zh-TW.md:50「壓縮右偏（right-skewed）分布（收入、人口數、詞數這類資料）」（首見；EN「right-skewed distributions」）；統計專門詞，同課其他分布類術語皆附英文 → 首見附 distribution。（嚴重度：低）
- [ok] 「特徵交互作用會讓特徵空間倍增」 → zh-TW.md:90「特徵交互作用（feature interaction）會讓特徵空間（feature space）倍增」；EN「Feature interactions multiply the feature space」，「倍增」為同一比喻性用法，未增添數字。

## phases/02-ml-fundamentals/09-model-evaluation
- [miss] 「真陽性率」「偽陽性率」首見未附英文 → zh-TW.md:107「ROC 曲線描繪不同分類閾值（threshold）下，真陽性率對偽陽性率的變化」（首見；:98–99 僅用「真陽性（TP）」「偽陽性（FP）」縮寫）；GLOSSARY true positive rate、false positive rate → 首見附英文。（嚴重度：低）
- [ok] 「分層」 → zh-TW.md:12「從頭實作 K 折（K-fold）與分層 K 折（stratified K-fold）交叉驗證」，首見已附英文；現況已修。
- [borderline] 「測試集是你的保留集保證」 → zh-TW.md:49「測試集是你的保留集（hold-out）保證：它確保你回報的表現，反映的是模型面對真正沒見過的資料時的樣子」（EN「The test set is your hold-out guarantee that the reported performance reflects…」）；語意完整、無增譯，「……是你的……保證」為翻譯腔但可讀。可選：「保留測試集，才能確保回報的表現反映模型面對未見資料時的樣子」。

## phases/02-ml-fundamentals/11-ensemble-methods
- [ok] 「邏輯斯迴歸」 → zh-TW.md:160（Mermaid 節點）「模型（model） 3：邏輯斯迴歸（logistic regression）」首見已附英文；:331 再次出現不需重複。

## phases/02-ml-fundamentals/12-hyperparameter-tuning
- [miss] 「訓練」首見未附英文 → zh-TW.md:3「超參數（hyperparameter）是訓練開始前你要轉動的旋鈕」（blockquote 首見）；GLOSSARY training→訓練 → 附 training。（嚴重度：低）
- [miss] 「收斂」首見未附英文 → zh-TW.md:130 表格「一循環（one-cycle） | 一個循環內先升後降 | 快速收斂」（首見）；GLOSSARY convergence→收斂 → 附 convergence。（嚴重度：低）

## phases/02-ml-fundamentals/15-time-series
- [miss] 「數值最佳化」首見未附英文 → zh-TW.md:200「它需要的數值最佳化超出本課範圍」（首見；EN「numerical optimization」）；「最佳化」為 GLOSSARY 術語 → 附英文。（嚴重度：低）

## phases/02-ml-fundamentals/16-anomaly-detection
- [ok] 「網路入侵」 → zh-TW.md:21「網路入侵造成資料損失」；「網路」為通用 CS 詞（判準 5），「入侵」為一般用語。
- [ok] 「伺服器回應時間」 → zh-TW.md:98「伺服器（server）回應時間」，首見已附英文；現況已修。
- [ok] 「基準模型」 → 本課 zh-TW.md 已無此詞（誤置或已改寫）；現為 :220「收集基準資料」（baseline data，非 GLOSSARY 的 baseline 模型用法）。同批 02-15 zh-TW.md:392「簡單的基準模型（baseline）」已附英文。

## phases/02-ml-fundamentals/17-imbalanced-data
- [miss] 「分類」首見未附英文 → zh-TW.md:23「真正要緊的分類裡，這到處都發生」（裸用「分類」的首見；:13「分類器（classifier）」已附英文，但不是 classification 本身）；GLOSSARY classification→分類 → 附 classification。（嚴重度：低）
- [ok] 「在線段上造一個新樣本」 → zh-TW.md:84「在 x 和那個鄰居之間的線段上造一個新樣本」；EN「Create a new sample on the line segment」，「造」略口語但語意精確、無誤。可選：改「生成」較正式。

## phases/02-ml-fundamentals/18-feature-selection
- [ok] 「不平衡分類器」 → 本課 zh-TW.md 無此詞（誤置）；實際在 02-17 zh-TW.md:13「評估不平衡分類器（classifier）」，首見已附英文。
- [miss] 「把權重推進到 0」 → zh-TW.md:57「L1 正則化把權重（weight）推進到 0」（EN「L1 regularization drives weights to zero」）；「推進到」為 drive to 的直譯，翻譯腔。建議「把權重壓到 0」或「使權重歸零」。（嚴重度：低）

## phases/10-llms-from-scratch/01-tokenizers
- [ok] 模型比較表「整表未翻譯」 → zh-TW.md:190–197 表頭已譯為「模型｜詞彙表大小｜Tokenizer 類型｜平均每個英文單字的 Token 數」，列值保留模型名與數值；現況已修。
- [miss] 「注意力容量」首見未附英文 → zh-TW.md:35「把注意力容量浪費在人類三歲就能掌握的事情上」（首見；EN「burning attention capacity」）；GLOSSARY attention→注意力 → 附 attention。（嚴重度：低）
- [ok] 「壓縮演算法」 → zh-TW.md:55「BPE 是一種貪婪壓縮演算法」；通用 CS 詞，判準 5 可不加註。（附帶：同句有「後來後來改用於」疊字，見附帶發現 A。）
- [miss] 「壓縮比」違反 GLOSSARY（另「分布」可接受） → zh-TW.md:320「壓縮比告訴你 tokenizer 的效能如何」；GLOSSARY compression ratio 指定「壓縮率」，「壓縮比」為未核定譯法（同課 :471 亦用「壓縮比」） → 全課統一為「壓縮率（compression ratio）」。「分布外（out-of-distribution）」「齊夫分布（Zipf distribution）」已附英文，可接受。（嚴重度：中）
- [miss] 「產詞率（Fertility）」 → zh-TW.md:467 表格「| 產詞率（Fertility） |」（本課唯一出現）；「產詞」字面為「產生詞」，與本指標（每個字詞的平均 token 數）語意不符，且 GLOSSARY 無此詞（GLOSSARY 規定新術語先補表）。建議保留「fertility」，定義為「每個字詞的平均 token 數」，並補入 GLOSSARY。（嚴重度：中）

## phases/10-llms-from-scratch/02-building-a-tokenizer
- [ok] 「剛好就是 256 個項目」 → zh-TW.md:65「你的基礎詞彙表剛好就是 256 個位元組值」，已改用「位元組值」；現況已修。
- [miss] 字元映射 `G` 被改為 `Ġ`（受保護內容未註記） → zh-TW.md:67「位元組（byte） 0x20（空格）在他們的映射中變成字元「Ġ」」；EN:67「Byte 0x20 (space) becomes the character "G" in their mapping.」。譯者改動了源文字元且未註記。STYLE 規定保護內容「先保留原文並交審閱者判斷；不得自行修正原文」。建議恢復「G」，並於審閱備註提示源文疑似遺失 Ġ，由審閱者決定是否回頭修正 en.md。（嚴重度：中）

## phases/10-llms-from-scratch/03-data-pipelines
- [miss] 「模型」「管線」首見未附英文 → zh-TW.md:1 標題「預訓練資料管線」（管線首見）、:3「> 模型是一面鏡子。」（模型首見）；GLOSSARY model、pipeline（機器學習資料處理流程）→ 首見附 model、pipeline。（嚴重度：低）

## phases/10-llms-from-scratch/04-pre-training-mini-gpt
- [miss] 「模型」「推論」首見未附英文 → zh-TW.md:3「……你在其上打造產品的模型內部究竟發生了什麼」（模型首見）；zh-TW.md:146「### KV Cache：為什麼推論能如此迅速」（推論首見，標題） → 附 model、inference。（嚴重度：低）

## phases/10-llms-from-scratch/05-scaling-distributed
- [ok] 英文殘留句（27、217、546） → zh-TW.md:27「……該次訓練的運算成本估計約 1 億美元；而 DeepSeek V3 ……約 560 萬美元」、:217「……成本約為 560 萬美元，對比 Meta 估計的 1 億美元」、:546「Llama 3 405B 據報約 1 億美元……」，三處皆已譯為中文，無英文整句殘留；現況已修。
- [miss] 「梯度同步」「模型狀態」首見未附英文 → zh-TW.md:13「在多張 GPU 之間進行梯度同步」、:15「……對模型狀態進行分片」（學習目標首見）→ 附 gradient synchronization、model states。（嚴重度：低）

## phases/10-llms-from-scratch/06-instruction-tuning-sft
- [miss] 「Total cost: $600. The result was a chatbot...」整段英文殘留 → zh-TW.md:25「……就對 Llama 7B 進行了 fine-tuning。Total cost: $600. The result was a chatbot that could follow instructions, answer questions, and hold conversations. Not as good as ChatGPT, but shockingly close for $600 and a few hours of training（總成本僅 600 美元，訓練數小時即產出能遵循指令的助理）」；英文整句保留，後接中文括號重述，內容重複。建議刪除英文句，只保留完整中文：「總成本僅 600 美元，訓練數小時即產出能遵循指令、回答問題並進行對話的聊天機器人，雖不及 ChatGPT，但已相當接近。」（嚴重度：高）
- [borderline] 「整整小了 15 倍／低了 15 倍」 → zh-TW.md:132「SFT 的學習率低了 15 倍」（EN「15x lower」）；:391「相較於預訓練中使用的 3e-4，整整小了 15 倍」（EN「15x smaller」）。「整整」為原文沒有的強調；「小了 15 倍」在中文可被讀成減去 15 倍。建議 :391 刪「整整」，或寫「約為預訓練學習率的 1/15」。
- [borderline] 「擊敗了……範例」 → zh-TW.md:27「由專業標註人員撰寫的 27,000 個範例，擊敗了從網路爬取、充斥雜訊的 100 萬個範例」（EN「beat 1 million noisy examples」）。「擊敗」用於模型效能比較在臺灣科技媒體常見，語意可懂，但擬人化且偏戲劇；「勝過」更貼近 beat 的效能語意。可選：「效果勝過」。

## phases/10-llms-from-scratch/07-rlhf
- [miss] Response A／Response B 範例全文英文、無繁中對照 → zh-TW.md:21「**回應 A：**「Quantum computing uses qubits that can exist in superposition, …」」、:23「**回應 B：**「Quantum computing is a type of computing …」」。兩段範例為整段英文，且無對應的繁中段落（STYLE：每個英文段落對應一個繁中段落）。建議逐段譯為繁中，或保留英文原例並另起繁中段。（嚴重度：高）
- [miss] 「單純在模式比對上湊合『高品質』的假象」 → zh-TW.md:108「產生冗長、語氣正式但言之無物的廢話，單純在模式比對上湊合「高品質」的假象」（EN:108「Producing verbose, formal-sounding but empty responses that pattern-match to "high quality"」）。「湊合」與「假象」增添了原文沒有的欺騙意涵，「廢話」比 empty 更重，語意偏離。建議「產生冗長、語氣正式卻空洞的回應，只是在表面模式上貼近獎勵模型認定的『高品質』」。（嚴重度：中）

## phases/10-llms-from-scratch/08-dpo
- [miss] 「偏好配對」「策略模型」首見未附英文 → zh-TW.md:3「DPO 直接在偏好配對上最佳化語言模型」、「（SFT、獎勵模型、策略模型）」（首見）；「偏好配對」未收入 GLOSSARY，「策略」為 GLOSSARY policy → 首見附 preference pair、policy，並補 GLOSSARY。（嚴重度：低）

## phases/10-llms-from-scratch/09-constitutional-ai-self-improvement
- [borderline] 「憲法式 AI」「群組相對策略最佳化」 → 「憲法式 AI」首見於正文 zh-TW.md:3「憲法式 AI（Constitutional AI）」，已附英文（標題 :1 無英文，屬標題慣例）；「群組相對策略最佳化」首見於 :13「推導 GRPO 目標函數（DeepSeek-R1 的群組相對策略最佳化）」，只附縮寫、未附 group-relative policy optimization 全稱。建議「群組相對策略最佳化（group-relative policy optimization，GRPO）」。

## phases/10-llms-from-scratch/10-evaluation
- [miss] 「真實性（faithfulness）」 → zh-TW.md:113「測量真實性（faithfulness，答案是否忠於檢索到的脈絡？）」；RAGAS 的 faithfulness 量測答案是否忠於檢索內容，與一般意義的 truthfulness（真實性）不同，術語標籤錯誤（括號內雖有說明）。建議「忠實度（faithfulness）」。（嚴重度：中）
- [borderline] 「200 多萬張人類偏好選票」 → zh-TW.md:37「超過 200 萬張人類偏好選票」、:512「超過 200 萬張人類偏好選票」（EN「2M+ human preference votes」）。「張」為紙本量詞，「選票」在網路配對投票語境稍失準，但仍可讀。可選：「200 多萬筆人類偏好投票」。

## phases/10-llms-from-scratch/11-quantization
- [borderline] 「記憶體減少 2／4／8 倍」 → zh-TW.md:214「從 FP16 轉為 INT8（LLM.int8()）：記憶體減少 2 倍」、:216「記憶體減少 4 倍」、:220「記憶體減少 8 倍」（EN「2x」「4x」「8x」 memory reduction）。「減少 N 倍」在中文可被讀成減去 N 倍；同課 :208 已用「記憶體減為四分之一」，寫法不一致。可選：統一為「用量降為原來的 1/2、1/4、1/8」。

## phases/10-llms-from-scratch/12-inference-optimization
- [miss] 「a $25k/month inference bill from a $5k/month」英文片語留在正文 → zh-TW.md:23「……正是將 a $25k/month inference bill from a $5k/month（每月 2.5 萬美元帳單降低至 5,000 美元服務相同流量）區隔開來的關鍵所在」；英文片語與中文重述並存。建議刪英文，只保留「每月 2.5 萬美元的推論帳單」與「5,000 美元的帳單」。（嚴重度：低）
- [miss] Further Reading 五筆說明整段英文 → zh-TW.md:779–783（「## Further Reading｜延伸閱讀」之後）：「Kwon et al., …——the vLLM paper that introduced paged KV cache management…」等五筆說明皆為英文，無繁中說明。建議逐筆譯成繁中說明，保留作者、篇名與連結。（嚴重度：高）
- [ok] 「草稿與目標模型在位置 j 出現歧異」 → zh-TW.md:161「若在位置 j 出現歧異，則接受前 j-1 個 token 並捨棄其餘部分」；EN「disagrees at position j」，語意一致；「歧異」略文雅但精確。

## phases/10-llms-from-scratch/15-speculative-decoding-eagle3
- [miss] 「加速比」「接受率」「殘差分布」首見未附英文 → zh-TW.md:14「根據接受率 `α` 與草稿對驗證成本比 `c` 計算預期加速比」、:15「從殘差分布拒絕抽樣」（學習目標首見）；GLOSSARY speedup→加速比、acceptance rate→接受率 → 附 speedup、acceptance rate、residual distribution。（嚴重度：低）

## phases/10-llms-from-scratch/16-differential-attention-v2
- [ok] 「雜訊底限會隨著脈絡長度線性增長」 → 現況 zh-TW.md:12「為何該底限會隨著脈絡長度增長」、:19「會隨脈絡長度增加而累積」，已無「線性」增譯；現況已修。數字（0.001%、127,999、12%）與 EN:19 一致。

## phases/10-llms-from-scratch/17-native-sparse-attention
- [miss] 「稀疏注意力顯然是唯一的答案」 → zh-TW.md:21「稀疏注意力（Sparse attention）顯然是唯一的答案」；EN:21「Sparse attention is the obvious answer.」「唯一」為原文沒有的排他性增譯。建議「稀疏注意力顯然是最直接的答案」。（嚴重度：中）

## phases/10-llms-from-scratch/18-multi-token-prediction
- [miss] 「生成吞吐量」首見未附英文 → zh-TW.md:3「這幾乎免費帶來了 1.8 倍的生成吞吐量」（首見；EN「1.8× throughput」）；「保留版面簡潔」不是 STYLE 允許的理由 → 首見附 throughput。（嚴重度：低）

## phases/10-llms-from-scratch/19-dualpipe-parallelism
- [miss] 「前向傳遞／反向傳遞」首見未附英文 → zh-TW.md:33「每個裝置只有在前一個裝置送達輸出時才能啟動前向傳遞，且只有在下游裝置送達上游梯度時才能啟動反向傳播」（首見）；GLOSSARY forward／backward pass → 附英文。同條「瓶頸」（GLOSSARY bottleneck）首見於 :84 亦未附英文。「記憶體」「裝置」為通用 CS 詞，可接受。（嚴重度：低）

## phases/10-llms-from-scratch/20-deepseek-v3-walkthrough
- [miss] 「低秩」「無輔助損失負載平衡」「隱藏狀態」首見未附英文 → zh-TW.md:15「無輔助損失路由」（首見）、:31「K 與 V 被壓縮至共享的低秩潛在表示中」（首見）、:52 標題「無輔助損失負載平衡」、:62「每個隱藏狀態同時受到……監督」 → 附 auxiliary-loss-free load balancing、low-rank、hidden state。（嚴重度：低）

## phases/10-llms-from-scratch/21-jamba-hybrid-ssm-transformer
- [miss] Mamba-3 術語首見未附英文 → zh-TW.md:3「Mamba-3（ICLR 2026）則在純 SSM 端引入複數值狀態空間與 MIMO 投影」（首見）、:15「（指數梯形離散化、複數值狀態更新、MIMO）」 → 首見附 complex-valued state space、exponential-trapezoidal discretization、complex-valued state update、multi-input multi-output（MIMO）。附帶：:3 另有「能混合配方歷經」疊字錯誤，見附帶發現 C。（嚴重度：低）

## phases/10-llms-from-scratch/22-async-hogwild-inference
- [miss] 「尚未被商業正式環境廣泛採用」 → zh-TW.md:97「截至 2026 年 4 月，Hogwild! 仍是一項……前沿研究方法，尚未被商業正式環境廣泛採用」；EN:97「Production adoption has not happened.」原文為「尚未發生生產採用」，譯文「廣泛採用」隱含已有少量採用，語意弱化。建議「尚未進入商業正式生產環境」。（嚴重度：中）
- [miss] 「推測解碼、投票集成、思維樹」首見未附英文 → zh-TW.md:3「推測解碼（第 10 階段第 15 課）」（首見）、:25「投票集成（執行 N 個模型，採多數決答案）、思維樹（展開多條分岔推理路徑……）」 → 附 speculative decoding、voting ensemble、tree of thought。「行程」（:35「N 個 worker 行程」）為通用 CS 詞，可接受。（嚴重度：低）
- [miss] 「c 相對於單步 decode 時間必須極其微小」 → zh-TW.md:70「若要讓多 worker 真正具備產能，`c` 相對於單步 decode 時間必須極其微小」；EN:70「`c` must be small relative to the per-step decode time.」「極其」為原文沒有的程度加強。建議「`c` 必須夠小，相對於單步 decode 時間」。（嚴重度：中）

## phases/10-llms-from-scratch/25-speculative-decoding
- [miss] 「推測解碼、拒絕抽樣、殘差分布、知識蒸餾」首見未附英文；「拒絕抽樣」違反 GLOSSARY → zh-TW.md:3「推測解碼（Leviathan 等人，2023 年）」（首見，括號內僅為作者年份）、:29「修正後的拒絕抽樣法則」、:30「修正後的殘差分布」；GLOSSARY 指定 rejection sampling→「拒絕取樣」。建議首見附英文，並改「拒絕取樣（rejection sampling）」。（嚴重度：低）
- [miss] 「結構化輸出（JSON、SQL）」增加原文沒有的示例 → zh-TW.md:107「文字可預測性高的對話／程式碼生成／結構化輸出（JSON、SQL）」；EN:107「structured output」，未列 JSON、SQL。屬增譯。建議刪「（JSON、SQL）」。（嚴重度：低）

## phases/10-llms-from-scratch/34-gradient-checkpointing
- [borderline] 標題「梯度檢查點與活化值重算」首見未附英文 → zh-TW.md:1「# 梯度檢查點與活化值重算」（標題無英文）；正文 :16「梯度檢查點（Gradient checkpointing，亦稱活化值重算，activation recomputation）」首見已附英文。標題慣例上可不附；可選：標題附 Gradient Checkpointing。

---

## Summary

### 計數
- 總條數：**97**（54 課）
- **ok：23**
- **borderline：9**（#1 00-07 他；#35 01-17 浮點運算；#49 02-09 保留集保證；#73、#74 10-06 整整／擊敗；#78 10-09 GRPO 全稱；#80 10-10 選票；#81 10-11 倍數寫法；#97 10-34 標題）
- **miss：65**，其中嚴重度 **高 3**、**中 10**、**低 52**。
  - 高：10-06 英文整段殘留；10-07 Response A／B 英文範例；10-12 Further Reading 英文說明。
  - 中：10-02 `G`→`Ġ` 受保護內容改動；10-01「壓縮比」（GLOSSARY 違規）；10-01「產詞率」（自創譯名，語意不符）；01-08「二階動差」（GLOSSARY 違規）；01-13「捨入雜訊」（GLOSSARY 違規＋重複＋增譯）；10-07「湊合……假象」（語意偏離）；10-10「真實性（faithfulness）」（術語誤譯）；10-17「唯一」（增譯）；10-22「尚未……廣泛採用」（語意弱化）；10-22「極其微小」（增譯）。
  - 低：其餘 52 條，多為 GLOSSARY 專門術語首見未附英文，屬 STYLE 規範，非資訊錯誤。
- 誤置條目（原報告歸屬錯誤，已在對應課判定）：#3（00-11 訓練日誌，實為 00-10）、#39（01-21 FFT，實為 01-20）、#56（02-16 基準模型，本課已無此詞）、#59（02-18 不平衡分類器，實為 02-17）。

### Miss 的優先修正清單（依嚴重度）
1. **10-06 英文整段殘留**（高）：刪除 :25 的英文整句，改為完整中文（見上）。
2. **10-07 Response A／B 英文範例**（高）：:21、:23 逐段譯為繁中，與 STYLE「每個英文段落對應一個繁中段落」一致。
3. **10-12 Further Reading 說明英文**（高）：:779–783 五筆說明逐筆譯為繁中，保留作者、篇名與連結。
4. **10-02 字元 `G`→`Ġ`**（中）：恢復源文「G」，在審閱備註提示來源疑似字元遺失，不自行改寫保護內容。
5. **10-17「唯一的答案」增譯**（中）：刪「唯一」，改「最直接的答案」。
6. **10-22「尚未被商業正式環境廣泛採用」語意弱化**（中）：改「尚未進入商業正式生產環境」。
7. **10-22「極其微小」增譯**（中）：改「必須夠小」。
8. **10-01「壓縮比」違反 GLOSSARY**（中）：全課（:320、:471 等）統一為「壓縮率（compression ratio）」。
9. **01-08「二階動差」違反 GLOSSARY**（中）：改「一階矩」「二階矩」，並附英文（:127–128）。
10. **01-13「捨入雜訊」（應為捨入誤差）**（中）：:21 改「捨入誤差（rounding error）」，同時刪重複的「悄悄」與增譯「拉低了準確率」。
11. **10-10「真實性（faithfulness）」誤譯**（中）：改「忠實度（faithfulness）」（:113）。
12. **10-07「湊合……假象」語意偏離**（中）：改寫 :108，與 EN 的 pattern-match 意思對齊。
13. **10-01「產詞率（Fertility）」自創譯名**（中）：保留 fertility 並定義為「每個字詞的平均 token 數」，補入 GLOSSARY。
14. **10-25「拒絕抽樣」違反 GLOSSARY**（低）：改「拒絕取樣（rejection sampling）」，並刪 :107 增加的「（JSON、SQL）」。
15. 其餘 low 項：依課程批次，把 GLOSSARY 專門術語在**首見處**補英文原詞（不改譯名）。

### 附帶發現（不在 97 條 kept 範圍內，屬修復後新引入或既有漏網）
- **A. 10-01 :55**「後來後來改用於 tokenization」疊字（修復「挪用」時引入）。
- **B. 10-10 :37**「缺點在於成本（每次評判 $0.10-$2.00 每次評判）」重複（修復「per judgment」時引入）。
- **C. 10-21 :3**「本課將深入剖析這兩種架構，解釋為何這套混合配方能混合配方歷經三年擴展仍持續發展」語句錯亂（修復 :3 時引入）。
- **D. 10-34 :16**「但活化值會徹底將你推入活化值會使記憶體需求超出上限」語句錯亂（修復「OOM 深淵」時引入）；EN:16 原意是活化值會把記憶體推過上限。
- **E. 00-11 :15**「辨識 macOS 與 Linux 之間辨識在遠端機器開發時常見的 macOS 與 Linux 差異」疊字（修復「踩坑」時引入）。
- **F. 10-07 全篇**「Reward Model」共 40 處保留英文、「獎勵模型」0 處；:12（學習目標）與 :73（標題）皆為「Reward Model（Reward Model）」重複標註。GLOSSARY 只收 reward→獎勵，譯法不一致；與 10-08 的「獎勵模型」用法也不一致。
- **G. 01-16 :41**「（target distribution）（target distribution）」重複（已列於 kept #34）。

### 方法與限制
- 每條均以 `grep -n` 定位現況 zh-TW.md 首見位置，並以 `en.md` 對照；首見判定依該課第一次出現的中文譯名行。
- 「首見」以檔案行序判定，不含 frontmatter 外的程式碼區塊。程式碼區塊與參考文獻的英文標題視為受保護或專有名稱，未計為殘留。
- 未修改任何譯稿或 repo 檔案；僅新增本報告與 `/private/tmp/zh-tw-review/` 下的輔助清單與掃描腳本。
