# Actor-Critic——A2C 與 A3C

> REINFORCE 很吵。加上一個學 `V̂(s)` 的評論者，從回報裡減掉它，就得到期望相同、變異低很多的優勢。這就是 actor-critic。A2C 同步跑；A3C 跨執行緒跑。兩者是每個現代深度 RL 方法的心智模型。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 9 · 04 (TD Learning), Phase 9 · 06 (REINFORCE)
**Time:** ~75 minutes

## The Problem｜問題

原味 REINFORCE 能動，但變異糟透了。蒙地卡羅回報 `G_t` 在回合之間可以差到 10 倍。把這個雜訊乘上 `∇ log π` 再平均，得到的梯度估計器要幾千個回合，才能把政策推進一段距離；那段距離，少得多的 DQN 更新就走得到。

變異來自用原始回報。如果你減掉基準 `b(s_t)`——任何狀態的函數，包含學出來的價值——期望不變，變異下降。最好算得出來的基準是 `V̂(s_t)`。現在乘上 `∇ log π` 的那個量是*優勢*：

`A(s, a) = G - V̂(s)`

動作如果產生高於平均的回報就是好的；低於平均就是壞的。帶著學出來的評論者的 REINFORCE，就是 *actor-critic*。評論者給行動者一個低變異的老師。2015 年之後每個深度政策方法都是這個（A2C、A3C、PPO、SAC、IMPALA）。

## The Concept｜核心概念

![Actor-critic: policy net plus value net, TD residual as advantage](../assets/actor-critic.svg)

**兩個網路，一個共享的損失：**

- **行動者（actor）** `π_θ(a | s)`：政策。抽樣來行動。用政策梯度訓練。
- **評論者（critic）** `V_φ(s)`：估計從該狀態起的期望回報。訓練來最小化 `(V_φ(s) - target)²`。

**優勢。** 兩種標準形式：

- *MC 優勢：* `A_t = G_t - V_φ(s_t)`。不偏，變異較高。
- *TD 優勢：* `A_t = r_{t+1} + γ V_φ(s_{t+1}) - V_φ(s_t)`。有偏（用了 `V_φ`），變異低非常多。也叫 *TD 殘差* `δ_t`。

**n 步優勢。** 在兩者之間內插：

`A_t^{(n)} = r_{t+1} + γ r_{t+2} + … + γ^{n-1} r_{t+n} + γ^n V_φ(s_{t+n}) - V_φ(s_t)`

`n = 1` 是純 TD。`n = ∞` 是 MC。大多數實作在 Atari 用 `n = 5`，在 MuJoCo 上的 PPO 用 `n = 2048`。

**廣義優勢估計（Generalized Advantage Estimation，GAE）。** Schulman 等人（2016）提出把所有 n 步優勢做指數加權平均：

`A_t^{GAE} = Σ_{l=0}^{∞} (γλ)^l δ_{t+l}`

其中 `λ ∈ [0, 1]`。`λ = 0` 是 TD（低變異、高偏差）。`λ = 1` 是 MC（高變異、不偏）。`λ = 0.95` 是 2026 年的預設——調到偏差／變異的旋鈕停在你要的位置。

**A2C：同步優勢 actor-critic。** 在 `N` 個平行環境上蒐集 `T` 步。每一步算優勢。在合併的批次上更新行動者和評論者。重複。它是 A3C 比較單純、比較好擴大規模的兄弟。

**A3C：非同步優勢 actor-critic。** Mnih 等人（2016）。生出 `N` 個工作執行緒，每個跑一個環境。每個工作者在自己的展開上本地算梯度，再非同步套到共享的參數伺服器。不需要重放緩衝——工作者跑不同軌跡，自然去掉相關。A3C 證明你可以在 CPU 上大規模訓練。2026 年，以 GPU 為基礎的 A2C（批次化的平行環境）是主流，因為 GPU 要大批次。

**合在一起的損失。**

