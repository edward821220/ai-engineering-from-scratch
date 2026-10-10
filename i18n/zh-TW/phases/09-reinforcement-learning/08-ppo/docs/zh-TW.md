# 近端政策（Proximal Policy Optimization，PPO）

> A2C 每次更新後就把那次展開丟掉。PPO 把政策梯度包進截斷的重要性比率，同一批資料可以做 10 個以上的 epoch，避免策略大幅偏移。Schulman 等人（2017）。到 2026 年，它仍是預設的政策梯度演算法。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 9 · 06 (REINFORCE), Phase 9 · 07 (Actor-Critic)
**Time:** ~75 minutes

## The Problem｜問題

A2C（第 07 課）是同政策的：梯度 `E_{π_θ}[A · ∇ log π_θ]` 要求資料從*當下*的 `π_θ` 抽樣。更新一次，`π_θ` 就變了；你用過的資料現在是異政策的。再用一次，梯度就有偏。

展開很貴。Atari 上，8 個環境 × 128 步的一次展開 = 1024 筆轉移，環境時間十來秒。走一步梯度就丟掉，很浪費。

信賴域政策（Trust Region Policy Optimization，TRPO，Schulman 2015）是第一個修法：約束每次更新，讓舊政策和新政策的 KL 散度停在 `δ` 以下。理論乾淨，但每次更新要做一次共軛梯度求解。2026 年沒有人在跑 TRPO。

PPO（Schulman 等人，2017）用一個簡單的截斷目標，換掉硬的信賴域約束。多一行程式。每次展開十個 epoch。不用共軛梯度。理論保證夠用。九年後，從 MuJoCo 到 RLHF，它仍是預設的政策梯度演算法。

## The Concept｜核心概念

![PPO clipped surrogate objective: ratio clipping at 1 ± ε](../assets/ppo.svg)

**重要性比率。**

`r_t(θ) = π_θ(a_t | s_t) / π_{θ_old}(a_t | s_t)`

這是新政策相對蒐集資料的那個政策的概似比（likelihood ratio）。`r_t = 1` 表示沒變。`r_t = 2` 表示新政策採取 `a_t` 的機率是舊政策的兩倍。

**截斷代理目標（clipped surrogate）。**

`L^{CLIP}(θ) = E_t [ min( r_t(θ) A_t, clip(r_t(θ), 1-ε, 1+ε) A_t ) ]`

兩項：

- 如果優勢 `A_t > 0`，而比率想長過 `1 + ε`，截斷就把梯度壓平——不要把好動作推到比舊機率高出 `+ε` 以上。
- 如果優勢 `A_t < 0`，而比率想越過 `1 - ε`（意思是比起截斷後的下降，我們會讓壞動作變得更可能），截斷就把梯度封頂——不要把壞動作推到比 `-ε` 更低。

`min` 處理另一個方向：如果比率已經往*有利*的方向動了，你仍然拿得到梯度（會傷到你的那一側不截斷）。

典型是 `ε = 0.2`。把目標畫成 `r_t` 的函數：分段線性，好的那一側是平屋頂，壞的那一側是平地板。

**完整的 PPO 損失。**

`L(θ, φ) = L^{CLIP}(θ) - c_v · (V_φ(s_t) - V_t^{target})² + c_e · H(π_θ(·|s_t))`

結構和 A2C 一樣，還是 actor-critic。三個係數，通常 `c_v = 0.5`、`c_e = 0.01`、`ε = 0.2`。

**訓練迴圈。**

1. 在 `N` 個平行環境上、每個走 `T` 步，蒐集 `N × T` 筆轉移。
2. 算優勢（GAE），凍成常數。
3. 把 `π_{θ_old}` 凍成當下 `π_θ` 的快照。
4. 做 `K` 個 epoch，每個小批次是 `(s, a, A, V_target, log π_old(a|s))`：
   - 計算 `r_t(θ) = exp(log π_θ(a|s) - log π_old(a|s))`。
   - 套上 `L^{CLIP}` + 價值損失 + 熵。
   - 走一步梯度。
5. 丟掉這次展開。回到步驟 1。

`K = 10`、小批次 64，是一組標準超參數。PPO 很穩：精確數字在 ±50% 以內很少要緊。

**KL 懲罰變體。** 原始論文提了另一個做法，用自適應的 KL 懲罰：`L = L^{PG} - β · KL(π_θ || π_old)`，`β` 依觀察到的 KL 調整。截斷版成為主流；KL 變體活在 RLHF 裡（對參考政策的 KL 本來就是你一直想要的另一條約束）。

