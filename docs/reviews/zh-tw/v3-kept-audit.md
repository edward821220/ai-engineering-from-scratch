# v3 維持原樣（kept）條目獨立複審

範圍：docs/reviews/zh-tw/r3.md 內全部 133 條「維持原樣」駁回（70 課，phase 06/07/08/09/11）。唯讀驗證，未修改任何譯稿。
譯稿：/private/tmp/aiefs-zh-tw-work/i18n/zh-TW/phases/<phase>/<lesson>/docs/zh-TW.md（現況；行號多已偏移，以關鍵字定位）。原稿：/private/tmp/aiefs-main-source/phases/<phase>/<lesson>/docs/en.md。詞表：i18n/zh-TW/GLOSSARY.md。
標記：`(rN.md:L)` 為該條在 docs/reviews/zh-tw/r3.md 的行號。

判定依據摘要：
- 首見英文：STYLE.md 與 GLOSSARY 標頭要求「中文譯名第一次出現在每課時附英文」；通用 CS 詞（程式碼、記憶體、網路、套件、框架、預設…）免附；領域術語（ML／RL／音訊／圖形／LLM 專門詞）未附即 miss。以腳本掃描每課首次出現位置，再人工判讀。
- GLOSSARY 譯法：以 GLOSSARY「譯法」欄為準（禁用欄由 check_translation.py 把關，譯法欄不在 gate 內）。
- 結構：官方 `scripts/check_translation.py --phase` 對 phase 06（17 課）、07（16）、08（15）、09（12）、11（17）全數 passed。段落空行差異未被 gate 攔截，故列為 borderline。
- 替代文字：check_translation.py 將整段 `![alt](path)` 列為受保護跨度，改譯會使 protected spans 不符，故 alt 英文判 ok。

---

## phases/06-speech-and-audio/01-audio-fundamentals
- [miss] K001（r3.md:7）「頻率箱／箱」→ frequency bin 應為「頻率槽」且首見附英文 → 現況：L43「每個頻率槽一個」首見無英文；L93「峰應該在箱 `440 * N / sr`」、L119「預期的箱上有三個峰」、L134 表格「鏡射到較低的箱」仍用「箱」（GLOSSARY frequency bin=頻率槽）→ 修法：L43 補「頻率槽（frequency bin）」，L93／L119／L134 的「箱」全改「頻率槽」。
- [miss] K002（r3.md:8）「降取樣」→ downsampling 應為「降採樣（downsampling）」→ 現況：L39「降採樣之前一定要先低通濾波」已採詞表譯名，但首見未附 downsampling（低）→ 修法：L39 補「（downsampling）」。
- [miss] K003（r3.md:10）首見中文術語缺英文 → 現況：L3「原始訊號」(signal)、L12「神經網路吃的是張量」(tensor)、L16「用什麼取樣率錄的」(sample rate)、L17「有沒有混疊」(aliasing)、L39「*奈奎斯特頻率*」(Nyquist frequency)、L41「**位元深度。**」(bit depth) 首見皆無英文；L47 STFT 已附 → 修法：六處首見補英文。張量、取樣率、混疊屬領域術語，駁回理由「篇章術語已具備繁中譯名」不成立。
- [miss] K004（r3.md:14）「幅度」→ GLOSSARY magnitude=「長度／大小」（或「模」），magnitude spectrum=「振幅頻譜」，amplitude=「振幅」 → 現況：L43「幅度是那個頻率的振幅」同段 amplitude 亦譯「振幅」，易混；L121「畫幅度」→ 修法：magnitude 改「模（magnitude）」或「振幅頻譜」，與振幅區分。

## phases/06-speech-and-audio/03-audio-classification
- [miss] K005（r3.md:30）首見中文技術術語未附英文 → 現況：L30「### 真正的挑戰是類別不平衡」、L20「算餘弦相似度」、L24「監督式學習」、L34「平衡抽樣」、L161「回報混淆矩陣」（GLOSSARY confusion matrix）、L163「交叉驗證準確率」（GLOSSARY cross-validation）首見皆無英文 → 修法：補 class imbalance／cosine similarity／supervised learning／balanced sampling／confusion matrix／cross-validation。巨觀 F1、mAP 已附英文。

## phases/06-speech-and-audio/04-speech-recognition-asr
- [miss] K006（r3.md:35）「束搜索」→「集束搜尋（beam search）」→ 現況：全篇已統一「集束搜尋」（L28、L74、L92、L164、L176），但首見 L28 未附 beam search（低）→ 修法：L28 補「（beam search）」。
- [miss] K007（r3.md:36）首見術語未附英文 → 現況：L12「音框和字元不是一對一」(frame)、L18「注意力編碼器–解碼器」(attention encoder–decoder)、L28「*條件獨立假設*」(conditional independence assumption)、L153「子詞」(subword) 首見無英文；「語音辨識」（標題）與「詞錯誤率（Word Error Rate）」已附 → 修法：補上述四項英文。

## phases/06-speech-and-audio/05-whisper-architecture-finetuning
- [miss] K008（r3.md:41）首見中文術語缺英文 → 現況：L3「弱監督音訊」(weakly supervised)、L3「30 秒視窗」(window；GLOSSARY window=視窗)、L14「領域偏移」(domain shift)、L41「時間戳」(timestamp)、L45「較短的要填充」(padding) 首見皆無英文；finding 所引「低秩轉接器」譯稿無此詞 → 修法：補英文。
- [ok] K009（r3.md:44）「一行，2026 年最強的通用 ASR」one-liner → 現行譯稿 L124 已無此句（現為標準 Trainer 迴圈句），en.md 亦無 one-liner；來源文字已失效 → 駁回合理，無需修改。

## phases/06-speech-and-audio/06-speaker-recognition-verification
- [miss] K010（r3.md:47）首見術語未附英文 → 現況：L12「未知的語者（*開放集合*）」(open-set)、L14「通道偏移」(channel shift)、L14「角度邊界」(angular margin)、L16「決策閾值」(threshold；GLOSSARY 閾值)、L22「餘弦相似度」(cosine similarity)、L36「分數正規化」(score normalization) 首見無英文 → 修法：補英文。

## phases/06-speech-and-audio/07-text-to-speech
- [miss] K011（r3.md:51）mel 譯名未依 GLOSSARY（mel-spectrogram=「梅爾頻譜圖」）→ 現況：L17「文字到 mel 頻譜圖」、L48「Mel 頻譜圖是內部表示」、L124「mel 頻譜圖重建損失」、L174「Mel 到波形」全篇仍混用 → 修法：統一「梅爾頻譜圖（mel-spectrogram）」，首見附英文。
- [miss] K012（r3.md:52）首見中文術語未附英文 → 現況：L12「韻律正確」(prosody)、L16「轉成音素」(phoneme)、L18「聲碼器」(vocoder)、L20「流匹配」(flow matching)、L30「變分推論」(variational inference；GLOSSARY) → 修法：補英文。

## phases/06-speech-and-audio/08-voice-cloning-conversion
- [miss] K013（r3.md:58）首見術語未附英文 → 現況：L27「零樣本仿製」(zero-shot cloning)、L36「自編碼器」(autoencoder)、L36「潛在空間」(latent space)、L38「神經編解碼器」(neural codec)、L44「同意紀錄」(consent record) 首見皆無英文；finding 所引「語碼」譯稿無此詞 → 修法：補英文。
- [borderline] K014（r3.md:59）「說話人」→「語者／說話者」→ 現況：全篇 11 次「說話人」（如 L3、L19、L27、L36、L152）；不在 GLOSSARY，屬大陸用語傾向，STYLE.md 要求避免中國慣用詞 → 取捨：屬用語偏好而非詞表硬性違規；若改，須與 06/06、06/10 等同步統一，建議低優先。

