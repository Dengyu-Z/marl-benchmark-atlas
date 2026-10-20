# Overcooked

[Environment index](../environment-index.md) · [中文入口](../../README.zh-CN.md)

Two cooks coordinate ingredient preparation, cooking and delivery. / 两名厨师协同备料、烹饪与送餐。

| Field | This entry |
| --- | --- |
| Resource type | online |
| Actions | discrete |
| Implementations | overcooked_ai and paper wrappers |
| Observations | layout/featurizer dependent |
| Reward | sparse deliveries; optional shaping |
| Evidence | Literature checked · 2026-10-20 |
| Runtime | Not run in this repository |

## What changes comparability

Different layouts, shaping schedules and wrappers change the problem. Overcooked and OvercookedV2 are distinct implementations.

## What to measure

Report sparse delivery score, shaped training reward separately, layout, horizon and partner protocol.

## Getting started

Useful for role/partner experiments, but held-out partners and layouts must be designed explicitly; they are not guaranteed by a single training run.

Hardware costs are not measured here. A recipe or upstream link does not establish a successful installation or baseline reproduction. See [verification levels](../verification.md).

## Primary sources / 官方入口

- [Official Overcooked-AI](https://github.com/HumanCompatibleAI/overcooked_ai)

## Papers in this edition

- [Optimistic Multi-Agent Policy Gradient](../../papers/optimappo.md)

Tags: `coordination`, `role-specialization`, `partner-generalization`
