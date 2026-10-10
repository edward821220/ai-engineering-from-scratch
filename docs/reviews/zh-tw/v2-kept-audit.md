# zh-TW「維持原樣」駁回複審（v2-kept-audit）

- 審閱來源：`/Users/edward/Desktop/ai-engineering-from-scratch/docs/reviews/zh-tw/r2.md`，共 385 條 finding，其中「維持原樣」100 條。`/private/tmp/zh-tw-review/r2.md` 是較舊版本，沒有任何「維持原樣」條目，未採用。
- 譯稿（現況）：`/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md`；英文原稿：`/private/tmp/aiefs-main-source/phases/<phase>/<lesson>/docs/en.md`。
- 行號一律是現況 zh-TW.md 行號，報告原行號已偏移。`:n` 表示該行。
- 判定依據：任務六條原則。另依 STYLE.md「已採中文譯名的術語……第一次出現在每課時附英文」與 GLOSSARY 指定譯名。「篇章術語已具備譯名」「基礎通用詞彙無需加註」這兩類駁回，只在詞彙確屬一般 CS 詞（程式碼、記憶體、終端機、網路、套件）時成立。
- 嚴重度（僅標註 miss）：P0＝資訊失真或整句英文殘留；P1＝GLOSSARY 違規、專門術語首見未附英文、縮寫缺全名、語意誤譯；P2＝翻譯腔、口語、標點。
- 檢查器實測（唯讀，於暫存字串上呼叫 `scripts/check_translation.py` 的 `_protected_spans` 與 `_mermaid_syntax`）：
  1. 圖片語法 `![alt](src)` 整段是 protected span，改譯 alt 必然報 `protected spans differ`。→ alt 文字事實上受檢查器保護。
  2. Mermaid flowchart 節點標籤會被剝離，改譯不報錯。→ 節點顯示文字可以翻譯。
  3. Mermaid timeline 標籤不會被剝離，改譯報 `mermaid node ids or edges differ`。→ 這是檢查器缺口。
  4. Mermaid `|邊標籤|` 不會被剝離，改譯會報錯；STYLE 也規定連線維持不變。

## phases/03-deep-learning-core/05-loss-functions
- [miss][P1] #1 「錨點／正樣本／負樣本」首見未附英文，駁回理由「篇章術語已具備譯名」→ :131「拿三個輸入：錨點、正樣本（同一類別）、負樣本（不同類別）。」無英文；triplet loss 是專門術語，STYLE 要求首見附英文，「已有譯名」不是豁免理由 → 建議「錨點（anchor）、正樣本（positive）、負樣本（negative）」。

## phases/03-deep-learning-core/08-weight-initialization
- [borderline] #2 「花了 512 個參數，得到 1」直譯後不清楚 → :19「你付了 512 個參數（parameter）的代價，只得到 1 個。」忠實，但「1 個」沒有名詞，要靠上下文才知道指「不同的神經元」。駁回理由與本句無關 → 取捨：保留忠實直譯，或補成「只換到 1 個不同的神經元」。
- [ok] #3 「刀鋒邊界」→ :23「「行」和「壞」的界線薄得像刀口。」是通順的意譯，優於報告建議稿。

## phases/03-deep-learning-core/09-learning-rate-schedules
- [miss][P1] #4 「LR range test」首見未附英文全名 → :139（Mermaid 節點「用學習率範圍測試<br/>找出 lr_max」）與 :403（「實作學習率範圍測試，Leslie Smith 的方法」）皆無英文；此為專門技術名稱 → 建議 :403 補「學習率範圍測試（learning-rate range test）」，:139 節點同步補英文。
- [miss][P1] #5 「cosine annealing with warm restarts」首見未附英文 → :405「實作帶暖重啟的餘弦退火，也就是 SGDR」無英文；「暖重啟」是專門術語，:419 表格「餘弦退火加暖重啟」也沒有英文對應 → 建議「帶暖重啟的餘弦退火（cosine annealing with warm restarts，SGDR）」。
- [miss][P1] #6 「穩定到尖銳的極小值」→ :21「才能沉進一個尖銳的極小值」。GLOSSARY「sharp minimum｜尖銳極小值」首見無英文；「沉進」是 settle into 的直譯 → 建議「才能收斂到尖銳極小值（sharp minimum）」。
- [ok] #7 「微調一個預訓練模型」→ :25「fine-tuning 一個預訓練（pretrained）模型時」已保留 GLOSSARY 指定的 fine-tuning 英文，語句通順。

## phases/03-deep-learning-core/10-mini-framework
- [miss][P1] #8 「訓練迴圈」「權重初始化」首見未附英文，駁回理由「基礎通用詞彙」→ :14「把所有零件接成一個能動的訓練迴圈」（學習目標首見）與 :19「權重初始化在另一個檔案」皆無英文。GLOSSARY「training loop｜訓練迴圈」「weight initialization｜權重初始化」為指定譯名，屬 ML 專門術語，不是通用 CS 詞 → 建議 :14 補「訓練迴圈（training loop）」，:19 補「權重初始化（weight initialization）」。

## phases/03-deep-learning-core/11-intro-to-pytorch
- [ok] #9 「磁碟受限的工作負載」→ :238「在受磁碟限制的工作負載上，例如大影像、音訊……」與原文語意一致，用語自然。

## phases/03-deep-learning-core/12-intro-to-jax
- [miss][P2] #10 「第一級支援」直譯生硬 → :218 表格「TPU 支援 | 一等支援，Google 兩邊都是自己做的」。「一等支援」是 first-class 的直譯，非中文技術慣用語；駁回理由「行文流暢」不成立 → 建議「官方一級支援（Google 自家研發）」。
- [borderline] #11 「隨機金鑰」→ 原字串已不存在。:492 表格列「沒有未明示 key 的隨機」仍不通順（「未明示 key 的隨機」讀來斷裂，key 也沒譯）；PRNG key 首見（:232）已附英文 → 取捨：現況已不是報告指的字串，但該列需要改寫，建議「沒有明確的 key 就不產生隨機數」。駁回理由錯誤，結論可接受。