## phases/06-speech-and-audio/09-music-generation
- [miss] K015（r3.md:63）首見術語未附英文 → 現況：L16「局部重畫」(inpainting)、L16「分軌」(stems)、L69「浮水印」(watermark)、L69「中繼資料」(metadata)、L102「色度圖」(chromagram) 首見無英文 → 修法：補英文。

## phases/06-speech-and-audio/10-audio-language-models
- [miss] K016（r3.md:67）首見術語未附英文 → 現況：L1 標題「音訊語言模型」(audio-language model)、L3「多音訊任務」(multi-audio)、L15「語意推理」(semantic reasoning)、L29「音訊編碼器」(audio encoder)、L159「說話人歸屬」(speaker attribution)、L171「音訊說明文字」(audio captioning) → 修法：補英文（含標題）。

## phases/06-speech-and-audio/11-real-time-audio-processing
- [miss] K017（r3.md:71）首見術語未附英文 → 現況：L24「全雙工」(full-duplex)、L30「音框」(frame)、L32「環形緩衝」(ring buffer)、L42「抖動緩衝」(jitter buffer)、L46「執行緒爭用」(thread contention) → 修法：補英文（批次管線已於 L3 附英文，不列）。

## phases/06-speech-and-audio/12-voice-assistant-pipeline
- [miss] K018（r3.md:74）首見術語未附英文 → 現況：L30「音訊擷取」(audio capture)、L170「結束點」(endpoint)、L171「預捲」(pre-roll) 首見皆無英文；finding 所引「對話式 AI」「延遲預算」「第一字裁切」譯稿無此詞 → 修法：補英文。

## phases/06-speech-and-audio/15-streaming-speech-to-speech-moshi-hibiki
- [miss] K019（r3.md:84）首見術語未附英文 → 現況：L12「延遲下限」(latency floor)、L16「音框」(frame)、L46「強化學習」(reinforcement learning) 首見皆無英文 → 修法：補英文。

## phases/06-speech-and-audio/16-anti-spoofing-audio-watermarking
- [miss] K020（r3.md:89）首見術語未附英文 → 現況：L1 標題「反仿冒」(anti-spoofing)、「音訊浮水印」(audio watermarking) 無英文；L16「可驗證的出處」(verifiable provenance)、L67「位元回復準確率」(bit recovery accuracy) → 修法：標題與首見處補英文。

## phases/06-speech-and-audio/17-audio-evaluation-metrics
- [miss] K021（r3.md:97）首見術語未附英文（低）→ 現況：多數已由英文縮寫緊鄰附註（CER、RTFx、MOS、DER）；仍缺 L3「語音辨識（WER、CER、RTFx）」之 speech recognition（括號內為指標名）、L46「說話人編碼器」之 speaker encoder（SECS 縮寫只指「說話人編碼器餘弦相似度」整體）→ 修法：L3 補「（speech recognition）」，L46 補「（speaker encoder）」。

## phases/07-transformers-deep-dive/01-why-transformers
- [miss] K022（r3.md:100）首見術語未附英文 → 現況：L12「序列模型」(sequence model) 首見無英文（循環神經網路、梯度消失、隱藏狀態、歸納偏差、狀態空間模型已附）；L14「平行化」「串列步驟」為次要 → 修法：L12 補「序列模型（sequence model）」。

## phases/07-transformers-deep-dive/02-self-attention-from-scratch
- [borderline] K023（r3.md:103）引導句與清單間空行（原文 "Every token generates three vectors:" 與清單相連；"This lesson produces:" 同）→ 現況：zh L39「每個 token 產生三個向量：」後空一行（L40），L310「這一課產出：」後空一行；官方檢查器通過 → 取捨：僅空行差異，內容與渲染無實質影響；若要嚴格對齊 STYLE「段落一一對應」，刪引導句後空行。
- [miss] K024（r3.md:104）「加權和」→ GLOSSARY weighted sum=「加權總和」→ 現況：L12「softmax 的加權和」、L45「輸出是值的加權和」、L135「### 值的加權和」、L137「所有值向量的加權和」→ 修法：全改「加權總和」（L156 圖節點同）。
- [miss] K025（r3.md:105）首見術語未附英文 → 現況：L3「查詢表」（query 首見未附）、L12「投影」(projection)、L14「注意力矩陣」(attention matrix)、L45「注意力分數」(attention score) → 修法：補英文。

## phases/07-transformers-deep-dive/03-multi-head-attention
- [miss] K026（r3.md:108）首見術語未附英文 → 現況：L3「注意力頭」(attention head)、L14「投影」(projection)、L14「子空間」(subspace)、L16「鍵」(key，首見無英文)、L39「潛在空間」(latent space) → 修法：補英文。

## phases/07-transformers-deep-dive/04-positional-encoding
- [miss] K027（r3.md:112）首見術語未附英文 → 現況：L1 標題「位置編碼」(positional encoding)、L18「外推」(extrapolation)、L20「注意力分數」(attention score)、L74「相對位置」(relative position) → 修法：補英文；finding 所引「順序不變性」「絕對正弦位置編碼」譯稿無此詞。

## phases/07-transformers-deep-dive/05-full-transformer
- [miss] K028（r3.md:116）首見術語未附英文 → 現況：L24「位置訊號」(position signal)、L27「殘差連接」(residual connection)、L28「層正規化」(layer normalization)、L28「殘差流」(residual stream)、L75「參數數量」(parameter count) → 修法：補英文。

## phases/07-transformers-deep-dive/06-bert-masked-language-modeling
- [miss] K029（r3.md:119）首見術語未附英文 → 現況：L12「預訓練」(pretraining)、L45「分布偏移」(distribution shift) 首見皆無英文；finding 所引「雙向編碼器」譯稿無此詞 → 修法：補英文。

## phases/07-transformers-deep-dive/07-gpt-causal-language-modeling
- [miss] K030（r3.md:123）GLOSSARY next-token prediction 保留英文（禁用「下一個詞預測」）→ 現況：L16「一次前向就得到 N 個平行的下一個 token 預測」未保留英文；首見未附英文：L16「因果遮罩」(causal mask)、L39「前綴平均」(prefix averaging)、L65「列隨機矩陣」(row-stochastic matrix)、L99「溫度」(temperature) → 修法：改「next-token prediction」並補英文。

## phases/07-transformers-deep-dive/08-t5-bart-encoder-decoder
- [miss] K031（r3.md:126）首見術語未附英文 → 現況：L1 標題「編碼器–解碼器模型」、L19「稠密表示」(dense representation)、L23「遮罩區段預測」(masked span prediction)、L24「去噪自編碼器」(denoising autoencoder)、L71「文字填空」(text infilling)、L113「哨兵 token」(sentinel token) → 修法：補英文。

## phases/07-transformers-deep-dive/09-vision-transformers
- [miss] K032（r3.md:130）首見術語未附英文 → 現況：L3「圖塊」(patch) 首見無英文、L14「線性投影」(linear projection)；finding 所引「監督式預訓練」「自監督特徵」譯稿無此詞 → 修法：補英文。

## phases/07-transformers-deep-dive/10-audio-transformers-whisper
- [miss] K033（r3.md:133）mel 譯名未依 GLOSSARY（mel-spectrogram=梅爾頻譜圖；frequency bin=頻率槽；spectrogram=頻譜圖）→ 現況：L18「對數 mel 頻譜」、L28「對數 mel 頻譜」、L104「### 步驟 2：對數 mel 頻譜（簡化）」、L116「代替 mel 頻帶」、L173「80 個 mel 頻帶」、L181「對數 mel」→ 修法：統一「梅爾頻譜圖」「梅爾頻率槽」「對數梅爾頻譜圖」，首見附英文。
- [miss] K034（r3.md:134）首見術語未附英文；頻譜未依詞表 → 現況：L17「語音活動偵測」(voice activity detection)、L17「語言辨識」(language identification)、L17「時間戳記」(timestamp)、L18「編碼器–解碼器」(encoder–decoder)、L32「步幅」(stride)、L168「前處理」(preprocessing) 首見無英文 → 修法：補英文。

