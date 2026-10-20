# Choose an environment by the question

[Home](../README.md) · [中文选型指南](selection-guide.zh-CN.md)

These are editorial starting points, not measured rankings of task difficulty or hardware cost. A feature of a simulator does not automatically create a generalization benchmark; define train/test distributions explicitly.

| Research question | Start with | Experimental control you must add or preserve |
| --- | --- | --- |
| Can agents learn sparse coordination? | [LBF](environments/lbf.md), [RWARE](environments/rware.md), sparse [GRF](environments/grf.md) | Sparse/dense reward, forced cooperation, early termination, success definition |
| Do agents discover useful roles? | [SMACv2](environments/smacv2.md), [VMAS](environments/vmas.md), [Overcooked](environments/overcooked.md) | Role metric, unit/goal heterogeneity, parameter sharing and reward |
| Does communication survive message loss? | Suitable [MPE](environments/mpe.md) communication scenarios | Explicit message channels, topology, loss/corruption process and test conditions |
| Does peer transfer help with new teammates? | [MPE](environments/mpe.md), [LBF](environments/lbf.md), [Overcooked](environments/overcooked.md) | Frozen teacher, held-out partners/contexts, equal budgets and no-transfer control |
| Is relative overgeneralization the failure? | [Didactic games](environments/coordination-games.md), the MMQ/OptiMAPPO configurations | Known optimum, payoff structure and controlled coordination penalties |
| Does a graph-local credit signal help? | [SUMO-RL](environments/sumo-rl.md), controlled graph-coupled games | Per-agent rewards, known graph, reward/advantage support and ratio support |
| Does a policy transfer to larger populations? | [SMACv2](environments/smacv2.md), [VMAS](environments/vmas.md), modified MPE | Population split, fixed observation/actor interface and zero-shot versus retraining |
| Can a simulator scale to many agents? | [SMAX](environments/smax.md), Jumanji, [NEOM](environments/neom.md), [CAMAR](environments/camar.md) | Compile/rollout/learner timing, batch size, hardware and memory |
| Can continuous controllers coordinate? | [MaBrax](environments/mabrax.md), [MA-MuJoCo](environments/mamujoco.md), [CAMAR](environments/camar.md) | Action partition, engine, control frequency and reward components |
| Does safety survive scaling? | SS-MARL's modified [MPE](environments/mpe.md), collision-aware routing | Separate cost and reward, constraint thresholds, obstacle distribution and unseen populations |
| Can training use only fixed data? | [OG-MARL](environments/og-marl.md) | Dataset version/quality, behavior coverage and any online interaction budget |
| What happens when agents enter or leave? | [Open Wildfire](environments/open-wildfire.md) | Entry/exit timing and agent/task openness; fixed-population runs are a separate control |

For a first experiment, use a small reset/step check, then train a baseline in one exact configuration. Widen the task set after the initial mechanism and evaluation protocol are clear. See [reproducibility](reproducibility.md).
