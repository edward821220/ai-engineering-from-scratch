# v2-final-audit：phases 03 / 04 / 06 終態複審（worker，唯讀）

## 範圍與依據

- 範圍：03-deep-learning-core（13 課）、04-computer-vision（28 課）、06-speech-and-audio（17 課）；共 265 條 finding（03 為 39 條、04 為 150 條，取自 r2；06 為 76 條，取自 r3）。
- 報告來源：`/Users/edward/Desktop/ai-engineering-from-scratch/docs/reviews/zh-tw/r2.md`（03/04 章節）、`.../r3.md`（06 章節）。
- 誤駁回稽核：`/private/tmp/zh-tw-review/v2-kept-audit.md`（03/04 的 kept 條目）、`v3-kept-audit.md`（06 的 kept 條目）。kept 判定以稽核為參照，並逐條重驗現況。
- 修復日誌：`f2-changelog.md`（03/04）、`f3-changelog.md`（06）、`f4-changelog.md`（04/15、04/20、04/21、06/08 等收尾）。`f1-changelog.md` 無 03/04/06 條目。
- 譯稿與原文：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`、`/private/tmp/aiefs-main-source/phases/<phase>/<lesson>/docs/en.md`；術語以 `GLOSSARY.md` 為準。
- 快照時間：2026-10-10 20:46（CST）。f4 仍在寫入：`f4-changelog.md` 為 605 行（20:38 更新），04/20 譯稿於 20:45:25 被改寫。下列 pending 課的判定皆為此快照。

## 判定定義

- `[verified]`：註記已修復，現況正確，且未改錯。
- `[not-fixed]`：註記已修復（或稽核 miss 已被修），但現況仍有問題；包含假修復（只改一部分）與修錯（修復本身造成重複、錯句或語意錯置）。
- `[kept-ok]`：維持原樣，且複審（稽核）同意，或屬忠實譯文。
- `[kept-wrong]`：維持原樣，但複審認為仍應修，或現況仍不通順。
- `[new-issue]`：報告未列、現況有明確錯誤（獨立存在，未與任何 finding 綁定）。
- 忽略項：程式碼、行內碼、數學式、URL、圖片 alt、Mermaid timeline 的英文、受保護內容。Mermaid 邊標籤（`|error|`）依 STYLE 維持原樣。

## 方法（可重現）

1. 逐條 finding 以關鍵字（取自報告引文的新譯或舊譯）在現況 zh-TW.md 定位，並以 `sed -n` / `grep -n` 取得行號與上下文；對照 en.md 同段。
2. 逐一抽查 f2/f3/f4 changelog 的編輯點（含 E 系列全域「抽樣→取樣」掃改）。
3. 全篇模式掃描（Python，跳過 code fence）：
   - 重複括註：`（X）（X）`，以及相鄰英文括註其中一方包含另一方（如 `（covariance matrix）（covariance）`）。
   - 疊字／疊詞：單字 `(.)\1`、雙字詞 `(.{2,10})\1`、空格分隔 `的 的`、`以 以`。
   - 殘留省略號 `……`。
   - GLOSSARY「禁用」欄 151 個詞：03/04/06 無命中。
   - 簡體字常見字集（如 这、为、说、进、时、数…）：無命中。
   - 掃描命中均人工判讀，正常疊詞（如 看看、一層層、常常、微微、想想）已排除。
4. 本報告未逐段重讀全部 58 課的全文；clean 課（03/06、04/05）只做模式掃描。

## phases/03-deep-learning-core/01-the-perceptron（2 條：verified 1 / not-fixed 1）

- `[not-fixed]` P1「邏輯閘」首見英文：註記已修復，但修錯。L87「看看這些邏輯閘（logic gate）（logic gate）：」與 L152「用邏輯閘（logic gate）（logic gate）訓練」皆重複括註。
- `[verified]` P2「做過的每一個神經網路」→「打造出來」：L21「至今打造出來的每一個神經網路」。

## phases/03-deep-learning-core/02-multi-layer-networks（2 條：verified 1 / not-fixed 1）

- `[verified]` P2「研究經費中斷了十多年」→「斷了」：L23「研究經費斷了十多年」，對應 en「killed funding for over a decade」。
- `[not-fixed]` P2 括號與標點：L121「（這一層的神經元數，前一層的神經元數）」已修；L346 表格「形狀為（當前層神經元數, 前一層神經元數）」仍是全形括號搭配半形逗號。

## phases/03-deep-learning-core/03-backpropagation（2 條：not-fixed 2）

- `[not-fixed]` P1「記憶體」首見英文：L73 首見「記憶體（memory）」已附英文，但同句「你拿記憶體（memory）（memory）換速度」重複括註（修錯）。
- `[not-fixed]` P2「地質年代」→依上下文改寫：L21 仍為「你得花上地質時間」（直譯，未依建議改寫）。

## phases/03-deep-learning-core/04-activation-functions（1 條：verified 1）

- `[verified]` P2「用曲線思考」→「以曲線思考」：L3「讓神經網路（neural network）能以曲線思考」，語句通順。

## phases/03-deep-learning-core/05-loss-functions（5 條：verified 2 / not-fixed 3）

- `[not-fixed]` P1「機率質量」首見英文：L79「模型學會把機率質量（probability mass）（probability mass）集中到正確答案上」重複括註（修錯）。
- `[not-fixed]` P1「正樣本對／負樣本對」首見英文：L119「這是正對：它們的 embedding 應該相似。批次（batch）裡的其他影像組成負對」仍無英文（en 為 "positive pair" / "negative pair"）。
- `[verified]` P1「錨點／正樣本／負樣本」（kept；稽核 miss #1，已由 f2 修）：L131「錨點（anchor）、正樣本（positive，同一類別）、負樣本（negative，不同類別）」。
- `[not-fixed]` P2「把 MSE 壓到最小的模型」：L19 現為「在分類問題上若在分類問題上使用 MSE 做最小化，模型會……，會很有把握地把每件事都預測成 0.5」——句首疊句＋殘留「……」（修錯；en "A model minimizing MSE on a classification problem will confidently predict 0.5 for everything"）。
- `[verified]` P2「$10,000 … $200,000」主句改寫：L39「大多數房子的預測誤差是 1 萬美元，但有一棟豪宅的誤差達 20 萬美元」，數字與 en 一致。

## phases/03-deep-learning-core/06-optimizers（clean）

- 報告為 clean，無 f2–f4 編輯；模式掃描無命中。`[kept-ok]`（無 finding）。

## phases/03-deep-learning-core/07-regularization（3 條：verified 3）

- `[verified]` P1「耐心視窗」→「容忍輪數（patience）」：L167「再多訓練一段容忍輪數（patience）」，與 GLOSSARY patience 一致。
- `[verified]` P2「對複雜度課的稅」→「對模型複雜度施加的懲罰」：L3「正則化是你對模型複雜度施加的懲罰」。
- `[verified]` P2「音高移動」→「音高偏移」：L161「音高偏移」。

## phases/03-deep-learning-core/08-weight-initialization（3 條：verified 1 / kept-ok 2）

- `[kept-ok]` P2「花了 512 個參數，得到 1」（kept；稽核 borderline #2）：L19「你付了 512 個參數（parameter）的代價，只得到 1 個。」忠實；「1 個」由上文「同一個神經元的 512 份複本」可解。
- `[kept-ok]` P2「刀鋒邊界」（kept；稽核 ok #3）：L23「「行」和「壞」的界線薄得像刀口。」通順，優於報告建議稿。
- `[verified]` P2 Mermaid「結果：配<br/>sigmoid/tanh 可以訓練」→「可用」：L120「結果：可用 sigmoid/tanh 訓練」。

## phases/03-deep-learning-core/09-learning-rate-schedules（4 條：verified 3 / kept-ok 1）

- `[verified]` P1「LR range test」（kept；稽核 miss #4，f2 修）：L139「用學習率範圍測試（LR range test）」、L403「學習率範圍測試（learning rate range test）」。
- `[verified]` P1「cosine annealing with warm restarts」（kept；稽核 miss #5，f2 修）：L405「帶暖重啟的餘弦退火（cosine annealing with warm restarts），也就是 SGDR」；L419 表格同步。
- `[verified]` P2「穩定到尖銳的極小值」（kept；稽核 miss #6，f2 修）：L21「收斂到尖銳極小值（sharp minimum）」。
- `[kept-ok]` P2「微調一個預訓練模型」（kept；稽核 ok #7）：L25「fine-tuning 一個預訓練（pretrained）模型時」。

## phases/03-deep-learning-core/10-mini-framework（3 條：verified 3）

- `[verified]` P1「訓練迴圈」「權重初始化」（kept；稽核 miss #8，f2 修）：L14「訓練迴圈（training loop）」、L19「權重初始化（weight initialization）」。
- `[verified]` P1「局部極小值」→加英文：L53「局部極小值（local minimum）」。
- `[verified]` P2「並排學習率」→「排程學習率」：L23「排程學習率（learning rate）」。

## phases/03-deep-learning-core/11-intro-to-pytorch（5 條：verified 4 / kept-ok 1）

- `[verified]` P1「訓練迴圈」→加英文：L13「標準訓練迴圈（training loop）」。
- `[verified]` P1「序列化」→加英文：L25「沒有序列化（serialization）」。
- `[verified]` P2「磁帶」→「運算記錄帶」：L103「以運算記錄帶為基礎的自動微分」。註：「運算記錄帶」未列於 GLOSSARY，未附 tape；見 new-issue N8（低）。
- `[verified]` P2「這五行不會」→「這五行不會變」：L215。
- `[kept-ok]` P2「磁碟受限的工作負載」（kept；稽核 ok #9）：L238「在受磁碟限制的工作負載上」。

## phases/03-deep-learning-core/12-intro-to-jax（5 條：verified 3 / not-fixed 1 / kept-wrong 1）

- `[not-fixed]` P1「急切」→「立即執行（eager execution）」：L13 已正確（「立即執行（eager execution）就地修改」）；但 L21 現為「它在 Python 裡立即執行（eager execution）地、一次一個地追蹤運算」，「立即執行地」語句不通（修錯）。
- `[verified]` P2「核心啟動」→「GPU kernel 啟動」：L21「每一次 `tensor + tensor` 都是一次獨立的GPU kernel 啟動」（「的GPU」缺半形空格，見 N7）。
- `[verified]` P2「彆扭一個星期，然後就通了」：L58「剛開始會覺得不太習慣，過一週左右就會上手」。
- `[verified]` P2「第一級支援」（kept；稽核 miss #10，f2 修）：L218「官方一級支援，Google 兩邊都是自己做的」；「官方」為小幅補譯，可接受。
- `[kept-wrong]` P2「隨機金鑰」（kept；稽核 borderline #11）：原字串已改，但 L492「沒有未明示 key 的隨機」仍讀來斷裂、key 未譯；稽核建議改「沒有明確的 key 就不產生隨機數」。低優先。

## phases/03-deep-learning-core/13-debugging-neural-networks（4 條：verified 4）

- `[verified]` P1「訓練迴圈」→加英文：L13「訓練迴圈（training loop）」。
- `[verified]` P1「梯度消失／梯度爆炸」（kept；稽核 miss #12，f2 修）：L14「找出梯度消失（vanishing gradient）或梯度爆炸（exploding gradient）」。
- `[verified]` P2「差一的錯誤」→「差一錯誤（off-by-one error）」：L19。
- `[verified]` P2「掛進一個 PyTorch 模型」→「掛接到」：L221「掛接到 PyTorch 模型」。

## phases/04-computer-vision/01-image-fundamentals（1 條：verified 1）

- `[verified]` P2「決定性的合成影像」→「可重現的合成影像」：L207「先用一張可重現的合成影像」。

## phases/04-computer-vision/02-convolutions-from-scratch（2 條：verified 1 / not-fixed 1）

- 狀態：f4 日誌無此課紀錄；檔案 17:34 後未再寫入，判為穩定，已判定。
- `[verified]` P1「核大小」→加英文：L13「核大小（kernel size）」。
- `[not-fixed]` P2「手設核」→「手動設計的卷積核」：L14 已改為「手動設計的卷積核」；但 L241「### 步驟 3：用手設的核驗證」、L320「### 步驟 6：一組手設的核」仍為「手設」。

## phases/04-computer-vision/03-cnns-lenet-to-resnet（5 條：verified 1 / kept-ok 3 / not-fixed 1）

- `[kept-ok]` P1 Mermaid timeline 節點英文（kept；稽核 borderline #13）：L29–33 仍為英文。依任務規定，Mermaid timeline 英文不計問題，且稽核指出檢查器不剝離 timeline 標籤。
- `[kept-ok]` P2「坐在縮放曲線上」（kept；稽核 borderline #14）：L21「知道每一族的縮放曲線，你才知道該坐在曲線的哪裡」，語意可懂。
- `[kept-ok]` P2 區塊重用句 run-on（kept；稽核 borderline #15）：L75「簡單，一種區塊類型重複使用，使它成為後面一切的參考點」，資訊完整，與英文 fragment 對應。
- `[verified]` P2「殘差連接買到 12 倍的參數效率」→「讓參數效率提高 12 倍」：L350「殘差連接讓參數效率提高 12 倍」。
- `[not-fixed]` P2「ImageNet 已經付過代價的表示」→「繼承 ImageNet 預訓練所學到的表示」：L360 現為「你現在有一個 10 類別的 CIFAR 分類器，繼承了 繼承 ImageNet 預訓練所學到的表示」——疊詞（修錯）。

## phases/04-computer-vision/04-image-classification（4 條：verified 1 / kept-ok 3）

- `[verified]` P0「列／行」（confusion matrix）→列／欄：L108「第 i 列第 j 欄是真實類別 i 被預測成類別 j 的次數」；L368「列是真實類別，欄是預測」，與 en「Rows are true classes, columns are predictions」一致。
- `[kept-ok]` P2「轉移」（kept；稽核 ok #16）：L19「是這整個階段能搬到其他任務的技能」，原文 "transfers" 非遷移學習。
- `[kept-ok]` P2「90 比 10」（kept；稽核 ok #17）：後句已點出多數類。
- `[kept-ok]` P2「準確率外洩」（kept；稽核 ok #18）：稽核判意譯與 accuracy leak 一致。

## phases/04-computer-vision/05-transfer-learning（clean）

- 報告為 clean，無 f2–f4 編輯；模式掃描無命中。`[kept-ok]`（無 finding）。

## phases/04-computer-vision/06-object-detection-yolo（3 條：verified 3）

- `[verified]` P1 IoU 首見（kept；稽核 miss #19，f2 修）：L13「計算框與框之間的交並比（intersection over union，IoU）」；L86「### 交並比（IoU）」。
- `[verified]` P2「該轉哪顆旋鈕」→「該調整哪個參數」：L15「並決定下一步該調整哪個參數」。
- `[verified]` P2「一個便宜的代理」→「成本低的近似指標」：L282。

## phases/04-computer-vision/07-semantic-segmentation-unet（2 條：verified 2）

- `[verified]` P1 IoU 首見（kept；稽核 miss #20，f2 修）：L15「交並比（intersection over union，IoU）」。
- `[verified]` P2「巨觀平均 Dice」（kept；稽核 miss #21，f2 修）：L259「這是宏平均（macro-average）Dice」，與 04/05 的「宏平均」一致。

## phases/04-computer-vision/08-instance-segmentation-mask-rcnn（2 條：verified 1 / kept-ok 1）

- `[verified]` P1 IoU 首見：L77「交並比（intersection over union，IoU）」。格式：L77「用 交並比（…） 0.7」與 L266、L279、L290 的「mAP@交並比（…）」含多餘半形空格或嵌入式寫法，見 N5。
- `[kept-ok]` P2「成本是處處都少十分之幾個 mAP 點」（kept；稽核 borderline #22）：L23「這裡弄錯，到處都會掉十分之幾個 mAP」，語意正確，偏口語。

## phases/04-computer-vision/09-image-generation-gans（4 條：verified 4）

- `[verified]` P1 GAN 標題（kept；稽核 miss #23，f2 修）：L1「# 影像生成（image generation）：生成對抗網路（GAN）」。
- `[verified]` P1「譜範數」→「譜正規化（spectral normalization）」：L14、L253、L272、L306 統一，且 E4 重複括註已去除（L14 只剩一個英文括註）。
- `[verified]` P1 minimax 首見（kept；稽核 miss #24，f2 修）：L12「極小極大（minimax）賽局」。
- `[verified]` P2「難的是走到那裡」→「要達到這點並不容易」：L54。
- 附帶：f2 E5「抽樣→取樣」於 239、251、294 已改，全課無生成語境「抽樣」殘留。

## phases/04-computer-vision/10-image-generation-diffusion（3 條：verified 3）

- `[verified]` P2「閉式的一步跳」→「閉式解的一步更新」：L37「### 閉式解的一步更新」。
- `[verified]` P2「訊號對雜訊比」→「訊噪比（signal-to-noise ratio）」：L304。
- `[verified]` P2「確定的 ODE」→「確定性 ODE」：L322「把取樣改寫成確定性 ODE」。
- 附帶：f2 E5 的 15 處「抽樣→取樣」已改，全課無「抽樣」殘留。

## phases/04-computer-vision/11-stable-diffusion（5 條：verified 3 / not-fixed 1 / kept-ok 1）

- `[verified]` P1 VAE 首見（kept；稽核 miss #25，f2 修）：L3「預訓練變分自編碼器（variational autoencoder，VAE）」。
- `[verified]` P2「由 CFG 引導」（kept；稽核 miss #26，f2 修）：L3「以快速的確定性 ODE 求解器取樣，並以無分類器引導（classifier-free guidance）控制生成方向」。
- `[verified]` P2「從潛在表示來注意」（kept；稽核 miss #27，f2 修）：L50「讓潛在表示去關注文字 embedding」。
- `[not-fixed]` P2「散布」→「分散式」：L96 現為「幾乎每個社群 fine-tune 都用 LoRA 分散式。」，英文為 "LoRA is how almost every community fine-tune is distributed"（以 LoRA 形式發布）。語意誤譯（修錯）。
- `[kept-ok]` P2「嚴格的授權要求」（kept；稽核 borderline #28）：L236「要目前最好、授權又嚴格，用 SD3 或 FLUX」，主詞略模糊，稽核判可保留。

## phases/04-computer-vision/12-video-understanding（3 條：verified 3）

- `[verified]` P1「膨脹」首見→「膨脹（inflation）」：L14。
- `[verified]` P2「把它們接起來的物理」→「連結這些影格的物理規律」：L3。
- `[verified]` P2「成本和準確率怎麼換」（kept；稽核 miss #29，f2 修）：L12「並預估它們在成本與準確率（accuracy）之間的取捨」。
- 附帶：L272 表格「把 2D 權重抬成 3D」與 04/26 已改的用語不一致，見 N9。

## phases/04-computer-vision/13-3d-vision-nerf（2 條：kept-ok 1 / verified 1）

- `[kept-ok]` P2「被擋在成長最快的區塊之外」（kept；稽核 borderline #30）：L21「會進不去這個領域成長最快的那一塊」，稽核判可保留。
- `[verified]` P2「點雲是感測器白送的」→「感測器可直接提供點雲」：L23。

## phases/04-computer-vision/14-vision-transformers（3 條：verified 3）

- `[verified]` P1 patch／positional embedding／class token 首見英文：L12「patch embedding（小塊 embedding）、positional embedding（位置 embedding）、class token（類別 token）」。附帶 spacing 問題見 N6。
- `[verified]` P2「沒有人以為這能換掉」→「當時沒有人認為這些歸納偏誤能被取代」：L19。
- `[verified]` P2「倒轉的瓶頸」→「倒置瓶頸（inverted bottleneck）」：L118。

## phases/04-computer-vision/15-real-time-edge（10 條：verified 8 / not-fixed 2）

- 狀態：f4 日誌僅 L12（D3，「參數與延遲之間的取捨」）有紀錄；L60、L267 無紀錄，仍為快照現況。檔案 20:18:31 後快照不變。
- `[verified]` P1 推論延遲、峰值記憶體、吞吐量首見（kept；稽核 miss #31，f2 修）：L12「推論延遲（inference latency）、峰值記憶體（peak memory）和吞吐量（throughput）」。
- `[verified]` P1「推論執行環境」首見→「推論執行環境（inference runtime）」：L21、L81。
- `[verified]` P1「量化感知訓練（QAT）」→全名：L72「量化感知訓練（quantisation-aware training, QAT）」。
- `[verified]` P1「剪枝」「蒸餾」首見英文：L76、L78「剪枝（pruning）」、L79「知識蒸餾（knowledge distillation）」。
- `[verified]` P2「裝置看過的最大值」→「裝置曾使用的最高記憶體量」：L45。
- `[verified]` P2「邊緣剖析」→「每個邊緣裝置的效能剖析都該守三條」：L52。
- `[not-fixed]` P2「延遲代理。比較架構有用，拿來當實際花掉的時間就會誤導」→ 改寫：L60 現為「FLOPs（每次推論的浮點運算數）是便宜、跟裝置無關的是粗略的延遲代理指標；適合比較架構，但不能當成實際執行時間」——「是…是…」雙重系詞，句子錯亂（修錯）。
- `[verified]` P2「每個參數的準確率最好」→「參數效率最佳」：L98–99。
- `[not-fixed]` P2「模型縮小掉掉的準確率」：L79 已改為「模型縮小後損失的準確率」；但 L267 表格「掉掉的準確率大部分補得回來」仍有「掉掉」疊字。
- `[verified]` P2「給獨立的命令列數字」（kept；稽核 miss #32，f2 修）：L241「可直接從命令列取得獨立的基準數字」。

## phases/04-computer-vision/16-vision-pipeline-capstone（8 條：verified 5 / kept-ok 2 / not-fixed 1）

- `[verified]` P1「偵測器／分類器／前處理」首見英文：L13「偵測器（detector，Mask R-CNN 或 YOLO）、分類器（classifier，ConvNeXt-Tiny）」；L14「前處理（preprocessing）」；Mermaid L31–34 已改中文節點。
- `[kept-ok]` P1 Mermaid「error」（kept；稽核 ok #33）：L39「REQ -.->|error| RESP」為連線標籤，STYLE 規定連線維持不變。
- `[verified]` P1「吞吐量」首見英文：L92「吞吐量（throughput）」（首見位置已改為 L92）。
- `[kept-ok]` P2「用資料契約縫在一起」（kept；稽核 ok #34）：L3「用資料契約（data contract）縫在一起」。
- `[verified]` P2「都可能安靜失敗」→「都可能在沒有明顯錯誤訊息的情況下失敗」：L21。附帶「安靜」用語見 N3。
- `[verified]` P2「bug 住在另外五個階段」→「問題通常出在另外五個階段」：L46。
- `[not-fixed]` P2「正式環境的樣板會收到同一種結構，再加」→ 改寫：L313 現為「正式環境的範本大致採用相同架構，另外還會加入：：」——重複冒號（修錯）。
- `[verified]` P2「吞吐量會乘上去」（kept；稽核 miss #35，f2 修）：L92「會成倍提升吞吐量（throughput）」。

## phases/04-computer-vision/17-self-supervised-vision（6 條：verified 6）

- `[verified]` P1「對比、老師與學生、遮罩重建、遮罩比例」首見英文（kept；稽核 miss #36，f2 修）：L12「對比式學習（contrastive learning，SimCLR）、老師與學生（teacher-student，DINO）、遮罩重建（masked reconstruction，MAE）」；L14「MAE 的 75% 遮罩比例（mask ratio）」。
- `[verified]` P2「說出各自在拉什麼目標」→「說明各方法分別最佳化什麼目標」：L12。
- `[verified]` P2「三個主要的自監督家族」→「三種主要的自監督方法」：L12。
- `[verified]` P2「損失在說：……」（kept；稽核 miss #37，f2 修）：L42「損失函數會拉近這兩個 embedding，並讓它遠離批次中其他影像的 embedding」。
- `[verified]` P2「變尖」→「銳化」：L66「也會銳化（除以很小的溫度）」。
- `[verified]` P2「編碼器只看得到的 25%」→「編碼器只處理可見的 25% 小塊」：L72。

## phases/04-computer-vision/18-open-vocab-clip（6 條：verified 5 / not-fixed 1）

- `[verified]` P1「影像編碼器、文字編碼器、雙塔、對比訓練、零樣本、餘弦相似度」首見英文（kept；稽核 miss #38，f2 修）：L3「影像編碼器（image encoder）」「文字編碼器（text encoder）」；L12「雙塔（two-tower）架構」「對比訓練（contrastive training）」；L13「零樣本（zero-shot）分類」；L14「餘弦相似度（cosine similarity）」。
- `[verified]` P2「對得上的（影像、說明文字）配對……」→改寫：L3「讓相符的影像與說明文字配對，在共享空間中落在同一點。訣竅就在於此。」「讓讓」疊字已修。
- `[verified]` P2「SAM 經由 CLIP 吃文字 prompt」→「SAM 透過 CLIP 接收文字 prompt」：L85。
- `[verified]` P2「每個視覺加語言的任務」→「每種結合視覺與語言的任務」：L89。
- `[verified]` P2「碰不到標籤」→「不需使用標籤」：L214。
- `[not-fixed]` P2「共通詞彙」→「到 2026 年仍是此領域的代表性模型」：L217 現為「2021 年 OpenAI 的模型。到 2026 年仍是這個領域的到 2026 年仍是此領域的代表性模型。」——疊句（修錯）。

## phases/04-computer-vision/19-ocr-document-understanding（8 條：verified 5 / not-fixed 3）

- `[not-fixed]` P1「連線時序分類」→「連結主義時序分類（Connectionist Temporal Classification，CTC）」：L13 現為「實作 CTC（連結主義時序分類（Connectionist Temporal Classification，CTC），Connectionist Temporal Classification）損失（loss）」——括註巢狀且英文重複（修錯）。
- `[verified]` P1「字元錯誤率，CER」「詞錯誤率，WER」（kept；稽核 miss #39，f2 修）：L80「字元錯誤率（character error rate，CER）」；L81「詞錯誤率（word error rate，WER）」。
- `[not-fixed]` P1「束搜尋」→「集束搜尋（beam search）」：L128 現為「貪心解碼器比集束搜尋（beam search）（beam search）簡單」——重複括註（修錯）。統一譯名已達成（L240、L245）；同課重複附英文屬風格偏差，低優先。
- `[verified]` P1「鍵值抽取」「編輯距離」首見英文（kept；稽核 miss #40，f2 修）：L76「鍵值抽取（key-value extraction）」；L83「JSON 上的編輯距離（edit distance）」。
- `[verified]` P0「把所有……的對齊加總」（kept；稽核 miss #41，f2 修）：L54「把所有「合併重複、拿掉空白之後會變成目標文字」的對齊機率加總，也就是邊緣化（marginalization）」。與 en「marginalises over all alignments that reduce to the target text」相符。
- `[verified]` P2「拉丁文字很直接，混排就不直接」→改寫：L257「拉丁文字的閱讀順序較簡單，混合版面則複雜得多」。
- `[verified]` P2「同一件事，改在詞的層級」→「計算方式相同，但以詞為單位」：L81。
- `[not-fixed]` P2「古典 OCR」「古典做法」→「傳統」：L12「傳統 OCR 管線」與 L254「傳統 OCR 模型」已改；但 L27「每一層都有古典做法和現代做法」、L31「### 古典管線」、L68「古典的 DB 加 CRNN 管線」、L222「古典的。」仍為「古典」，未依 r2 建議全篇統一。

## phases/04-computer-vision/20-image-retrieval-metric（9 條：verified 8 / not-fixed 1）

- 狀態：f4 在 L48 有 D2 紀錄（表格「對比」未改，標 [存疑]）；檔案 20:45:25 仍在變動。以下為 20:46 快照判定。
- `[verified]` P1「三元組、對比、以 proxy 為基礎」首見英文（kept；稽核 miss #42，f2 修）：L12「三元組（triplet）、對比（contrastive）、以及以 proxy 為基礎（proxy-based）的度量學習損失」。
- `[verified]` P1「乘積量化」首見英文：L94「乘積量化（product quantisation）」。
- `[verified]` P1「實例級／類別級」首見英文（kept；稽核 miss #43，f2 修）：L19「電商的實例級（instance-level）比對」；L96「實例級對類別級（category-level）檢索」；L100「類別級（category-level）」。
- `[not-fixed]` P1「ImageNet 標籤當標準結果」→「以 ImageNet 標籤作為真實標籤」：L231 現為「再用留出切分、以 以 ImageNet 標籤作為真實標籤」——「以 以」疊字（修錯）。
- `[verified]` P2「給這張查詢影像，把我的目錄排出來」→「依這張查詢影像，為我的商品目錄排序」：L19。
- `[verified]` P2「兩個設計決定整套系統」→改寫：L21「整套系統由兩項設計決定：由哪個模型產生 embedding，以及如何透過索引大規模尋找最近鄰」。
- `[verified]` P2「它不大，但槓桿很高」→「這項技術範圍不大，卻能帶來很大的效益」：L23。
- `[verified]` P2「margin 可以直接控」→「可直接控制 margin」：L49。
- `[verified]` P2「FAISS 平面索引」→「FAISS 精確平坦索引（IndexFlat）」：L231（同行的「以 以」見上一條）。
- 附帶（f4 存疑，未處理）：L48 表格「**對比**」——GLOSSARY 中 contrastive loss＝對比損失，而該欄為損失家族。見 N1。

## phases/04-computer-vision/21-keypoint-pose（9 條：verified 8 / not-fixed 1）

- 狀態：f4 日誌僅 L80（D1，補「交並比（IoU）」）；L76 無紀錄，仍為快照現況。檔案 20:18:31 後快照不變。
- `[verified]` P1 關鍵點術語首見英文（kept；稽核 miss #44，f2 修）：L3「熱圖迴歸器（heatmap regressor）」；L12「由上而下（top-down）和由下而上（bottom-up）」；L61「次像素定位（sub-pixel localization）」；L80「正確關鍵點百分比（Percentage of Correct Keypoints，PCK）」「物件關鍵點相似度（Object Keypoint Similarity，OKS）」，以及 f4 補的「關鍵點版的交並比（IoU）」。
- `[verified]` P1「拿標準結果」→「取得真實標註資料」：L88「多視角架設（CMU Panoptic）取得真實標註資料」。
- `[verified]` P2「其餘都是細節」→「其餘都是資料整理」：L3。
- `[verified]` P2「每一個結構都一樣」→「每種任務遵循相同的結構」：L19。
- `[not-fixed]` P2「漂亮，而且能放大」→「方法簡潔，而且可擴展到任意人數，不用依人裁切」：L76 現為「方法簡潔，而且可擴展到任意人數到任意人數，不用依人裁切」——疊詞（修錯）。
- `[verified]` P2「正式環境的品質已經解掉」→「2D 姿態估計已達正式環境可用的品質」：L84。
- `[verified]` P2「把 2D 預測抬到 3D」→「將 2D 預測提升為 3D 姿態」：L86「用一個小 MLP 將 2D 預測提升為 3D 姿態（VideoPose3D）」。
- `[verified]` P2「關鍵點頭」→「關鍵點預測頭」：L112「### 步驟 2：很小的關鍵點預測頭」。
- `[verified]` P2「小到一個小模型一分鐘就學得會」→「簡單到小型模型約一分鐘就能學會」：L175。

## phases/04-computer-vision/22-3d-gaussian-splatting（7 條：verified 5 / kept-wrong 1 / not-fixed 1）

- `[not-fixed]` P1「3x3 的共變異數」→「3×3 共變異數矩陣（covariance matrix）」：L39 現為「3×3 共變異數矩陣（covariance matrix）（covariance）」——重複括註（修錯）。
- `[verified]` P1「給一張標準結果影像」→「給定一張真實影像」：L90。
- `[kept-wrong]` P1「位置、旋轉、尺度、不透明度」首見英文（kept；稽核 borderline #45）：L13 仍無英文（position／scale／opacity），但同一列 quaternion、spherical harmonics、feature 已附英文，標註不一致。稽核建議補齊。低優先。
- `[verified]` P2「數學裡活動的部分夠多」→「數學涉及的細節很多」：L23。
- `[verified]` P2「世界座標在 mu、3D 共變異數是 Sigma 的高斯」→改寫：L62「具有世界座標位置 `mu` 和 3D 共變異數 `Sigma` 的高斯」。
- `[verified]` P2「用來做體積影片」→「用於體積式影片」：L119。
- `[verified]` P2「64 個高斯落進那兩個形狀」→「64 個高斯逐漸排列成那兩個形狀」：L264。

## phases/04-computer-vision/23-diffusion-transformers-rectified-flow（8 條：verified 7 / not-fixed 1）

- `[verified]` P1「抽樣／抽樣器」→「取樣／取樣器」（f2 E5 全課）：全課已無生成語境「抽樣」，見 L89、L246。殘留「抽出來的輸出」（L285）與「抽出的樣本」（L332）見 N4。
- `[verified]` P1「雜訊排程」「速度」首見英文（kept；稽核 miss #46，f2 修）：L3「雜訊排程（noise schedule）」；L66「速度（velocity）」。
- `[verified]` P2「一段話講完整流流」→「用一段話說明整流流」：L56。
- `[verified]` P2「一條愈來愈吵的 SDE」→「雜訊逐漸增強的 SDE」：L58。
- `[verified]` P2「prompt 更準」→「更能準確遵循 prompt」：L23。
- `[verified]` P2「更緊地跟著 prompt」→「預設就更能遵循 prompt」：L89「整流流模型預設就更能遵循 prompt」（f2 疊字已修）。
- `[not-fixed]` P2「目前品質的尖端是」→「目前品質表現領先的是 FLUX.2 和 SD4」：L115 現為「目前品質表現領先的是 FLUX.2 和 SD4 FLUX.2 和 SD4。」——重複片語（修錯）。
- `[verified]` P2「`diffusers` 用同一套 API 把每一個都提供了」→「以統一的 API 支援這些模型」：L289。

## phases/04-computer-vision/24-sam3-open-vocab-segmentation（7 條：verified 6 / not-fixed 1）

- `[verified]` P1「文字和影像的對齊」→「文字與影像定位（text-image grounding）」：L23。
- `[verified]` P1「消融」→「元件移除實驗」：L82「要對偵測器元件做研究或元件移除實驗」。
- `[verified]` P1「一次前向」→「一次前向傳遞（forward pass）」：L3、L21。
- `[not-fixed]` P2「可下 prompt」→「可接受 prompt 的」或「可提示的」：f2 改為「可接受 prompt 的」後，L12、L21、L23、L52、L281 出現「可接受 prompt 的 的」（「的 的」疊字，修錯）。
- `[verified]` P2「存在頭」→「概念存在性預測頭」：L65、L283。
- `[verified]` P2「模型吃進去什麼」→「模型接收什麼」：L115。
- `[verified]` P2「回應本體保持小」→「讓回應資料保持精簡」：L165「RLE 仍讓回應資料保持精簡」（f2 疊字「仍讓讓」已修）。

## phases/04-computer-vision/25-vision-language-models（7 條：verified 6 / not-fixed 1）

- `[not-fixed]` P1「GUI 代理／視覺代理／代理能力」→「GUI agent／visual agent／agentic 能力」：L71 已改為「GUI agent」；但 L80「### 視覺代理」、L82「**視覺代理（visual agent）**的基準，代理操作圖形介面」、L84「### 代理能力加 RoPE 變體」、L275 表格「視覺代理」仍用中文「代理」。GLOSSARY 規定 agent 在 AI agent 語境保留英文。
- `[verified]` P1「T-RoPE（時間的旋轉位置 embedding）」→「T-RoPE（temporal Rotary Position Embedding）」：L86。
- `[verified]` P2「換任何一塊都是機械式的」→「替換任何一個元件都很直接」：L23。
- `[verified]` P2「可訓練的訊號只有幾十億參數」→「只需訓練投影器中數十億個參數，成本就相對低」：L51。註：句末「成本就相對低，代價很低」語意重複，屬小問題。
- `[verified]` P2「把常見桌面工作的迴圈閉起來」→「完成常見桌面工作的操作流程」：L82。
- `[verified]` P2「描述沒有完全落在影像上」→「描述內容沒有完全以影像為根據」：L90。
- `[verified]` P2「哪個物件在哪個上面」→「哪個物件位於另一個物件上方」：L106。

## phases/04-computer-vision/26-monocular-depth（9 條：verified 7 / not-fixed 2）

- `[verified]` P1「標準結果」→「真實深度值／真值」：L3「誤差可以落到和真實深度值差幾個百分點以內」；L134「先把預測對到真實深度值」；L250「預測落在真實深度值 25% 以內的像素比例」。
- `[not-fixed]` P1「閾值準度」「Delta 準度」→「閾值準確率」「Delta 準確率」：L100「閾值準確率」已改；但 L250 表格仍為「Delta 準度」，L261「把深度準度抬起來的編碼器家族」仍用「準度」（GLOSSARY accuracy＝準確率）。
- `[verified]` P1「飛時」→「飛時測距（time-of-flight）」：L19。
- `[verified]` P1「針孔相機」首見英文：L15「用深度圖和針孔相機（pinhole camera）」。
- `[verified]` P2「距離的比例沒有錨在公尺上」→「但距離比值沒有對應到實際公尺尺度」：L29（f2 疊字「但但」已修）。
- `[verified]` P2「大小恆常」→「大小恆常性」：L57。
- `[verified]` P2「看起來更霧、更藍」→「看起來更朦朧、偏藍」：L58。
- `[verified]` P2「真的沒有紋理，或會反光的表面」→「缺乏紋理或具有反光特性的表面」：L66。
- `[not-fixed]` P2「把……抬成／抬到 3D」→依句型改為「映射至 3D」「轉換為 3D 點雲」：「抬」仍保留於 L15「把 2D 偵測抬成 3D 點」、L23「把 2D 物件抬成 3D 點雲」、L84「抬到相機座標裡的 3D 點」、L152「把深度抬成點雲」、L239「抬成點雲」、L251「把 (u, v, d) 抬到 (X, Y, Z)」。

## phases/04-computer-vision/27-multi-object-tracking（6 條：verified 5 / not-fixed 1）

- `[not-fixed]` P1「多物件追蹤準度／偵測準度／標準結果」→「準確率」「真實標註」：L95「MOTA（多物件追蹤準確率…）」、L97「偵測準確率（DetA）和關聯準確率（AssA）」已改；但 L97「HOTA（高階追蹤準度，…）」仍為「準度」（GLOSSARY accuracy＝準確率）；L96、L244、L267、L273 仍有「標準結果」（ground truth），未改為真實標註。
- `[verified]` P1「ID 精度和召回」→「ID 精確率和召回率」：L96。
- `[verified]` P1「以偵測為基礎的追蹤、以查詢為基礎的追蹤、匈牙利指派」首見英文（kept；稽核 miss #47，f2 修）：L12「以偵測為基礎的追蹤（tracking-by-detection）」「以查詢為基礎的追蹤（query-based tracking）」；L13「匈牙利指派（Hungarian assignment）」。
- `[verified]` P1「共變異」→「共變異數（covariance）」：L58「帶共變異數（covariance）」。
- `[verified]` P2「面對影片的產品」→「所有以影片為核心的產品」：L21。
- `[verified]` P2「吃每一影格的偵測」→「接收每一影格的偵測結果」：L191。

## phases/04-computer-vision/28-world-models-video-diffusion（11 條：verified 10 / not-fixed 1）

- `[verified]` P1「代理式推理」→「agentic 推理」：L23。
- `[verified]` P1「旋轉位置 embedding（RoPE）」→「Rotary Position Embedding（RoPE）」：L159。
- `[verified]` P1「潛在動作、分開的注意力」首見英文（kept；稽核 miss #48，f2 修）：L35「潛在動作（latent action）的影片 DiT」；L49「從觀察到的影片推論潛在動作（latent action）」；L64「分開（divided attention）」；L188「分開的注意力（divided attention）區塊」。
- `[verified]` P1「從新的先驗抽一個」→「從新的先驗取樣」：L71。
- `[not-fixed]` P2「悄悄接手機器人的模擬到真實」→「正逐漸成為機器人模擬轉實體部署的主流」：L21 現為「世界模型這個典範，正在正逐漸成為機器人模擬轉實體部署的主流」——疊詞（修錯）。
- `[verified]` P2「生成到一半，你不能轉它」（kept；稽核 miss #49，f2 修）：L48「生成過程中無法引導它」；L73「生成過程中沒有東西能引導它」。
- `[verified]` P2「再用以後影格的預測條件」→「再以這些動作為條件預測未來影格」：L49。
- `[verified]` P2「角落案例」→「特殊情境」：L90。
- `[verified]` P2「無限的 3D 展開」→「無限延續的 3D 模擬」：L115。
- `[verified]` P2「機器人在外面實際在用的堆疊」→「實際部署中的機器人堆疊」：L262。
- `[verified]` P2「想像出來的展開」→「想像中的未來演進序列」：L265。

## phases/06-speech-and-audio/01-audio-fundamentals（9 條：verified 8 / not-fixed 1）

- `[verified]` P1 K001「頻率箱／箱」→「頻率槽」（kept；f3 K001 修）：L43「每個頻率槽（frequency bin）一個」；L93「峰應該在頻率槽」；L119「確認預期的頻率槽上有三個峰」；L134「鏡射到較低的頻率槽」。
- `[verified]` P1 K002「降取樣」→「降採樣（downsampling）」（kept；f3 K002 修）：L39「降採樣（downsampling）之前一定要先低通濾波」。
- `[verified]` P1「視窗函數／Hann 視窗／hop」→「窗函數（window）」「Hann 窗」「跳躍長度（hop size）」：L47「每一框乘上窗函數（window）」「跳躍長度（hop size）」；L121「跳躍長度（hop size） 160、Hann 窗」。
- `[verified]` P1 K003 首見英文（kept；f3 K003 修）：L3「原始訊號（signal）」；L12「張量（tensor）」；L16「取樣率（sample rate）」；L17「混疊（aliasing）」；L32「奈奎斯特（Nyquist）」；L41「位元深度（bit depth）」。註：L39「奈奎斯特頻率」的英文括註被 f4 E2 去重（Nyquist 已於 L32 首見），可接受。
- `[verified]` P2「第一階是懂取樣和傅立葉」→「第一階是先搞懂取樣與傅立葉轉換」：L3。
- `[verified]` P2「會出安靜的 bug」→「會產生不易察覺的 bug」：L12。
- `[not-fixed]` P2「可以沒有歧義地表示到／露出來的是／真的音訊用不上」→「可明確表示至／回傳的是／實際音訊則不適用」：L39「可明確表示至 sr/2」已改；但 L41「讀的是 int16，露出來的是 `[-1, 1]` 的 float32 陣列」仍未改；L89「真的音訊用不上」仍未改。
- `[verified]` P2 K004「幅度」→「模（magnitude）」：L43「模（magnitude）是那個頻率的振幅」；L121「畫振幅頻譜」。
- `[verified]` P2「示範沒有額外依賴」→「示範不需安裝額外套件」：L57。

## phases/06-speech-and-audio/02-spectrograms-mel-features（10 條：verified 5 / not-fixed 5）

- 狀態：f2/f3/f4 日誌均無此課紀錄，檔案 mtime 未在修復期間變動；r3 標示的多數 [已修復] 在現況未落實。
- `[not-fixed]` P1 Mel 尺度／mel 頻譜圖／mel 箱 → 梅爾刻度（mel scale）、梅爾頻譜圖（mel-spectrogram）、梅爾頻率槽：標題 L1 已改「梅爾刻度」，但首見（L1 與 L16「梅爾頻譜圖再推一步」「梅爾刻度把頻率軸扭到對上這個」）皆無英文；L16 仍有「mel 尺度的頻譜圖」，L98「80 個 mel」，L126–131 表格「對數 mel」；L26「80 個 梅爾頻率槽」。
- `[not-fixed]` P1「視窗函數（window）／Hann 視窗／hop」→「跳躍長度（hop size）」：L22「典型是 25 毫秒視窗、10 毫秒 hop」；L128–130 表格「10 毫秒 hop」仍未譯。L52「### 步驟 2：Hann 窗」已改。
- `[not-fixed]` P1「STFT（短時傅立葉轉換）」「啁啾」→「啁啾訊號（chirp）」：L22「短時傅立葉轉換（Short-Time Fourier Transform，STFT）」已改；L151「它合成一段啁啾（頻率從 200 掃到 4000 Hz）」無「訊號（chirp）」英文（GLOSSARY chirp＝啁啾訊號）。
- `[verified]` P1「ASR 準度／top-1 準度」→「準確率」：L153「比較 ASR 準確率」「回報 top-1 準確率」，與 en "ASR accuracy" 一致。
- `[verified]` P2「說話人辨識」→「語者辨識」：L32「語者辨識（x-vector、ECAPA）仍在用」。
- `[not-fixed]` P2「頻譜圖解決這個」等數處：L14「頻譜圖解決了這個問題」已改；L16「梅爾刻度把頻率軸扭到對上這個」未改；L139「安靜地失敗」未改（建議「靜默失敗」）；L142「正規化漂掉」未改（建議「飄移」）；L32「特徵去掉相關」未改。
- `[verified]` P2「2026 年仍然會交付出去的坑」→「2026 年仍會隨產品上線的陷阱」：L137。
- `[verified]` P2「用來做細的時間控制」→「用來精細控制時間」：L129。
- `[not-fixed]` P2「關鍵詞偵測」→「關鍵字偵測（keyword spotting）」：L133 已改為「關鍵字偵測」，但首見未附英文（minor）。
- `[verified]` P2「Mel 數量不合」→「數量不一致」：L139「數量不一致。」。

## phases/06-speech-and-audio/03-audio-classification（6 條：verified 4 / not-fixed 2）

- `[verified]` P1「每一類的召回、top-1／top-5 準度、準度 80% 以上、交叉驗證準度」→「召回率」「準確率」：L3「每一類的召回率」；L40「top-1 準確率」；L120「準確率 80% 以上」。
- `[verified]` P1「平均精度均值（mAP）」→「平均精確率均值（mAP）」：L41、L175。
- `[verified]` P1 K005 首見英文（kept；f3 K005 修）：L30「### 真正的挑戰是類別不平衡（class imbalance）」；L20「餘弦相似度（cosine similarity）」；L24「監督式學習（supervised learning）」；L34「平衡抽樣（balanced sampling）」；L161「混淆矩陣（confusion matrix）」；L163「5 折交叉驗證（cross-validation）準確率」。
- `[not-fixed]` P2「領域偏移很強（乾淨對上吵）」「和一座標過的庫算……回前 K 名的多數決」→改寫：L14「領域偏移明顯（乾淨音訊與雜訊音訊）」已改；但 L20 仍為「和一座標過的庫算餘弦相似度（cosine similarity），回前 K 名的多數決」，直譯語句未改。
- `[not-fixed]` P2「晚到 2017 年」→「直到 2017 年，這種方法在 ESC-50 上仍勝過當時最佳的神經網路基準」：L81 現為「直到 2017 年，這種方法在 ESC-50 上仍勝過當時最佳的神經網路基準，這還打贏 ESC-50 上當時最好的神經網路基準。」——句尾殘留重複子句（修錯）。
- `[verified]` P2「fine-tuning BEATs 的頭，幾小時就拿到目前最好的 95%」→改寫：L153「只要 fine-tune BEATs 的分類頭，幾小時內就能達到 SOTA 表現的 95%」。

## phases/06-speech-and-audio/04-speech-recognition-asr（4 條：verified 2 / not-fixed 2）

- `[verified]` P1「束搜索」→「集束搜尋（beam search）」（kept；稽核 K006）：L28「用集束搜尋（beam search）或淺層融合」；全篇統一為「集束搜尋」。
- `[verified]` P1 K007 首見英文（kept；f3 K007 修）：L12「音框（frame）和字元不是一對一」；L18「注意力編碼器–解碼器（attention encoder–decoder）」；L28「條件獨立假設（conditional independence assumption）」；L153「字元、詞、子詞（subword）的 WER」。
- `[not-fixed]` P2「序列模型黏起來」「你要一個字串」「三種表述解這個」→改寫：L3 現為「每個時間步都在做音訊分類，再用一個懂英文、也懂靜音的再用了解英文與靜音的序列模型把它們串起來」——錯亂句（修錯）；L12「你要一個字串」與 L14「三種表述解這個」均未改。
- `[not-fixed]` P2「在靜音上跑 Whisper 會幻覺」「用 VAD 當閘」：L152「讓 Whisper 處理靜音會產生幻覺」已改；但「一定要用 VAD 當閘」未依建議改為「一律先用 VAD 篩掉靜音」。

## phases/06-speech-and-audio/05-whisper-architecture-finetuning（6 條：verified 3 / not-fixed 2 / kept-ok 1；另有子項 kept-wrong 1）

- `[verified]` P1「卷積降取樣」→「卷積降採樣」：L26「卷積降採樣（步幅 2）」。
- `[verified]` P1 K008 首見英文（kept；f3 K008 修）：L3「弱監督（weakly supervised）音訊」「30 秒視窗（window）」；L14「領域偏移（domain shift）」；L41「時間戳（timestamp）」；L45「較短的要填充（padding）」。
- `[not-fixed]` P2「第一個當成商品交付的 ASR」「領域偏移會把它打垮」：L12「第一個能像一般商品般使用的 ASR 模型」已改；L14 仍為「領域偏移（domain shift）會把它打垮」，未依建議改寫。
- `[not-fixed]` P2「一切都釘在 30 秒」「VAD 閘／用 VAD 當閘」：L45「輸入長度固定為 30 秒」已改；但 L158「呼叫之前一定用 VAD 當閘」、L160「或用 VAD 當閘」未改。
- `[kept-ok]` P2「一行，2026 年最強的通用 ASR」（kept；稽核 K009）：現況無此句（來源已失效，稽核確認），不列。
- `[verified]` P2「低秩轉接器」→「低秩適配器（low-rank adapter）」：L182。
- 子項 `[kept-wrong]`（低）：L26「80 個 mel，10 毫秒 hop」與 L47「**對數 mel 正規化。**」的「對數 mel」首見未附英文；r3 kept 原列「對數 mel 正規化」，稽核未逐條列 miss。低優先。

## phases/06-speech-and-audio/06-speaker-recognition-verification（3 條：verified 2 / not-fixed 1）

- `[verified]` P1 K010 首見英文（kept；f3 K010 修）：L12「未知的語者（*開放集合（open-set）*）」；L14「通道偏移（channel shift，電話對上筆電）」「角度邊界（angular margin）」；L16「決策閾值（threshold）」；L22「餘弦相似度（cosine similarity）」；L36「分數正規化（score normalization）」。
- `[verified]` P2「說話人辨識／說話人」→「語者」：全課已統一為「語者」。
- `[not-fixed]` P2「對……很脆」「把……抹平」「回……」「一次吵的註冊會毒掉錨點」→改寫：L143「單次含雜訊的註冊會污染參考 embedding」已改；但 L14「對通道偏移……和情緒很脆」未改；L50「再把邊界抹平」未改；L100 現為「回傳……。兩個都要報。」——原文 "Returns (eer, threshold_at_eer). Report both."，省略了回傳值（資訊遺漏，修錯），建議保留或譯為「回傳 EER 與 EER 處的閾值」。

## phases/06-speech-and-audio/07-text-to-speech（6 條：verified 3 / not-fixed 2 / kept-wrong 1）

- `[kept-wrong]` P1 K011「mel 頻譜圖／Mel 頻譜圖」→「梅爾頻譜圖（mel-spectrogram）」（kept）：K011 所列 L3、L17、L18、L28、L48、L124、L174 已依 GLOSSARY 修正；但 L26「發出 mel 音框」殘留小寫 mel。低優先。
- `[verified]` P1 K012 首見英文（kept；f3 K012 修）：L12「韻律（prosody）」；L16「音素（phoneme）」；L18「聲碼器（vocoder）」；L20「流匹配（flow matching）」；L30「變分推論（variational inference）」。
- `[verified]` P1「標準結果」→「真實音訊」：L62 表格「真實音訊 | 4.08」，全課無「標準結果」。
- `[not-fixed]` P2「ASR 把語音倒成文字」等數處：L3「ASR 將語音轉成文字」已改；但 L12「正確發出「plants」的母音」未改（現為「「plants」的母音對」）；L20「被端到端擴散和流匹配（flow matching）模型弄模糊」未改；L83「音素是通用的橋」未改（建議「橋梁」）；L124「已經商品化」未改（建議「已成為成熟商品」）；L149「除非你在做歷史」未改（語意不清，建議「除非你是研究語音合成發展史」）。
- `[not-fixed]` P2「群眾來源」「信賴區間更緊」：L52「由群眾評分」已改；L53「每次標註的信賴區間更緊」未改（建議「較窄」，低優先）。
- `[verified]` P2「為未知 token 交付一個退路的字素到音素模型」→「為未知 token 準備字素轉音素模型作為備援」：L154。

## phases/06-speech-and-audio/08-voice-cloning-conversion（4 條：verified 1 / kept-ok 1 / not-fixed 2）

- 狀態：f4 日誌有 L31（B，「基模型」）與 L27（E1，去重）紀錄；檔案 20:18:31 後快照不變。
- `[verified]` P1 K013 首見英文（kept；f3 K013 修，f4 E1 去重）：L12「零樣本（zero-shot）或少樣本仿製」；L36「自編碼器（autoencoder）」「潛在空間（latent space）」；L38「神經編解碼器（neural codec）」；L44「可驗證的同意紀錄（consent record）」。
- `[kept-ok]` P1 K014「說話人」→「語者」（kept；稽核 borderline）：全篇仍用「說話人」，非 GLOSSARY 禁用詞；屬用語偏好，稽核判不列 miss。
- `[not-fixed]` P2 直譯／口語：L12「用消費級 GPU 高品質仿製任何人的聲音」已改；但 L38「短 prompt 上的品質和 ElevenLabs 打得平」未改（建議「可媲美」）；L44「存在一改就看得到的日誌裡」未改（建議「記錄在可偵測竄改的日誌中」）。
- `[not-fixed]` P2「對語言和口音穩」「把對齊弄破」「目標池裡的最近鄰」「酬載」：L35「不易受語言和口音影響」已改；L89「會把對齊弄破」未改；L112「大約 32 位元的酬載」、L154「偵測酬載」未改（建議「承載資料」）。另見 N2。

## phases/06-speech-and-audio/09-music-generation（3 條：verified 1 / not-fixed 2）

- `[verified]` P1 K015 首見英文（kept；f3 K015 修）：L16「分軌（stems），或局部重畫（inpainting）」；L69「浮水印（watermark）」「中繼資料（metadata）」；L102「色度圖（chromagram）」。
- `[not-fixed]` P2「要對上的功能」「條件是文字或旋律 embedding」「開放社群裡最接近 Suno 的東西」「可以安全交付的模式」「洗版權的 prompt」「開放模型的字常常糊掉」：L16 已改「值得對照的功能」；L24「條件是文字或旋律 embedding」、L26「開放社群裡最接近 Suno 的東西」、L64「可以安全交付的模式」、L138「洗版權的 prompt」、L141「開放模型的字常常糊掉」均未改。
- `[not-fixed]` P2「每一代都有授權」「模型會離開 BPM」「再用正式的立體聲重建補上」：L67「每次生成均附授權」已改；L140「速度漂掉。模型會離開 BPM。」、L142「再用正式的立體聲重建補上」未改。

## phases/06-speech-and-audio/10-audio-language-models（3 條：verified 1 / not-fixed 2）

- `[verified]` P1 K016 首見英文（kept；f3 K016 修）：L1 標題「音訊語言模型（audio-language model）」；L3「多音訊（multi-audio）」；L15「語意推理（semantic reasoning）」；L29「音訊編碼器（audio encoder）」；L159「說話人歸屬（speaker attribution）」；L171「音訊說明文字（audio captioning）」。
- `[not-fixed]` P2「差距基本上合上了」等：L3 現為「開放和封閉的開放模型與封閉模型的差距幾乎消失」——錯亂句（修錯，見 N 優先清單）；L12「問題跨好幾個軸」、L19「自由形式的自然語言答案」、L66「這一欄對每個人都難看」、L73「說話人輪次」、L159「歸屬推理／語者辨識能力就會失效」、L161「基準挑最好看的」均未改。
- `[not-fixed]` P2「這是 ASR 的地盤」「把音訊編碼器的特徵接到……空間」「語音進、語音出」「完全匹配的迴圈是健全性檢查」：L14「這屬於 ASR 的範疇」已改；L30「把音訊編碼器的特徵（feature）接到 LLM 的 token embedding 空間」、L37「語音進、語音出」、L143「這個完全匹配的迴圈是健全性檢查」未改。

## phases/06-speech-and-audio/11-real-time-audio-processing（2 條：verified 1 / not-fixed 1）

- `[verified]` P1 K017 首見英文（kept；f3 K017 修）：L24「全雙工（full-duplex）」；L30「音框（frame）」；L32「環形緩衝（ring buffer）」；L42「抖動緩衝（jitter buffer）」；L46「執行緒爭用（thread contention）」。
- `[not-fixed]` P2「感覺是活的」等：L12「你要一個反應自然的語音助理」已改；但 L32「熱路徑上不做配置」（建議「避免在熱路徑配置記憶體」）、L34「把下游工作閘住」（建議「停止下游處理」）、L42「抹平」（建議「平滑封包到達時間」）、L46「把音訊執行緒餓死」、L140「延遲地板」（建議「延遲下限」）均未改。

## phases/06-speech-and-audio/12-voice-assistant-pipeline（3 條：verified 1 / not-fixed 2）

- `[verified]` P1 K018 首見英文（kept；f3 K018 修）：L30「音訊擷取（audio capture）」；L170「結束點（endpoint）」；L171「預捲（pre-roll）」。
- `[not-fixed]` P2「縫在一起」等：L3 現為「第 01 到 11 課的東西整合前 01–11 課的內容」——重複句（修錯）；L34「LLM 出 20 個 token」、L38「你一定會撞上的三種失敗」、L42「一定用 VAD 當閘」、L151「一直聽是隱私負債」均未改（建議「LLM 產生」「常見的三種失敗模式」「使用 VAD 篩除靜音」「隱私風險」）。
- `[not-fixed]` P2「把個人資料永遠記下來」「保留 30 天，靜態加密」：L146「永久記錄個人資料」已改；「靜態加密」未改（建議「並對儲存中的資料加密」）。

## phases/06-speech-and-audio/13-neural-audio-codecs（2 條：not-fixed 2）

- `[not-fixed]` P1「神經音訊編解碼器、知覺音質、殘差向量量化、碼本、音框率、語意 token／聲學 token」首見英文：標題 L1「神經音訊編解碼器」與 L12「**神經音訊編解碼器**」無英文；L16「知覺音質」無英文；RVQ 已附英文（L25）。
- `[not-fixed]` P2「語意和聲學的分開」等（修錯，嚴重）：L3 現為「語意 token 對上音框率（frame rate） 的分開，第一本碼本是語意、其餘是聲學」；L54 標題「語意 token 對上音框率（frame rate）」；L61「**音框率（frame rate）（碼本 1 到 7）。** 編碼音色、說話人身分、韻律、背景雜訊、細細節」；L63「再預測音框率（frame rate）（條件是語意加說話人參考）」。英文原文 L3、L54、L61、L63 皆為 semantic／acoustic tokens（聲學 token），「聲學 token」被誤替換為「音框率（frame rate）」，語意錯置。
- 另：L61、L177「細細節」疊字；L19「這放不大」（建議「難以擴展」）；L27「每本 1024 個碼」；L136「1000 個 token 對 transformer 幾乎太小」；L156「會安靜地失敗」（建議「靜默失敗」）未改。

## phases/06-speech-and-audio/14-voice-activity-detection-turn-taking（2 條：not-fixed 2）

- `[not-fixed]` P1「語意輪次偵測器、端點、預捲、準度、精度和召回」→統一並首見附英文：L155「回報精確率（precision）和召回率（recall）」已改；但 L30「第 3 層：語意輪次偵測器」與 L3 首見「輪次偵測」皆無英文（turn detection）；「端點偵測（endpointing）」未出現（已改為「結束點」，可接受）。
- `[not-fixed]` P2「成敗，看兩個決定」等：L3「成敗取決於兩項判斷」已改；但 L14「這一框是語音嗎？VAD。每一框、二元。」未改（建議「逐框進行二元分類」）；L18「2026 年的答案：Silero VAD（開放、深度學來的）」未改（建議「以深度學習訓練」）；L41「串流語音轉文字有往前看的延遲」未改（建議「前瞻延遲」）；L54「要合規或更高準確率就升級到 Cobra」已改準確率但「合規」未改（低優先）；L145「一定要留滾動的預捲」未改（低優先）。

## phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki（3 條：verified 2 / not-fixed 1）

- `[verified]` P1 K019 首見英文（kept；f3 K019 修）：L12「延遲下限（latency floor）」；L16「音框（frame）」；L46「GRPO 強化學習（reinforcement learning）」。
- `[not-fixed]` P2「語音到語音」等數處：L3「Hibiki 一塊一塊做語音轉語音的翻譯」已改；L12「管線形狀把你卡住」、L14「持續吐音訊」、L32「依它已經產出的」未改；L48「新語言大約 1000 小時就能適配」未改（建議「調整以支援新語言」）；L83「Moshi 露出一個 WebSocket 伺服器」未改（建議「提供 WebSocket 伺服器介面」）；L129「沒有管線黏合程式」未改（建議「不需要黏合管線的程式碼」）。L36「又不把主要語句打斷」已改。
- `[verified]` P2「聲音在場感」→「聲音臨場感」：L62「它是市面上「聲音臨場感」最好的 TTS」。

## phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking（4 條：verified 3 / not-fixed 1）

- `[verified]` P1「詮釋資料」→「中繼資料」：L16「音訊檔和中繼資料做密碼學簽章」；L71、L147 已統一。
- `[verified]` P1 K020 首見英文（kept；f3 K020 修）：L1 標題「語音反仿冒（anti-spoofing）與音訊浮水印（audio watermarking）」；L16「可驗證的出處（verifiable provenance）」；L67「位元回復準確率（bit recovery accuracy）」。
- `[not-fixed]` P2「把真實語音和假的分開」等：L3「一個偵測器（AASIST、RawNet2），區分真實與合成語音」已改；但 L33「真實部署」（建議「實際部署」）、L49「噪音混合」（建議「混入雜訊」）、L58「可以把它拿掉」（建議「可移除浮水印」）、L63「時間上的操作」（建議「時間軸上的操作」）、L71「它就什麼也做不了」、L147「每一次生成都帶著出去」（建議「每次生成都附帶」）、L153「（不能商量）」（建議「不可妥協」）未改。
- `[verified]` P2「對仿冒穩健的 ASV（SASV）給生物辨識系統」→改寫：L31「另一賽道是用於生物辨識系統的防仿冒 ASV（SASV）」。

## phases/06-speech-and-audio/17-audio-evaluation-metrics（6 條：verified 4 / not-fixed 2）

- `[verified]` P0「字幕基準」→「音訊描述基準」：L92「AudioCaps／Clotho：音訊描述基準」，與 en "Captioning benchmarks" 一致。
- `[verified]` P1「標準結果是 4.08」→「真實音訊的 UTMOS 為 4.08」：L44。
- `[verified]` P1「mAP（平均精度的平均）」→「mAP（平均精確率的平均值）」：L70。
- `[not-fixed]` P1「每一類召回、macro F1 加每一類召回、1800 題難的」→「每一類召回率」「1800 道較難題目」：L74「每一類召回率」已改；但 L88「**MMAU-Pro。** 1800 題難的，四類」未改（題目描述不通順）。
- `[verified]` P1 K021 首見英文（kept；f3 K021 修）：L3「語音辨識（speech recognition，WER、CER、RTFx）」；L46「SECS（說話人編碼器餘弦相似度，speaker encoder cosine similarity）」。
- `[not-fixed]` P2「各自量不同的軸」等：L12「各自衡量不同面向」已改；但 L12「用錯指標，就是你交付一個……的方式」未改（建議「就可能交付一個……的模型」）；L64「AMI 會議：DER 大約 10% 到 20% 算真實」未改（建議「屬合理範圍」）；L82「消費級音樂的最後一句話仍然是這個」未改；L191「賭注高就付錢找領域小組」未改（建議「付費委託領域專家評分」）；L193「依人群切片報」未改（建議「依不同人口群體分層回報」）。

---

## 附加：new-issue（獨立，未與 finding 綁定）

- N1 `[new-issue]` 04/20 L48 表格「**對比**」（損失家族欄）——GLOSSARY 中 contrastive loss＝對比損失，而 contrastive learning＝對比式學習。f4 D2 已標 [存疑] 且未改。需決定。
- N2 `[new-issue]` 06/08 L154「回報位元準度」——GLOSSARY accuracy＝準確率（06/16 已用「位元回復準確率」）。
- N3 `[new-issue]` 04/16 L50「安靜的失敗就變成會大聲報出來的失敗」、L68「安靜回傳空區域的裁切」——「安靜」與 GLOSSARY「靜默錯誤」及 06/02 建議「靜默失敗」不一致（P2）。
- N4 `[new-issue]` 04/23 L285「抽出來的輸出應該像淡淡的色塊」、L332「比較…抽出的樣本」——生成語境未依 GLOSSARY 改「取樣」（P2）。
- N5 `[new-issue]` 04/08 L77「用 交並比（…） 0.7」多餘半形空格；L266、L279、L290「mAP@交並比（…）=…」嵌入式寫法（格式，低）。
- N6 `[new-issue]` 04/14 L12「實作patch embedding」、L249「的patch embedding（小塊 embedding） 和positional embedding（位置 embedding） 形狀」——中英文間缺半形空格（格式，低）。
- N7 `[new-issue]` 03/12 L21「獨立的GPU kernel 啟動」——中英文間缺半形空格（格式，低）。
- N8 `[new-issue]` 03/11 L103「運算記錄帶」——非 GLOSSARY 術語，未附英文 tape（低）。
- N9 `[new-issue]` 04/12 L272 表格「把 2D 權重抬成 3D」——與 04/26 修正後的「映射至 3D」用語不一致（低）。
- N10 `[new-issue]` 06/16 L183「說話人驗證加 CM」、06/17 L110「說話人辨識」——與 06/06 統一的「語者」不一致（低）。
- N11 `[new-issue]` 06/04 L171 表格「對所有音框到 token 的對齊做邊際」——marginalize 譯為「做邊際」生硬，建議「邊際化」（低）。
- N12 `[new-issue]` 06/02 L26「80 個 梅爾頻率槽」、L28「得到 梅爾頻譜圖」、L30「對數 梅爾頻譜圖」——中文間多餘半形空格（格式，低）。
- N13 `[new-issue]` 06/05 L26「10 毫秒 hop」未譯（GLOSSARY hop size＝跳躍長度；與 06/02 同類，低）。

---

## Summary

### 計數

| 類別 | 03 | 04 | 06 | 合計 |
| --- | ---: | ---: | ---: | ---: |
| verified | 26 | 118 | 41 | 185 |
| not-fixed | 8 | 20 | 32 | 60 |
| kept-ok | 4 | 11 | 2 | 17 |
| kept-wrong | 1 | 1 | 1 | 3 |
| 合計（finding） | 39 | 150 | 76 | 265 |
| new-issue（獨立，未計入上表） | 2 | 6 | 6 | 14（N1–N13，N10 含 2 處） |

- 03：kept 共 12 條（verified 7、kept-ok 4、kept-wrong 1）。
- 04：kept 共 37 條（verified 25、kept-ok 11、kept-wrong 1）。
- 06：kept 共 21 條（verified 18、kept-ok 2、kept-wrong 1）。
- 「not-fixed」含假修復（只改一部分）與修錯（修復造成的重複、錯句、語意錯置）。修錯共約 25 處，列於下方優先清單。
- 注意：r2/r3 的 [已修復] 註記可靠度低。06/02（f 日誌無紀錄，多數 P1/P2 未修）、06/07、06/09、06/10、06/11、06/12、06/14、06/15、06/16 的 P2 用語建議大多未套用；不宜以註記計為已修。

### not-fixed 優先清單（依嚴重度）

P0／P1（語意錯置、錯句、資訊遺漏、GLOSSARY 硬性違規、首見英文缺漏）：
1. 06/13 L3、L54、L61、L63：「聲學 token」被譯為「音框率（frame rate）」，語意錯置；另 L61、L177「細細節」疊字。
2. 06/10 L3：「開放和封閉的開放模型與封閉模型的差距幾乎消失」錯亂句。
3. 06/04 L3：「用一個懂英文、也懂靜音的再用了解英文與靜音的序列模型」錯亂句。
4. 06/12 L3：「第 01 到 11 課的東西整合前 01–11 課的內容」重複句。
5. 06/06 L100：「回傳……。」省略回傳值（資訊遺漏）。
6. 04/11 L96：「都用 LoRA 分散式」語意誤譯（英文為以 LoRA 形式發布）。
7. 03/05 L19：「在分類問題上若在分類問題上使用 MSE 做最小化，模型會……」疊句與殘留省略號。
8. 06/03 L81：句尾殘留重複子句。
9. 04/19 L13：CTC 括註巢狀重複；L128：「（beam search）（beam search）」。
10. 04/20 L231：「以 以 ImageNet」疊字（f4 未處理）。
11. 04/24 L12、L21、L23、L52、L281：「可接受 prompt 的 的」（5 處）。
12. 04/22 L39：「（covariance matrix）（covariance）」重複括註。
13. 03/01 L87、L152；03/03 L73；03/05 L79：重複括註（logic gate、memory、probability mass）。
14. 04/23 L115：「FLUX.2 和 SD4 FLUX.2 和 SD4」。
15. 04/18 L217：「到 2026 年仍是這個領域的到 2026 年仍是此領域的」。
16. 04/03 L360：「繼承了 繼承」。
17. 04/16 L313：「加入：：」重複冒號。
18. 04/28 L21：「正在正逐漸」。
19. 04/21 L76：「到任意人數到任意人數」。
20. 04/15 L60：「是…是…」語句錯亂；L267 表格「掉掉的準確率」。
21. 03/12 L21：「立即執行（eager execution）地」語句不通。
22. 06/14 L3 首見「輪次偵測」與 L30「語意輪次偵測器」無英文；06/13 標題、L12「神經音訊編解碼器」、L16「知覺音質」首見無英文。
23. 06/02 整課 mel 術語（梅爾刻度／梅爾頻譜圖）首見無英文、殘留小寫 mel；hop 未譯（L22、L128–130）；L151「啁啾」未附 chirp。
24. 06/17 L88「1800 題難的」。
25. 04/25 L80、L82、L84、L275 殘留「代理」（GLOSSARY agent 保留英文）。
26. 04/26 L250「Delta 準度」、L261「深度準度」（GLOSSARY accuracy＝準確率）；「抬成 3D」仍見 L15、L23、L84、L152、L239、L251。
27. 04/27 L97「HOTA（高階追蹤準度）」；「標準結果」仍見 L96、L244、L267、L273。
28. 06/07 L12「「plants」的母音對」、L20、L83、L124、L149（語意不清或直譯）。
29. 06/08 L89「把對齊弄破」、L112／L154「酬載」、L154「位元準度」（N2）。
30. 03/05 L119「正對／負對」首見無英文。
31. 04/19 L27、L31、L68、L222「古典」未統一為「傳統」。
32. 06/15 L83「露出一個 WebSocket 伺服器」、L48「適配」。
33. 06/16 L33、L49、L58、L63、L71、L147、L153 等 P2 直譯（多數未改）。
34. 06/11 L32「熱路徑上不做配置」、L34「閘住」、L42「抹平」、L46「餓死」、L140「延遲地板」。

P2（用語、直譯，多為建議未套用）：其餘 not-fixed 條目見各課節。

### kept-wrong 清單（低優先）

- 03/12 L492「沒有未明示 key 的隨機」（kept；稽核 borderline #11）：仍斷裂，建議「沒有明確的 key 就不產生隨機數」。
- 04/22 L13「位置、旋轉、尺度、不透明度」首見未附英文（kept；稽核 borderline #45）：同列其他參數已附英文，標註不一致。
- 06/07 L26「發出 mel 音框」殘留小寫 mel（K011 的其餘行已修）。
- 子項：06/05 L26「對數 mel」首見未附英文（K008 相關，稽核未逐條列出）。

### new-issue 清單

N1（04/20 L48「對比」，GLOSSARY 對比損失，f4 存疑待決）、N2（06/08 L154「位元準度」）、N3（04/16「安靜」用語）、N4（04/23「抽出」取樣）、N5–N13（格式與用語一致性，低優先）。

### 系統性觀察

1. 修錯模式集中：多處修復在原句內「附加」而未刪原文，產生「（X）（X）」「的 的」「繼承了 繼承」「正在正逐漸」「：：」等，共約 25 處，全部列於 not-fixed 清單。建議以本報告的模式掃描（重複括註、疊字、疊句、`……`）重跑 03/04/06 全篇，並檢討 `check_translation.py` 為何未攔截。
2. 06 的 r3 修復有一批「已修復」註記未落實（見 06/02、06/07、06/09、06/10、06/11、06/12、06/14）。f3 日誌對 06/02 無條目，表示這些修正並未執行。
3. f2（03/04）與 f3（06）的 kept→fixed 修復品質高：04 kept 的 25 條、06 kept 的 18 條已確認修到位（僅少數語句錯誤另列）。E 系列全域「抽樣→取樣」（04/09、04/10、04/11、04/23、04/28）已檢查，無生成語境「抽樣」殘留（僅 N4 的「抽出」）。
4. GLOSSARY 禁用詞與簡體字掃描：03/04/06 均無命中。

### 未完成與風險

- f4 仍在寫入（快照 20:46）。04/20（20:45 寫入）、04/15、04/21 的判定可能變動；04/02、06/08 已穩定。建議 f4 完成後重跑本報告第 3 節掃描並複核 04/15 L60、L267、04/20 L231、04/21 L76。
- 需決定：04/20 L48「對比」是否改為「對比損失」（N1）；06/06 L100 是否保留 (eer, threshold_at_eer)（建議保留）。
- 未逐段全文重讀全部 58 課；clean 課（03/06、04/05）以模式掃描為主。
- 03/04 的 Mermaid timeline 英文、Mermaid 邊標籤、圖片 alt 依規則不計問題。

### 建議下一步

由修復者依上方 not-fixed 優先清單（1–34）逐條修正；先處理 1–21 的修錯與語意錯置，再補 22–34 的首見英文與用語。修正後對 03/04/06 重跑模式掃描，並在 f4 收尾後複核 04/15、04/20、04/21。