## phases/03-deep-learning-core/13-debugging-neural-networks
- [miss][P1] #12 「梯度消失／梯度爆炸」首見未附英文，駁回理由「基礎通用詞彙」→ :14「找出梯度消失或梯度爆炸」。GLOSSARY「vanishing gradient｜梯度消失」「exploding gradient｜梯度爆炸」為指定譯名，屬 ML 專門術語 → 建議「梯度消失（vanishing gradient）或梯度爆炸（exploding gradient）」。

## phases/04-computer-vision/03-cnns-lenet-to-resnet
- [borderline] #13 Mermaid 時間軸節點仍為英文 → :29–33 timeline 區塊（標題 "Four ideas, four families"，節點如 "Conv + pool + FC for digits, trained on CPU, 60k params"）。STYLE 要求翻譯 Mermaid 節點顯示文字，駁回理由「語境流暢」與此無關。但實測 `_mermaid_syntax` 不剝離 timeline 標籤，改譯會被判為結構差異 → 取捨：要嘛先擴充 `_mermaid_syntax` 支援 timeline 再翻譯，要嘛由 supervisor 明確豁免（見 Summary 決策 B）。
- [borderline] #14 「坐在縮放曲線上」→ :21「知道每一族的縮放曲線，你才知道該坐在曲線的哪裡。」語意可懂，「坐在」是直譯 → 取捨：可接受；若求自然可改「你才知道自己該落在曲線的哪一段」。
- [borderline] #15 區塊重用句的 run-on → :75「簡單，一種區塊類型重複使用，使它成為後面一切的參考點。」破折號同位語被逗號串接，「簡單」與後段銜接生硬，但資訊完整 → 取捨：可改「這份簡單（一種區塊類型重複使用）讓它成為後面一切的參考點」。

## phases/04-computer-vision/04-image-classification
- [ok] #16 「轉移」→ :19「是這整個階段能搬到其他任務的技能」。原文 "transfers to every other task" 指技能可遷移，不是遷移學習，報告的前提不成立；現譯語意正確（「搬到」略口語）。
- [ok] #17 「90 比 10」→ :105「一個 90 比 10 的二元分類器如果永遠預測多數類，準確率是 90%」，後句已點出多數類，比例清楚。
- [ok] #18 「準確率外洩」→ :392「把 ImageNet 的統計值貼過來，會漏掉大約 1% 準確率」，意譯與原文 accuracy leak 一致。

## phases/04-computer-vision/06-object-detection-yolo
- [miss][P1] #19 「IoU」首見未附中文全名或英文全名，駁回理由「保留原結構以維護受保護格式與公式」→ :13「計算框與框之間的 IoU」為首見；:86 標題「### IoU」。公式在 :91，但首見不是公式。GLOSSARY「intersection over union (IoU)｜交並比（IoU）」是指定譯名 → 建議 :13 改「交並比（intersection over union，IoU）」，:86 標題同步為「交並比（IoU）」。

## phases/04-computer-vision/07-semantic-segmentation-unet
- [miss][P1] #20 「IoU」首見未展開 → :15「讀每個類別的 IoU 和 Dice」為首見，GLOSSARY 指定「交並比（IoU）」 → 建議「交並比（intersection over union，IoU）」。
- [miss][P2] #21 「巨觀平均 Dice」→ :259「這是巨觀平均（macro-average）Dice」。同批次 05-sentiment 已統一為「宏平均」（05-05 :164–172），本課仍用「巨觀」，造成跨課譯名不一致 → 建議「宏平均（macro-average）Dice」。

## phases/04-computer-vision/08-instance-segmentation-mask-rcnn
- [borderline] #22 「成本是處處都少十分之幾個 mAP 點」→ :23「這裡弄錯，到處都會掉十分之幾個 mAP」語意正確，但漏「點」，「掉」偏口語 → 取捨：可接受；若求精確可改「到處都會損失零點幾個 mAP 點」。

## phases/04-computer-vision/09-image-generation-gans
- [miss][P1] #23 標題「GAN」首見未附中文全名，駁回理由「保留原結構」→ :1「# 影像生成（image generation）：GAN」。H1 不屬檢查器保護範圍（只保護固定 `##` 章節標題）。GLOSSARY「generative adversarial network (GAN)｜生成對抗網路（GAN）」 → 建議「# 影像生成（image generation）：生成對抗網路（GAN）」。
- [miss][P1] #24 「minimax」首見未附英文 → :12「說明生成器（generator）和判別器（discriminator）之間的極小極大賽局」無英文。譯名「極小極大」本身正確，報告建議的「極大極小」反而不是慣用語；缺的只是英文原詞 → 建議「極小極大（minimax）賽局」。

## phases/04-computer-vision/11-stable-diffusion
- [miss][P1] #25 「VAE」首見未展開，駁回理由「保留原結構」→ :3（blockquote）「跑在預訓練 VAE 的潛在空間」為首見；散文不屬保護格式。GLOSSARY「variational autoencoder (VAE)｜變分自編碼器（VAE）」 → 建議「變分自編碼器（variational autoencoder，VAE）」。
- [miss][P1] #26 「由 CFG 引導」→ :3「……抽樣用快速的確定性 ODE 求解器，方向由無分類器引導（classifier-free guidance）來轉。」兩個問題：(a)「由……來轉」是 steered by 的直譯翻譯腔；(b) 同句「抽樣」在生成語境應為「取樣」，GLOSSARY「sampling｜抽樣」條註明生成模型演算法用「取樣」 → 建議「以快速的確定性 ODE 求解器取樣，並以無分類器引導（classifier-free guidance）控制生成方向」。
- [miss][P2] #27 「從潛在表示來注意」→ :50「每一個解析度都有交叉注意力層，從潛在去注意文字 embedding。」「從潛在去注意」是 attend from latents 的直譯，不合技術文件語域 → 建議「讓潛在表示去關注文字 embedding」。
- [borderline] #28 「嚴格的授權要求」→ :236「要目前最好、授權又嚴格，用 SD3 或 FLUX。」原文 "strict licensing requirements"。「授權又嚴格」主詞模糊，讀者可能以為授權條款本身嚴格 → 取捨：保留或改「授權要求又嚴格」。

