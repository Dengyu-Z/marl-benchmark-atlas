# SMACv2

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Randomized unit teams and starting conditions extend SMAC. / 随机化队伍与初始条件的战斗协作基准。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 随机生成队伍中的己方作战单位 |
| 要完成什么 | 在随机单位构成和初始位置下击败敌队，学习更稳健的配合。 |
| 每一步做什么 | 选择移动或攻击目标，可用动作随战况变化。 |
| 动作到底是哪类 | 离散；人数、单位类型和 mask 需逐配置核查。 |
| 奖励何时出现 | 战斗奖励、胜利奖励与视野设置由具体配置决定。 |
| 可先比较的算法 | MAPPO／HAPPO／QMIX；同时固定种族、生成分布、视野和评估种子。 |

适用范围：SC2 引擎版 SMACv2；不是 SMAX 中名称相似的任务。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | StarCraft II + SMACv2 |
| Observations | local sight; configuration-dependent |
| Reward | configuration-dependent combat reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Do not confuse engine-based SMACv2 with SMAX tasks named smacv2_*_units. Race, team generator, unit distribution and field of view must be recorded.

## What to measure

Report win rate and return over held-out episode seeds; separate training seeds from evaluation seeds.

## Getting started

Run the provided optional protoss_5_vs_5 smoke recipe only after SC2 and the required maps are installed. Install cost is not a measured runtime estimate.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official SMACv2](https://github.com/oxwhirl/smacv2)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [R3DM: Enabling Role Discovery and Diversity Through Dynamics Models in Multi-agent Reinforcement Learning](../../papers/r3dm.md)

Tags: `coordination`, `heterogeneity`, `population-generalization`, `combat`