## phases/07-transformers-deep-dive/11-mixture-of-experts
- [borderline] K035（r3.md:138）「When to pick MoE」「When NOT to pick MoE」引導句後空行（zh L131、L137；en L131、L136 無空行）→ 取捨：僅格式，官方檢查器通過；可刪空行對齊原文。
- [miss] K036（r3.md:140）首見術語未附英文 → 現況：L14「路由器」(router)、L14「活躍參數」(active parameters)、L44「### 負載平衡的問題」(load balancing)、L49「專家容量」(expert capacity)、L54「### 共用專家」(shared experts)、L58「細粒度專家」(fine-grained experts)、L79「專家平行」(expert parallelism) 首見無英文；L50「輔助損失」括號內為論文名（DeepSeek-V3），不算附英文 → 修法：補英文。

## phases/07-transformers-deep-dive/12-kv-cache-flash-attention
- [borderline] K037（r3.md:143）「2026 defaults」引導句後空行（zh L106「2026 年的預設：」後空行；en L106 與清單相連）→ 取捨：同 K035，格式差異。
- [miss] K038（r3.md:144）GLOSSARY speedup=「加速比」、forward pass=「前向傳遞」→ 現況：「加速」見 L93 表頭「參考硬體上的加速」、L108「2 到 3 倍加速」、L109「2 到 4 倍加速」、L213「相對每次重新編碼 P 的加速」；「前向」見 L87、L98、L100、L104「你付 1 次大模型前向」、L213 → 修法：加速→加速比（含表頭）；前向→前向傳遞。
- [miss] K039（r3.md:145）首見術語未附英文 → 現況：L12「隱藏狀態」(hidden state；GLOSSARY)、L19「分塊」(tiling)、L174「工作集」(working set)、L204「前綴快取」(prefix caching) → 修法：補英文。HBM／SRAM 原文即英文，駁回此子項合理。

## phases/07-transformers-deep-dive/13-scaling-laws
- [miss] K040（r3.md:149）首見術語未附英文 → 現況：L12「訓練運算」(training compute)、L40「損失天花板」(loss floor)、L51「運算最佳」(compute-optimal)、L127「資料策展」(data curation)、L127「漸近線」(asymptote)、L137「運算最佳前緣」(compute-optimal frontier)、L150「突現能力」(emergent abilities) → 修法：補英文。

## phases/07-transformers-deep-dive/14-build-a-transformer-capstone
- [miss] K041（r3.md:154）首見術語未附英文 → 現況：L14「端到端訓練」(end-to-end)、L60「訓練迴圈」(training loop；GLOSSARY)、L76「驗證損失」(validation loss)、L87「位元組級」(byte-level)、L171「梯度裁剪」(gradient clipping)、L172「學習率排程」(learning-rate schedule) → 修法：補英文。

## phases/07-transformers-deep-dive/15-attention-variants
- [miss] K042（r3.md:157）首見術語未附英文 → 現況：L1 標題「稀疏」(sparse)、L14「拓樸」(topology)、L17「區塊注意力」(block attention)、L18「差分注意力」(differential attention)、L50「稀疏模式」(sparse pattern) → 修法：補英文；標題「稀疏」可依 GLOSSARY sparsity=「稀疏性」統一用語。

## phases/08-generative-ai/01-generative-models-taxonomy-history
- [miss] K043（r3.md:163）GLOSSARY 違規：forward pass=「前向傳遞」、noise schedule=「雜訊排程」→ 現況：L26「推論很快，一次前向」；L127「沒有噪聲排程」→ 修法：前向→前向傳遞；噪聲排程→雜訊排程。finding 列舉的「對 log p(x) 取樣」「前向傳遞」等字串在譯稿中多不存在，需以實際行文為準。

## phases/08-generative-ai/02-autoencoders-vae
- [miss] K044（r3.md:166）首見術語未附英文 → 現況：L12「編碼空間」(encoding space)、L16「KL 懲罰」(KL penalty)、L113「潛在空間」(latent space) 首見皆無英文 → 修法：補英文。

## phases/08-generative-ai/03-gans-generator-discriminator
- [miss] K045（r3.md:169）首見術語未附英文 → 現況：L1 標題「GAN——產生器對鑑別器」(generator／discriminator)、L30「純量機率」(scalar)、L37「**訓練迴圈。**」(training loop) → 修法：補英文（含標題）。

## phases/08-generative-ai/04-conditional-gans-pix2pix
- [miss] K046（r3.md:173）首見術語未附英文 → 現況：L14「配對資料」(paired data)、L26「感受野」(receptive field)、L142「吞吐量」(throughput) 首見皆無英文；finding 所引「無條件 GAN」「知覺損失」譯稿無此詞 → 修法：補英文。

## phases/08-generative-ai/06-diffusion-ddpm-from-scratch
- [borderline] K047（r3.md:180）「三個直覺」三項之間無空行（zh L50–52 相連；en L50、L52 間有空行）→ 取捨：格式差異，內容不變，官方檢查器通過。
- [miss] K048（r3.md:181）首見術語未附英文 → 現況：L12「鞍點」(saddle point)、L20「前向過程」(forward process)、L28「反向過程」(reverse process)、L95「### 步驟 4：反向取樣」(reverse sampling)、L111「## 時間條件」(time conditioning)、L170「漸進蒸餾」(progressive distillation) → 修法：補英文。

## phases/08-generative-ai/07-latent-diffusion-stable-diffusion
- [borderline] K049（r3.md:184）Stage 1／Stage 2 兩項之間空行（en L24、L26 間有空行；zh L24–25 相連）→ 取捨：格式差異，可刪空行對齊。

## phases/08-generative-ai/08-controlnet-lora-conditioning
- [borderline] K050（r3.md:188）LoRA 與 ControlNet-lite 項目間空行（en L77、L79 有空行；zh L77–78 相連）→ 取捨：格式差異。
- [miss] K051（r3.md:190）GLOSSARY base model=「基模型」→ 現況：L54「每個基底模型大約 20 MB」；首見未附英文：L1 標題「條件」(conditioning)、L26「跳躍連接」(skip connection)、L32「恆等」(identity)、L42「線性層」(linear layer)、L54「交叉注意力」(cross-attention)、L104「執行時縮放」(runtime scaling)、L138「影像條件配接器」(image-conditioning adapter) → 修法：基底模型→基模型；補英文。

## phases/08-generative-ai/09-inpainting-outpainting-editing
- [miss] K052（r3.md:193）GLOSSARY noise=「雜訊」（隨機雜訊、雜訊排程）→ 現況：「噪聲」仍用於擴散雜訊：L48「幾乎從噪聲生成」、L77「輸出 5 維的噪聲預測」、L137「帶噪聲程度的圖生圖」；「條件訊號」已統一（L38） → 修法：噪聲→雜訊（全篇）。
- [miss] K053（r3.md:194）首見術語未附英文 → 現況：L28「前向擴散」(forward diffusion)、L38「條件訊號」(conditioning signal)、L56「邊界假影」(boundary artifacts)、L79「反向過程」(reverse process)、L99「遮罩膨脹」(mask dilation) → 修法：補英文；finding 所引「接縫殘差」「影像分割」「CPU 卸載」譯稿無此詞。

## phases/08-generative-ai/10-video-generation
- [miss] K054（r3.md:197）首見術語未附英文 → 現況：L14「時空壓縮」(spatiotemporal compression)、L15「時間一致性」(temporal consistency)、L97「耦合」(coupling)、L119「長寬比」(aspect ratio；GLOSSARY 有詞條) → 修法：補英文。

