# Version and protocol traps

[Home](../README.md) · [中文入口](../README.zh-CN.md)

The unit of comparison is an exact experiment configuration, not an environment family name. The following differences are grounded in the supplied papers or the linked official documentation.

| Similar labels | Difference to preserve | Evidence |
| --- | --- | --- |
| SMAC / SMACv2 / SMAX | Game engine versus JAX simulation, random team generators and reward semantics | Sable Appendix B.2; [SMAC](https://github.com/oxwhirl/smac), [SMACv2](https://github.com/oxwhirl/smacv2), [JaxMARL](https://github.com/bold-lab-ai/JaxMARL) |
| `smacv2 5 units` in Sable / engine SMACv2 | Sable puts this task under SMAX | Sable Appendix C Table 2 |
| Python RWARE / Sable Jumanji RWARE | Collision resolution versus collision termination in the supplied paper | Sable Appendix B.1 |
| Standard LBF / Sable scaling LBF | Observation packing was modified for the large-population experiments | Sable Appendix B.3 |
| MaBrax / MA-MuJoCo | Brax versus MuJoCo physics even for the same joint partition | Sable Appendix B.6 |
| MPE `simple_spread` across libraries | Continuous/discrete switch, action vector, local_ratio, observations and episode limits | Sable Appendix B.5; [MPE2 Simple Spread](https://mpe2.farama.org/environments/simple_spread/) |
| Default MPE / MMQ / SS-MARL / communication-prior tasks | Coordination penalties, safety costs or message constraints alter the task | Respective paper cards: [MMQ](../papers/mmq.md), [SS-MARL](../papers/safe-marl.md), [communication priors](../papers/communication-priors.md) |
| SMAC dense / sparse rewards | A dense-reference curve and a sparse-task curve answer different questions | LAIES Section 5.1 |
| Return / win rate / event success | Reward shaping and conditioning can make these move in different directions | Metric definitions must accompany results |
| Environment step / agent step / gradient update | Multiplying by agents, batch size or update ratio changes the budget | Record counters and their units explicitly |
| Final / maximum / mean-over-training / absolute | Sable reports these separately; do not merge their reference tables | Sable Appendix C Tables 2–6; use the evaluation implementation for the precise absolute-performance definition |
| Simulator SPS / end-to-end training speed | Compilation, rendering, policy inference and optimizer costs differ | CAMAR Experimental Evaluation; Sable efficiency experiments |
| 250 episodes / 250 independent seeds | The open-credit manuscript describes evaluation runs with a fixed seed, not independent training replications | Open-credit experimental section |

For context-conditioned peer transfer, retain the no-transfer continuation and equal total budgets. Evaluate a decentralized actor without the teacher if deployment is decentralized. Measure retained skills on a separate retention context set. These are design recommendations, not a claim that the seed papers all use this protocol.

## Example: why higher event success can coexist with lower return

A policy can improve `P(success | attempted load)` while attempting fewer loads, reaching fewer food items, or spending more steps/collision penalties on each attempt. Log the numerator and denominator of event metrics and the full episode return. Do not interpret one conditional event rate as a substitute for total task performance.
