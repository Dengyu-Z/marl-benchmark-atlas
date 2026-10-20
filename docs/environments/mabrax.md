# MaBrax

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents control different joint groups of one robot. / 多个智能体共同控制机器人的不同关节。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 同一个机器人不同关节的控制器 |
| 要完成什么 | 多个控制器共同让机器人前进，并控制能耗与姿态。 |
| 每一步做什么 | 每个控制器输出其负责关节的力矩数值。 |
| 动作到底是哪类 | 连续：一个实数向量；动作维度取决于关节划分。 |
| 奖励何时出现 | 通常每步都有前进和控制代价相关反馈。 |
| 可先比较的算法 | 连续动作 MAPPO／HAPPO／HASAC／MADDPG；标准离散 QMIX 不能直接接力矩向量。 |

适用范围：Sable 附录 B.6 的 JaxMARL／Brax 机器人任务。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | JaxMARL + Brax |
| Observations | local joint and root-body information |
| Reward | forward progress minus control costs |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

MaBrax uses Brax physics. Matching a MA-MuJoCo joint partition does not make simulation dynamics or reference returns identical.

## What to measure

Record robot, joint partition, observation radius, simulator backend and reward components; compare continuous-action-compatible baselines.

## Getting started

Sable uses five robot/partition tasks. Start with a small partition; benchmark compilation and rollout separately.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)

Tags: `continuous-control`, `heterogeneity`, `jax`