`L(θ, φ) = -E[ A_t · log π_θ(a_t | s_t) ]  +  c_v · E[(V_φ(s_t) - G_t)²]  -  c_e · E[H(π_θ(·|s_t))]`

三項：政策梯度損失、價值回歸、熵獎勵。`c_v ~ 0.5`、`c_e ~ 0.01` 是標準起點。

```figure
actor-critic
```

## Build It｜動手實作

### 步驟 1：一個評論者

線性評論者 `V_φ(s) = w · features(s)`，用 MSE 更新：

```python
def critic_update(w, x, target, lr):
    v_hat = dot(w, x)
    err = target - v_hat
    for j in range(len(w)):
        w[j] += lr * err * x[j]
    return v_hat
```

表格式環境上，評論者幾百個回合就收斂。Atari 上，把線性評論者換成共享的 CNN 主幹，加上價值頭。

### 步驟 2：n 步優勢

給定長度 `T` 的展開，以及自助用的最終 `V(s_T)`：

```python
def compute_advantages(rewards, values, gamma=0.99, lam=0.95, last_value=0.0):
    advantages = [0.0] * len(rewards)
    gae = 0.0
    for t in reversed(range(len(rewards))):
        next_v = values[t + 1] if t + 1 < len(values) else last_value
        delta = rewards[t] + gamma * next_v - values[t]
        gae = delta + gamma * lam * gae
        advantages[t] = gae
    returns = [a + v for a, v in zip(advantages, values)]
    return advantages, returns
```

`returns` 是評論者的目標。`advantages` 是乘上 `∇ log π` 的那個量。

### 步驟 3：合在一起的更新

```python
for step_i, (x, a, _r, probs) in enumerate(traj):
    adv = advantages[step_i]
    target_v = returns[step_i]

    # critic
    critic_update(w, x, target_v, lr_v)

    # actor
    for i in range(N_ACTIONS):
        grad_logpi = (1.0 if i == a else 0.0) - probs[i]
        for j in range(N_FEAT):
            theta[i][j] += lr_a * adv * grad_logpi * x[j]
```

同政策，每次更新一次展開，行動者和評論者各有學習率。

### 步驟 4：平行化（A3C 對上 A2C）

- **A3C：** 拉起 `N` 個執行緒。每個跑自己的環境和自己的前向。定期把梯度更新推進共享的主程式。主程式不上鎖——競爭沒關係，只是多一點雜訊。
- **A2C：** 在單一程序裡跑 `N` 個環境實例，把觀測疊成 `[N, obs_dim]` 批次，批次前向，批次反向。GPU 利用率較高，行為確定，比較好推理。2026 年的預設。

我們的玩具程式為了清楚是單執行緒；改成批次 A2C 是三行 NumPy。

## 容易踩的坑

- **評論者還沒準，就開行動者梯度。** 評論者如果是隨機的，基準沒有資訊，你就是在純雜訊上訓練。先把評論者暖機幾百步，再開政策梯度，或把行動者的學習率放慢。
- **優勢正規化。** 每個批次把優勢正規化成零均值、單位標準差。幾乎不花成本，訓練卻穩定非常多。
- **共享主幹。** 影像輸入時，行動者和評論者共用特徵抽取器。頭分開。共享特徵同時靠兩種損失來學。
- **同政策契約。** A2C 的資料正好只用一次更新。再用，梯度就有偏（PPO 加的就是重要性抽樣修正）。
- **熵崩塌。** 沒有 `c_e > 0`，政策在幾百次更新內就變得幾乎確定，不再探索。
- **報酬尺度。** 優勢的大小跟報酬尺度走。把報酬正規化（例如除以移動標準差），不同任務的梯度大小才一致。

## Use It｜實際應用

2026 年 A2C／A3C 很少是最終選擇，但後面每個方法精煉的都是這個架構：