## phases/08-generative-ai/12-3d-generation
- [borderline] K055（r3.md:203）「Two 2023-2024 innovations on top:」引導句後空行（zh L31「上面還有兩個 2023 到 2024 的新做法：」後空行）→ 取捨：格式差異，內容不變。
- [miss] K056（r3.md:204）GLOSSARY runtime=「執行環境」、optimizer=「最佳化器」→ 現況：L151「沒有單一主導的執行期（runtime）」、L157「離線調校器（optimizer，慢）」→ 修法：改「執行環境（runtime）」「最佳化器（optimizer）」。
- [miss] K057（r3.md:205）首見術語未附英文 → 現況：L29「可微分」(differentiable)、L142「密度」(density)、L129「基礎模型」(foundation model)、L157「推論伺服器」(inference server) → 修法：補英文。NeRF、triplane、SDS、Gaussian Splatting 原文即英文，駁回此子項合理。

## phases/08-generative-ai/13-flow-matching-rectified-flows
- [miss] K058（r3.md:208）首見術語未附英文 → 現況：L1 標題「整流流」(rectified flow)、L12「反向過程」(reverse process)、L12「隨機遊走」(random walk)、L63「蒸餾」(distillation)、L161「部署配方」(deployment recipe) → 修法：補英文。

## phases/08-generative-ai/14-evaluation-fid-clip-score
- [borderline] K059（r3.md:211）「Failure modes」標題與清單之間空行（zh L34、L50、L68 後空行；en 相連）→ 取捨：格式差異，三處同類。
- [miss] K060（r3.md:213）首見術語未附英文 → 現況：L1 標題「人類偏好」(human preference)、L12「樣本品質」(sample quality)、L32「多變量高斯」(multivariate Gaussian)、L37「特徵抽取器」(feature extractor)、L83「質性檢視」(qualitative inspection)、L91「特徵向量」(feature vector)、L152「樣本數」(sample size) → 修法：補英文。

## phases/08-generative-ai/19-visual-autoregressive-var
- [borderline] K061（r3.md:216）「Three structural wins」與 Build It 子步驟引言後空行（zh L75 後空行；en L73 起相連）→ 取捨：格式差異。
- [miss] K062（r3.md:217）首見術語未附英文 → 現況：L1 標題「下一尺度預測」(next-scale prediction)、L12「自迴歸生成」(autoregressive generation)、L78「尺度內平行生成」(intra-scale parallel generation)、L92「條件分布」(conditional distribution)、L107「注意力遮罩」(attention mask)、L111「尺度數量」(number of scales) → 修法：補英文。

## phases/09-reinforcement-learning/02-dynamic-programming
- [miss] K063（r3.md:224）GLOSSARY policy=「策略」→ 現況：本課「政策」27 次、「策略」0 次（如 L16「黃金標準政策」、L26「給定政策 `π`」）→ 修法：全文改「策略」（策略迭代、策略評估、最佳策略、隨機策略）。
- [miss] K064（r3.md:225）首見術語未附英文 → 現況：L16「模型式 RL」(model-based RL)、L22「不動點迭代」(fixed-point iteration)、L39「終止狀態」(terminal state)、L49「隨機變體」(stochastic variant)、L142「平手規則」(tie-breaking rule)、L199「同步更新」(synchronous update) → 修法：補英文。

## phases/09-reinforcement-learning/03-monte-carlo-methods
- [miss] K065（r3.md:228）多項 GLOSSARY 違規 → 現況：「政策」25 次、「策略」2 次（policy=策略）；「重要性抽樣」見 L36、L141、L198（importance sampling=「重要性取樣」）；「估計器」見 L16、L30、L156（estimator=「估計量」）；「報酬」4 次（reward=「獎勵」）→ 修法：依詞表統一。
- [miss] K066（r3.md:229）首見術語未附英文 → 現況：L3「強化學習」「動態規劃」「回報」、L24「每次造訪」(every-visit)、L26「增量平均」(incremental mean)、L32「探索」(exploration)、L34「覆蓋」(coverage)、L38「控制」(control)、L106「同政策」(on-policy)、L186「偏差－變異取捨」(bias–variance tradeoff) → 修法：補英文。

## phases/09-reinforcement-learning/04-q-learning-sarsa
- [miss] K067（r3.md:233）GLOSSARY policy=「策略」、reward=「獎勵」→ 現況：「政策」17 次、「策略」0 次；「報酬」6 次 → 修法：改詞。statistical variance 譯「變異」（L12、L16）屬 GLOSSARY variance 備註允許的 bias–variance 語境，不列為違規。
- [miss] K068（r3.md:234）首見術語未附英文 → 現況：L3「蒙地卡羅」(Monte Carlo)、L14「動態規劃」(dynamic programming)、L16「轉移」(transition)、L16「一步目標」(one-step target)、L34「探索」(exploration)、L34「貪婪」(greedy)、L42「探索雜訊」(exploration noise)、L130「重放緩衝」(replay buffer)、L130「目標網路」(target network)、L188「資格跡」(eligibility traces) → 修法：補英文。

## phases/09-reinforcement-learning/05-dqn
- [miss] K069（r3.md:238）GLOSSARY reward=「獎勵」、forward pass=「前向傳遞」→ 現況：「報酬」10 次、「獎勵」0 次（如 L38「報酬截斷」、L134「報酬尺度」）；L88「前向：線性 → ReLU → 線性」→ 修法：改「獎勵」「獎勵截斷」（依 reward=獎勵 類推）、「前向傳遞」。
- [miss] K070（r3.md:239）首見術語未附英文 → 現況：L16「轉移」(transition)、L20「超參數」(hyperparameter)、L30「梯度下降法」(gradient descent)、L127「特徵抽取器」(feature extractor)、L132「局部盆地」(local basin)、L135「冷啟動」(cold start)、L136「目標同步頻率」、L137「觀測前處理」(observation preprocessing) → 修法：補英文。

## phases/09-reinforcement-learning/06-policy-gradients-reinforce
- [miss] K071（r3.md:244）首見術語未附英文 → 現況：L131「熵獎勵」(reward)、L74「權重向量」(weight vector)、L76「對數機率」(log-probability)、L92「展開」(rollout)、L131「熵崩塌」(entropy collapse)、L133「樣本效率」(sample efficiency)、L135「功勞分配」(credit assignment)、L194「優勢」(advantage) → 修法：補英文。

## phases/09-reinforcement-learning/07-actor-critic-a2c-a3c
- [miss] K072（r3.md:249）首見術語未附英文 → 現況：L3「評論者」(critic)、L18「行動者」(actor)、L12「蒙地卡羅回報」(Monte Carlo)、L34「內插」(interpolation)、L44「高偏差、高變異」(high bias／high variance)、L46「平行環境」(parallel environments)、L48「非同步」(asynchronous)、L48「參數伺服器」(parameter server)、L54「價值回歸」(value regression)、L126「共享主幹」(shared trunk)、L127「重要性抽樣修正」(importance-sampling correction)、L142「聯賽訓練」(league training)、L142「模仿預訓練」(imitation pretraining) → 修法：補英文。

## phases/09-reinforcement-learning/08-ppo
- [miss] K073（r3.md:253）GLOSSARY policy=「策略」、proximal policy optimization=「近端策略最佳化（PPO）」、constraint=「限制條件」、code=「程式碼」→ 現況：L1 標題「近端政策（Proximal Policy Optimization，PPO）」；L16「信賴域政策（Trust Region Policy Optimization，TRPO）」；L16、L18「約束」；L18「多一行程式」；全篇「政策」→ 修法：改「近端策略最佳化（PPO）」「信賴域策略最佳化（TRPO）」「限制條件」「程式碼」，並全文政策→策略。
- [miss] K074（r3.md:254）首見術語未附英文 → 現況：L3「重要性比率」(importance ratio)、L36「優勢」(advantage)、L49「**訓練迴圈。**」(training loop)、L51「平行環境」(parallel environments)、L53「快照」(snapshot)、L139「梯度正負號」(gradient sign) → 修法：補英文。