## phases/04-computer-vision/12-video-understanding
- [miss][P2] #29 「成本和準確率怎麼換」→ :12「並預估它們的成本和準確率（accuracy）怎麼換」。學習目標使用口語「怎麼換」，不合技術文件語域；駁回理由「行文流暢」不成立 → 建議「成本與準確率之間的取捨」。

## phases/04-computer-vision/13-3d-vision-nerf
- [borderline] #30 「被擋在成長最快的區塊之外」→ :21「只懂 2D 影像的視覺工程師，會進不去這個領域成長最快的那一塊」。語意已由後句的領域清單釐清，口語感略重 → 取捨：可保留，或改「會錯過這個領域成長最快的部分」。

## phases/04-computer-vision/15-real-time-edge
- [miss][P1] #31 「推論延遲、峰值記憶體、吞吐量」首見未附英文，駁回理由「行文流暢」→ :12「量任何 PyTorch 模型的推論延遲、峰值記憶體和吞吐量」。「推論延遲」「峰值記憶體」是效能評測專門術語；「吞吐量」在 04-16 :92 已附 throughput，本批次應一致 → 建議「推論延遲（inference latency）、峰值記憶體（peak memory）和吞吐量（throughput）」。
- [miss][P2] #32 「給獨立的命令列數字」→ :241「`benchmark_app`（OpenVINO）和 `trtexec`（TensorRT）給獨立的命令列數字。」直譯 standalone CLI numbers，「給……數字」是翻譯腔，語意含糊。`benchmark_app` 等程式名受保護，但這句是散文，「保留原結構」理由不成立 → 建議「可直接從命令列取得獨立的基準數字」。

## phases/04-computer-vision/16-vision-pipeline-capstone
- [ok] #33 Mermaid「error」→ :39「REQ -.->|error| RESP」。這是連線（邊）標籤。STYLE.md 規定 Mermaid「只翻譯節點顯示文字；……連線……維持不變」，且檢查器不剝離 `|…|` 邊標籤（實測改譯會失敗）。駁回結論成立，但 finding 的依據「連線文字原則上需翻譯」與 STYLE 相反，理由應改引 STYLE 條款。
- [ok] #34 「用資料契約縫在一起」→ :3「用資料契約（data contract）縫在一起」保留原比喻，語意通順，可接受。
- [miss][P2] #35 「吞吐量會乘上去」→ :92「批次……吞吐量（throughput）會乘上去」。「乘上去」是 multiplies 的直譯，非慣用語 → 建議「能成倍提升吞吐量」（保留倍數語意，不加「大幅」之類的強度詞）。

## phases/04-computer-vision/17-self-supervised-vision
- [miss][P1] #36 「對比」「老師與學生」「遮罩重建」「遮罩比例」首見未附英文，駁回理由「基礎通用詞彙」→ :12「對比（SimCLR）、老師與學生（DINO）、遮罩重建（MAE）」；:14「MAE 的 75% 遮罩比例」。GLOSSARY「contrastive learning｜對比式學習」，本課卻用「對比」，未依詞彙表。這些是 SSL 專門術語 → 建議「對比式學習（contrastive learning，SimCLR）」「老師與學生（teacher-student，DINO）」「遮罩重建（masked reconstruction，MAE）」，:14 補「遮罩比例（mask ratio）」。
- [miss][P2] #37 「損失在說：……」→ :42「損失在說：這兩個 embedding 應該靠近，而且這個 embedding 應該離批次裡其他影像的 embedding 很遠。」擬人化翻譯腔，後句「這個 embedding」指涉不清 → 建議「損失函數會拉近這兩個 embedding，並讓它遠離批次中其他影像的 embedding」。

## phases/04-computer-vision/18-open-vocab-clip
- [miss][P1] #38 「影像編碼器、文字編碼器、雙塔架構、對比訓練、零樣本分類、餘弦相似度」首見未附英文，駁回理由「基礎通用詞彙」→ :12「說明 CLIP 的雙塔架構，以及對比訓練的目標」；:14「從零實作零樣本分類：……算餘弦相似度」。GLOSSARY「zero-shot｜零樣本」「cosine similarity｜餘弦相似度」是指定譯名，屬 ML 專門術語 → 建議首見補「零樣本（zero-shot）分類」「餘弦相似度（cosine similarity）」「雙塔（two-tower）架構」「對比訓練（contrastive training）」，:3 的「影像編碼器（encoder）」改「影像編碼器（image encoder）」。另 :3「讓讓相符的影像」有重複字，是已修復項引入的誤植 → 建議刪一個「讓」。

## phases/04-computer-vision/19-ocr-document-understanding
- [miss][P1] #39 「字元錯誤率，CER」「詞錯誤率，WER」首見只給中譯與縮寫，駁回理由「基礎通用詞彙」→ :80–81。這是 OCR 評估專門指標，英文原文為 Character／Word Error Rate → 建議「字元錯誤率（character error rate，CER）」「詞錯誤率（word error rate，WER）」。
- [miss][P1] #40 「鍵值抽取」「編輯距離」首見未附英文 → :76「表單用**鍵值抽取**模型」（key-value extraction 為任務名）；:83「JSON 上的編輯距離」。GLOSSARY「edit distance｜編輯距離」為指定譯名 → 建議「鍵值抽取（key-value extraction）」「編輯距離（edit distance）」。
- [miss][P0] #41 「把所有……的對齊加總」→ :54「CTC 損失把所有「合併重複、拿掉空白之後會變成目標文字」的對齊加總。」原文 "CTC loss marginalises over all alignments…" 指對齊機率的加總。譯文漏「機率」，讀者會以為是把對齊（路徑）數相加，技術意義失真。駁回理由「行文流暢」不成立 → 建議「CTC 損失把所有……的對齊機率加總（即邊緣化）」。

