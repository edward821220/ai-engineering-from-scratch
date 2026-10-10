# 深度 Q 網路（Deep Q-Networks，DQN）

> 2013 年：Mnih 用一個 Q-learning 網路直接吃原始像素，在七個 Atari 遊戲上勝過每個古典 RL agent。2015 年：擴到 49 個遊戲，發表在 Nature，點燃深度 RL 的時代。DQN 就是 Q-learning，加上三個讓函數近似（function approximation）穩定的技巧。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 3 · 03 (Backpropagation), Phase 9 · 04 (Q-learning, SARSA)
**Time:** ~75 minutes

## The Problem｜問題

表格式 Q-learning 需要每個（狀態, 動作）配對各有一個 Q 值。棋盤大約有 10⁴³ 個狀態。一張 Atari 幀是 210×160×3 = 100,800 個特徵。表格式 RL 在幾千個狀態就死了，更不用說幾十億。

修法事後看很明顯：用神經網路 `Q(s, a; θ)` 換掉 Q 表。但這個「事後明顯」花了幾十年。Q-learning 配上單純的函數近似，會在「致命三角（deadly triad）」下發散——函數近似 + 自助 + 異政策學習。Mnih 等人（2013、2015）找出三個讓學習穩定的工程技巧：

1. **經驗重放（experience replay）** 去掉轉移之間的相關。
2. **目標網路（target network）** 把自助目標凍住。
3. **報酬截斷（reward clipping）** 把梯度大小正規化。

Atari 上的 DQN，是第一次有單一架構、單一組超參數，從原始像素解出幾十個控制問題。之後所有「深度 RL」——DDQN、Rainbow、Dueling、Distributional、R2D2、Agent57——都疊在這個三技巧的基底上。

## The Concept｜核心概念

![DQN training loop: env, replay buffer, online net, target net, Bellman TD loss](../assets/dqn.svg)

**目標。** DQN 在神經 Q 函數上最小化一步 TD 損失：

`L(θ) = E_{(s,a,r,s')~D} [ (r + γ max_{a'} Q(s', a'; θ^-) - Q(s, a; θ))² ]`

`θ` = 線上網路（online network），每一步用梯度下降法更新。`θ^-` = 目標網路，定期從 `θ` 複製過來（大約每 1 萬步）。`D` = 重放緩衝（replay buffer），裝過去的轉移。

**三個技巧，依重要性排序：**

**經驗重放。** 一個裝 `~10⁶` 筆轉移的環形緩衝（ring buffer）。每個訓練步驟均勻隨機抽一個小批次（minibatch）。這打斷時間相關（連續幀幾乎一樣），讓網路可以反覆從罕見、有報酬的轉移學習，也讓連續的梯度更新不再彼此相關。沒有它，神經網路上的同政策 TD 在 Atari 會發散。

**目標網路。** Bellman 方程式兩邊都用同一個網路 `Q(·; θ)`，目標每次更新都在動——「追自己的尾巴」。修法：留第二個網路 `Q(·; θ^-)`，權重凍住。每 `C` 步，複製 `θ → θ^-`。這樣，回歸目標一次能穩住幾千個梯度步驟。軟更新（soft update）`θ^- ← τ θ + (1-τ) θ^-`（DDPG、SAC 在用）是比較平滑的變體。

**報酬截斷。** Atari 的報酬大小從 1 到 1000 以上都有。截到 `{-1, 0, +1}`，避免任何單一遊戲支配梯度。報酬大小本身要緊時，這樣做是錯的；Atari 只在乎正負，所以沒問題。

**雙 DQN（Double DQN）。** Hasselt（2016）修最大化偏差：用線上網路*挑選*動作，用目標網路*評估*它。

`target = r + γ Q(s', argmax_{a'} Q(s', a'; θ); θ^-)`

直接換上去就好，而且一直比較好。預設就用它。

**其他改進（Rainbow，2017）：** 優先重放（prioritized replay，TD 誤差高的轉移多抽）、對決架構（dueling，把 `V(s)` 和優勢頭分開）、雜訊網路（noisy networks，學出來的探索）、n 步回報、分布式 Q（distributional Q，C51／QR-DQN）、多步自助。每一項加幾個百分點；增益大致可加。

```figure
f3-dqn-stability
```

## Build It｜動手實作

這裡的程式只用標準函式庫、不用 NumPy——我們在一個很小的連續 GridWorld 上手寫單隱藏層 MLP，所以每一步訓練都是微秒級。演算法和規模化的 Atari DQN 相同。

