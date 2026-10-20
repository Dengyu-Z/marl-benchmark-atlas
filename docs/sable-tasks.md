# Sable: the 45-task main benchmark

[Paper card](../papers/sable.md) · [中文说明](sable-guide.zh-CN.md)

Source: supplied Sable arXiv:2410.01706v5, Section 4 and Appendix C Table 2 (PDF p.25), with task semantics in Appendix B. Task labels below are typographically normalized paper labels, not tested environment registration strings. The printed humanoid partition is normalized as `9|8`; Connector labels retain the table form (`con-5x5x3a`).

| Suite | Main tasks |
| --- | --- |
| [RWARE / Robot Warehouse](environments/rware.md) | 15 |
| [Level-Based Foraging](environments/lbf.md) | 7 |
| [Connector](environments/connector.md) | 4 |
| [SMAX](environments/smax.md) | 11 |
| [MaBrax](environments/mabrax.md) | 5 |
| [MPE / MPE2](environments/mpe.md) | 3 |

**Total: 45.** NEOM and the extra 32/64/128-agent LBF scalability configurations are outside this table.

| Suite | Paper task label | Actions | Implementation |
| --- | --- | --- | --- |
| RWARE / Robot Warehouse | `tiny-2ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `tiny-2ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `tiny-4ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `tiny-4ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `small-4ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `small-4ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `medium-4ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `medium-4ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `large-4ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `large-4ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `xlarge-4ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `xlarge-4ag-hard` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `medium-6ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `large-8ag` | discrete | Jumanji via Mava |
| RWARE / Robot Warehouse | `large-8ag-hard` | discrete | Jumanji via Mava |
| Level-Based Foraging | `8x8-2p-2f-coop` | discrete | Jumanji via Mava |
| Level-Based Foraging | `2s-8x8-2p-2f-coop` | discrete | Jumanji via Mava |
| Level-Based Foraging | `10x10-3p-3f` | discrete | Jumanji via Mava |
| Level-Based Foraging | `2s-10x10-3p-3f` | discrete | Jumanji via Mava |
| Level-Based Foraging | `15x15-3p-5f` | discrete | Jumanji via Mava |
| Level-Based Foraging | `15x15-4p-3f` | discrete | Jumanji via Mava |
| Level-Based Foraging | `15x15-4p-5f` | discrete | Jumanji via Mava |
| Connector | `con-5x5x3a` | discrete | Jumanji via Mava |
| Connector | `con-7x7x5a` | discrete | Jumanji via Mava |
| Connector | `con-10x10x10a` | discrete | Jumanji via Mava |
| Connector | `con-15x15x23a` | discrete | Jumanji via Mava |
| SMAX | `2s3z` | discrete | JaxMARL via Mava |
| SMAX | `3s5z` | discrete | JaxMARL via Mava |
| SMAX | `3s vs 5z` | discrete | JaxMARL via Mava |
| SMAX | `6h vs 8z` | discrete | JaxMARL via Mava |
| SMAX | `5m vs 6m` | discrete | JaxMARL via Mava |
| SMAX | `10m vs 11m` | discrete | JaxMARL via Mava |
| SMAX | `3s5z vs 3s6z` | discrete | JaxMARL via Mava |
| SMAX | `27m vs 30m` | discrete | JaxMARL via Mava |
| SMAX | `smacv2 5 units` | discrete | JaxMARL via Mava |
| SMAX | `smacv2 10 units` | discrete | JaxMARL via Mava |
| SMAX | `smacv2 20 units` | discrete | JaxMARL via Mava |
| MaBrax | `hopper 3x1` | continuous | JaxMARL via Mava |
| MaBrax | `halfcheetah 6x1` | continuous | JaxMARL via Mava |
| MaBrax | `walker2d 2x3` | continuous | JaxMARL via Mava |
| MaBrax | `ant 4x2` | continuous | JaxMARL via Mava |
| MaBrax | `humanoid 9\|8` | continuous | JaxMARL via Mava |
| MPE / MPE2 | `simple spread 3ag` | continuous | JaxMARL via Mava |
| MPE / MPE2 | `simple spread 5ag` | continuous | JaxMARL via Mava |
| MPE / MPE2 | `simple spread 10ag` | continuous | JaxMARL via Mava |
