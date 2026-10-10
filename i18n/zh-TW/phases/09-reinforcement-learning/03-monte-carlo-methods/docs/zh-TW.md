# 蒙地卡羅方法（Monte Carlo）——從完整回合學習

> 動態規劃需要模型。蒙地卡羅只要回合，別的都不用。把政策跑起來，看回報，再平均。這是強化學習裡最單純的想法——也是後面一切的鑰匙。

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 9 · 01 (MDPs), Phase 9 · 02 (Dynamic Programming)
**Time:** ~75 minutes

## The Problem｜問題

動態規劃很漂亮，但它假設你能查每個狀態和動作的 `P(s' | s, a)`。真實世界幾乎沒有東西是這樣運作的。機器人沒辦法解析地算出關節力矩之後、相機像素的分布。定價演算法沒辦法把每一種可能的顧客反應積分進去。LLM 沒辦法在一個 token 之後枚舉所有可能的續寫。

你需要一個方法，只要能從環境*抽樣*就夠。把政策跑起來。得到一條軌跡（trajectory）`s_0, a_0, r_1, s_1, a_1, r_2, …, s_T`。用它估計價值。這就是蒙地卡羅。

從 DP 走到 MC，在觀念上很重要：我們從*已知模型 + 精確回推*走到*抽樣出來的展開 + 平均後的回報*。變異跳上去，適用範圍卻炸開。這一課之後的每個 RL 演算法——TD、Q-learning、REINFORCE、PPO、GRPO——骨子裡都是蒙地卡羅估計器，有時再疊一層自助（bootstrapping）。

## The Concept｜核心概念

![Monte Carlo: rollout, compute returns, average; first-visit vs every-visit](../assets/monte-carlo.svg)

**一句話講完核心：** `V^π(s) = E_π[G_t | s_t = s] ≈ (1/N) Σ_i G^{(i)}(s)`，其中 `G^{(i)}(s)` 是在政策 `π` 下、造訪 `s` 之後觀察到的回報。

**首次造訪對上每次造訪 MC。** 給定一個多次造訪狀態 `s` 的回合，首次造訪 MC 只算第一次造訪起的回報；每次造訪 MC 把每次造訪都算進去。兩者在極限都是不偏（unbiased）的。首次造訪比較好分析（樣本是獨立同分布，iid）。每次造訪每個回合用到更多資料，實務上通常收斂比較快。

**增量平均。** 不要把所有回報都存起來，改更新累計平均：

`V_n(s) = V_{n-1}(s) + (1/n) [G_n - V_{n-1}(s)]`

重新整理：`V_new = V_old + α · (target - V_old)`，其中 `α = 1/n`。把 `1/n` 換成常數步長（step size）`α ∈ (0, 1)`，就得到一個非平穩（non-stationary）的 MC 估計器，能跟上 `π` 的變化。這一步，就是從 MC 跳到 TD、再跳到每個現代 RL 演算法的全部。

**探索現在成了問題。** DP 用枚舉碰到每個狀態。MC 只看得到政策會造訪的狀態。如果 `π` 是確定的，狀態空間整片區域永遠抽不到，它們的價值估計就永遠停在零。三個修法，依歷史順序：

1. **探索性起始（exploring starts）。** 每個回合從隨機的 (s, a) 配對開始。保證覆蓋；實務上不現實（你沒辦法把機器人「重設」到任意狀態）。
2. **ε-貪婪。** 依當下的 Q 取貪婪動作，但以機率 `ε` 挑一個隨機動作。所有狀態－動作配對在漸近意義下都會被抽到。
3. **異政策（off-policy）MC。** 在行為政策（behavior policy）`μ` 下蒐集資料，用重要性抽樣（importance sampling）去學目標政策（target policy）`π`。變異很高，但它是通往 DQN 這類重放緩衝（replay buffer）方法的橋。

**蒙地卡羅控制。** 評估 → 改進 → 評估，就像政策迭代，只是評估改成抽樣式的：

1. 跑 `π`，得到一個回合。
2. 用觀察到的回報更新 `Q(s, a)`。
3. 讓 `π` 依 `Q` 取 ε-貪婪。
4. 重複。

在溫和條件下（每個配對被造訪無限次，`α` 滿足 Robbins-Monro）以機率 1 收斂到 `Q*` 和 `π*`。

```figure
epsilon-greedy
```

## Build It｜動手實作

### 步驟 1：展開 → (s, a, r) 的清單