## phases/04-computer-vision/20-image-retrieval-metric
- [miss][P1] #42 「三元組、對比、以 proxy 為基礎」首見未附英文，駁回理由「基礎通用詞彙」→ :12「說明三元組、對比、以及以 proxy 為基礎的度量學習損失（loss）」。GLOSSARY「triplet loss｜三元組損失」已列為術語，屬度量學習專門術語 → 建議「三元組（triplet）、對比（contrastive）、以 proxy 為基礎（proxy-based）的度量學習損失」。
- [miss][P1] #43 「實例級／類別級」首見未附英文 → :19「電商的實例級比對」為首見；:96 標題「實例級對類別級檢索」；:100–101 條列 → 建議首見補「實例級（instance-level）」，:100 補「類別級（category-level）」。

## phases/04-computer-vision/21-keypoint-pose
- [miss][P1] #44 關鍵點術語首見未附完整英文，駁回理由「行文流暢」→ :12「分辨由上而下和由下而上的姿態估計」（top-down／bottom-up 未附）；:61 標題「次像素定位」（sub-pixel localization 未附）；:80「PCK（正確關鍵點百分比）和 OKS（物件關鍵點相似度）」只有中譯與縮寫，無英文全名；:3「熱圖（heatmap）迴歸器」只附 heatmap，未附 heatmap regression → 建議首見處補「由上而下（top-down）」「由下而上（bottom-up）」「次像素定位（sub-pixel localization）」「正確關鍵點百分比（Percentage of Correct Keypoints，PCK）」「物件關鍵點相似度（Object Keypoint Similarity，OKS）」。

## phases/04-computer-vision/22-3d-gaussian-splatting
- [borderline] #45 參數名「位置、旋轉、尺度、不透明度」首見未附英文 → :13「說出每個高斯的六個參數：位置、旋轉四元數（quaternion）、尺度、不透明度、球諧（spherical harmonics）顏色、可選特徵（feature）」。同一列中 quaternion、spherical harmonics、feature 已附英文，position／scale／opacity 沒有，標註不一致 → 取捨：這幾個是通用詞，但在本句是參數名；建議補齊英文，與同列一致。

## phases/04-computer-vision/23-diffusion-transformers-rectified-flow
- [miss][P1] #46 「雜訊排程」「速度」首見未附英文，駁回理由「基礎通用詞彙」→ :3（blockquote）「把雜訊排程換成一條直線的流」為首見；:66「訓練網路去預測速度 `v_theta(...)`」為速度首見。GLOSSARY「noise schedule｜雜訊排程」（:1491，保留英文否）為指定譯名，首見應附英文；「velocity｜速度」（:1239）註明為動量語境，本課是整流流的速度場，語境不同 → 建議首見補「雜訊排程（noise schedule）」「速度（velocity）」，並由譯者確認「速度」在整流流語境的譯名。

## phases/04-computer-vision/27-multi-object-tracking
- [miss][P1] #47 「以偵測為基礎的追蹤」「以查詢為基礎的追蹤」「匈牙利指派／演算法」首見未附英文，駁回理由「基礎通用詞彙」→ :12「分辨以偵測為基礎的追蹤和以查詢為基礎的追蹤」；:13「從零實作 IoU 加匈牙利指派」。這些是 MOT 專門術語 → 建議「以偵測為基礎的追蹤（tracking-by-detection）」「以查詢為基礎的追蹤（query-based tracking）」「匈牙利指派（Hungarian assignment）」。

## phases/04-computer-vision/28-world-models-video-diffusion
- [miss][P1] #48 「潛在動作」「分開的注意力」首見未附英文，駁回理由「基礎通用詞彙」→ :49「從觀察到的影片推論潛在動作」為首見散文（:35 是 Mermaid 節點）；:188「### 步驟 3：分開的注意力區塊」。這兩詞是 latent action 與 divided attention 的專門譯名 → 建議首見補「潛在動作（latent action）」「分開的注意力（divided attention）」。
- [miss][P2] #49 「生成到一半，你不能轉它」→ :48「生成到一半，你不能轉它。」與 :73「生成到一半沒有東西能轉它」。steer mid-rollout 直譯成「轉」，讀者難以理解「轉」指什麼；駁回理由「行文流暢」不成立 → 建議「生成過程中無法引導它」。

## phases/05-nlp-foundations-to-advanced/01-text-processing
- [miss][P1] #50 「詞性標註器」首見未附英文，駁回理由「保留原結構」→ :135「缺的那一塊是詞性標註器。」無英文；GLOSSARY「part-of-speech tagging｜詞性標記」為詞彙表詞 → 建議「詞性標註器（POS tagger）」。

## phases/05-nlp-foundations-to-advanced/04-glove-fasttext-subword
- [ok] #51 「把共現矩陣做了矩陣分解」→ :3「GloVe 把共現（co-occurrence）矩陣做了矩陣分解（matrix factorization）」語意完整，僅「矩陣」重複，句型可接受。
- [borderline] #52 「數語料庫裡每一對相鄰的配對」→ :28「數語料庫（corpus）裡每一對相鄰的配對。」語意可推，但沒有說明是統計出現次數 → 取捨：可改「統計語料中每一對相鄰 token 的出現次數」。

## phases/05-nlp-foundations-to-advanced/06-named-entity-recognition
- [miss][P1] #53 「發射機率」「轉移機率」「維特比解碼」首見未附英文，駁回理由「基礎通用詞彙」→ :42「給定標記時 token 的發射機率，以及標記到標記的轉移機率。用維特比解碼。」GLOSSARY「transition probability｜轉移機率」為指定譯名；emission probability、Viterbi decoding 同屬 HMM 專門術語 → 建議「發射機率（emission probability）」「轉移機率（transition probability）」「維特比解碼（Viterbi decoding）」。

