# SUMO-RL traffic signals

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Traffic signals cooperate through a road network. / 路口信号灯通过道路网络形成耦合控制问题。

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