```python
def rollout(env, policy, max_steps=200):
    trajectory = []
    s = env.reset()
    for _ in range(max_steps):
        a = policy(s)
        s_next, r, done = env.step(s, a)
        trajectory.append((s, a, r))
        s = s_next
        if done:
            break
    return trajectory
```

沒有模型，只有 `env.reset()` 和 `env.step(s, a)`。介面和 gym 環境一樣，只是精簡過。

### 步驟 2：計算回報（反向掃描）

```python
def returns_from(trajectory, gamma):
    returns = []
    G = 0.0
    for _, _, r in reversed(trajectory):
        G = r + gamma * G
        returns.append(G)
    return list(reversed(returns))
```

一次掃描，`O(T)`。向後的遞迴 `G_t = r_{t+1} + γ G_{t+1}` 不用重新加總。

### 步驟 3：首次造訪 MC 評估

```python
def mc_policy_evaluation(env, policy, episodes, gamma=0.99):
    V = defaultdict(float)
    counts = defaultdict(int)
    for _ in range(episodes):
        trajectory = rollout(env, policy)
        returns = returns_from(trajectory, gamma)
        seen = set()
        for t, ((s, _, _), G) in enumerate(zip(trajectory, returns)):
            if s in seen:
                continue
            seen.add(s)
            counts[s] += 1
            V[s] += (G - V[s]) / counts[s]
    return V
```

真正做事的是三行：首次造訪時把狀態標成看過、把計數加一、更新累計平均。

### 步驟 4：ε-貪婪 MC 控制（同政策，on-policy）

```python
def mc_control(env, episodes, gamma=0.99, epsilon=0.1):
    Q = defaultdict(lambda: {a: 0.0 for a in ACTIONS})
    counts = defaultdict(lambda: {a: 0 for a in ACTIONS})

    def policy(s):
        if random() < epsilon:
            return choice(ACTIONS)
        return max(Q[s], key=Q[s].get)

    for _ in range(episodes):
        trajectory = rollout(env, policy)
        returns = returns_from(trajectory, gamma)
        seen = set()
        for (s, a, _), G in zip(trajectory, returns):
            if (s, a) in seen:
                continue
            seen.add((s, a))
            counts[s][a] += 1
            Q[s][a] += (G - Q[s][a]) / counts[s][a]
    return Q, policy
```

### 步驟 5：和 DP 的黃金標準比較

`V^π` 的 MC 估計，在回合數走向無限時，應該和第 02 課的 DP 結果一致。實務上：4×4 GridWorld 跑 5 萬個回合，可以進到 DP 答案的 `~0.1` 以內。

## 容易踩的坑

- **無限回合。** MC 要求回合會*終止*。如果政策可能永遠打轉，就把 `max_steps` 封頂，把封頂當成隱含的失敗。隨機政策的 GridWorld 常常逾時——這很正常，只要你算對。
- **變異。** MC 用完整回報。回合一長，變異（variance）就很大——結尾一個倒楣的報酬，會把 `V(s_0)` 挪動同樣的量。TD 方法（第 04 課）用自助把這個切開。
- **狀態覆蓋。** 全新的 Q 如果有平手，貪婪 MC 永遠只會試一個動作。你*必須*探索（ε-貪婪、探索性起始、UCB）。
- **非平穩政策。** 如果 `π` 會變（像 MC 控制那樣），舊回報來自另一個政策。常數 α 的 MC 處理得了；樣本平均的 MC 不行。
- **異政策重要性抽樣。** 權重 `π(a|s)/μ(a|s)` 沿著軌跡相乘。變異隨視野爆炸。改用逐步（per-decision）加權重要性抽樣來壓住，或改走 TD。

## Use It｜實際應用

2026 年蒙地卡羅方法的角色：

| 用途 | 為什麼用 MC |
|------|-------------|
| 短視野遊戲（二十一點、撲克） | 回合自然終止；回報乾淨。 |
| 已記錄政策的離線評估 | 在存下來的軌跡上平均折扣回報。 |
| 蒙地卡羅樹搜尋（AlphaZero） | 從樹葉做 MC 展開，引導選擇。 |
| LLM 的 RL 評估 | 給定一個政策，在抽樣出來的完成結果上算平均報酬。 |
| PPO 裡的基準（baseline）估計 | 優勢目標 `A_t = G_t - V(s_t)` 用的是 MC 的 `G_t`。 |
| 教 RL | 真正會動的演算法裡最單純的——把自助剝掉，核心就露出來。 |