## phases/05-nlp-foundations-to-advanced/07-pos-tagging-parsing
- [miss][P1] #54 「轉移機率」「發射機率」「維特比解碼」首見未附英文 → :87「兩張表：轉移機率（給定前一個標記的標記），發射機率（給定標記的詞）。……用維特比解碼」。同上 GLOSSARY，且 :87 的「拉普拉斯平滑（Laplace smoothing）」已附英文，本句標註不一致 → 建議補「轉移機率（transition probability）」「發射機率（emission probability）」「維特比解碼（Viterbi decoding）」。

## phases/05-nlp-foundations-to-advanced/08-cnns-rnns-for-text
- [borderline] #55 「閘」作為 gate 的簡稱 → :30「LSTM 加上閘」首見無英文；:108「遺忘閘（forget gate）」；:192–193「輸入閘、遺忘閘、輸出閘」。GLOSSARY 無 gate 條目，本課混用「閘」與完整譯名 → 取捨：統一為「閘門（gate）」較穩；若保留「閘」，首見 :30 應附 gate。

## phases/05-nlp-foundations-to-advanced/10-attention-mechanism
- [borderline] #56 圖片 alt「Bahdanau attention: decoder queries all encoder states」仍為英文 → :20 `![Bahdanau attention: …](../assets/attention.svg)`。檢查器把整段圖片語法列為 protected span，改 alt 必然失敗（已實測）。駁回結論在現行工具下成立，但理由應改為「檢查器保護」而非「語境流暢」；無障礙缺口需 supervisor 決策（Summary 決策 A）。
- [miss][P1] #57 「加法分數／乘法分數」首見未附英文 → :44「**Bahdanau（加法）分數。**」、:51「**Luong（乘法）分數。**」。加法／乘法注意力是專門術語，本文首見無英文（表格 :213–214 才出現「加法注意力」，已在本文之後）→ 建議「Bahdanau（加法注意力，additive attention）分數」「Luong（乘法注意力，multiplicative attention）分數」。

## phases/05-nlp-foundations-to-advanced/11-machine-translation
- [borderline] #58 「短程」→ :146「短程、推論（inference）便宜、英－法／德／西」。原文 "Short runs" 本身模糊，譯文忠實 → 取捨：保留直譯，或依作者意圖改「短文本」。駁回理由「符合臺灣技術語境」不足以支撐，但原文不清時保留直譯可接受。

## phases/05-nlp-foundations-to-advanced/12-text-summarization
- [borderline] #59 「空句預訓練目標」→ :26「Pegasus 特別用缺句生成預訓練目標（gap-sentence generation objective）」。P0 修正已附英文，首見問題已解；但括註用的是 "generation"，原文是 "gap-sentence pretraining objective"→ 取捨：與原文不逐字一致，建議統一為 gap-sentence pretraining objective，或註明來源用詞。
- [borderline] #60 圖片 alt「Extractive TextRank vs abstractive transformer」仍為英文 → :22 alt。protected span 規則同 05-10。

## phases/05-nlp-foundations-to-advanced/13-question-answering
- [borderline] #61 圖片 alt「QA architectures: extractive, retrieval-augmented, generative」→ :24 alt。protected span 規則同上。
- [borderline] #62 「前 `k` 段」→ :28「檢索器從語料庫找出前 `k` 段」、:122「有沒有把對的段落放進前 `k`」。原文 top-`k` 指依相關性排序的前 k 名；「前 k」容易被讀成文件順序的前 k 筆 → 取捨：建議「排名前 `k` 的段落」以保留排序語意。

## phases/05-nlp-foundations-to-advanced/15-topic-modeling
- [borderline] #63 「句子 transformer」→ :35「用句子 transformer（例如 `all-MiniLM-L6-v2`）把每份文件編碼」。sentence transformer 是專有名稱，中英拼接。駁回理由「保留原結構」不成立；但拼接可讀 → 取捨：保留完整英文 sentence transformer，或寫「句子轉換器（sentence transformer）」。
- [borderline] #64 圖片 alt「LDA mixture model vs BERTopic clustering」→ :24 alt。protected span 規則同上。

## phases/05-nlp-foundations-to-advanced/16-text-generation-pre-transformer
- [borderline] #65 圖片 alt「N-gram model: count, smooth, generate」→ :20 alt。protected span 規則同上。
- [miss][P1] #66 「三元模型／三元」首見未附英文，駁回理由「基礎通用詞彙」→ :34「三元模型用兩個 token 的記憶來玩」為首見（:42 「三元是 3」亦同）。trigram 是 n-gram 系列的專門術語 → 建議首見補「三元模型（trigram model）」。
- [miss][P1] #67 「仍面對的分岔因子」→ :33「模型猜完之後仍面對的分岔因子」。branching factor 是 perplexity 語境的專門術語，首見無英文，「分岔因子」也不是慣用譯名 → 建議「模型猜完之後仍需面對的分支數（branching factor）」。
- [ok] #68 「小的隨機旋鈕（溫度）」→ :181「再加一個小的隨機旋鈕（溫度，temperature）」保留原比喻，並附 temperature 英文，忠實。

## phases/05-nlp-foundations-to-advanced/17-chatbots-rule-to-neural
- [borderline] #69 圖片 alt「Chatbot evolution: rule-based → retrieval → neural → agent」→ :20 alt。protected span 規則同上。
- [miss][P1] #70 「檢索再接地／檢索接地」→ :50「先檢索再接地（RAG）讓它不幻覺」；:163「每次呼叫模型前先注入相關文件的檢索接地」。grounding 首見無英文；GLOSSARY 未指定 grounding 譯名，「接地」在本文無說明，「檢索接地」搭配少見 → 建議首見寫「以檢索到的文件作為依據（grounding）」，:163 改「以檢索到的文件作為依據（grounding）」。

## phases/05-nlp-foundations-to-advanced/18-multilingual-nlp
- [borderline] #71 圖片 alt「Cross-lingual transfer via shared multilingual embedding space」→ :20 alt。protected span 規則同上。
- [borderline] #72 「切分倍率稅（fertility）」→ :167「切分倍率稅（fertility）。低資源語言的文本，每個詞切出的 token 比英文多很多。」附英文且後句有釋義，語意正確。「稅」字突兀（fertility tax 的比喻直譯）→ 取捨：可保留，或改「切分倍率（fertility）代價」。

