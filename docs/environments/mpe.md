# MPE / MPE2

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Particle agents navigate, communicate or compete in a 2D world. / 二维粒子导航、通信和协作或竞争。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 二维平面上移动的小圆点 |
| 要完成什么 | 以 simple_spread 为例：分工覆盖所有地标，同时减少相互碰撞。 |
| 每一步做什么 | 离散版选择方向；连续版输出各方向的控制强度。 |
| 动作到底是哪类 | 两种版本都有；Sable 使用连续版，MPE2 默认可设为离散。 |
| 奖励何时出现 | simple_spread 根据地标距离和碰撞给反馈，回报通常可以是负数。 |
| 可先比较的算法 | MAPPO／HAPPO 两种动作都可；QMIX 选离散版；MADDPG 选连续版；HARL HASAC 有两种分支。 |

适用范围：密集奖励说明只针对 simple_spread；不能推广到所有 MPE 场景。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | both |
| Implementations | JaxMARL / MPE2 / historical MPE |
| Observations | scenario-dependent; do not assume every task is partially observable |
| Reward | scenario and local_ratio dependent |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Smoke passed for the specific MPE2/Python LBF recipe; see [ledger](../verification.md) |

## What changes comparability

Sable uses continuous JaxMARL simple_spread for 3/5/10 agents. MPE2 supports discrete and continuous actions and exposes a different action vector. This repository's MPE2 smoke example is not an exact Sable reproduction.

## What to measure

Record N, landmarks, local_ratio, action dimensionality, termination and max_cycles. The reward can be negative because distance and collision costs are penalties.

## Getting started

Best first reset/step example here. Communication priors, MMQ and SS-MARL modify different parts of MPE; their scores belong to different task definitions.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [MPE2](https://github.com/Farama-Foundation/MPE2)
- [Simple Spread API](https://mpe2.farama.org/environments/simple_spread/)
- [JaxMARL](https://github.com/bold-lab-ai/JaxMARL)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Reinforcement Learning with Communication-Constrained Priors](../../papers/communication-priors.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)
- [Scalable Safe Multi-Agent Reinforcement Learning for Multi-Agent System](../../papers/safe-marl.md)
- [Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning](../../papers/mmq.md)

Tags: `coordination`, `communication`, `continuous-control`
