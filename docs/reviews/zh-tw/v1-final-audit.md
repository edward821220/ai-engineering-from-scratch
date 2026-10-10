# zh-TW 終態複審（v1-final-audit）：phases 00 / 01 / 02（共 52 課）

- 譯稿：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`；原文：同路徑 `en.md`。
- 依據：`docs/reviews/zh-tw/r1.md`（範圍內 r1 條目）、`v1-kept-audit.md`（維持原樣的複審判定）、`f1-changelog.md`、`f4-changelog.md`、`GLOSSARY.md`、`STYLE.md`。
- 行號：一律為現況 zh-TW.md 行號，以關鍵字定位；`en` 對照以 en.md 同課同行為準（有換行差異的課已另行對齊）。
- 唯讀：未編輯任何譯稿或 repo 檔案。輔助腳本與掃描輸出位於 `/private/tmp/zh-tw-review/v1-final-scratch/`。

## 判定類別

- `[verified]`：註記已修復，現況正確且未改錯；或維持原樣但已由 kept-audit 判 miss 並經 f1 修好。
- `[not-fixed]`：註記已修復（或 kept 項經複審判 miss），但現況仍有問題，含假修復、修錯、疊註、疊字、錯亂句、占位符殘留。
- `[kept-ok]`：維持原樣，複審同意。
- `[kept-wrong]`：維持原樣，但複審認為仍應修。
- `[new-issue]`：r1 未提，現況有明確錯誤或結構偏差。
- `[note]`：r1 無 finding 的課的覆核備註，不計入判定數。

`P0/P1/P2` 為 r1 嚴重度；`(kept)` 為 r1 維持原樣項；`(f1)` 為 f1 日誌所列修復位置。

判定方法摘要：
1. 逐條 r1 finding：以關鍵字在現況 zh-TW.md 定位，確認首見英文附註與譯文內容。
2. 全量自動掃描（52 課）：疊字、三連疊字、重複括號註記、簡體字、GLOSSARY 禁用譯名、翻譯腔樣式、英文殘留（≥4 詞）、代碼區塊／行內碼／URL／metadata／標題層級／表格與清單計數，與 en.md 逐項比對。
3. f1 與 f4 日誌所列編輯位置逐一回看周邊文字。
4. 掃描候選與 r1 項逐一以 en.md 對照，未對照者不計為問題。

---

## phases/00-setup-and-tooling/01-dev-environment
- [note] r1 無 finding（clean）。覆核：Step 7 段落在譯文中為單行、原文為多行換行，內容完整（z161、z180、z182、z184 對應 en 161–192）；無疊字、重複註記、英文殘留或 GLOSSARY 禁用詞。

## phases/00-setup-and-tooling/02-git-and-collaboration
- [note] r1 無 finding（clean）。覆核：z3「版本控制（version control）」首見已附英文；自動掃描無新問題。未逐句通讀。

## phases/00-setup-and-tooling/03-gpu-setup-and-cloud
- [note] r1 無 finding（clean）。覆核：z1 標題「雲端」未附英文，依 kept-audit 標題慣例可接受；自動掃描無新問題。未逐句通讀。

## phases/00-setup-and-tooling/04-apis-and-keys
- [verified] P2 z154「我的請求被限速了」（常見說法欄）：已採用語，與 r1 建議一致。

## phases/00-setup-and-tooling/05-jupyter-notebooks
- [verified] P1 z12「Jupyter 擴充功能（extension）」：首見已附英文。
- [verified] P1 z19「分段執行程式碼（code）」。
- [verified] P1 z21「除錯（debugging）惡夢」。
- [verified] P1 z51「選擇介面（interface）」。
- [not-fixed] P1 z57（r1 z55「檔案瀏覽器和終端機」）：表格譯為「完整 IDE 體驗、多個分頁、終端機（terminal）」，漏譯 en「file browser」（檔案瀏覽器）。終端機有附英文，但「檔案瀏覽器」被刪，屬漏譯。
- [not-fixed] P1 z59（r1 z55「整合在編輯器中」）：譯為「已編輯器（editor），支援 Git 整合和除錯」，語句錯亂。en 為「Already in your editor」，應為「已整合在編輯器（editor）中」。
- [verified] P1 z89「自動完成（autocomplete）」。
- [verified] P1 z111「Jupyter 專用指令（command）」。
- [verified] P1 z227「變數仍留在記憶體（memory）中」。

## phases/00-setup-and-tooling/06-python-environments
- [verified] P1 z24「模型（model）函式庫（libraries）」：首見已附英文。
- [not-fixed] P1 z28「自己的套件（package）（package）」（r1 z28 已修復）：同一英文註記連續重複兩次，疊註。

## phases/00-setup-and-tooling/07-docker-for-ai
- [kept-wrong] (kept, 低) P2 z19「結果你的模型在他的電腦上崩潰」：en 為 `their machine`（中性）；譯文以「他」指稱同事，新增男性指涉，原文無此資訊。建議「同事的電腦上」，與 kept-audit 建議相同且零成本。
- [not-fixed] P1 z12–z15（r1「程式碼、模型、多服務、掛載、建置」）：程式碼首見已附英文（z13）；但「模型」（z13「讓模型、資料集…」）、「掛載」（z13「掛載為磁碟區」）、「建置」（z12「建置支援 GPU 的 Docker 映像」）、「服務」（z15「多服務 AI 應用程式」）首見皆無英文。r1 標示已修復與現況不符。GLOSSARY 收 mount→掛載、build→建置，屬需附英文之詞。（低）
- [verified] P1 z382「隔離行程」：r1 的 process 修正已完成。
- [verified] P1 z48「一個指令（command）」。
- [verified] P1 z129「除錯（debugging）時間」。
- [verified] P1 z313「共用網路（network）」。
- [not-fixed] P1 z375「API 伺服器（API server）（API server）」：r1 已修復，但英文註記重複兩次，疊註。
- [not-fixed] P1 z383「映像層（image layer）（image layer）」：表格內英文註記重複兩次，疊註。

## phases/00-setup-and-tooling/08-editor-setup
- [verified] P1 z12「程式碼（code）」；P1 z14「除錯（debugging）」：首見皆附英文。
- [verified] P1 z19「終端機（terminal）工作流程」。
- [verified] P1 z25「AI 工程（AI engineering）」。
- [verified] P1 z14「遠端 GPU 主機（host）」。
- [verified] P1 z137「遠端檔案系統（filesystem）」。
- [verified] P1 z144「伺服器（server）元件（component）」。
- [verified] P1 z180「語言伺服器（language server）」。
- [verified] P1 z185「學習曲線（learning curve）」。
- [verified] P1 z108、z112、z194「訓練程式檔案」：r1 統一修正已完成，無「訓練程式」單獨留存。

## phases/00-setup-and-tooling/09-data-management（f4 收尾，已確認 f4-changelog 有 C3 紀錄；檔案 mtime 穩定）
- [verified] P2 z19「並將資料集納入版本控制」。
- [verified] P2 z61「資料集大到無法完整存放在磁碟上」。
- [verified] P2 z252「具名子集（train／val／test）」。
- [verified] P1 z12「函式庫（library）」；z15「模型（model）」：首見皆附英文。
- [verified] P1 z19「AI 專案（project）」；「訓練」首見於 z14，以「訓練／驗證／測試集切分（training/validation/test split）」附英文。
- [verified] P1 z72「記憶體（memory）用量」。
- [verified] P1 z166「伺服器（server）」。
- [verified] P1 z252「訓練資料（training data）」。
- [verified] (kept→f1) z216「文字分類（text classification）基礎」、z220「影像分類（image classification）基礎」：首見已附英文。f4 C3 的 z216「tokenization、分類（classification）」與 en「Tokenization, classification」相符。
- [verified] P1 z258「預設（default）」。
- [verified] P1 z256「擴充功能（extension）」。

## phases/00-setup-and-tooling/10-terminal-and-shell
- [verified] P2 z19「每個 AI 工作流程都離不開 shell」。
- [verified] P1 z21「不深究 Bash 程式」：r1 的 script→程式 修正已完成。
- [verified] P1 z12「訓練（training）日誌」。
- [verified] P1 z19「編輯器（editor）」。
- [verified] P1 z110「背景行程（process）」。
- [verified] P1 z139「日誌檔（log file）」。
- [verified] P1 z220「記憶體（memory）」。
- [verified] P1 z337「伺服器（server）」。

## phases/00-setup-and-tooling/11-linux-for-ai
- [not-fixed] P2 z15（r1「容易讓遠端工作的開發者踩到的差異」）：r1 建議句未保留。f1 附帶修復改為「辨識遠端機器開發時常讓人踩坑的 macOS 與 Linux 差異」，把 r1 已判為中國網路用語的「踩坑」重新引入；z269 已改「踩雷」，兩處不一致。
- [verified] P2 z19「你就會進入 Ubuntu 環境」。
- [verified] P2 z19「一邊支付 GPU 閒置期間的費用」。
- [verified] P2 z23「檔案系統目錄結構」。
- [kept-ok] (kept) P1「訓練日誌」：本課無此詞（誤置）。實際位於 00/10 z12，已附「訓練（training）」。
- [verified] P1 z19「雲端 GPU（cloud GPU）」、「介面（interface）」。
- [verified] P1 z120「軟體（software）」。
- [verified] P1 z170「推論（inference）伺服器」。
- [verified] P1 z265「驅動程式（driver）」。
- [verified] P1 z263「核心（kernel）」。
- [verified] P1 z279「區分大小寫（case-sensitive）」。
- [verified] P1 z303「專案（project）資料夾」。
- [verified] P1 z304「記憶體（memory）」。
- [verified] P1 z306「快取（cache）」。
- [verified] P1 z269「踩雷」。

## phases/00-setup-and-tooling/12-debugging-and-profiling
- [verified] P0 z3「它們會讓模型悄悄用垃圾資料訓練，卻呈現漂亮的 loss 曲線」：與 en「They train silently on garbage and report a beautiful loss curve」一致。
- [not-fixed] P2 z21（r1「沉默的失敗…」）：現況「你需要能在這些在這些靜默失敗耗掉時間和運算資源前就將它們找出來的除錯工具」，修復時重複「在這些」，疊字。
- [verified] P2 z44「print 除錯常被低估，其實不該如此」。
- [verified] P2 z19「問題可能出在張量放錯裝置」。
- [verified] P2 z367「點選行號旁的空白處」。
- [verified] P1 z19「網頁應用程式（web app）」。
- [verified] P1 z21「除錯工具（debugging tools）」。
- [verified] P1 z44「除錯器（debugger）」。
- [kept-ok] (kept) P1 z106「日誌檔」「終端機輸出」：通用 CS 詞，依 kept-audit 判準 5 不加註。
- [verified] P1 z164「記憶體分析（memory profiling）」。
- [verified] P1 z369「前處理管線（preprocessing pipeline）」。
- [verified] (kept→f1) P1 z379「前向傳遞（forward pass）和反向傳遞（backward pass）」：kept-audit 判 miss，f1 已補英文。

## phases/01-math-foundations/01-linear-algebra-intuition
- [not-fixed] (kept→f1) z435「LoRA（low-rank adaptation，low-rank adaptation）」：f1 保留英文後，同一英文在括號內重複兩次。en 為「LoRA (low-rank adaptation)」。（低）
- [not-fixed] P1 z14（r1 z12「基底」）：現況「與基底（basis）（basis）」，英文註記重複，疊註。
- [verified] P1 z33「原點（origin）」。
- [verified] P1 z39「像素（pixel）」。
- [verified] P1 z88「迴歸（regression）」。
- [verified] P1 z100「新資訊（information）」。
- [verified] P1 z438「白化轉換（whitening transform）」。
- [verified] P1 z445「縮放矩陣（scaling matrix）」。

## phases/01-math-foundations/02-vectors-matrices-operations
- [verified] P1 z12「Matrix 類別（class）」。
- [not-fixed] P1 z15（r1「神經網路框架」）：現況「神經網路框架中偏置相加」首見無英文。r1 標示已修復為「神經網路框架（framework）」，但未出現。（低）
- [verified] P1 z19「讀程式碼（code）時看到這行」。
- [verified] (kept→f1) z27「模型（model）處理的每張影像都是一個像素（pixel）值矩陣」。
- [verified] P1 z35「資料點（data point）」。
- [verified] P1 z57「內側維度（dimension）」。
- [verified] (kept→f1) z73「純量（scalar）乘法」、「學習率（learning rate）」；z78「初始化（initialization）、殘差連接（residual connection）」。
- [verified] (kept→f1) z102「偏置向量（bias vector）」。陣列為通用程式詞，kept-ok。
- [kept-ok] (kept) z102「陣列」：通用程式詞。
- [not-fixed] P1 z82（r1「讓初學者踩坑」→「常讓初學者搞混」）：現況「這個區別常常常讓初學者搞混」，三連「常」，疊字。en「trips up beginners constantly」。

## phases/01-math-foundations/03-matrix-transformations
- [verified] P2 z3「矩陣就像能重塑空間的機器」。
- [verified] P2 z21「推移矩陣會使點的位置傾斜」。
- [verified] P2 z177「多數向量經過矩陣變換後」。
- [verified] (kept→f1) z14「特徵值（eigenvalue）與特徵向量（eigenvector）」。
- [verified] P1 z19「模型（model）穩定性」。
- [verified] (kept→f1) z21「神經網路（neural network）對資料做的每個變換」。
- [verified] (kept→f1) z436「神經網路權重（weight）分析」。
- [verified] P1 z27「線性變換（linear transformation）」。
- [verified] (kept→f1) z213「變異數（variance）」、「降維（dimensionality reduction）」。
- [verified] P1 z450「正交矩陣（orthogonal matrix）」。

## phases/01-math-foundations/04-calculus-for-ml
- [verified] P1 z328「前向傳遞（forward pass）」。
- [verified] (kept→f1) z209「正定（所有特徵值（eigenvalues） > 0）」：英文註記已補。括號巢狀，屬格式小瑕疵，不計為錯誤。
- [verified] (kept→f1) z257「預設最佳化器（optimizer）」。
- [verified] (kept→f1) z257「移動平均數與變異數（variance）」。
- [verified] P1 z304「資料分布（data distribution）」。
- [verified] P1 z322「策略最佳化（policy optimization）」。
- [verified] P1 z14「權重更新（weight update）」。
- [verified] P1 z572「訓練迴圈（training loop）」。

## phases/01-math-foundations/05-chain-rule-and-autodiff
- [verified] P2 z19「輸出是層層函數組合的結果」。
- [verified] P2 z23「耗時與一次前向傳遞成正比」。
- [verified] P2 z60「讓連鎖律的運作一目了然」。
- [verified] P1 z3「神經網路（neural network）」。
- [verified] (kept→f1) z1「連鎖律與自動微分（automatic differentiation）」。
- [kept-ok] (kept) z12「Value 類別」：class 為通用程式詞。
- [verified] P1 z19「矩陣乘法（matrix multiply）」。
- [verified] (kept→f1) z13「前向傳遞（forward pass）與反向傳遞（backward pass）」。
- [verified] (kept→f1) z384「神經網路（neural network）訓練迴圈（training loop）」、「所有商業深度學習（deep learning）框架」。
- [verified] P1 z425「除錯不收斂的訓練迴圈」；全課「偵錯」已無殘留，z513 為「除錯時不可或缺」。
- [verified] P1 z514「加權總和」：已統一為 GLOSSARY 譯名。

## phases/01-math-foundations/06-probability-and-distributions
- [verified] P0 z216「越負代表機率越低」：與 en「more negative means lower probability」一致，修正已完成。
- [verified] P1 z175「列總和與欄總和」。
- [verified] (kept→f1) z12「常態分布（normal distribution）的機率質量函數」；z13「期望值與變異數（variance）」；z14「數值穩定性技巧（numerical stability trick，減去最大 logit）」。
- [verified] (kept→f1) z19「分類器（classifier）輸出」、「語言模型（language model）」。
- [verified] (kept→f1) z21「機率分布（probability distribution）」、「損失函數（loss function）」。
- [verified] (kept→f1) z46「條件機率（conditional probability）與獨立性（independence）」。
- [verified] (kept→f1) z99「為二元分類（binary classification）建模」；z107「為多類別分類（multi-class classification）建模」。
- [verified] (kept→f1) z157「聯合分布（joint distribution）與邊際分布（marginal distribution）」。
- [verified] P2 z19「這些都是機率的實際應用」。
- [verified] P2 z155「梯度變異數高，代表訓練雜訊較大」。

## phases/01-math-foundations/07-bayes-theorem
- [verified] (kept→f1) z180「信賴區間（confidence intervals，關於程序）」、「可信度區間（credible intervals，關於參數）」。
- [verified] (kept→f1) z23「垃圾郵件篩選器（spam filter）、…機器學習（machine learning）模型」。
- [verified] P1 z114「特徵（feature）」。
- [verified] (kept→f1) z14「L2 正則化（regularization）」；z162「一個懲罰（penalty）大參數值的先驗」。
- [verified] P1 z257「浮點數（floating point）」。
- [verified] P1 z340「管線（pipeline）」。
- [verified] P1 z353「變分推論（variational inference）」。
- [verified] P1 z403「串流（streaming）」。
- [verified] P2 z64「是正規化因子」。
- [not-fixed] P2 z181（r1「先驗扮演正則化」）：表格現況仍為「先驗扮演正則化」，r1 標示已修復為「先驗相當於正則化」，未套用。
- [verified] P2 z72「能檢出 99% 的患者」。
- [verified] P2 z336「tokenization 和」。
- [verified] P2 z348「硬幣正面機率估計」。
- [not-fixed] P2 z452（r1「硬幣偏差」）：現況「用 Beta(2,2) 先驗計算偏差的 MAP 估計」，仍用「偏差」，與 z348 的修正不一致，易被讀為統計偏差。en 為「compute the MAP estimate of the bias」。（低）

## phases/01-math-foundations/08-optimization
- [verified] P1 z79「批次梯度下降法」。
- [verified] P1 z19「損失函數（loss function）」。
- [verified] (kept→f1) z127「一階矩（first moment，m）」、z128「二階矩（second moment，v）」、z368「一階與二階矩初始化為零」。GLOSSARY「動差」已無殘留。
- [verified] (kept→f1) z15「學習率排程（learning rate schedule，…）」；z14「損失地景（loss landscape）」。
- [verified] P2 z81「雜訊較大」。
- [not-fixed] P2 z12（r1「vanilla 梯度下降法」）：現況「從零實作 標準梯度下降法、帶動量的 SGD，以及 Adam」，「標準」已採用，但 r1 要求首見附「vanilla gradient descent」英文，未附。（低）

## phases/01-math-foundations/09-information-theory
- [verified] P1 z95「距離度量（distance metric）」。
- [verified] P1 z108「特徵選擇（feature selection）」。
- [verified] (kept→f1) z110「條件熵（conditional entropy）」；z130「聯合熵（joint entropy）」。
- [not-fixed] P2 z19（r1「同一個想法換了不同的帽子」）：現況「它們其實是其實都源自同一個概念，只是應用情境不同」，句子重複、錯亂，修復未通順。
- [kept-ok] (kept) z21「把正確的標籤，透過一個由學到的權重構成的雜訊通道傳送出去」：與 en 一致，屬風格，kept-audit 判 ok。
- [verified] P2 z51「熵是分布中所有可能結果的平均驚訝程度」。
- [verified] P2 z221「發揮正則化作用」。

## phases/01-math-foundations/10-dimensionality-reduction
- [verified] P1 z47、z67、z133、z361「座標系統」：首見 z47 已統一；全課 grep 無「座標系」（未接「統」）殘留。
- [verified] P1 z19「像素（pixel）」。
- [verified] P1 z91「前處理（preprocessing）」。
- [verified] P1 z97「機率分布（probability distribution）」。
- [verified] P1 z157「可解釋性（interpretability）」。
- [verified] P2 z3「高維資料有其結構，從適當的視角觀察才能看出來」。
- [verified] (kept→f1) z97「找出一個 2D 配置，使其點對的機率分布與原空間一致」：kept-audit 判 miss，f1 已修。
- [verified] P2 z124「適合發表的 2D 圖」。
- [verified] P2 z186「適當的成分數量可由以下條件判斷」。

## phases/01-math-foundations/11-singular-value-decomposition
- [not-fixed] P1 z199（r1「矩陣項目」）：現況「其中大多數項目都缺失」仍為「項目」；en「where most entries are missing」，r1 要求改為「元素」。（低）
- [verified] P1 z218「缺失元素」；z520「用列平均填補缺失元素」：已統一為「元素」。
- [verified] P1 z71「自然座標系統」。
- [not-fixed] P1 z14、z284、z286、z302（r1「廣義反矩陣」）：r1 要求首見補 pseudoinverse，現況中文譯名已消失，全篇只見英文「pseudoinverse」，與 GLOSSARY「pseudoinverse→廣義反矩陣」不符。z284 標題「用 SVD 計算pseudoinverse」中英間缺空格。（低）
- [verified] P1 z19「最小平方法（least squares）」。
- [verified] P1 z218「內積（dot product）」。
- [verified] P1 z138「數值精度（numerical precision）」。
- [verified] P1 z282「訊號處理（signal processing）」。
- [verified] P1 z518「相對誤差（relative error）」。
- [not-fixed] P2 z27（r1「依序執行三種操作」）：現況「依序完成三步：旋轉、縮放、再旋轉：旋轉、縮放、旋轉。」，修復後重複列舉，語句錯亂。en「rotate, scale, rotate」。
- [verified] P2 z176「灰階影像可表示為由像素強度構成的矩陣」。
- [verified] P2 z195（r1「漸層」）：「整體結構（形狀、整體形狀與強度變化）」已改掉「漸層」，但「形狀」與「整體形狀」重複，屬冗詞，不影響語意。
- [verified] P2 z250「雜訊底限」。

## phases/01-math-foundations/12-tensor-operations
- [verified] P2 z29「張量是具有統一資料型別的多維數值陣列」。
- [verified] P2 z65「在記憶體中，2D 陣列會以一維位元組序列儲存」。
- [verified] P2 z61「悄悄降低效能」。
- [verified] P2 z21「形狀規則」（r1「形狀契約」已改）。

## phases/01-math-foundations/13-numerical-stability
- [verified] (kept→f1) z21「32 位元浮點運算中累積的捨入誤差（rounding error），悄悄吃掉了你的準確率」：與 en 一致。
- [verified] P1 z50、z85「捨入雜訊」：與 en「rounding noise」一致，符合 GLOSSARY。
- [verified] P1 z97「相對誤差（relative error）」。
- [not-fixed] P1 z282（r1「損失縮放」）：現況「損失縮放（loss scaling）（loss scaling）」，英文註記重複，疊註。
- [new-issue] z594（表格，未列於 r1）：「損失縮放（loss scaling）（loss scaling）」，同型疊註。
- [kept-ok] (kept) z103「Welford 演算法」：人名已為英文，與 GLOSSARY 一致。
- [not-fixed] P2 z3（r1「會露出破綻的抽象」）：現況「浮點數是一種浮點數是一種有漏洞的抽象」，修復時疊字。

## phases/01-math-foundations/14-norms-and-distances
- [verified] P1 z19「像素（pixel）陣列」。
- [verified] P1 z21「推薦引擎（recommendation engine）」。
- [note] 譯文段落合併為單行，與原文換行差異，段落數與 en 相同（130 段），內容無遺漏。

## phases/01-math-foundations/15-statistics-for-ml
- [verified] P1 z142「對角線元素」。
- [verified] (kept→f1) z103「常態分布（normal distribution）」。
- [verified] P1 z509「信賴水準（confidence level）」。
- [verified] P1 z128「過度擬合（overfitting）」。
- [not-fixed] P2 z312（r1「也就是進行多重比較」）：現況「同時檢定許多假設，同時檢定許多假設（多重比較）時（multiple comparisons）時，有些結果會只…」，句子重複、錯亂。en「When you test many hypotheses」。

## phases/01-math-foundations/16-sampling-methods
- [not-fixed] P1 z23（r1「策略梯度」）：現況「估計策略梯度（policy gradient）（policy gradient）」，疊註。
- [verified] P1 z15「目標分布（target distribution）」。
- [verified] (kept→f1) z41「將簡單分布的樣本變換成目標分布（target distribution）的樣本」：f1 已刪重複註記。
- [verified] P1 z189「平穩分布（stationary distribution）為目標分布（target distribution）」：f1 已刪重複。
- [not-fixed] P1 z13（r1「溫度取樣」）：現況「實作溫度取樣（temperature sampling）（temperature sampling）」，疊註。z242 標題首見附英文，正確。
- [verified] P1 z265「機率質量（probability mass）」。
- [verified] P2 z14「讓梯度透過取樣步驟反向傳播（backpropagation）」。

## phases/01-math-foundations/17-linear-systems
- [kept-ok] (kept, borderline) z114「約需十億次浮點運算」：首見未附英文，但「浮點運算」為數值計算通用詞。同課 z135 已附「浮點運算（floating-point arithmetic）」。可選補「（floating-point operations）」，非錯誤。
- [verified] P1 z275「過度擬合（overfitting）」。
- [verified] P2 z167「正交矩陣滿足 Q^T Q = I」。
- [verified] P2 z334「若要解含有數百萬個未知數的大型稀疏系統」。

## phases/01-math-foundations/18-convex-optimization
- [not-fixed] P1 z13（r1「二次收斂」）：現況「二次收斂（quadratic convergence）（quadratic convergence）」，疊註。
- [not-fixed] P1 z19（r1「局部最小值」）：現況「局部最小值（local minimum）（local minimum）」，疊註。
- [new-issue] z535（表格，未列於 r1）：「局部最小值（local minimum）（local minimum）」，同型疊註。
- [not-fixed] P1 z21（r1「學習率排程」）：現況「學習率排程（learning rate schedule）（learning rate schedule）」，疊註。
- [not-fixed] P2 z23（r1「在違反凸性所有良好性質的情況下仍能運作」）：現況「以及深度學習如何即使不具備凸性帶來的良好性質，深度學習仍能運作」，修復後句子重複、不通順。
- [verified] P2 z94「梯度下降法不會卡在次佳的局部解」。
- [verified] P2 z349「在含有 n 個參數的函數中」。

## phases/01-math-foundations/19-complex-numbers
- [not-fixed] P1 z19（r1「複數向量空間」）：現況「複數向量空間（complex vector space）（complex vector spaces）」，英文註記重複且詞形不同，疊註。
- [verified] (kept→f1) z385「正交基底（orthogonal basis）」；「頻域（frequency domain）」已附英文。
- [verified] P2 z12「以直角座標形式和極式實作複數運算」。
- [verified] P2 z100「它與正實軸的夾角」。
- [verified] P2 z216「i 可視為將複數旋轉 90 度的算子」。
- [verified] P2 z237「不同頻率能以不同解析度編碼位置」。

## phases/01-math-foundations/20-fourier-transform
- [verified] P1 z41、z441「複數正弦訊號（complex sinusoid）」：f1 已刪 z441 重複註記。
- [verified] (kept→f1) z69「另一種座標系統（coordinate system）」。
- [not-fixed] P1 z55（r1「共軛對稱」）：現況「共軛對稱（conjugate symmetry）（conjugate symmetry）」，疊註。
- [verified] P2 z25「以頻譜圖作為輸入表示」。
- [verified] P2 z55「對實值訊號而言」。
- [verified] P2 z173「DFT 將訊號視為週期訊號」。
- [verified] P2 z392「若要加窗或做更進階的頻譜分析」。

## phases/01-math-foundations/21-graph-theory
- [verified] (kept→ok) z14「正規化相鄰矩陣（normalized adjacency matrix）」：首見已附英文。
- [verified] P1 z91「圖形走訪（graph traversal）」。
- [not-fixed] P1 z87（r1「度分布」）：現況「網路的度分布（degree distribution）（degree distribution）」，疊註。
- [new-issue] z238（表格，未列於 r1）：「度分布（degree distribution）（degree distribution）」，同型疊註。
- [not-fixed] P1 z240（r1「圖分割」，原列於 z176）：現況「圖分割（graph partitioning）（graph partitioning）」，疊註。
- [verified] P2 z52「若圖有 n 個節點」。
- [verified] P2 z149「3 個連通分量」。
- [kept-ok] (kept) z14「透過 FFT 乘法進行卷積」：本課無此句（誤置）；實際位於 01/20 z14，已附英文。

## phases/01-math-foundations/22-stochastic-processes
- [verified] P1 z23「反向運作的馬可夫鏈」。
- [not-fixed] P1 z31（r1「轉移矩陣」，原列於 z29）：現況「具有轉移矩陣（transition matrix）（transition matrix）」，疊註。
- [new-issue] z446（表格，未列於 r1）：「轉移矩陣（transition matrix）（transition matrix）」，同型疊註。
- [verified] P1 z41「原點（origin）」。
- [verified] (kept→ok) z56「變異數（variance）為 1」；「標準常態分布（standard normal distribution）」已附英文。
- [verified] P1 z60「平均值（mean）」。
- [verified] P2 z424「順帶取得近似的貝氏後驗樣本」。

## phases/02-ml-fundamentals/01-what-is-machine-learning
- [not-fixed] P1 z21（r1「不必重寫程式碼」）：現況「…你可以用新資料重新訓練（retrain）模型，程式碼（code）。」。原句的否定「不必重寫」已丟失，句子不通。en「retrain the model with new data, not rewrite the code」。語意錯誤，屬改錯。
- [verified] P1 z141「特徵工程（feature engineering）」。
- [verified] P1 z221「懲罰項（penalty term）」。
- [verified] (kept→f1) z235「偏差（bias）」、z237「變異（variance）」。
- [verified] P2 z149「讓它預測新資料」。
- [not-fixed] P2 z362（r1「在前一課的限制上繼續往前建構」）：現況「每一課都會每一課都會接續前一課」，疊句。

## phases/02-ml-fundamentals/02-linear-regression
- [verified] P1 z21「訓練迴圈（training loop）」。
- [verified] P1 z23「基準模型（baseline）」。
- [verified] P1 z524「多項式次數（degree）」。
- [verified] P1 z513「數值穩定性（numerical stability）」。
- [verified] P2 z522「哪一種方法的成本曲線最平滑？」。
- [verified] P2 z533「透過最佳化將它最小化」。
- [new-issue] (低，結構) 題目之間（z523、z525）各插入空行，en 為緊湊清單（z522–z524）。譯文變成鬆散清單，段落數 82 對 80，結構與原文不一致。內容無遺漏。

## phases/02-ml-fundamentals/03-logistic-regression
- [kept-ok] (kept) z19「你想根據腫瘤大小預測腫瘤是惡性還是良性」：predict 為一般動詞用法。
- [verified] P1 z23「實務上最廣泛使用的演算法（algorithm）之一」。
- [verified] P1 z58「導數（derivative）」。
- [verified] (kept→f1) z100「sigmoid 引入了非線性（nonlinearity）」。
- [verified] P1 z526「預設（default）0.5」：英文註記已補；括號巢狀，屬格式小瑕疵。
- [verified] P2 z526「機率高於這個閾值時」。
- [new-issue] (低，結構) 題目之間（z508、z510、z512）各插入空行，en 為緊湊清單（z507–z509），同 02/02 的結構差異。

## phases/02-ml-fundamentals/04-decision-trees
- [verified] P1 z41「資料點（data point）」。
- [not-fixed] P1 z122（r1「決策樹迴歸」→「迴歸樹（regression tree）」）：標題現況「迴歸樹（regression tree）（regression）」，多出一組英文註記。en 為「Decision trees for regression」。（低）
- [verified] P1 z158「預設值（default）」。
- [verified] (kept→f1) z447「樹的分段常數（piecewise-constant）預測」。
- [verified] P2 z98「將排序後相鄰且不同的特徵值取中點，作為候選閾值」。
- [verified] P2 z190「資料有空間或序列結構時」。
- [verified] P2 z445「在含有 3 個類別的二維資料集上」。

## phases/02-ml-fundamentals/05-support-vector-machines
- [verified] P1 z23「深度學習（deep learning）」。
- [verified] P1 z23「演算法（algorithm）」。
- [verified] P1 z80「記憶體（memory）」。
- [verified] P1 z246「求解器（solver）」。
- [not-fixed] P2 z189（r1「對於 D 維空間中 d 次的多項式核」）：現況「在 D 維空間中，d 次多項式核的明確特徵空間……，明確建立特徵空間需要 O(D^d) 個維度」。「……」是 r1 建議文字的佔位符，en 無此內容；「明確特徵空間」重複，句子不通。en「the explicit feature space has O(D^d) dimensions」。

## phases/02-ml-fundamentals/06-knn-and-distances
- [verified] P1 z3「演算法（algorithm）」。
- [verified] P1 z84「預設（default）」。
- [verified] P1 z167「中位數（median）」。
- [verified] P1 z202「記憶體（memory）」（表格，通用詞）。
- [verified] P1 z37「目標值（target）」。
- [verified] P2 z196「所有運算都留到預測時才做」。

## phases/02-ml-fundamentals/07-unsupervised-learning
- [verified] P1 z15「管線（pipeline）」。
- [verified] P1 z65「密度（density）式分群（density-based clustering）」。
- [verified] P1 z82「階層式分群（hierarchical clustering）」。
- [not-fixed] P1 z480（r1「收斂速度（convergence）」）：現況「比較這種方法與隨機初始化的收斂速度（convergence）（convergence speed）」，英文註記重複且詞義不同，疊註。
- [verified] P2 z118「以分群偵測異常」。
- [verified] P2 z472「反覆指派資料點並重新計算質心」。
- [note] r1 結構檢查中「合併」誤報 merge 缺失，屬檢查器誤報，不計問題。

## phases/02-ml-fundamentals/08-feature-engineering
- [verified] P1 z29「特徵處理管線（feature pipeline）」。
- [verified] (kept→f1) z50「壓縮右偏（right-skewed）分布（distribution，收入、人口數、詞數這類資料）」：英文註記已補，但嵌在舉例括號內，可讀性差，建議拆開。非錯誤。
- [verified] P1 z78「缺失值（missing value）」。
- [verified] P1 z88「特徵交互作用（feature interaction）」。
- [not-fixed] P1 z15（r1「過濾法（filter method）」）：現況「套用過濾法（filter method）（filter method）特徵選擇」，疊註。
- [verified] P2 z25「最值得投入的工作」。
- [kept-ok] (kept) z90「特徵交互作用（feature interaction）會讓特徵空間（feature space）倍增」：「倍增」為原文 multiply 的比喻用法，kept-audit 判 ok。

## phases/02-ml-fundamentals/09-model-evaluation（f4 收尾，已確認 f4-changelog 有 C4 紀錄；檔案 mtime 穩定）
- [verified] P1 z12「類別不平衡（class imbalance）」。
- [verified] (kept→f1+f4) z98–z99 表格：「真陽性（true positive，TP）」「偽陰性（false negative，FN）」「偽陽性（false positive，FP）」「真陰性（true negative，TN）」全名已補，與 en 一致。
- [verified] (kept→f1) z107「真陽性率（true positive rate）對偽陽性率（false positive rate）的變化」。
- [kept-ok] (kept) z12「分層 K 折（stratified K-fold）」：首見已附英文，kept-audit 判 ok。
- [kept-ok] (kept, borderline) z49「測試集是你的保留集（hold-out）保證」：直譯但語意完整、無增譯，可選改為「保留測試集，才能確保回報的表現反映…」。
- [verified] P2 z113「對所有誤差採線性懲罰」。
- [new-issue] z137（r1 未列）：粗體標題「類別不平衡（class imbalance）（class imbalance）」，英文註記重複，疊註。

## phases/02-ml-fundamentals/10-bias-variance
- [not-fixed] P1 z23（r1「模型容量」）：現況「模型容量（model capacity）（model capacity）」，疊註。
- [not-fixed] P1 z29（r1「分布」）：現況「同一個分布（distribution）（distribution）」，疊註。
- [verified] P1 z21「20 次（degree-20）多項式（polynomial）」。
- [verified] P2 z126「樣本數方向的雙重下降」。
- [not-fixed] P2 z127（r1「epoch 維度雙重下降」）：現況仍為「epoch 維度雙重下降（epoch-wise double descent）」，r1 要求改為「訓練 epoch 方向」，未套用。（低）
- [verified] P2 z234「兩條曲線都進入平台期」。
- [verified] P2 z388「訓練與驗證分數差距最大的地方」。

## phases/02-ml-fundamentals/11-ensemble-methods
- [not-fixed] P1 z27（r1「分類器」）：現況「分類器（classifier）（classifier）」，疊註。
- [verified] P1 z13「模型（model）」；P1 z19「訓練（training）」：首見皆附英文。
- [kept-ok] (kept) Mermaid 節點「邏輯斯迴歸（logistic regression）」：首見已附英文於圖中節點，kept-audit 判 ok。
- [verified] P1 z88「加權總和（weighted sum）」。
- [not-fixed] P2 z88（r1「集成所產生的系統性誤差」）：現況「每個新模型（model）都在修正目前為止的目前集成的系統性誤差」，「目前」重複，句子不通。en「Each new model corrects the current ensemble's systematic error」。
- [not-fixed] P2 z173（r1「對號入座」）：現況「學會學會依輸入選擇合適的模型（model）」，疊字。

## phases/02-ml-fundamentals/12-hyperparameter-tuning
- [verified] P1 z19「模型（model）」。
- [verified] (kept→f1) z3「訓練（training）開始前」。
- [verified] P1 z59「分布（distribution）」。
- [verified] (kept→f1) z130「快速收斂（convergence）」。
- [verified] P2 z104「在這個候選點」。
- [verified] P2 z227「對以梯度為基礎的方法來說」。
- [verified] P2 z362「以模型（model）為基礎的實作」。

## phases/02-ml-fundamentals/13-ml-pipelines
- [verified] P1 z3「模型（model）不是產品，管線（pipeline）才是」。
- [verified] P1 z12「模型（model）訓練（model training）」。
- [new-issue] z176（r1「模型登錄（model registry）」）：現況「MLflow 的 Model Registry（模型（model）登錄（model registry））」，英文重複、括號巢狀，冗餘。（低）
- [not-fixed] P2 z3（r1「已部署的預測」）：現況「管線涵蓋從原始資料到從原始資料到部署後產生的預測」，疊句。
- [verified] P2 z21「兩份程式碼後來不再一致」。

## phases/02-ml-fundamentals/14-naive-bayes
- [verified] P1 z54「聯合分布（joint distribution）」。
- [verified] P1 z68「矩陣乘法（matrix multiplication）」。
- [verified] P1 z169「預設（default）起點」。
- [verified] P1 z66「特徵冗餘（feature redundancy）」。
- [verified] P2 z374「頻率資訊雜訊較大」。
- [not-fixed] P2 z386（r1「它看到的是自己並不是為了處理而設計的計數」）：現況「但但這些計數並非 BernoulliNB 設計來處理的輸入」，疊字。

## phases/02-ml-fundamentals/15-time-series
- [verified] P1 z12「分解（decomposition）」。
- [verified] P1 z19「變數」：r1 的 z19 已改寫，不再含「變數」；首見為 z296「同一個變數（variable）的時間落後版本」，已附英文。
- [verified] (kept→f1) z200「數值最佳化（numerical optimization）」。
- [verified] P1 z389「平均絕對誤差（mean absolute error）」（括號巢狀，格式可接受）。
- [verified] P2 z23「模式會隨時間改變」。
- [verified] P2 z188「舊資料會造成干擾」。
- [verified] P2 z392「季節性簡單基準模型」。

## phases/02-ml-fundamentals/16-anomaly-detection
- [verified] (kept→f1) z33「一個平時只花 $50 的帳戶卻刷了 $50,000」：英文整句殘留已譯，與 en 一致。
- [verified] (kept→f1) z417「誤報代表不必要的停機，造成 $50,000 的損失；漏掉故障則要花 $500,000 維修」：英文殘留已譯。
- [verified] P1 z19「伺服器（server）」。
- [kept-ok] (kept) z21「網路入侵」：「網路」為通用 CS 詞，kept-audit 判 ok。
- [verified] P1 z92「預設（default）閾值（threshold）」。
- [kept-ok] (kept) z98「伺服器（server）回應時間」：英文已附，kept-audit 判 ok。
- [verified] P1 z119「只能單變數（每個特徵各自套用）」；z434「多變數異常」：已統一為「變數」。
- [kept-ok] (kept, 誤置) 「基準模型（baseline）」：本課無此詞。z220 為「收集基準資料」，語境不同。
- [verified] P2 z13「並為每種類型選擇合適的偵測方法」。
- [verified] P2 z399「資料分布改變／漂移」。

## phases/02-ml-fundamentals/17-imbalanced-data
- [verified] P1 z15「類別不平衡（class imbalance）資料管線」；z1 標題已附英文。
- [verified] (kept→f1) z23「真正要緊的分類（classification）裡」。
- [verified] P1 z157「預設（default）閾值（threshold）」。
- [verified] P1 z88「內插（interpolation）」：與 GLOSSARY「內插」一致。
- [verified] P1 z462「一個程式檔」。
- [not-fixed] P2 z25（r1「準確率失敗」）：現況「準確率的問題在於……，是因為它把所有正確預測一視同仁」，「……」是 r1 建議文字的佔位符，en「Accuracy fails because…」。句子含未譯的占位符。
- [kept-ok] (kept) z84「在 x 和那個鄰居之間的線段上造一個新樣本」：kept-audit 判 ok，「造」為口語但語意精確，可選「生成」。

## phases/02-ml-fundamentals/18-feature-selection
- [verified] P1 z19「模型（model）」。
- [verified] P1 z211「合成資料（synthetic data）」。
- [verified] P1 z129「參數（parameter）」。
- [verified] (kept→f1) z57「L1 正則化使權重（weight）歸零」。
- [kept-ok] (kept, 誤置) 「不平衡分類器」：本課無此詞。實際位於 02/17 z13，已附英文。
- [verified] P2 z23「而且模型也更容易解釋」。
- [verified] (kept→f1) 「把權重推進到 0」→「使權重（weight）歸零」（z57，f1 修復）。
- [verified] P2 z119「移除排名最低的 10% 特徵」。

---

## Summary

### 計數（只計各課節內的判定行；不含 `[note]` 與下方優先清單的重列）

| 類別 | 條數 |
|---|---|
| verified | 291 |
| not-fixed | 48 |
| kept-ok | 18 |
| kept-wrong | 1 |
| new-issue | 8 |
| 合計判定 | 366 |
| note（無 finding 課的覆核備註） | 5 |

- 課數：52（00 共 12 課、01 共 22 課、02 共 18 課）。
- 無 finding 課（r1 clean）：00/01、00/02、00/03；覆核結果見各課 `[note]`。
- f4 收尾課：00/09、02/09。已確認 f4-changelog 有 C3／C4 紀錄，檔案 mtime 自 20:18:31 未變，已納入本次判定。
- 誤置條目（已於對應課判定）：00/11「訓練日誌」、01/21「透過 FFT 乘法進行卷積」、02/16「基準模型」、02/18「不平衡分類器」。

### 優先清單

**A. 語意錯誤、占位符殘留、錯亂句（須優先修）**
1. [not-fixed] 02/01 z21：「不必重寫程式碼」改成「……重新訓練（retrain）模型，程式碼（code）。」，否定丟失，語意錯。
2. [not-fixed] 02/05 z189：「明確特徵空間……」含 r1 建議文字的省略號佔位符，且句子重複。
3. [not-fixed] 02/17 z25：「準確率的問題在於……，是因為…」含佔位符省略號。
4. [not-fixed] 00/05 z57：表格漏譯「檔案瀏覽器」（en「file browser」）。
5. [not-fixed] 00/05 z59：「已編輯器（editor），支援 Git 整合和除錯」語句錯亂，應為「已整合在編輯器（editor）中」。
6. [not-fixed] 01/09 z19：「它們其實是其實都源自同一個概念」句子錯亂。
7. [not-fixed] 01/11 z27：「依序完成三步：旋轉、縮放、再旋轉：旋轉、縮放、旋轉」重複列舉。
8. [not-fixed] 01/15 z312：「同時檢定許多假設，同時檢定許多假設（多重比較）時（multiple comparisons）時…」句子重複錯亂。
9. [not-fixed] 01/18 z23：「以及深度學習如何即使不具備凸性…深度學習仍能運作」句子重複、不通。
10. [not-fixed] 02/11 z88：「修正目前為止的目前集成的系統性誤差」，「目前」重複。

**B. 疊字（修復引入）**
- 00/12 z21「在這些在這些靜默失敗」；01/02 z82「常常常」；01/13 z3「浮點數是一種浮點數是一種」；02/01 z362「每一課都會每一課都會」；02/11 z173「學會學會」；02/13 z3「從原始資料到從原始資料到」；02/14 z386「但但」。

**C. 疊註（英文註記重複，r1 已修復但修錯）**
- 00/06 z28；00/07 z375、z383；01/01 z14、z435；01/13 z282、z594（新）；01/16 z13、z23；01/18 z13、z19、z21、z535（新）；01/19 z19；01/20 z55；01/21 z87、z238（新）、z240；01/22 z31、z446（新）；02/04 z122（標題多一組「（regression）」）；02/07 z480；02/08 z15；02/09 z137（新）；02/10 z23、z29；02/11 z27。
- 這一類多為 r1「首見附英文」建議被重複套用。建議全域掃 `（X）（X）` 與同一英文連續註記，逐處刪除後者。

**D. 用語回歸與術語缺漏**
- [not-fixed] 00/11 z15：f1 附帶修復重新引入「踩坑」，與 z269「踩雷」不一致。
- [not-fixed] 00/07 z13、z12、z15：「模型」「掛載」「建置」「服務」首見無英文，GLOSSARY 收 mount、build。
- [not-fixed] 01/02 z15：「神經網路框架」首見無英文（r1 標示已修）。
- [not-fixed] 01/07 z181：「先驗扮演正則化」未套用 r1 修正。
- [not-fixed] 01/07 z452：「偏差的 MAP 估計」仍用「偏差」，與 z348 不一致。
- [not-fixed] 01/08 z12：「標準梯度下降法」首見未附 vanilla gradient descent。
- [not-fixed] 01/11 z14、z284、z286、z302：「廣義反矩陣」中文譯名消失，僅留英文 pseudoinverse，違反 GLOSSARY。z199「其中大多數項目都缺失」仍為「項目」（en entries，r1 要求「元素」）。
- [not-fixed] 02/10 z127：「epoch 維度雙重下降」未依 r1 改為「訓練 epoch 方向」。

**E. 維持原樣項的複審**
- [kept-wrong] 00/07 z19：「結果你的模型在他的電腦上崩潰」，en 為 their（中性），譯文新增男性指涉。建議「同事的電腦上」。
- 其餘 kept 項：18 條 kept-ok，其中 4 條為誤置條目（00/11、01/21、02/16、02/18），1 條為 borderline 可選改寫（02/09 z49），其餘為通用詞或首見已附英文。

**F. 結構與格式（低）**
- [new-issue] 02/02 練習 z523、z525；02/03 練習 z508、z510、z512：題目之間插入空行，原文為緊湊清單，譯文為鬆散清單（段落數 82 對 80、551 對 549）。內容無遺漏。
- [new-issue] 02/13 z176：「MLflow 的 Model Registry（模型（model）登錄（model registry））」英文重複、括號巢狀，冗餘。
- [verified] 格式小瑕疵（不計錯）：01/04 z209、02/03 z526、02/15 z389 括號巢狀；02/08 z50 英文註記嵌入舉例括號；01/11 z195 「形狀、整體形狀」冗詞。

### 覆核方法與殘留風險

- 方法：逐條 r1 finding 以關鍵字定位現況行並對照 en.md；kept 項依 v1-kept-audit 判定並自行覆核；全量自動掃描（52 課）：疊字、三連字、重複括號註記、簡體字、GLOSSARY ✗ 禁用譯名、翻譯腔樣式、英文殘留（≥4 詞並排除參考文獻標題）、結構（代碼區塊內容、行內碼、URL、metadata、標題層級、表格與清單計數、空行）與 en.md 逐項比對。
- 未通讀：00/02、00/03 與多數未經修改的段落，僅經自動掃描與抽樣。仍可能存在未被 pattern 捕捉的誤譯。
- 未執行 `scripts/check_translation.py`（本任務為唯讀，且檢查器可能寫出輸出檔）。
- 掃描與輔助腳本保存於 `/private/tmp/zh-tw-review/v1-final-scratch/`。
- 結構比對中，00/01、01/14 有段落換行差異（原文多行段落譯為單行），段落與區塊數與 en.md 相同，已逐段核對內容，不計為問題。

### 建議下一步

先一次修正 A（10 條）與 B、C 全部疊字疊註，再修 D 的術語缺漏與 E 的 00/07 z19。修完後以以下 pattern 重跑掃描：`（(.+?)）（\1）`、三連字 `(.)\1\1`、省略號佔位符 `……` 出現在句中、`項目` 作為矩陣元素用法，並對 02/13 z176 與 02/02、02/03 練習空行做結構確認。之後依最終版本重做本次終態複審。