## phases/05-nlp-foundations-to-advanced/19-subword-tokenization
- [borderline] #73 圖片 alt「BPE vs Unigram vs WordPiece, character-by-character」→ :20 alt。protected span 規則同上。

## phases/05-nlp-foundations-to-advanced/20-structured-outputs-constrained-decoding
- [borderline] #74 圖片 alt「Constrained decoding masking invalid tokens at each step」→ :26 alt。protected span 規則同上。

## phases/05-nlp-foundations-to-advanced/21-nli-textual-entailment
- [borderline] #75 圖片 alt「NLI: three-way classification, premise vs hypothesis」→ :28 alt。protected span 規則同上。
- [miss][P1] #76 「RTE」表格未附英文全名 → :165「| RTE | 辨識文本蘊涵 | NLI 的舊名；同一個任務。 |」。原文表格第二欄是 Recognizing Textual Entailment，譯文只留中文名，英文全名遺失 → 建議「辨識文本蘊涵（Recognizing Textual Entailment）」。
- [miss][P2] #77 「在正式環境裡卻是承重的」→ :3「表面無聊，在正式環境（production）裡卻是承重的。」load-bearing 直譯，「承重的」作述語不合中文技術語域 → 建議「在正式環境裡卻是不可或缺的基礎」。

## phases/05-nlp-foundations-to-advanced/22-embedding-models-deep-dive
- [miss][P1] #78 「MTEB」首見只給中文描述，駁回理由「基礎通用詞彙」→ :38 標題「### MTEB 排行榜只說了一部分」；:40「大規模文本 embedding 評測——推出時（2022）8 類任務共 56 個」無英文全名（原文 Massive Text Embedding Benchmark）；:201 詞彙表列也沒有。MTEB 是基準名稱 → 建議 :40 補「大規模文本 embedding 評測（Massive Text Embedding Benchmark，MTEB）」。
- [borderline] #79 圖片 alt「Dense, sparse, and multi-vector embeddings」→ :26 alt。protected span 規則同上。
- [borderline] #80 「不理延遲（latency）的尾端」→ :144「不理延遲（latency）的尾端。MTEB 分數藏起 p99 延遲。」語意可懂，但是直譯；「延遲長尾（latency tail）」是領域常用說法 → 取捨：可改「忽略延遲長尾（latency tail）」。

## phases/05-nlp-foundations-to-advanced/23-chunking-strategies-rag
- [borderline] #81 圖片 alt「Six chunking strategies visualized on one passage」→ :26 alt。protected span 規則同上。
- [miss][P1] #82 「固定切塊、遞迴、語意、句子、父文件、延遲切塊、脈絡化檢索」首見未附英文，駁回理由「基礎通用詞彙」→ :28「**固定切塊。**」、:30「**遞迴。**」、:32「**語意。**」、:34「**句子。**」、:36「**父文件。**」、:38「**後置切塊（2024）。**」、:40「**脈絡化檢索（Anthropic，2024）。**」。這些是 RAG 切塊策略的專門名稱，首見皆無英文；後置切塊（late chunking）與脈絡化檢索（contextual retrieval）也未附英文 → 建議首見補 fixed chunking、recursive chunking、semantic chunking、sentence chunking、parent-document、late chunking、contextual retrieval。

## phases/05-nlp-foundations-to-advanced/24-coreference-resolution
- [borderline] #83 圖片 alt「Coreference clustering: mentions → entities」→ :25 alt。protected span 規則同上。
- [miss][P1] #84 「提及配對分類器」「提及排序」「基於 span 的端到端」首見未附完整英文，駁回理由「行文流暢」→ :39「提及配對分類器（classifier）」（只附 classifier）；:40「提及排序」；:41「基於 span 的端到端（Lee 等人，2017）」。這些是專門技術名稱 → 建議「提及配對分類器（mention-pair classifier）」「提及排序（mention-ranking）」「基於 span 的端到端（span-based end-to-end）」。
- [miss][P2] #85 「……lunch.」。→ :3「「She called him. He did not answer. The doctor was at lunch.」。」引號內句末已有英文句點，引號外又加中文句號，重複。依標點慣例應只保留引號內的句點 → 建議刪除「」」後的「。」。
- [borderline] #86 「表面 NLP……之間的黏合」→ :14「它是表面 NLP（NER、剖析）和下游語意之間的黏合：資訊抽取、問答、摘要、知識圖譜（knowledge graph）。」「表面」可讀成「膚淺」，與 surface-level 的「淺層／表層」意思有落差；「黏合」是 glue 的直譯，仍可懂 → 取捨：建議「表層 NLP……與下游語意任務之間的橋樑」。

## phases/05-nlp-foundations-to-advanced/25-entity-linking
- [borderline] #87 圖片 alt「Entity linking pipeline: mention → candidates → disambiguated entity」→ :29 alt。protected span 規則同上。
- [miss][P1] #88 「候選生成、消歧、提及召回率」首見未附英文，駁回理由「行文流暢」→ :22「**候選生成。**」無英文；:43「**提及召回率（recall）（候選生成）。**」只附 recall；「消歧」的首見在 :1 標題，且標題格式錯誤（見範圍外 E1）→ 建議 :22 補「候選生成（candidate generation）」，:43 改「提及召回率（mention recall）」，並補 disambiguation 首見英文。
- [miss][P2] #89 「Jordan beat the press.」。→ :12「有一句：「Jordan beat the press.」。」與 05-24 相同的引號後句號重複 → 建議刪除「」」後的「。」。

