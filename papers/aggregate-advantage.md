# Aggregate in the Advantage, Not the Ratio: A Canonical-Form Analysis of Cooperative Multi-Agent Policy Optimization

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | supplied preprint arXiv:2607.17924v1 |
| Policy regime | on-policy |
| Training / execution | PPO; graph-local aggregation |
| Evidence locator | Section 4; Appendix C.1–C.3 |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

Controlled graph-coupled games plus SUMO-RL traffic signals. Appendix C.3 uses a 28×7 grid with 196 signals; it is not a standard SMAC benchmark.

[Didactic coordination games](../docs/environments/coordination-games.md), [SUMO-RL traffic signals](../docs/environments/sumo-rl.md)

## Protocol details retained

Known coupling graphs and per-agent rewards are essential to this study. Preserve graph, reward support and ratio support separately.

## Source and implementation

[Paper / primary record](https://arxiv.org/abs/2607.17924)

[Author code](https://github.com/RS2002/MAPO)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