## phases/09-reinforcement-learning/09-reward-modeling-rlhf
- [miss] K075（r3.md:259）首見術語未附英文；另 GLOSSARY reward 違規 → 現況：L3「獎勵」(reward)、L3「語言模型」(language model)、L14「純量報酬」(scalar)、L18「過程報酬模型」(process reward model)、L48「分布內／分布外」(in-/out-of-distribution)、L53「組內相對基準」(group-relative baseline)、L53「驗證器」(verifier)、L83「對數損失」(log loss)、L184「報酬蒸餾」 首見無英文；「策略」首見 L40 亦未附 policy；全篇「報酬」32 次、「獎勵」10 次（含 L1 標題「報酬模型」）→ 修法：reward 依詞表改「獎勵」（如「獎勵模型」），並補英文。

## phases/09-reinforcement-learning/10-multi-agent-rl
- [miss] K076（r3.md:264）首見術語未附英文 → 現況：L14「馬可夫性質」(Markov property)、L14「非定態」(non-stationary)、L16「集中訓練」「分散執行」「反事實基準」「聯賽對戰」「自我對弈」、L24「聯合動作」(joint action)、L24「完全合作」(fully cooperative)、L29「功勞分配」(credit assignment)、L30「策略」(policy)、L43「價值分解」(value decomposition)、L163「學習曲線」(learning curve) → 修法：補英文。
- [borderline] K077（r3.md:265）CTDE 段與「例子：」清單之間空行（zh L38–40；en L38–39 相連）→ 取捨：格式差異。

## phases/09-reinforcement-learning/11-sim-to-real-transfer
- [miss] K078（r3.md:270）首見術語未附英文 → 現況：L3「真實落差」(sim-to-real gap)、L14「飽和」(saturation)、L16「分布偏移」(distribution shift)、L22「條件分布」(conditional distribution)、L30「模型誤差」(model error)、L34「殘差模擬器」(residual simulator)、L35「觀測適應」(observation adaptation)、L37「特權學習」「教師」「學生」「蒸餾」→ 修法：補英文。（「死區」於括號內已附 deadband，不列。）

## phases/09-reinforcement-learning/12-rl-for-games
- [miss] K079（r3.md:274）GLOSSARY 違規 → 現況：policy=策略 — 「政策」17 次、「策略」1 次；reward=獎勵 — 「報酬」20 次、「獎勵」2 次；base model=基模型 — L67「基底模型」、L69「基底模型」；rejection sampling=拒絕取樣 — L71「拒絕抽樣（rejection sampling）」；L209「群組相對政策（Group Relative Policy Optimization）」→ 修法：依詞表統一（群組相對策略最佳化）。
- [miss] K080（r3.md:275）首見術語未附英文 → 現況：L1 標題「遊戲上的強化學習」(reinforcement learning)、L16「訊號」(signal)、L46「訓練迴圈」(training loop)、L46「潛在空間」(latent space)、L63「組內相對基準」(group-relative baseline)、L67「思維鏈」(chain of thought)、L71「軌跡」(trajectory)、L80「完美資訊」(perfect information)、L146「獎勵操弄」(reward hacking)、L151「消融」(ablation)、L200「完整序列」(full sequence) → 修法：補英文。

## phases/11-llm-engineering/01-prompt-engineering
- [miss] K081（r3.md:282）GLOSSARY provider=「服務供應商」（API 服務語境）→ 現況：本課「提供者」5 次、「服務供應商」0 次（L174 表格「提供者」）、「廠商」3 次 → 修法：改「服務供應商」，首見附 provider。

## phases/11-llm-engineering/02-few-shot-cot
- [miss] K082（r3.md:286）原文 "Add five words"，譯稿數量錯誤 → 現況：L21「加上這七個字——「我們一步一步思考」（Let's think step by step）」→ 修法：改「加上這 5 個英文單字」或「加上短短一句……」。
- [ok] K083（r3.md:287）「生成式 sampling 應用取樣」「組基準的變異／組平均」→ 現行譯稿無「組基準」「組平均」「變異」用詞（所引段落已不存在）；生成式 sampling 全篇採「抽樣」，符合 GLOSSARY sampling 預設譯法（「取樣」僅用於生成演算法名稱，如 top-k 取樣）→ 駁回合理。
- [miss] K084（r3.md:288）首見術語未附英文；前向傳播未依詞表 → 現況：L1 標題「少樣本、思維鏈與思維樹」(few-shot／CoT／ToT)、L15「零樣本」(zero-shot)、L21「溫度」(temperature)、L25「多數決」(majority vote)、L53「問答」(question answering；GLOSSARY)、L86「前向傳播」（GLOSSARY forward pass=前向傳遞）、L110「### 自洽性：多路抽樣，一次投票」(self-consistency)、L194「節點」(node)、L229「結構化提示」(structured prompting)、L229「分隔符號」(delimiters)、L25「工具呼叫」(tool calling) → 修法：補英文；前向傳播改前向傳遞。

## phases/11-llm-engineering/03-structured-outputs
- [miss] K085（r3.md:292）GLOSSARY provider=「服務供應商」→ 現況：L57「所有主流提供者皆原生支援此功能」→ 修法：改「服務供應商」，首見附 provider。
- [miss] K086（r3.md:293）首見術語未附英文 → 現況：L1 標題「受限解碼」(constrained decoding)、L3「幻覺」(hallucination)、L3「型別化資料」(typed data)、L16「擷取」(extraction)、L57「工具呼叫」(tool calling)、L59「解碼器」(decoder；GLOSSARY)、L521「詞彙表」(vocabulary)、L523「型別合規」(type compliance)、L525「信心分數」(confidence score) → 修法：補英文。

## phases/11-llm-engineering/04-embeddings
- [miss] K087（r3.md:298）首見術語未附英文；提供者未依詞表 → 現況：L13「餘弦相似度」(cosine similarity)、L13「提供者」（GLOSSARY 服務供應商）、L38「隱藏層」(hidden layer)、L95「群集」(clustering)、L107「內積」(inner product)、L139「召回率」(recall)、L163「分塊」(chunking)、L173「閾值」(threshold)、L184「雙編碼器」「交叉編碼器」(bi-encoder／cross-encoder)、L322「向量索引」(vector index)、L493「正交」(orthogonal) → 修法：補英文；提供者→服務供應商。

## phases/11-llm-engineering/05-context-engineering
- [miss] K088（r3.md:303）首見術語未附英文 → 現況：L1 標題「脈絡工程：視窗、預算、記憶與檢索」(context engineering)、L3「少樣本」(few-shot)、L3「工具定義」(tool definition)、L13「生成緩衝」(generation buffer)、L14「滑動視窗」(sliding window)、L147「動態脈絡組裝」(dynamic context assembly)、L323「動態工具挑選」(dynamic tool selection)、L562「餘弦相似度」(cosine similarity)、L562「語意去重」(semantic deduplication)、L564「脈絡回放」(context replay)、L568「脈絡壓縮器」(context compressor) → 修法：補英文（「迷失在中間（lost-in-the-middle）」已附英文，不列）。

## phases/11-llm-engineering/06-rag
- [miss] K089（r3.md:307）GLOSSARY provider=「服務供應商」、Euclidean distance=「歐幾里得距離」→ 現況：L78 表格「提供者」；L107「L2（歐氏）距離（Euclidean distance）」→ 修法：改「服務供應商」「歐幾里得距離」。
- [miss] K090（r3.md:308）首見術語未附英文 → 現況：L14「語意搜尋」(semantic search)、L101「內積」(inner product)、L179「吞吐量」(throughput)、L180「查詢延遲」(query latency)、L236「### 步驟 3：餘弦相似度搜尋」(cosine similarity search)、L407「資料來源歸屬」(source attribution)、L421「正交」(orthogonal)、L434「問答」(question answering)、L435「節點」(node) → 修法：補英文。

