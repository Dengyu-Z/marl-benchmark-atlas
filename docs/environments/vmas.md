# VMAS

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Vectorized 2D multi-robot simulation with configurable scenarios. / 支持批量运行的二维多机器人仿真。

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
