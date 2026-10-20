# OG-MARL

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Datasets and baselines for learning from fixed multi-agent trajectories. / 基于固定多智能体轨迹学习的离线数据与基线。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 已经记录好的多智能体轨迹中的行为主体 |
| 要完成什么 | 用已有轨迹学习新策略；训练时未必允许重新向环境采样。 |
| 每一步做什么 | 动作由所选离线数据集决定，不是统一的一种。 |
| 动作到底是哪类 | 取决于具体数据来源；先查数据字段与行为策略。 |
| 奖励何时出现 | 奖励是轨迹里已经记录的数值，还需检查数据质量与覆盖。 |
| 可先比较的算法 | 选择离线 MARL 方法；off-policy 有 replay 不等于能可靠离线学习，不能直接照搬在线 MAPPO。 |

适用范围：这是离线数据资源集合，而不是一个在线游戏。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | offline-dataset |
| Actions | both |
| Implementations | offline dataset collection + baseline code |
| Observations | dataset dependent |
| Reward | recorded returns; collection-policy dependent |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

This is an offline data resource, not one of Sable's six online suites. Dataset version, source simulator, collection policies and train/evaluation protocol are part of its identity.

## What to measure

Record dataset quality, transition/episode counts, behavior coverage and online evaluation budget, if any.

## Getting started

Added as a separate resource entry so online environments and fixed datasets are never conflated. Specific downloadable datasets are not enumerated here.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official OG-MARL](https://github.com/instadeepai/og-marl)

## Papers in this edition

Resource entry; not evaluated by the seed paper set.

Tags: `offline-rl`, `dataset-quality`, `coverage`
