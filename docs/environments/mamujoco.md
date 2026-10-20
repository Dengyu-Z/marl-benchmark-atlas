# Multi-Agent MuJoCo

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Split a MuJoCo robot's actuators among collaborating agents. / 将 MuJoCo 机器人执行器分配给多个智能体。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | MuJoCo 机器人各部分的控制器 |
| 要完成什么 | 共同控制一个机器人运动；例如不同智能体控制不同腿或关节组。 |
| 每一步做什么 | 输出关节控制量／力矩向量。 |
| 动作到底是哪类 | 连续；维度由机器人和关节分组决定。 |
| 奖励何时出现 | 常见运动任务逐步给予前进、存活或控制代价反馈，具体组成随任务变化。 |
| 可先比较的算法 | 连续动作 MAPPO／HAPPO／HASAC／MADDPG；需核对局部观测半径和动作划分。 |

适用范围：本文指运动控制任务；版本与 MaBrax 不可直接互换。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | MA-MuJoCo / Gymnasium-Robotics variants |
| Observations | joint-partition and observation-radius dependent |
| Reward | robot-specific locomotion reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Original MA-MuJoCo, newer wrappers and MaBrax must be tracked as separate implementations. Match partition, MuJoCo version and observation configuration.

## What to measure

Report episode return, robot, partition and evaluation noise. Do not compare values across different reward normalizations.

## Getting started

Relevant for OptiMAPPO and MMQ. Use the implementation referenced by each paper rather than substituting a similarly named environment.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Original repository](https://github.com/schroederdewitt/multiagent_mujoco)
- [Gymnasium-Robotics](https://robotics.farama.org/)

## Papers in this edition

- [Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning](../../papers/mmq.md)
- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `continuous-control`, `heterogeneity`
