# 模擬到真實的轉移（sim-to-real transfer）

> 在模擬器裡訓練、上了硬體就失敗的正則化，是記住了模擬器的特性的正則化。域隨機化（domain randomization）、域適應（domain adaptation）、系統識別（system identification），是讓學到的控制器跨過真實落差的三個工具。

**Type:** Learn
**Languages:** Python
**Prerequisites:** Phase 9 · 08 (PPO), Phase 2 · 10 (Bias/Variance)
**Time:** ~45 minutes

## The Problem｜問題

訓練真的機器人又慢、又危險、又貴。雙足要幾百萬個訓練回合才學會走路；真的雙足只要摔一次，硬體就壞了。模擬給你無限次重設、可重現的確定性、平行環境，而且沒有實體損傷。

但模擬器是錯的。軸承的摩擦比 MuJoCo 模型多。相機有鏡頭畸變，模擬器沒放進去。馬達有延遲、背隙（backlash）、飽和，99% 的模擬模型都跳過。風、灰塵、會變的光線，破壞在無菌渲染上訓練的正則化。**真實落差（reality gap）**——模擬分布和真實分布之間的系統性差異——是部署到機器人上的 RL 的核心問題。

你需要一個正則化，*對模擬到真實的分布偏移很穩*。三個歷史上的做法：把模擬器隨機化（域隨機化）、用一點真實資料來調正則化（域適應／fine-tuning）、或辨識真實系統的參數再讓模擬對齊（系統識別）。2026 年的主流配方把三個合在一起，加上大規模平行模擬（GPU 上的 Isaac Sim、Isaac Lab、Mujoco MJX）。

## The Concept｜核心概念

![Three sim-to-real regimes: domain randomization, adaptation, system identification](../assets/sim-to-real.svg)

**域隨機化（DR）。** Tobin 等人，2017；Peng 等人，2018。訓練時，把真實機器人上可能不一樣的每個模擬參數都隨機化：質量、摩擦係數、馬達 PD 增益、感測器雜訊、相機位置、光線、紋理、接觸模型。正則化學到「今天在哪個模擬裡」的條件分布，並在整段範圍上泛化。真實機器人若落在訓練包絡裡，正則化就會動。

- **好處：** 不需要真實資料。一份配方，很多機器人。
- **壞處：** 隨機化過頭，會生出「什麼都能做、卻過度謹慎」的正則化。雜訊太多，就近似正規化太多。

**系統識別（SI）。** 訓練之前，用真實世界的資料擬合模擬器的參數。如果你量得到真機器人手臂關節的摩擦，就把它放進模擬。再訓練一個預期那些數值的正則化。需要碰得到真實系統，但直接縮小真實落差。

- **好處：** 精確、低雜訊的訓練目標。
- **壞處：** 殘餘的模型誤差正則化看不見；沒辨識到的小效應（例如馬達死區，deadband）仍會讓部署失敗。

**域適應。** 在模擬裡訓練，再用少量真實資料 fine-tune。兩種味道：

- **Real2Sim2Real：** 用真實展開學一個殘差模擬器 `f(s, a, z) - f_sim(s, a)`，在修正過的模擬裡訓練。不用很多真實資料就把落差補上。
- **觀測適應：** 訓練一個正則化，用學到的特徵抽取器（例如 GAN 的像素對像素）把真實觀測映成像模擬的觀測。控制器留在模擬裡。

**特權學習／教師－學生。** Miki 等人，2022（ANYmal 四足）。在模擬裡訓練一個*教師*，它看得到特權資訊（privileged information）：真實摩擦、地形高度、IMU 漂移。再蒸餾一個*學生*，只看真實感測器的觀測。學生學會從歷史推論特權特徵，對物理參數很穩。

**大規模平行模擬。** 2024 到 2026。Isaac Lab、Mujoco MJX、Brax 都能在一張 GPU 上跑幾千隻平行機器人。4,096 個平行人形上的 PPO，幾小時就蒐集到好幾年的經驗。「真實落差」隨訓練分布變寬而縮小；那 4,096 個環境各自有不同的隨機參數時，DR 幾乎不額外花錢。

**2026 年的真實配方（以四足走路為例）：**

