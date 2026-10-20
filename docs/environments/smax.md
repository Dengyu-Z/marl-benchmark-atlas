# SMAX

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

A JAX combat simulator inspired by SMAC, without the StarCraft II engine. / 无需星际争霸引擎的 JAX 战斗协作环境。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 战斗小队中的己方单位 |
| 要完成什么 | 配合走位、集火和攻击时机，击败敌方队伍。 |
| 每一步做什么 | 选择移动、停止或攻击某个敌人。 |
| 动作到底是哪类 | 离散：攻击目标数量影响动作数量；还需检查可用动作 mask。 |
| 奖励何时出现 | Sable 同时奖励战斗伤害与最终胜利。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX；保持攻击可用性 mask 与同一单位生成器。 |

适用范围：JaxMARL 的 SMAX；不能用 SC2 引擎结果代替。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | JaxMARL |
| Observations | local combat observations |
| Reward | combat shaping plus victory reward in Sable |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

SMAX is not SMAC or engine-based SMACv2. The three smacv2_*_units labels in Sable are still SMAX tasks. Never merge their win-rate or return tables.

## What to measure

Record win rate and return separately, unit composition, opponent generator, attack availability and reward settings.

## Getting started

Useful for accelerator-based combat experiments; separate compile time from steady-state throughput.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `coordination`, `heterogeneity`, `jax`
