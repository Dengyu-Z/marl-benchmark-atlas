# NEOM (Sable scalability task)

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

A synthetic cooperative task for scaling to many agents. / 用于大规模智能体扩展实验的合成协作任务。

| Field | This entry |
| --- | --- |
| Resource type | paper-specific |
| Actions | discrete |
| Implementations | Sable paper/code |
| Observations | position target and action-history description in paper |
| Reward | paper-defined coordination reward |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

NEOM belongs to the additional scalability study, not the six-suite 45-task main performance benchmark. A current public API path is not verified in this edition.

## What to measure

Record agent count, solved coordination criteria, memory and throughput; distinguish recurrent context scaling from agent scaling.

## Getting started

Consult Sable Section 4.2 and Appendix B.7. No local smoke recipe or current upstream API is asserted.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Sable / Mava](https://github.com/instadeepai/Mava)

## Papers in this edition

- [Sable: a Performant, Efficient and Scalable Sequence Model for MARL](../../papers/sable.md)

Tags: `scalability`, `coordination`