### 步驟 1：重放緩衝

```python
class ReplayBuffer:
    def __init__(self, capacity):
        self.buf = []
        self.capacity = capacity
    def push(self, s, a, r, s_next, done):
        if len(self.buf) == self.capacity:
            self.buf.pop(0)
        self.buf.append((s, a, r, s_next, done))
    def sample(self, batch, rng):
        return rng.sample(self.buf, batch)
```

Atari 容量約 5 萬；我們的玩具環境 5 千就夠。

### 步驟 2：一個很小的 Q 網路（手寫 MLP）

```python
class QNet:
    def __init__(self, n_in, n_hidden, n_actions, rng):
        self.W1 = [[rng.gauss(0, 0.3) for _ in range(n_in)] for _ in range(n_hidden)]
        self.b1 = [0.0] * n_hidden
        self.W2 = [[rng.gauss(0, 0.3) for _ in range(n_hidden)] for _ in range(n_actions)]
        self.b2 = [0.0] * n_actions
    def forward(self, x):
        h = [max(0.0, sum(w * xi for w, xi in zip(row, x)) + b) for row, b in zip(self.W1, self.b1)]
        q = [sum(w * hi for w, hi in zip(row, h)) + b for row, b in zip(self.W2, self.b2)]
        return q, h
```

前向：線性 → ReLU → 線性。整個網路就是這樣。

### 步驟 3：DQN 更新

```python
def train_step(online, target, batch, gamma, lr):
    grads = zeros_like(online)
    for s, a, r, s_next, done in batch:
        q, h = online.forward(s)
        if done:
            y = r
        else:
            q_next, _ = target.forward(s_next)
            y = r + gamma * max(q_next)
        td_error = q[a] - y
        accumulate_grads(grads, online, s, h, a, td_error)
    apply_sgd(online, grads, lr / len(batch))
```

形狀就是第 04 課的 Q-learning，兩個差別：(a) 我們對可微的 `Q(·; θ)` 做反向傳播，而不是去查表，(b) 目標用的是 `Q(·; θ^-)`。

### 步驟 4：外層迴圈

每個回合，依 `Q(·; θ)` 做 ε-貪婪動作，把轉移推進緩衝，抽一個小批次，走一步梯度，定期同步 `θ^- ← θ`。模式是這樣：

```python
for episode in range(N):
    s = env.reset()
    while not done:
        a = epsilon_greedy(online, s, epsilon)
        s_next, r, done = env.step(s, a)
        buffer.push(s, a, r, s_next, done)
        if len(buffer) >= batch:
            train_step(online, target, buffer.sample(batch), gamma, lr)
        if steps % sync_every == 0:
            target = copy(online)
        s = s_next
```

在我們這個很小的 GridWorld 上，狀態是 16 維獨熱（one-hot），agent 大約 500 個回合就學到接近最佳的政策。Atari 上，把這個放大到 2 億幀，並加上 CNN 特徵抽取器。

## 容易踩的坑

- **致命三角。** 函數近似 + 異政策 + 自助可能發散。DQN 用目標網路加重放緩衝壓住；兩個都不要拿掉。
- **探索。** ε 必須衰減，通常在訓練前約 10% 從 1.0 降到 0.01。早期探索不夠，Q 網路會收斂到一個局部盆地。
- **高估。** 雜訊 Q 上的 `max` 往上偏。正式環境一律用雙 DQN。
- **報酬尺度。** 把報酬截斷或正規化；梯度大小和報酬大小成正比。
- **重放緩衝的冷啟動。** 緩衝裡有幾千筆轉移之前不要訓練。大約 20 筆樣本上的早期梯度會過擬合。
- **目標同步頻率。** 太頻繁 ≈ 沒有目標網路；太稀疏 ≈ 目標過期。Atari DQN 用 1 萬個環境步。經驗法則：大約每訓練視野的 1/100 同步一次。
- **觀測前處理。** Atari DQN 疊 4 幀，讓狀態滿足馬可夫。任何帶速度資訊的環境都需要疊幀，或用循環狀態。

## Use It｜實際應用

2026 年，DQN 很少還是最先進的，但它仍是異政策演算法的參考：