## phases/11-llm-engineering/07-advanced-rag
- [miss] K091（r3.md:312）英文例句整句未譯 → 現況：L22 中文段落內保留「真正包含答案的區塊寫著 "$47.2M in Q3 2025" but uses the word "earnings" instead of "revenue." The embedding model thinks "revenue strategy" is closer to the query than "Q3 earnings were $47.2M."」，僅在括號內補譯，屬未完成翻譯 → 修法：整句譯為繁中，只保留必要引文關鍵字。
- [miss] K092（r3.md:314）首見術語未附英文 → 現況：L26「近似最近鄰」(approximate nearest neighbor)、L40「骨幹」(backbone)、L47「詞頻」(term frequency)、L47「逆文件頻率」(inverse document frequency)、L47「文件頻率」(document frequency)、L47「飽和」(saturation)、L533「社群偵測」(community detection)、L15「多重查詢」(multi-query) → 修法：補英文。

## phases/11-llm-engineering/08-fine-tuning-lora
- [miss] K093（r3.md:318）英文殘句整句保留並重複譯 → 現況：L24「在雲端服務商租用兩張 A100 的花費為 $3-4/hour on cloud providers. Training for 3 epochs on 50,000 examples takes 6-10 hours. That's $30-40 per experiment（兩張 A100 每小時約 3-4 美元，…）」→ 修法：刪英文殘句，整合為單一繁中段落（租用成本、訓練時間、單次實驗成本）。
- [miss] K094（r3.md:320）GLOSSARY base model=「基模型」→ 現況：全篇「基礎模型」19 次、「基模型」0 次（如 L15）；首見未附英文：L13「預訓練」(pretraining)、L13「注意力層」(attention layer)、L22「最佳化器」(optimizer)、L38「線性層」(linear layer)、L57「參數縮減比例」(parameter reduction ratio)、L75「初始化」(initialization)、L77「縮放因子」(scaling factor)、L96「目標層」(target layers)、L118「適應能力」(adaptability)、L134「常態分布」(normal distribution)、L134「資料型別」(data type)、L138「顯存」(GPU memory)、L521「相關性係數」(correlation coefficient) → 修法：基礎模型→基模型；補英文。（「內在秩」已附英文，不列。）
- [miss] K095（r3.md:321）增譯與強化語氣 → 現況 L134：「神經網路權重高度服從常態分布」（原文 "roughly"，此處增強）；「其資訊損失顯著低於均勻 4 位元量化（INT4）」（原文 "loses less information"，增「顯著」）；「這在資訊理論上被證明是常態分布資料的最佳量化表示法」（原文無「被證明」）→ 修法：改「大致符合常態分布」、「保留的資訊比均勻 4 位元量化更多」，刪「被證明」。
- [miss] K096（r3.md:323）風格：過度渲染與直譯（抽驗 118 條列舉用語，63 條仍在）→ 現況例：L28「更深層的本質缺陷」、L30「絕不破壞」、L103「黃金甜蜜點」、L124「徹底重構」、L165「大爆發」、L171「權威經典」、L175「一站式全能」、L186「徹底消除」→ 修法：依 STYLE.md 改為節制的技術教材語氣（如「較深層的問題」「不會破壞」「最合適的折衷點」「大幅改變」）。

## phases/11-llm-engineering/09-function-calling
- [miss] K097（r3.md:325）例子與原文欄位不符 → 現況 L130：「從凌亂履歷中擷取出的 `{name, price, in_stock}` JSON 物件」；原文 "extract product info from text as {name, price, in_stock}" → 修法：改「從文字中擷取產品資訊」。
- [miss] K098（r3.md:328）首見術語未附英文；provider 未依詞表 → 現況：L13「函式呼叫迴圈」(function-calling loop)、L90「### 各家提供者對比」（GLOSSARY 服務供應商）、L113「### 平行函式呼叫」(parallel function calling)、L126「### 結構化輸出 vs 函式呼叫」、L148「速率限制」(rate limit)、L16「錯誤傳遞」、L180「### 步驟 1：定義工具註冊表」(tool registry) → 修法：補英文；提供者→服務供應商。
- [miss] K099（r3.md:329）風格：直譯、誇大、語意偏移（抽驗 104 條，63 條仍在）→ 現況例：L3「實體操作」、L24「免責聲明之下」、L26「真實溫度」「關鍵橋樑」、L109「陋習」、L115「一口氣」、L124「平行並行」→ 修法：改為「實際操作」「帶有免責聲明的幻覺」「目前溫度」「關鍵環節」「平行執行」等。

## phases/11-llm-engineering/10-evaluation
- [miss] K100（r3.md:336）首見術語未附英文；provider 未依詞表 → 現況：L13「評估資料集」(evaluation dataset)、L13「邊界情況」(edge cases)、L14「確定性斷言」(deterministic assertions)、L15「回歸測試」(regression testing)、L15「品質衰退」(quality regression)、L16「格式遵循度」(format compliance)、L20「幻覺率」(hallucination rate)、L24「基準測試」(benchmark)、L26「信賴區間」(confidence interval)、L60「語意相似度」(semantic similarity)、L62「語意品質」(semantic quality)、L64「人工評審」(human review)、L140「統計顯著性」(statistical significance)、L152「樣本規模」(sample size)、L199「少樣本」(few-shot)、L217「可觀測性」(observability)、L857「評分函式」(scoring function)；L766「模型提供者」（GLOSSARY 服務供應商）→ 修法：補英文；提供者→服務供應商。
- [miss] K101（r3.md:337）風格：過度渲染（抽驗 138 條，76 條仍在）→ 現況例：L3「賭博與祈禱」「護城河」、L24「必然下場」、L64「終極黃金標準」、L72「極致吞吐」、L106「客觀選出贏家」→ 修法：依 STYLE.md 改寫。

## phases/11-llm-engineering/11-caching-cost
- [miss] K102（r3.md:339）英文殘句 → 現況 L73：「一段 2,000 token 的系統提示平時需消耗 $0.005 normally costs $0.000625 on cache hits. Over 100K requests, that saves $437.50/day（…）」→ 修法：整句譯為繁中，刪英文殘句。
- [miss] K103（r3.md:341）增譯（高達、系統保證、無條件）→ 現況 L153：「提供高達 50% 的對折折扣優惠…系統保證在 24 小時內回傳運算結果」；L835：「提供無條件的 50% 半價優惠」（原文 "flat 50% discount"、"results come back within 24 hours"）→ 修法：改「固定 50% 折扣」「24 小時內回傳結果」，刪「高達」「系統保證」「無條件」。
- [miss] K104（r3.md:342）重複字與 Stop 規則缺漏 → 現況：L169「自動將所有請求降級導向平價平價模型」（重複）；L884「達 95% 時完全停用外部模型呼叫，僅提供快取庫存資料」未明示「拒絕新請求」（原文 reject new requests；L170 已正確）→ 修法：刪重複字；L884 補「拒絕新請求」。
- [miss] K105（r3.md:343）GLOSSARY threshold=「閾值」（禁用閥值）；provider=「服務供應商」→ 現況：「門檻」見 L67（表頭「最低快取門檻」）、L81、L317、L880「兩道相似度門檻」；「提供者」「原廠」見 L14、L24、L63、L65、L67、L79、L890 等 → 修法：門檻→閾值；提供者→服務供應商。
- [miss] K106（r3.md:344）首見術語未附英文 → 現況：L13「語意快取」(semantic caching)、L16「前綴快取」(prefix caching)、L96「精確快取」(exact caching)、L111「配額」(quota)、L135「成本追蹤」(cost tracking)、L151「批次處理」(batch processing)、L196「快取命中率」(cache hit rate)、L37「向量資料庫」(vector database)、L878「移動平均」(moving average)、L882「分類準確率」(classification accuracy)、L892「確定性呼叫」(deterministic calls) → 修法：補英文。finding 所稱「免費層」現行譯稿已無此詞（表格為「免費版（Free）」），此子項失效。
- [miss] K107（r3.md:345）風格：過度渲染（抽驗 116 條，65 條仍在）→ 現況例：L3「糟糕的單位經濟效益」、L26「殘酷算數」、L41「毫無意義」、L100「表現完美」、L107「關乎生死存亡」、L109「虛擬水桶」、L149「最為燒錢」→ 修法：依 STYLE.md 改寫。