| 方法 | 和 A2C 的關係 |
|------|---------------|
| PPO | A2C + 截斷的重要性比率，好做多輪更新 |
| IMPALA | A3C + V-trace 異政策修正 |
| SAC（第 9 階段 · 07） | 帶軟價值評論者的異政策 A2C（下一課） |
| GRPO（第 9 階段 · 12） | 沒有評論者的 A2C——組內相對優勢 |
| DPO | 把 A2C 化成偏好排序損失，不用抽樣 |
| AlphaStar／OpenAI Five | 帶聯賽訓練和模仿預訓練的 A2C |

2026 年的論文裡看到「advantage」，就想到 actor-critic。

## Ship It｜交付成果

存成 `outputs/skill-actor-critic-trainer.md`：

```markdown
---
name: actor-critic-trainer
description: Produce an A2C / A3C / GAE configuration for a given environment, with advantage estimation and loss weights specified.
version: 1.0.0
phase: 9
lesson: 7
tags: [rl, actor-critic, gae]
---

Given an environment and compute budget, output:

1. Parallelism. A2C (GPU batched) vs A3C (CPU async) and the number of workers.
2. Rollout length T. Steps per env per update.
3. Advantage estimator. n-step or GAE(λ); specify λ.
4. Loss weights. `c_v` (value), `c_e` (entropy), gradient clip.
5. Learning rates. Actor and critic (separate if using).

Refuse single-worker A2C on environments with horizon > 1000 (too on-policy, too slow). Refuse to ship without advantage normalization. Flag any run with `c_e = 0` and observed entropy < 0.1 as entropy-collapsed.
```

## Exercises｜練習

1. **簡單。** 在 4×4 GridWorld 上，用 MC 優勢（`G_t - V(s_t)`）訓練 actor-critic。和第 06 課帶移動平均基準的 REINFORCE 比樣本效率。
2. **中等。** 改成 TD 殘差優勢（`r + γ V(s') - V(s)`）。量優勢批次的變異。下降多少？
3. **困難。** 實作 GAE(λ)。掃描 `λ ∈ {0, 0.5, 0.9, 0.95, 1.0}`。畫最終回報和樣本效率的關係。這個任務上，偏差／變異最好的點在哪？

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 行動者 | 「政策網路」 | `π_θ(a\|s)`，用政策梯度更新。 |
| 評論者 | 「價值網路」 | `V_φ(s)`，用 MSE 回歸到回報或 TD 目標來更新。 |
| 優勢 | 「比平均好多少」 | `A(s, a) = Q(s, a) - V(s)`，或它的估計。拿來乘 `∇ log π`。 |
| TD 殘差 | 「δ」 | `δ_t = r + γ V(s') - V(s)`；一步優勢估計。 |
| GAE | 「內插的旋鈕」 | n 步優勢的指數加權和，由 `λ` 參數化。 |
| A2C | 「同步 actor-critic」 | 跨環境做批次；每次展開走一步梯度。 |
| A3C | 「非同步 actor-critic」 | 工作執行緒把梯度推進共享的參數伺服器。原始論文；2026 年比較少見。 |
| 自助 | 「在視野盡頭用 V」 | 把展開截斷，加上 `γ^n V(s_{t+n})` 把和式收尾。 |

## Further Reading｜延伸閱讀

- [Mnih et al. (2016). Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783) ——A3C，原始的非同步 actor-critic 論文。
- [Schulman et al. (2016). High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438) ——GAE。
- [Sutton & Barto (2018). Ch. 13 — Actor-Critic Methods](http://incompleteideas.net/book/RLbook2020.pdf) ——基礎；評論者是神經網路時，搭配第 9 章的函數近似一起看。
- [Espeholt et al. (2018). IMPALA](https://arxiv.org/abs/1802.01561) ——可擴展的分散式 actor-critic，帶 V-trace 異政策修正。
- [OpenAI Baselines / Stable-Baselines3](https://stable-baselines3.readthedocs.io/) ——值得一讀的上線級 A2C／PPO 實作。
- [Konda & Tsitsiklis (2000). Actor-Critic Algorithms](https://papers.nips.cc/paper/1786-actor-critic-algorithms) ——雙時間尺度 actor-critic 分解的基礎收斂結果。
