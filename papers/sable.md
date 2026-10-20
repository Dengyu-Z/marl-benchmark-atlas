# Sable: a Performant, Efficient and Scalable Sequence Model for MARL

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | ICML 2025; supplied arXiv v5 |
| Policy regime | on-policy |
| Training / execution | centralized autoregressive execution |
| Evidence locator | Section 4; Appendix B.1–B.7; Appendix C Tables 2–6; Appendix D |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

45 main tasks in six suites; NEOM and modified LBF are additional scaling experiments. Do not present the main Sable actor as a local-observation-only decentralized actor.

[RWARE / Robot Warehouse](../docs/environments/rware.md), [Level-Based Foraging](../docs/environments/lbf.md), [Connector](../docs/environments/connector.md), [SMAX](../docs/environments/smax.md), [MaBrax](../docs/environments/mabrax.md), [MPE / MPE2](../docs/environments/mpe.md), [NEOM (Sable scalability task)](../docs/environments/neom.md)

## Protocol details retained

Main protocol: 10 independent trials per task, 20M environment timesteps per run, 122 evaluation intervals, 32 episodes per interval. Task means and suite IQM use 95% bootstrap intervals. Main baselines: MAT, MAPPO, IPPO, MASAC, HASAC, QMIX; eligibility varies by action space.

## Source and implementation

[Paper / primary record](https://arxiv.org/abs/2410.01706)

[Author code](https://github.com/instadeepai/Mava)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