## phases/11-llm-engineering/12-guardrails
- [miss] K108（r3.md:347）遺漏原文例子 → 現況 L96：「若規定輸出需在 500 字以內，強制執行截斷或重新生成」；原文另有「If the model returns an 8,000 word essay when you asked for a one-sentence summary, truncate or regenerate」→ 修法：補回「若要求一句摘要卻收到 8,000 字文章，就截斷或重新生成」。
- [miss] K109（r3.md:349）遺漏與錯譯 → 現況：L124 NeMo 段未提「Integrates with any LLM」；L126「針對參考文獻的幻覺檢驗」（原文 "against reference text"，應為參考文字）；L128 Presidio 未說明「Works on both input and output」→ 修法：三處補回/更正。
- [miss] K110（r3.md:350）增譯（機率詮釋）→ 現況 L773：「回傳 0.0 到 1.0 的機率評分」（原文 "Returns scores from 0.0 to 1.0"，無機率詮釋）→ 修法：改「類別分數」。（L78 的「準確率」用法正確。）
- [miss] K111（r3.md:352）適用對象改寫 → 現況 L178：「最高軍規防禦則留給金融結算、醫療與國防關鍵系統」；原文 "Maximum security is for financial services, healthcare, and government." → 修法：改「金融服務、醫療與政府」。
- [miss] K112（r3.md:353）首見術語未附英文；詞表用語 → 現況：L1 標題「防護欄、安全防禦與內容過濾」(guardrails／content filtering)、L13「越獄」(jailbreak)、L32「間接注入」(indirect injection)、L16「偽陽性（誤判）」「偽陰性（漏判）」（括號為譯注，無英文）、L24「資料外洩」(data leakage；GLOSSARY 為「資料洩漏」)、L52「輸出驗證」(output validation)、L66「分類器」(classifier)、L67「內容隔離」(content isolation)、L76「話題分類」(topic classification)、L128「實體辨識」(entity recognition)、L870「滑動視窗」(sliding window) → 修法：補英文；資料外洩→資料洩漏。
- [miss] K113（r3.md:354）風格與絕對化（抽驗 133 條，70 條仍在）→ 現況例：L3「瞬間繳械投降」「固若金湯」、L60「完全無法區分」、L82「毫無例外全是」、L148「不可攻破」→ 修法：依 STYLE.md 改寫。

## phases/11-llm-engineering/13-production-app
- [miss] K114（r3.md:357）英文括號殘句與重複譯 → 現況 L236：「**每月總額：** **$7,556/month** (with caching saving ~$4,070/month)（快取層每月實質省下約 4,070 美元）」→ 修法：刪英文殘句，只保留中文金額與節省額。
- [miss] K115（r3.md:359）檢核項目增寫 jitter 要求 → 現況 L252「所有 LLM 外部呼叫皆包裝帶有抖動的指數退避重試」；原文 L252 "Exponential backoff on all LLM API calls"（jitter 僅見於第 1 層說明）→ 修法：改「所有 LLM API 呼叫皆採用指數退避」。
- [miss] K116（r3.md:360）增寫保證與時效 → 現況 L137「品質微幅下降，但保證響應」（原文 "Slightly lower quality"）；L136「對終端使用者完全無感」（原文 "Transparent to user"）；L175「瞬間秒級回滾」（原文 "instant rollback"）→ 修法：刪「保證響應」，「完全無感」改「對使用者無感」，「秒級」刪除。
- [miss] K117（r3.md:361）首見術語未附英文（領域詞）→ 現況：L63「語意快取」(semantic caching)、L196「分塊」(chunking)、L15「百分位數」(percentile)、L208「負載平衡器」(load balancer；GLOSSARY)、L165「快取命中率」(cache hit rate)、L3「優雅降級」(graceful degradation)、L16「健康檢查」(health check) → 修法：補英文。
- [miss] K118（r3.md:362）風格（抽驗 83 條，43 條仍在）→ 現況例：L3「陽春 Demo」、L22「模型智商」、L24「擠爆」、L28「飆破」、L268「總結集大成」「緊密咬合」→ 修法：依 STYLE.md 改寫。

## phases/11-llm-engineering/14-model-context-protocol
- [miss] K119（r3.md:366）首見術語未附英文 → 現況：L3「能力宣告」(capability declaration)、L14「支援版本」(supported version)、L21「授權」(authorization)、L63「工具引數」(tool arguments)、L108「快取範疇」(cache scope)、L126「遙測」(telemetry)、L226「狀態代號」(status code)、L233「背壓」(backpressure) → 修法：補英文。
- [ok] K120（r3.md:367）圖說替代文字英文；延伸閱讀連結標題英文 → 替代文字（L29）受 check_translation.py 保護（整段 `![alt](path)` 為受保護跨度，改譯會使 protected spans 不符）；全譯稿 80 張圖的替代文字皆為英文；延伸閱讀連結標題全譯稿 1195 條為英文、17 條含中文，屬慣例 → 駁回合理（可及性議題另案評估）。
- [miss] K121（r3.md:368）風格與冗詞（抽驗 57 條，35 條仍在）→ 現況例：L3「統一通用」「徹底無狀態化」「長連線」、L23「大幅收斂」「完全無需」、L41「徹底廢除」、L126「嚴禁採納」→ 修法：依 STYLE.md 改寫。

## phases/11-llm-engineering/15-prompt-caching
- [miss] K122（r3.md:371）GLOSSARY provider=「服務供應商」→ 現況：全篇「提供者」12 次、「服務供應商」0 次（如 L3「模型提供者端」、L16「三大提供者」、L164）→ 修法：改「服務供應商」，首見附 provider。
- [miss] K123（r3.md:373）首見術語未附英文 → 現況：L182「端點」(endpoint)、L168「快取中斷點」(cache breakpoint)、L217「佈局最佳化器」(optimizer；GLOSSARY 最佳化器)、L164「預熱」(warm-up)、L3「前綴」(prefix)、L162「命中率」(hit rate)、L22「寫入溢價」(cache-write premium)、L22「讀取折扣」(cache-read discount)、L101「快取鍵」(cache key)、L224「快取標記」(cache marker) → 修法：補英文。
- [miss] K124（r3.md:374）風格（抽驗 62 條，28 條仍在）→ 現況例：L3「全額付費」、L16「三大提供者」、L32「不可變的不變量」、L45「永遠無法命中」、L49「淨省錢」、L169「粉碎每一次快取命中」、L242「四大關鍵支點」→ 修法：依 STYLE.md 改寫。（L20 圖說替代文字英文屬受保護內容，不列。）

## phases/11-llm-engineering/16-langgraph-state-machines
- [borderline] K125（r3.md:378）「merge／branch／fork」首見未附英文 → 現況：L3「多路分岔」（fork）、L24「合併」（merge）首見無英文；GLOSSARY merge 備註「一般描述仍可依語境使用『合併』」、fork／branch 條目限 Git／GitHub 語境，LangGraph 圖操作語境未違反詞表 → 取捨：譯名可保留，但依 STYLE 首見仍宜補（fork）（merge）；不補則為例外。
- [miss] K126（r3.md:379）首見術語未附英文 → 現況：L26「條件邊」(conditional edge)、L28「檢查點快照」(snapshot)、L36「狀態增量」(state delta)、L57「子圖」(subgraph)、L25「函式簽章」(function signature)、L3「中斷」(interrupt) 首見無英文（標題「狀態機」已附 Agent State Machine，可接受）→ 修法：補英文（條件邊、狀態增量、子圖為領域術語）。
- [ok] K127（r3.md:380）圖說替代文字英文 → 同 K120：替代文字受 check_translation.py 保護，全譯稿一致 → 駁回合理。

