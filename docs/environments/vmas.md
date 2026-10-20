# VMAS

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Vectorized 2D multi-robot simulation with configurable scenarios. / 支持批量运行的二维多机器人仿真。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 二维模拟器里的机器人或移动实体 |
| 要完成什么 | 不是一个固定游戏；任务可以是导航、搬运、协作覆盖或竞争。 |
| 每一步做什么 | 根据场景输出移动控制；部分场景也支持离散动作。 |
| 动作到底是哪类 | 环境家族支持两类动作；先选具体 scenario。 |
| 奖励何时出现 | 奖励与任务一起定义，不能给整个 VMAS 一个固定的稀疏度。 |
| 可先比较的算法 | 先确定场景和合作／竞争关系，再用动作类型筛选；不要对整个家族给统一算法排名。 |

适用范围：VMAS 是模拟器与场景集合，不是单一数据集。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | both |
| Implementations | PyTorch vectorized simulator |
| Observations | scenario-dependent |
| Reward | scenario-dependent shared or per-agent reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

A simulator family is not a single benchmark. DiCo tasks have their own observation, reward and goal-assignment choices. CAMAR uses VMAS as a throughput comparator, not necessarily a policy-quality baseline.

## What to measure

For diversity studies record SND, parameter sharing, goal assignment and reward in addition to entropy.

## Getting started

Start with a documented scenario in BenchMARL. Record batch size and simulator device for throughput comparisons.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official VMAS](https://github.com/proroklab/VectorizedMultiAgentSimulator)
- [BenchMARL](https://github.com/facebookresearch/BenchMARL)

## Papers in this edition

- [CAMAR: Continuous Actions Multi-Agent Routing](../../papers/camar-paper.md)
- [Controlling Behavioral Diversity in Multi-Agent Reinforcement Learning](../../papers/dico.md)

Tags: `coordination`, `behavioral-diversity`, `continuous-control`, `vectorized`