1. 大規模平行模擬，重力、摩擦、馬達增益、負載都做域隨機化。
2. 教師正則化用特權資訊訓練（地形圖、身體速度的真值）。
3. 學生正則化從教師蒸餾，只用本體感覺（proprioception，腿部關節編碼器）。
4. 可選：用真實 IMU 上的自編碼器做觀測適應。
5. 部署。10 個以上的環境零樣本（zero-shot）就上。失敗的話，用帶安全約束的 PPO 做幾分鐘的真實世界 fine-tuning。

```figure
f3-reality-gap
```

## Build It｜動手實作

這一課的程式是個很小的示範：在*有雜訊*轉移的 GridWorld 上做域隨機化。我們訓練一個正則化，它在「模擬」裡經歷隨機的滑動機率，再在訓練時沒見過的滑動程度的「真實」上評估。這個形狀直接對得上 MuJoCo 到硬體的轉移。

### 步驟 1：參數化的模擬

```python
def step(state, action, slip):
    if rng.random() < slip:
        action = random_perpendicular(action)
    ...
```

`slip` 是模擬器暴露出來的參數。真的機器人上，它可以是摩擦、質量、馬達增益——任何在模擬和真實之間會偏移的東西。

### 步驟 2：用 DR 訓練

每個回合開始，抽樣 `slip ~ Uniform[0.0, 0.4]`。訓練 PPO、Q-learning，或任何方法。做很多個回合。

### 步驟 3：在「真實」滑動上做零樣本評估

在 `slip ∈ {0.0, 0.1, 0.2, 0.3, 0.5, 0.7}` 上評估。前四個在訓練支撐裡；`0.5` 和 `0.7` 在外面。DR 訓練的正則化在支撐內應該接近最佳，到外面則平順地變差。固定滑動訓練的正則化，一出訓練滑動就脆。

### 步驟 4：和窄訓練比較

用只有 `slip = 0.0` 再訓練第二個正則化。在同一組 `slip` 掃描上評估。真實滑動一大於 0，你應該看到災難性的下跌。

## 容易踩的坑

- **隨機化太多。** 在 `slip ∈ [0, 0.9]` 上訓練，正則化會謹慎到連最佳路徑都不敢走。對齊*預期*的真實世界分布，不是「什麼都可能發生」。
- **隨機化太少。** 在很薄的一片上訓練，正則化完全不能泛化。用自適應課程（自動域隨機化，Automatic Domain Randomization），正則化變好就把分布加寬。
- **參數空間認錯。** 隨機化了錯的東西（真實落差是馬達延遲，你卻隨機化相機色相），DR 沒有幫助。先把真的機器人量過。
- **特權資訊外洩。** 教師如果用全域狀態來做動作，而不只是用觀測，學生可能追不上。要確定給定觀測歷史，學生做得到教師的正則化。
- **模擬到模擬的轉移就失敗。** 正則化如果對更難的模擬變體都不穩，對真實世界也不會穩。部署前一定要在留出的模擬變體上測。
- **沒有真實世界的安全包絡。** 正則化在模擬裡會動、「在真實裡也會動」，若沒有低階安全護罩（safety shield），仍可能弄壞硬體。在一個不學習的控制器裡加上速率上限、力矩上限、關節上限。

## Use It｜實際應用

2026 年的模擬到真實堆疊：

| 領域 | 堆疊 |
|------|------|
| 腿式移動（ANYmal、Spot、人形） | Isaac Lab + DR + 特權教師／學生 |
| 操作（靈巧手、取放） | Isaac Lab + DR + 給視覺用的 DR-GAN |
| 自駕 | CARLA／NVIDIA DRIVE Sim + DR + 真實 fine-tune |
| 無人機競速 | RotorS／Flightmare + DR + 線上適應 |
| 手指／手內操作 | OpenAI Dactyl（前所未有規模的 DR） |
| 工業手臂 | MuJoCo-Warp + SI + 少量真實 fine-tune |

任何規模的控制，工作流程都一樣：能擬合的模擬先擬合，擬合不了的就隨機化，訓練很大的正則化，蒸餾，帶著安全護罩部署。

## Ship It｜交付成果