```figure
ppo-clip
```

## Build It｜動手實作

### 步驟 1：展開當下就把 `log π_old(a | s)` 留住

```python
for step in range(T):
    probs = softmax(logits(theta, state_features(s)))
    a = sample(probs, rng)
    s_next, r, done = env.step(s, a)
    buffer.append({
        "s": s, "a": a, "r": r, "done": done,
        "v_old": value(w, state_features(s)),
        "log_pi_old": log(probs[a] + 1e-12),
    })
    s = s_next
```

快照只在展開當下拍一次。更新的那些 epoch 裡它不變。

### 步驟 2：計算 GAE 優勢（第 07 課）

和 A2C 一樣。在整個批次上正規化。

### 步驟 3：截斷代理目標的更新

```python
for _ in range(K_EPOCHS):
    for mb in minibatches(buffer, size=64):
        for rec in mb:
            x = state_features(rec["s"])
            probs = softmax(logits(theta, x))
            logp = log(probs[rec["a"]] + 1e-12)
            ratio = exp(logp - rec["log_pi_old"])
            adv = rec["advantage"]
            surrogate = min(
                ratio * adv,
                clamp(ratio, 1 - EPS, 1 + EPS) * adv,
            )
            # backprop -surrogate, add value loss, subtract entropy
            grad_logpi = onehot(rec["a"]) - probs
            if (adv > 0 and ratio >= 1 + EPS) or (adv < 0 and ratio <= 1 - EPS):
                pg_grad = 0.0  # clipped
            else:
                pg_grad = ratio * adv
            for i in range(N_ACTIONS):
                for j in range(N_FEAT):
                    theta[i][j] += LR * pg_grad * grad_logpi[i] * x[j]
```

「截斷 → 梯度變零」這個模式是 PPO 的核心。如果新政策在有利方向已經漂太遠，更新就停。

### 步驟 4：價值與熵

在評論者目標上加標準 MSE，在行動者上加熵獎勵，和 A2C 一樣。

### 步驟 5：診斷

每次更新要看三件事：

- **平均 KL** `E[log π_old - log π_θ]`。應該停在 `[0, 0.02]`。如果衝過 `0.1`，就降低 `K_EPOCHS` 或 `LR`。
- **截斷比例（clip fraction）**——比率落在 `[1-ε, 1+ε]` 外面的樣本比例。應該是 `~0.1-0.3`。如果是 `~0`，截斷從未觸發 → 提高 `LR` 或 `K_EPOCHS`。如果是 `~0.5+`，你在把這次展開擬合過頭 → 把它們降低。
- **解釋變異（explained variance）** `1 - Var(V_target - V_pred) / Var(V_target)`。評論者品質的度量。評論者學會之後，應該往 1 爬。

## 容易踩的坑

- **截斷係數調歪。** `ε = 0.2` 是實務上的標準。降到 `0.1`，更新就太膽小；`0.3+` 會帶來不穩定。
- **epoch 太多。** `K > 20` 常常不穩定，因為政策漂離 `π_old` 太遠。把 epoch 封頂，大網路尤其要。
- **沒有報酬正規化。** 報酬尺度一大，就吃進截斷範圍。算優勢之前先把報酬正規化（移動標準差）。
- **忘了優勢正規化。** 每個批次零均值、單位標準差是標準做法。跳過它，PPO 在大多數基準（benchmark）上會垮。
- **學習率不衰減。** PPO 受惠於學習率線性衰減到零。常數學習率常常比較差。
- **重要性比率算錯。** 為了數值穩定，一律用 `exp(log_new - log_old)`，不要用 `new / old`。
- **梯度正負號錯。** 最大化代理目標 = *最小化* `-L^{CLIP}`。正負號反了，是最常見的 PPO bug。

## Use It｜實際應用

PPO 是 2026 年預設的 RL 演算法，涵蓋的領域多到令人意外：

| 用途 | PPO 變體 |
|------|----------|
| MuJoCo／機器人控制 | 帶高斯政策的 PPO，GAE(0.95) |
| Atari／離散遊戲 | 帶類別政策的 PPO，滾動的 128 步展開 |
| 給語言模型的 RLHF | 帶對參考模型 KL 懲罰的 PPO，報酬來自回應結尾的報酬模型 |
| 大規模遊戲 agent | IMPALA + PPO（AlphaStar、OpenAI Five） |
| 推理語言模型 | GRPO（第 12 課）——沒有評論者的 PPO 變體 |
| 只有偏好的資料 | DPO——把 PPO+KL 化成閉式，不用線上抽樣 |

