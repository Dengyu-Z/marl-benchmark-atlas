# Mitigating Relative Over-Generalization in Multi-Agent Reinforcement Learning

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | supplied arXiv:2411.11099v1 |
| Policy regime | off-policy |
| Training / execution | decentralized MaxMax Q-learning |
| Evidence locator | Section 5.1; Figure 3; Appendix A |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

Differential games, six modified MPE scenarios and MA-MuJoCo Half-Cheetah. RO-specific reward shaping changes the benchmark relative to default MPE.

[Didactic coordination games](../docs/environments/coordination-games.md), [MPE / MPE2](../docs/environments/mpe.md), [Multi-Agent MuJoCo](../docs/environments/mamujoco.md)

## Protocol details retained

Distinguish joint-entry reward/solo-entry penalties, heterogeneous agents/targets, sequential tasks and the trained prey. Full budgets remain to be transcribed.

## Source and implementation

[Paper / primary record](https://arxiv.org/abs/2411.11099)

[Author code](https://github.com/Tingz0/Maxmax_Q_learning)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
