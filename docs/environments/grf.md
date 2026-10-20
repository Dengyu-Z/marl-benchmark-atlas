# Google Research Football

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Cooperative football scenarios with passing, movement and scoring. / 通过传球、跑位和射门完成配合。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Football engine + Python wrappers |
| Observations | observation-representation dependent |
| Reward | sparse scoring or shaped, by experiment |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Academy scenario, controlled-player count, observation representation, shared reward and scoring/checkpoint shaping are part of the task identity.

## What to measure

Report score/win or completion as appropriate, return, episode limits and reward mode.

## Getting started

CEE, LAIES and g-MAT all use football, but sparse/dense settings must be checked before comparing their plots.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official GRF](https://github.com/google-research/football)

## Papers in this edition

- [Causality-Aware Efficient Exploration for Cooperative Multi-Agent Reinforcement Learning](../../papers/cee.md)
- [Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning](../../papers/lazy-agents.md)
- [Learning group collaboration for efficient multi-agent reinforcement learning](../../papers/g-mat.md)

Tags: `sparse-reward`, `coordination`, `sports`