## phases/05-nlp-foundations-to-advanced/26-relation-extraction-kg
- [borderline] #90 圖片 alt「Text → triples → knowledge graph」→ :25 alt。protected span 規則同上。
- [borderline] #91 「脈絡精確率（precision）、脈絡召回率（recall）」→ 報告定位錯誤：05-26 的 zh-TW.md 沒有這串文字。實際位於 05-27 :20、:46（以及 05-13 :130–131、05-14 :182）。實質問題在 05-27，已列為 05-27 的 miss，判定以該條為準。
- [miss][P1] #92 「AEVS（錨定–抽取–驗證–補充）」首見未附英文全名，駁回理由「基礎通用詞彙」→ :21「2026 年的答案是 AEVS 式的錨定再驗證管線」為首見，:35「**AEVS（錨定–抽取–驗證–補充，2026）。**」也沒有英文全名（原文 Anchor-Extraction-Verification-Supplement）→ 建議首見改「AEVS（Anchor-Extraction-Verification-Supplement，錨定–抽取–驗證–補充）」。
- [ok] #93 「出處（provenance）」→ :3「和它們的出處（provenance）彙整」已附英文；:207 表格「出處｜連回來源的連結｜每個三元組帶著文件 id 和字元 span，指回來源」有釋義，與原文 provenance（可追溯的來源資訊）語意相符，可接受。

## phases/05-nlp-foundations-to-advanced/27-llm-evaluation-frameworks
- [borderline] #94 圖片 alt「Four evaluation dimensions, LLM-as-judge architecture」→ :28 alt。protected span 規則同上。
- [miss][P1] #95 「答案相關性、脈絡精確率、脈絡召回率」首見未附完整英文，駁回理由「行文流暢」→ :20「四個 RAG 指標：忠實度（faithfulness）、答案相關性、脈絡精確率（precision）、脈絡召回率（recall）」。「答案相關性」無英文；「脈絡精確率」「脈絡召回率」只括註通用的 precision／recall，原文是 context-precision／context-recall → 建議「答案相關性（answer relevance）」「脈絡精確率（context precision）」「脈絡召回率（context recall）」。
- [miss][P0] #96 整句英文殘留 → :32「為什麼行得通：……GPT-4o-mini $0.003 per scored case enables 1000-sample regression eval runs for under $5，也就是每個案例約 0.003 美元、1000 個樣本不到 5 美元。」英文整句留在中文正文，後面已有完整中文譯文，屬整句未翻譯 → 建議刪除英文整句，只保留「GPT-4o-mini 每個已評分案例約 0.003 美元……」的中文句。

## phases/05-nlp-foundations-to-advanced/28-long-context-evaluation
- [borderline] #97 圖片 alt「NIAH baseline, RULER multi-task, LongBench holistic」→ :24 alt。protected span 規則同上。
- [miss][P1] #98 「Gemini 3 Pro 廣告……廣告上的 ≠ 用得上的」→ :3「Gemini 3 Pro 廣告 1000 萬個 token 的脈絡。……廣告上的 ≠ 用得上的。long-context evaluation告訴你，……」。advertises／advertised 在此是模型宣稱的容量，直譯「廣告」易被讀成廣告行為，且「廣告上的」不通順；「long-context evaluation」未譯，與中文之間也缺半形空格 → 建議「Gemini 3 Pro 宣稱支援 1000 萬個 token 的脈絡……宣稱的容量不等於實際可用容量。長脈絡評估（long-context evaluation）會告訴你……」。

## phases/05-nlp-foundations-to-advanced/29-dialogue-state-tracking
- [borderline] #99 圖片 alt「DST: dialog history → slot-value state」→ :26 alt。protected span 規則同上。
- [borderline] #100 「DST 是……之間的轉折」→ :14「DST 是使用者說的話、和後端執行的事之間的轉折。」hinge 指承接兩端的關鍵連接點，「轉折」易讀成事件轉折 → 取捨：建議「樞紐」或「連接橋樑」（報告建議的「關鍵橋樑」亦可）。

---

## 範圍外觀察（不計入 100 條；屬已修復項或未覆蓋的問題，未做完整稽核）

- E1【高】05/25 entity-linking 標題錯誤：`/phases/05-nlp-foundations-to-advanced/25-entity-linking/docs/zh-TW.md:1` 為「# 實體連結與實體連結與消歧（entity linking and disambiguation）（entity linking）」，字串重複且括註錯置。全檔共 11 處（含標題）附了「（entity linking and disambiguation）」括註（:1、:23、:25、:33、:39、:44、:46、:66、:170、:171、:180），首見規範被濫用。這是已修復項「消歧」的結果。
- E2【高】04-16 capstone 已修復項（偵測器／分類器／前處理）的現況是中英夾雜。散文仍用英文 detector／classifier／preprocessing（:13、:14、:19、:74、:75、:84）；Mermaid 節點仍是英文顯示文字（:31「加preprocessing」、:32「detector<br/>…」、:34「classifier<br/>…」）。flowchart 節點可翻譯（實測通過），STYLE 也要求翻譯。
- E3【中】04/18 :3「讓讓相符的影像」重複字，為已修復項引入的誤植（見上方該課附帶項）。
- E4【低】09-image-generation-gans :14「譜正規化（spectral normalization）（spectral norm）」括註重複。
- E5【中】「抽樣」在生成語境違反 GLOSSARY（sampling 生成用「取樣」）。未被 r2 覆蓋的課：04/09（:239、:251、:294）、04/10（:13、:15、:21、:69、:90、:106 等，含「抽樣器（sampler）」）、04/11（:3、:19、:21、:51、:146）。已修復的課有 04/23、04/28、05/09、05/16、05/20。04/12 的「影格抽樣」屬選取語境，不算違規。
- E6【低】中英之間缺半形空格：05/17 :50「是LLM agent」、05/28 :3「long-context evaluation告訴你」。

---

## Summary

- 總數：100 條「維持原樣」（編號 #1–#100 為報告內順序，與 kept-items 清單一致）。
  - [ok] 11：#3、#7、#9、#16、#17、#18、#33、#34、#51、#68、#93。
  - [borderline] 38：圖片 alt 18 條（#56、#60、#61、#64、#65、#69、#71、#73、#74、#75、#79、#81、#83、#87、#90、#94、#97、#99）；其他 20 條（#2、#11、#13、#14、#15、#22、#28、#30、#45、#52、#55、#58、#59、#62、#63、#72、#80、#86、#91、#100）。
  - [miss] 51：P0 2（#41、#96）、P1 38、P2 11（#10、#21、#27、#29、#32、#35、#37、#49、#77、#85、#89）。