PPO 的*損失形狀*——截斷代理目標 + 價值 + 熵——是 DPO、GRPO，以及幾乎每條 RLHF 管線的鷹架。

## Ship It｜交付成果

存成 `outputs/skill-ppo-trainer.md`：

```markdown
---
name: ppo-trainer
description: Produce a PPO training config and a diagnostic plan for a given environment.
version: 1.0.0
phase: 9
lesson: 8
tags: [rl, ppo, policy-gradient]
---

Given an environment and training budget, output:

1. Rollout size. `N` envs × `T` steps.
2. Update schedule. `K` epochs, minibatch size, LR schedule.
3. Surrogate params. `ε` (clip), `c_v`, `c_e`, advantage normalization on.
4. Advantage. GAE(`λ`) with explicit `γ` and `λ`.
5. Diagnostics plan. KL, clip fraction, explained variance thresholds with alerts.

Refuse `K > 30` or `ε > 0.3` (unsafe trust region). Refuse any PPO run without advantage normalization or KL/clip monitoring. Flag clip fraction sustained above 0.4 as drift.
```

## Exercises｜練習

1. **簡單。** 在 4×4 GridWorld 上跑 PPO，`ε=0.2, K=4`。在相同的環境步數下，和 A2C（每次展開一個 epoch）比樣本效率。
2. **中等。** 掃描 `K ∈ {1, 4, 10, 30}`。畫回報隨環境步數的變化，並追蹤每次更新的平均 KL。這個任務上，KL 在哪個 `K` 炸開？
3. **困難。** 把截斷代理目標換成自適應 KL 懲罰（`KL > 2·target` 就把 `β` 加倍，`KL < target/2` 就減半）。比較最終回報、穩定度，以及不靠截斷的程度。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 重要性比率 | 「r_t(θ)」 | `π_θ(a\|s) / π_old(a\|s)`；偏離蒐集資料那個政策多遠。 |
| 截斷代理目標 | 「PPO 的主要技巧」 | `min(r·A, clip(r, 1-ε, 1+ε)·A)`；有利那一側過了截斷，梯度就變平。 |
| 信賴域 | 「TRPO／PPO 的意圖」 | 限制每次更新的 KL，保證單調改進。 |
| KL 懲罰 | 「軟的信賴域」 | 另一種 PPO：`L - β · KL(π_θ \|\| π_old)`。`β` 自適應。 |
| 截斷比例 | 「截斷多久觸發一次」 | 診斷量——應該在 0.1 到 0.3；外面就是調歪了。 |
| 多 epoch 訓練 | 「資料重用」 | 每次展開做 K 個 epoch；用變異換樣本效率。 |
| 大致同政策 | 「大多時候同政策」 | PPO 名義上是同政策，但 K>1 個 epoch 會安全地用到稍微異政策的資料。 |
| PPO-KL | 「另一種 PPO」 | KL 懲罰變體；用在 RLHF，因為對參考政策的 KL 本來就是一條約束。 |

## Further Reading｜延伸閱讀

- [Schulman et al. (2017). Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) ——那篇論文。
- [Schulman et al. (2015). Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477) ——TRPO，PPO 的前身。
- [Andrychowicz et al. (2021). What Matters In On-Policy RL? A Large-Scale Empirical Study](https://arxiv.org/abs/2006.05990) ——每個 PPO 超參數都做了消融。
- [Ouyang et al. (2022). Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) ——InstructGPT；RLHF 裡的 PPO 配方。
- [OpenAI Spinning Up — PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) ——乾淨的現代講法，附 PyTorch。
- [CleanRL PPO implementation](https://github.com/vwxyzjn/cleanrl) ——很多論文用的單檔 PPO 參考。
- [Hugging Face TRL — PPOTrainer](https://huggingface.co/docs/trl/main/en/ppo_trainer) ——語言模型上 PPO 的上線配方；和下一課（RLHF）一起讀。
- [Engstrom et al. (2020). Implementation Matters in Deep Policy Gradients](https://arxiv.org/abs/2005.12729) ——那篇「37 個程式層級調整」；哪些 PPO 技巧是承重的，哪些是傳說。