現代深度 RL 演算法（PPO、SAC）用 `n` 步回報或 GAE，在純 MC（完整回報）和純 TD（一步自助）之間內插。兩個端點是同一個估計器的實例。

## Ship It｜交付成果

存成 `outputs/skill-mc-evaluator.md`：

```markdown
---
name: mc-evaluator
description: Evaluate a policy via Monte Carlo rollouts and produce a convergence report with DP-comparison if available.
version: 1.0.0
phase: 9
lesson: 3
tags: [rl, monte-carlo, evaluation]
---

Given an environment (episodic, with reset+step API) and a policy, output:

1. Method. First-visit vs every-visit MC. Reason.
2. Episode budget. Target number, variance diagnostic, expected standard error.
3. Exploration plan. ε schedule (if needed) or exploring starts.
4. Gold-standard comparison. DP-optimal V* if tabular; otherwise a bound from a Q-learning / PPO baseline.
5. Termination check. Max-step cap, timeouts, handling of non-terminating trajectories.

Refuse to run MC on non-episodic tasks without a finite horizon cap. Refuse to report V^π estimates from fewer than 100 episodes per state for tabular tasks. Flag any policy with zero-variance actions as an exploration risk.
```

## Exercises｜練習

1. **簡單。** 在 4×4 GridWorld 上，實作均勻隨機政策的首次造訪 MC 評估。跑 1 萬個回合。把 `V(0,0)` 畫成回合數的函數，和 DP 的答案畫在一起。
2. **中等。** 實作 ε-貪婪 MC 控制，`ε ∈ {0.01, 0.1, 0.3}`。比較 2 萬個回合後的平均回報。曲線長什麼樣子？偏差－變異取捨落在哪裡？
3. **困難。** 實作*異政策* MC 加上重要性抽樣：在均勻隨機政策 `μ` 下蒐集資料，為確定性最佳政策 `π` 估計 `V^π`。比較普通 IS、逐步 IS、加權 IS。哪個變異最低？

## Key Terms｜關鍵術語

| 術語 | 常見說法 | 實際意義 |
|------|-----------------|-----------------------|
| 蒙地卡羅 | 「隨機抽樣」 | 用從分布抽出的獨立同分布樣本做平均，來估計期望。 |
| 回報 `G_t` | 「未來報酬」 | 從步驟 `t` 到回合結束的折扣報酬加總：`Σ_{k≥0} γ^k r_{t+k+1}`。 |
| 首次造訪 MC | 「每個狀態只算一次」 | 一個回合裡只有第一次造訪會計入價值估計。 |
| 每次造訪 MC | 「每次造訪都用」 | 每次造訪都計入；稍微有偏，但樣本效率較高。 |
| ε-貪婪 | 「探索雜訊」 | 以機率 `1-ε` 挑貪婪動作；以機率 `ε` 挑隨機動作。 |
| 重要性抽樣 | 「修正從錯的分布抽樣」 | 用 `π(a\|s)/μ(a\|s)` 的乘積把回報重新加權，從 `μ` 的資料估計 `V^π`。 |
| 同政策 | 「從自己的資料學」 | 目標政策 = 行為政策。原味 MC、PPO、SARSA。 |
| 異政策 | 「從別人的資料學」 | 目標政策 ≠ 行為政策。經過重要性抽樣的 MC、Q-learning、DQN。 |

## Further Reading｜延伸閱讀

- [Sutton & Barto (2018). Ch. 5 — Monte Carlo Methods](http://incompleteideas.net/book/RLbook2020.pdf) ——標準講法。
- [Singh & Sutton (1996). Reinforcement Learning with Replacing Eligibility Traces](https://link.springer.com/article/10.1007/BF00114726) ——首次造訪對上每次造訪的分析。
- [Precup, Sutton, Singh (2000). Eligibility Traces for Off-Policy Policy Evaluation](http://incompleteideas.net/papers/PSS-00.pdf) ——異政策 MC 和變異控制。
- [Mahmood et al. (2014). Weighted Importance Sampling for Off-Policy Learning](https://arxiv.org/abs/1404.6362) ——現代的低變異 IS 估計器。
- [Tesauro (1995). TD-Gammon, A Self-Teaching Backgammon Program](https://dl.acm.org/doi/10.1145/203330.203343) ——MC／TD 自我對弈收斂到超越人類的第一個大規模實證；這個階段後半每一課的概念前身。
