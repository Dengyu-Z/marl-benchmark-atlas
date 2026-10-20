# Connector

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Agents draw non-crossing paths from start to target without trapping each other. / 路径一旦走过就会阻塞，需协作连接起点与终点。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | Jumanji |
| Observations | Sable uses a local-view wrapper |
| Reward | connection reward plus step penalty in Sable |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Sable Appendix B.4 gives a paper-specific observation and reward description. Paper labels such as con-5x5x3a are not guaranteed to be registered environment IDs.

## What to measure

Report connected-agent fraction, return and time to completion. Distinguish reward aggregation per agent from team sums.

## Getting started

Use the smallest paper task before raising grid size and number of paths. Keep generator, wrapper and reward parameters with results.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Jumanji](https://github.com/instadeepai/jumanji)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)
- [Multi-Agent Guided Policy Optimization](../../papers/magpo.md)

Tags: `coordination`, `routing`, `jax`
