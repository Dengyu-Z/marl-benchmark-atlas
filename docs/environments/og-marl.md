# OG-MARL

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Datasets and baselines for learning from fixed multi-agent trajectories. / 基于固定多智能体轨迹学习的离线数据与基线。

| Field | This entry |
| --- | --- |
| Resource type | offline-dataset |
| Actions | both |
| Implementations | offline dataset collection + baseline code |
| Observations | dataset dependent |
| Reward | recorded returns; collection-policy dependent |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

This is an offline data resource, not one of Sable's six online suites. Dataset version, source simulator, collection policies and train/evaluation protocol are part of its identity.

## What to measure

Record dataset quality, transition/episode counts, behavior coverage and online evaluation budget, if any.

## Getting started

Added as a separate resource entry so online environments and fixed datasets are never conflated. Specific downloadable datasets are not enumerated here.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official OG-MARL](https://github.com/instadeepai/og-marl)

## Papers in this edition

Resource entry; not evaluated by the seed paper set.

Tags: `offline-rl`, `dataset-quality`, `coverage`
