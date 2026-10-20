# SUMO-RL traffic signals

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Traffic signals cooperate through a road network. / 路口信号灯通过道路网络形成耦合控制问题。

## 先看懂这个环境

| 你要知道什么 | 直观解释 |
| --- | --- |
| 智能体是谁 | 道路网络中控制信号灯的路口控制器 |
| 要完成什么 | 调节交通灯，让网络里的排队和等待下降。 |
| 每一步做什么 | 按离散决策选择信号相位；周期等参数需记录。 |
| 动作到底是哪类 | 离散相位选择，具体任务定义为准。 |
| 奖励何时出现 | 通常有路口交通状态相关反馈；排队、等待等目标的定义可不同。 |
| 可先比较的算法 | MAPPO 等图上合作方法；选择局部／团队奖励聚合必须与问题一致。 |

适用范围：SUMO-RL 信号控制；本文映射的是图耦合交通设置。

这里的算法名称表示**可检查的候选接口**，不是性能排名，也不代表已经跑通。动作类型只是第一道筛选；继续看[算法适配指南](../algorithm-fit.zh-CN.md)。

## Implementation and evidence

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | SUMO + sumo-rl |
| Observations | intersection-local traffic features |
| Reward | per-signal traffic objective |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Road network, demand/routes, signal timings, SUMO version and reward definition affect results. The MAPO 28×7 experiment is a specific configuration.

## What to measure

Record team reward, queue length and waiting time; preserve the graph and local reward support.

## Getting started

Useful for graph-local credit assignment. There is no claim that the large 196-signal experiment is a low-compute starting point.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official SUMO-RL](https://github.com/LucasAlegre/sumo-rl)

## Papers in this edition

- [Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization](../../papers/aggregate-advantage.md)

Tags: `graph-coupling`, `credit-assignment`, `traffic`