## phases/11-llm-engineering/17-agent-framework-tradeoffs
- [miss] K128（r3.md:382）增譯（「字典」）→ 現況 L14「你所謂的檢查點只能是一份序列化的對話紀錄字典」；原文 "your checkpoint is a pickle of a conversation log"（pickle，未指字典）→ 修法：改「以 pickle 序列化的對話紀錄」。
- [miss] K129（r3.md:385）數量級增譯與語氣加強 → 現況 L87「若該 agent 每日需執行數萬次，請一律堅持顯式路由」；原文 "If the agent runs thousands of times a day, prefer explicit routing" → 修法：改「每日數千次」「優先採用顯式路由」。
- [miss] K130（r3.md:387）GLOSSARY 違規與增譯 → 現況：L101「快速驗證可行性，不想被特定框架綁定技術債」（原文 "no framework commitment"；「技術債」為增譯）；L101「純 Python + 提供者原廠 SDK」（GLOSSARY provider SDK→服務供應商 SDK）；L117「編排調度（Orchestration）」（GLOSSARY orchestration=「編排」）→ 修法：改「不想被特定框架綁定」、「服務供應商 SDK」、「編排」。
- [miss] K131（r3.md:388）首見未附英文（低）→ 現況：框架、程式碼、預設、建置、記憶體、除錯、行程、工作階段、模型、序列化多屬通用 CS 詞，可省；但 L26「節點」（GLOSSARY node=「節點」）為圖論領域術語，首見無英文 → 修法：補「節點（node）」。
- [miss] K132（r3.md:389）風格（抽驗 20 條，12 條仍在）→ 現況：L3「兜售著相同的展示 Demo」、L14「抽象層開始到處漏水」、L16「挑選地表最強框架」、L24「最不適用的災難場景」、L101「永遠是速度最快、最透明的終極框架」→ 修法：依 STYLE.md 改寫。
- [ok] K133（r3.md:390）圖說替代文字英文 → 同 K120：替代文字受 check_translation.py 保護 → 駁回合理。

---

## Summary

計數（133 條）：miss 116 ／ borderline 12 ／ ok 5。
- borderline：K014、K023、K035、K037、K047、K049、K050、K055、K059、K061、K077、K125（格式空行或用語偏好，不影響內容；可低優先處理）。
- ok：K009、K083、K120、K127、K133（來源已失效、或受 check_translation.py 保護的替代文字／連結慣例）。

### miss 優先修正清單

P0｜資訊保真、未譯英文、增譯或遺漏（先修）
1. K091 11/07 L22：英文例句整段未譯。
2. K093 11/08 L24、K102 11/11 L73、K114 11/13 L236：英文殘句夾在中文段落中（含括號重複譯）。
3. K082 11/02 L21：「five words」譯成「這七個字」。
4. K097 11/09 L130：範例「從凌亂履歷中擷取」與原文欄位示範不符。
5. K111 12 L178：譯稿把原文 financial services／healthcare／government 改成「金融結算、醫療與國防關鍵系統」；應改回「金融服務、醫療與政府」。
6. K116 13 L136／L137／L175：「保證響應」「完全無感」「秒級回滾」為原文沒有的承諾。
7. K103 11 L153、L835：「高達 50%」「系統保證」「無條件」。
8. K095 11/08 L134：roughly→「高度」、less information→「顯著低於」、增寫「被證明」。
9. K108、K109 12 L96、L124、L126、L128：遺漏 8,000 字例子、Integrates with any LLM、Presidio 輸入輸出；reference text 誤作參考文獻。
10. K115 13 L252：檢核項目增寫 jitter。K128 17 L14（增「字典」）、K129 17 L87（數萬次）、K110 12 L773（機率評分）。
11. K104 11 L169 重複「平價平價」；L884 缺「拒絕新請求」。

P1｜GLOSSARY 譯法違規（系統性，建議批次修）
- policy→策略：K063（09/02，「政策」27 次、「策略」0）、K065（09/03）、K067（09/04）、K073（09/08 含標題）、K076（09/10 L30）、K075（09/09 L40）、K079（09/12）。
- reward→獎勵：K069（09/05 「報酬」10 次）、K067（09/04 「報酬」6 次）、K075（09/09 「報酬」32 次、含標題）、K079（09/12 「報酬」20 次）、K065（09/03）。
- provider→服務供應商：K081（01 L174）、K085（03 L57）、K087（04 L13）、K089（06 L78）、K098（09 L90）、K100（10 L766）、K105（11/11）、K122（15，全篇 12 次）、K130（17 L101）。
- base model→基模型：K051（08/08 L54）、K094（08/LoRA 19 次）、K079（09/12 L67、L69）。
- mel／頻譜：K011（07 L17、L48、L124、L174）、K033（10 L18、L28、L104、L116、L173、L181）、K001（01 「箱」L93、L119、L134）。
- speedup／forward pass：K038（12 「加速」L93、L108、L109、L213；「前向」L87、L98、L100、L104）、K043（01 L26）、K069（05 L88）、K084（02 L86）。
- runtime／optimizer：K056（3D L151、L157）。
- noise：K052（09 L48、L77、L137）、K043（01 L127「噪聲排程」）。
- threshold：K105（11/11 「門檻」L67、L81、L317、L880）。
- 其他：K030（next-token prediction 應保留英文，07 L16）；K130（orchestration=編排，17 L117）；K089（Euclidean distance=歐幾里得距離，06 L107）；K065（importance sampling=重要性取樣；estimator=估計量；03 L16、L30、L36、L141、L198）；K079（rejection sampling=拒絕取樣，12 L71）；K073（proximal policy optimization=近端策略最佳化，08 L1）；K024（weighted sum=加權總和，02 L12、L45、L135、L137）；K004（magnitude=長度／大小或模，01 L43、L121）。

P2｜風格與過度渲染（批次改寫；抽驗顯示大量殘留）
- K096 11/08、K099 11/09、K101 11/10、K107 11/11、K113 11/12、K118 11/13、K121 11/14、K124 11/15、K132 11/17。

P3｜首見英文（領域術語；批次補註）
- 其餘 miss 條目（如 K001、K003、K005、K007、K010、K012、K013、K016–K020、K022、K025–K034、K036、K039–K046、K048、K051、K053、K054、K057、K058、K060、K062、K064、K066、K068、K070–K072、K074、K075、K076、K078、K080、K084–K088、K090、K092、K094、K098、K100、K106、K112、K117、K119、K123、K126、K131）。
- 低優先：K002、K006、K021、K131 的首見缺漏僅一兩處。

判讀注意：
- 133 條中有數條引文字串在現行譯稿中不存在（如 K009、K013「語碼」、K018「對話式 AI」、K019「語意連貫」、K027「順序不變性」、K032「監督式預訓練」、K046「無條件 GAN」、K053「接縫殘差」、K106「免費層」、K083「組基準的變異」等）。這類條目的其餘子項仍需依現況判斷，本報告已分別註記。
- check_translation.py 只驗 GLOSSARY 禁用欄（forbidden variants）、結構與保護跨度，不驗譯法欄，也不驗首見英文；因此本輪所列 policy、reward、provider、base model 等違規能通過 gate。
- r3.md 有兩份：docs/reviews/zh-tw/r3.md（18:22，本次採用）與 /private/tmp/zh-tw-review/r3.md（17:24，較舊，未採用）。
