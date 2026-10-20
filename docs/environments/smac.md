# SMAC

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Control allied combat units against the built-in opponent. / 控制己方单位协同作战。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | SC2 游戏引擎中的己方作战单位 |
| 要完成什么 | 协同击败内置 AI 控制的敌军；训练的是己方团队。 |
| 每一步做什么 | 选择移动、停止、攻击等命令，并使用可用动作 mask。 |
| 动作到底是哪类 | 离散；每张地图的单位和动作数量不同。 |
| 奖励何时出现 | 可用稠密战斗奖励或稀疏胜利奖励，必须看论文配置。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX 等离散合作方法；先完成 SC2 与地图安装。 |

适用范围：原版 SMAC；SC2 游戏版本、地图与奖励模式都是任务定义的一部分。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | StarCraft II + SMAC |
| Observations | local sight and available-action masks |
| Reward | dense or sparse; paper-specific |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Pin the StarCraft II build, maps, SMAC revision and reward mode. R3DM records SC2 4.10; another build is not automatically comparable.

## What to measure

Report win rate, return, map and evaluation action mode. Keep action-availability masks during evaluation.

## Getting started

Requires external game installation. Validate one process before parallel workers; a learner GPU is not the same as the simulator process.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official SMAC](https://github.com/oxwhirl/smac)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [R3DM: Enabling Role Discovery and Diversity Through Dynamics Models in Multi-agent Reinforcement Learning](../../papers/r3dm.md)
- [Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning](../../papers/lazy-agents.md)
- [Learning group collaboration for efficient multi-agent reinforcement learning](../../papers/g-mat.md)
- [In-Context Fully Decentralized Cooperative Multi-Agent Reinforcement Learning](../../papers/rac.md)

Tags: `coordination`, `heterogeneity`, `combat`
