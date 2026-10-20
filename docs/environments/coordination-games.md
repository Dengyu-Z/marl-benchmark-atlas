# Didactic coordination games

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Small games isolate coordination failures and relative overgeneralization. / 用可控小博弈隔离协作与相对过度泛化机制。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 选择数字或小博弈动作的决策者 |
| 要完成什么 | 通过联合动作获得高收益，用可控例子分析协调失败。 |
| 每一步做什么 | 矩阵博弈选行／列；CoordSum 选数字；微分博弈输出连续控制。 |
| 动作到底是哪类 | 这个分类中有离散也有连续；每种游戏要单独定义。 |
| 奖励何时出现 | 收益直接由 payoff table、上下文或已知耦合图决定。 |
| 可先比较的算法 | 离散游戏可测 QMIX／PPO 类；连续游戏选连续策略。已知最优解适合机制诊断，不代表复杂任务性能。 |

适用范围：教学／诊断任务的集合，不是统一的可比环境。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | paper-specific |
| Actions | both |
| Implementations | paper-specific implementations |
| Observations | constant, phase or context observation |
| Reward | explicit payoff/coupling design |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

RAC matrix games, MAGPO CoordSum, MMQ differential games and MAPO graph-coupled games are distinct tasks. This grouping is for discovery, not for pooling numerical results.

## What to measure

Publish payoff table, horizon, initial-state distribution, observation and optimal joint solution. A toy-game effect does not establish general benchmark improvement.

## Getting started

Use for a fast mechanism check before a larger simulator. Select the exact game and retrieve the original implementation from the relevant paper card.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

See the linked paper cards for each game implementation.

## Papers in this edition

- [In-Context Fully Decentralized Cooperative Multi-Agent Reinforcement Learning](../../papers/rac.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)
- [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](../../papers/aggregate-advantage.md)
- [Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning](../../papers/mmq.md)
- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `mechanism-diagnosis`, `relative-overgeneralization`, `credit-assignment`