| 任務 | 首選方法 | 為什麼不用 DQN？ |
|------|----------|------------------|
| 離散動作、類似 Atari | Rainbow DQN 或 Muesli | 同一個框架，技巧更多。 |
| 連續控制 | SAC／TD3（第 9 階段 · 07） | DQN 沒有政策網路。 |
| 同政策／高吞吐 | PPO（第 9 階段 · 08） | 沒有重放緩衝；比較好擴大規模。 |
| 離線 RL | CQL／IQL／Decision Transformer | 保守的 Q 目標，不會因自助炸開。 |
| 大的離散動作空間（推薦系統） | 帶動作 embedding 的 DQN，或 IMPALA | 可以用；附加的裝飾很重要。 |
| 語言模型的 RL | PPO／GRPO | 序列層級，不是步層級；損失不一樣。 |

這些教訓現在還通用。重放和目標網路出現在 SAC、TD3、DDPG、SAC-X、AlphaZero 的自我對弈緩衝，以及每個離線 RL 方法裡。報酬截斷在 PPO 裡以優勢正規化的形式活下來。這個架構就是藍圖。

## Ship It｜交付成果

存成 `outputs/skill-dqn-trainer.md`：

```markdown
---
name: dqn-trainer
description: Produce a DQN training config (buffer, target sync, ε schedule, reward clipping) for a discrete-action RL task.
version: 1.0.0
phase: 9
lesson: 5
tags: [rl, dqn, deep-rl]
---

Given a discrete-action environment (observation shape, action count, horizon, reward scale), output:

1. Network. Architecture (MLP / CNN / Transformer), feature dim, depth.
2. Replay buffer. Capacity, minibatch size, warmup size.
3. Target network. Sync strategy (hard every C steps or soft τ).
4. Exploration. ε start / end / schedule length.
5. Loss. Huber vs MSE, gradient clip value, reward clipping rule.
6. Double DQN. On by default unless explicit reason to disable.

Refuse to ship a DQN with no target network, no replay buffer, or ε held at 1. Refuse continuous-action tasks (route to SAC / TD3). Flag any reward range > 10× per-step mean as needing clipping or scale normalization.
```

## Exercises｜練習

1. **簡單。** 跑 `code/main.py`。畫每個回合的回報曲線。移動平均超過 -10 要幾個回合？
2. **中等。** 關掉目標網路（Bellman 目標的兩邊都用線上網路）。量訓練有多不穩——回報是震盪還是發散？
3. **困難。** 加上雙 DQN：用線上網路挑 `argmax a'`，用目標網路評估。在報酬有雜訊的 GridWorld 上跑 1 千個回合，比較有沒有雙 DQN 時，`Q(s_0, best_a)` 相對真的 `V*(s_0)` 的偏差。

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| DQN | 「深度 Q-learning」 | 帶神經 Q 函數、重放緩衝、目標網路的 Q-learning。 |
| 經驗重放 | 「打亂的轉移」 | 每個梯度步驟均勻抽樣的環形緩衝；讓資料去掉相關。 |
| 目標網路 | 「凍住的自助」 | 定期複製一份 Q，用在 Bellman 目標裡；讓訓練穩定。 |
| 致命三角 | 「RL 為什麼發散」 | 函數近似 + 自助 + 異政策 = 沒有收斂保證。 |
| 雙 DQN | 「最大化偏差的修法」 | 線上網路選動作，目標網路評估它。 |
| 對決 DQN | 「V 頭和 A 頭」 | 把 Q 拆成 V + A − mean(A)；輸出相同，梯度流更好。 |
| Rainbow | 「所有技巧」 | DDQN + PER + 對決 + n 步 + 雜訊 + 分布式，合在一個裡。 |
| PER | 「優先重放」 | 依 TD 誤差的大小成比例抽轉移。 |

## Further Reading｜延伸閱讀

- [Mnih et al. (2013). Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) ——2013 年 NeurIPS 工作坊論文，深度 RL 從這裡開始。
- [Mnih et al. (2015). Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236) ——Nature 論文，49 個遊戲的 DQN。
- [Hasselt, Guez, Silver (2016). Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) ——DDQN。
- [Wang et al. (2016). Dueling Network Architectures](https://arxiv.org/abs/1511.06581) ——對決 DQN。
- [Hessel et al. (2018). Rainbow: Combining Improvements in Deep RL](https://arxiv.org/abs/1710.02298) ——把技巧疊起來的那篇。
- [Sutton & Barto (2018). Ch. 9 — On-policy Prediction with Approximation](http://incompleteideas.net/book/RLbook2020.pdf) ——教科書怎麼講「致命三角」（函數近似 + 自助 + 異政策）；DQN 的目標網路和重放緩衝就是為了馴服它。
- [CleanRL DQN implementation](https://docs.cleanrl.dev/rl-algorithms/dqn/) ——消融研究用的單檔 DQN 參考；適合和這一課從零寫的版本一起讀。
