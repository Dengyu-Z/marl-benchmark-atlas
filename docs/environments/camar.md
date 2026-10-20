# CAMAR

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Continuous multi-agent routing with obstacles and configurable dynamics. / 含障碍和不同动力学的连续多智能体路径规划。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 要穿过障碍到达终点的移动机器人 |
| 要完成什么 | 让多个机器人分别到达目标，同时控制碰撞、路径和耗时。 |
| 每一步做什么 | 输出连续运动控制，具体含义取决于动力学模型。 |
| 动作到底是哪类 | 连续；不同动力学下控制向量的含义不同。 |
| 奖励何时出现 | 目标、距离／时间和碰撞项的权重随具体设置变化。 |
| 可先比较的算法 | 连续 MAPPO／HAPPO／MASAC／MADDPG；同时记录成功、碰撞和路径质量。 |

适用范围：CAMAR 连续路径规划；不是网格上按上下左右走的同一类动作接口。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | continuous |
| Implementations | CAMAR |
| Observations | local vector observations |
| Reward | goal, path and collision terms |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Holonomic versus other dynamics, maps, agent sizes and collision handling define different tasks. Reported simulator SPS is not a claim about learner end-to-end speed.

## What to measure

Use goal-reaching success, time/path quality and collision metrics together; retain the benchmark's tiered evaluation protocol.

## Getting started

This edition provides a literature card and upstream links, without a local installation or a performance claim.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official CAMAR](https://github.com/AIRI-Institute/CAMAR)
- [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/40209)

## Papers in this edition

- [CAMAR: Continuous Actions Multi-Agent Routing](../../papers/camar-paper.md)

Tags: `routing`, `continuous-control`, `heterogeneity`