- miss 依主因分類（各條只計一類）：
  - GLOSSARY 指定譯名或保留英文未遵守（P1，6）：#19、#20（IoU 未用「交並比（IoU）」）、#23（GAN 標題）、#25（VAE）、#26（「抽樣」應為「取樣」）、#36（「對比」應為「對比式學習」）。
  - 專門術語首見未附英文、縮寫缺全名（P1，31）：#1、#4、#5、#6、#8、#12、#24、#31、#38、#39、#40、#42、#43、#44、#46、#47、#48、#50、#53、#54、#57、#66、#67、#70、#76、#78、#82、#84、#88、#92、#95。
  - 語意誤譯（P1，1）：#98。
  - 整句英文殘留或資訊失真（P0，2）：#41、#96。
  - 翻譯腔、口語、標點、跨課一致性（P2，11）。

- 駁回理由與判定的交叉統計（kept-items 原理由 → 本次判定）：
  - 「基礎通用詞彙無需加註英文，避免版面冗贅」18 條：17 條 miss、1 條 borderline（#59）。這類理由多數套用在 ML、RAG、SSL、OCR、MOT 等專門術語上，不是 STYLE.md 所允許的一般 CS 詞。
  - 「保留原結構以維護受保護格式與公式」9 條：7 條 miss（多為一般散文或 H1 標題，不屬受保護內容）、1 條 ok（#33，Mermaid 邊標籤，STYLE 與檢查器都保護）、1 條 borderline（#63）。
  - 「原譯符合臺灣技術語境且行文流暢」71 條：26 條 miss、35 條 borderline（含 alt 18 條）、10 條 ok。
  - 「篇章術語已具備繁中正式譯名，保留版面簡潔」2 條：1 條 miss（#1）、1 條 borderline（#2）。

- miss 優先修正清單（課程以 phase-lesson 編號標示，行號為現況 zh-TW.md）：
  1. P0 #96（05-27 :32）：刪除英文整句「GPT-4o-mini $0.003 per scored case enables …」，保留中文譯文。
  2. P0 #41（04-19 :54）：CTC 句補上「機率」，譯為對齊機率的加總（marginalises）。
  3. P1 GLOSSARY 指定譯名（6 條）：04-09 :1 GAN 標題→「生成對抗網路（GAN）」；04-11 :3 VAE→「變分自編碼器（VAE）」；04-06 :13、04-07 :15 IoU→「交並比（IoU）」；04-11 :3「抽樣」→「取樣」並改寫「由……來轉」；04-17 :12「對比」→「對比式學習（contrastive learning）」。
  4. P1 縮寫缺全名（6 條）：05-21 :165 RTE；05-22 :40 MTEB；05-26 :21、:35 AEVS；05-27 :20、:45 RAG 指標；04-19 :80–81 CER／WER；04-21 :12、:61、:80 關鍵點術語。
  5. P1 語意誤譯（3 條，#70、#67 亦計入上方「專門術語」類）：05-28 :3「廣告」（advertise）→「宣稱」，並補 long-context evaluation 的譯文與空格；05-17 :50、:163「接地」→ 補 grounding 英文並改譯；05-16 :33「分岔因子」→「分支數（branching factor）」。
  6. P1 其餘專門術語首見未附英文（23 條）：#1、#4、#5、#6、#8、#12、#24、#31、#38、#40、#42、#43、#46、#47、#48、#50、#53、#54、#57、#66、#82、#84、#88。修法單純（首見補括註），可一次處理。
  7. P2 風格（11 條）：#10（03-12 :218「一等支援」）、#21（04-07 :259「巨觀平均」→「宏平均」，與 05-05 一致）、#27（04-11 :50「從潛在去注意」）、#29（04-12 :12「怎麼換」）、#32（04-15 :241）、#35（04-16 :92「乘上去」）、#37（04-17 :42「損失在說」）、#49（04-28 :48、:73「轉它」）、#77（05-21 :3「承重的」）、#85（05-24 :3）、#89（05-25 :12）引號後句號重複。

- 需要 supervisor 決策（不屬譯文修正，未擅自決定）：
  - 決策 A：圖片 alt 文字（18 條）。檢查器把整段 `![alt](src)` 列為 protected span，改譯必然失敗（已實測）。選項一：接受 alt 保留英文，並把審閱理由改為「檢查器保護」；選項二：調整 `scripts/check_translation.py` 的 IMAGE 保護範圍，只保護 `(src)`，之後再統一翻譯 alt。
  - 決策 B：04-03 Mermaid 時間軸（#13，:29–33）。檢查器不剝離 timeline 標籤，改譯會報錯（已實測）。選項一：擴充 `_mermaid_syntax` 支援 timeline 後翻譯；選項二：明確豁免並記錄。
  - 決策 C（譯者取捨，非阻塞）：其餘 borderline 用詞，如「閘」「短程」「前 k 段」「句子 transformer」「切分倍率稅」「不理延遲的尾端」「表面 NLP」「DST 轉折」等。

- 驗證與限制：
  - 本次只寫入本報告與暫存輔助檔（`/private/tmp/zh-tw-review/kept-items.tsv`、`locate.py`），未修改任何譯稿或 repo 檔案；`git diff --cached --name-only` 結果為 0，未暫存任何檔案。repo 內既有的未追蹤目錄 `docs/plans/` 並非本次產生。
  - 檢查器行為實測（alt 保護、timeline 不剝離、flowchart 節點可改、`|邊標籤|` 不可改）是在暫存字串上以唯讀方式呼叫 `_protected_spans` 與 `_mermaid_syntax` 完成，未改動 `scripts/`。
  - 本次只稽核「維持原樣」100 條，未稽核「已修復」的 285 條。範圍外 E1–E6 是在查核過程中順帶發現的，不代表完整抽驗。
  - 所有行號均為現況 zh-TW.md 行號，報告原行號已偏移。