存成 `outputs/skill-sim2real-planner.md`：

```markdown
---
name: sim2real-planner
description: Plan a sim-to-real transfer pipeline for a given robot + task, covering DR, SI, and safety.
version: 1.0.0
phase: 9
lesson: 11
tags: [rl, sim2real, robotics, domain-randomization]
---

Given a robot platform, a task, and access to real hardware time, output:

1. Reality gap inventory. Suspected sources ranked by expected impact (contact, sensing, actuation delay, vision).
2. DR parameters. Exact list, ranges, distribution. Justify each range against real measurements.
3. SI steps. Which parameters to measure; measurement method.
4. Teacher/student split. What privileged info the teacher uses; what obs the student uses.
5. Safety envelope. Low-level limits, emergency stops, backup controller.

Refuse to deploy without (a) a zero-shot sim-variant test, (b) a safety shield, (c) a rollback plan. Flag any DR range wider than 3× measured real variability as likely over-randomized.
```

## Exercises｜練習

1. **簡單。** 在固定滑動的 GridWorld（slip=0.0）上訓練一個 Q-learning agent。在 slip ∈ {0.0, 0.1, 0.3, 0.5} 上評估。畫回報隨滑動的變化。
2. **中等。** 訓練一個 DR 的 Q-learning agent，抽樣 `slip ~ Uniform[0, 0.3]`。用同一組掃描評估。在 slip=0.5（分布外）時，DR 買到多少？
3. **困難。** 實作課程：從 slip=0.0 開始，正則化達到最佳的 90% 就把 DR 範圍加寬。和固定 DR 基準比，零樣本到達 slip=0.3 總共要多少環境步。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 真實落差 | 「模擬到真實的差異」 | 訓練和部署之間，物理／感測分布的偏移。 |
| 域隨機化（DR） | 「在隨機的模擬上訓練」 | 訓練時把模擬參數隨機化，讓正則化泛化。 |
| 系統識別（SI） | 「量真實、擬合模擬」 | 估計真實的物理參數，再把模擬設成一樣。 |
| 域適應 | 「在真實資料上 fine-tune」 | 模擬訓練之後，用少量真實世界 fine-tune；可以改觀測，也可以改動態。 |
| 特權資訊 | 「給教師的真值」 | 只有模擬有的資訊；學生必須從觀測歷史推論。 |
| 教師／學生 | 「把特權蒸餾成可觀測」 | 教師用捷徑訓練；學生學會不靠捷徑去模仿。 |
| ADR | 「自動域隨機化」 | 正則化變好就把 DR 範圍加寬的課程。 |
| Real2Sim | 「用真實資料把落差補上」 | 學一個殘差，讓模擬模仿真實展開。 |

## Further Reading｜延伸閱讀

- [Tobin et al. (2017). Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907) ——DR 的原始論文（機器人的視覺）。
- [Peng et al. (2018). Sim-to-Real Transfer of Robotic Control with Dynamics Randomization](https://arxiv.org/abs/1710.06537) ——動態的 DR，四足移動。
- [OpenAI et al. (2019). Solving Rubik's Cube with a Robot Hand](https://arxiv.org/abs/1910.07113) ——Dactyl，大規模 ADR。
- [Miki et al. (2022). Learning robust perceptive locomotion for quadrupedal robots in the wild](https://www.science.org/doi/10.1126/scirobotics.abk2822) ——ANYmal 的教師－學生。
- [Makoviychuk et al. (2021). Isaac Gym: High Performance GPU Based Physics Simulation for Robot Learning](https://arxiv.org/abs/2108.10470) ——驅動 2025 到 2026 部署的大規模平行模擬。
- [Akkaya et al. (2019). Automatic Domain Randomization](https://arxiv.org/abs/1910.07113) ——ADR 課程方法。
- [Sutton & Barto (2018). Ch. 8 — Planning and Learning with Tabular Methods](http://incompleteideas.net/book/RLbook2020.pdf) ——Dyna 的框架（用模型來規劃和展開），撐起現代的模擬到真實管線。
- [Zhao, Queralta & Westerlund (2020). Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](https://arxiv.org/abs/2009.13303) ——模擬到真實方法的分類，附基準結果。
