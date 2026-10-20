# Google Research Football

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Cooperative football scenarios with passing, movement and scoring. / 通过传球、跑位和射门完成配合。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 足球场上由算法控制的球员 |
| 要完成什么 | 通过跑位、传球、配合和射门，在指定足球场景中完成目标。 |
| 每一步做什么 | 从移动、传球、射门等足球动作中选一个。 |
| 动作到底是哪类 | 离散；具体动作集合由环境配置决定。 |
| 奖励何时出现 | 只奖励进球与附加中途奖励是不同设置。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX 等合作方法；必须匹配可控球员数和团队奖励协议。 |

适用范围：Google Research Football；academy 场景、观测表示与奖励塑形需单独记录。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Football engine + Python wrappers |
| Observations | observation-representation dependent |
| Reward | sparse scoring or shaped, by experiment |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Academy scenario, controlled-player count, observation representation, shared reward and scoring/checkpoint shaping are part of the task identity.

## What to measure

Report score/win or completion as appropriate, return, episode limits and reward mode.

## Getting started

CEE, LAIES and g-MAT all use football, but sparse/dense settings must be checked before comparing their plots.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official GRF](https://github.com/google-research/football)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning](../../papers/lazy-agents.md)
- [Learning group collaboration for efficient multi-agent reinforcement learning](../../papers/g-mat.md)

Tags: `sparse-reward`, `coordination`, `sports`
