# Multi-Agent Guided Policy Optimization

[Paper index](../docs/paper-index.md) · [中文入口](../README.zh-CN.md)

| Field | Record |
| --- | --- |
| Source/version | ICLR 2026 (printed supplied PDF header) |
| Policy regime | on-policy |
| Training / execution | centralized guidance; decentralized actors |
| Evidence locator | Section 5, PDF pp.6–8; Appendix B; Appendix C |
| Checked | 2026-10-20 |
| Verification | Literature checked; no reproduction claimed |

## Benchmark mapping

43 JAX tasks: CoordSum 4, LBF 7, Connector 4, MPE 3, RWARE 15, SMAX 10. CoordSum replaces MaBrax relative to Sable and SMAX counts differ.

[Didactic coordination games](../docs/environments/coordination-games.md), [Level-Based Foraging](../docs/environments/lbf.md), [Connector](../docs/environments/connector.md), [MPE / MPE2](../docs/environments/mpe.md), [RWARE / Robot Warehouse](../docs/environments/rware.md), [SMAX](../docs/environments/smax.md)

## Protocol details retained

Centralized guidance and decentralized deployment must be recorded separately. This mapping does not import Sable hyperparameters into MAGPO.

## Source and implementation

[Paper / primary record](https://arxiv.org/abs/2507.18059)

[Author code](https://github.com/liyheng/MAGPO)

Publication labels describe the supplied document or the linked primary record, not a continuing publication-status monitor. Missing budgets or URLs are intentionally left unresolved. See [source policy](../docs/source-policy.md).
