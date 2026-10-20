# A comparable experiment record

[Home](../README.md) · [JSON record template](../templates/reproduction-record.json)

## Preserve task identity

| Component | Minimum record |
| --- | --- |
| Simulator | Repository URL, commit or package version; SC2/MuJoCo/Brax version where applicable |
| Task | Registered ID plus generator parameters, map/layout, agent/food/obstacle counts, unit compositions |
| Observations | Per-agent input, global critic input, sight, neighbor radius, histories, masks, identity features |
| Actions | Discrete/continuous, shape, bounds, availability, communication channels |
| Rewards and costs | Shared versus individual, shaping, normalization, safety costs, constraint thresholds |
| Episode boundaries | Time limits, success/collision termination, truncation handling, resets and curriculum |
| Model and training | Parameter sharing, recurrent state, optimizer, learning rates and checkpoint selection |
| Budget | Joint environment transitions, agent transitions and gradient updates as separate counters |
| Evaluation | Training seeds, episode seeds, action sampling mode, episode count, horizon and held-out contexts |
| Statistics | Per-training-seed summaries, aggregation definition, uncertainty method and interval |
| System | Hardware, process count, parallel environments, simulator/learner device and package manifest |

## Verification levels

1. **Literature checked:** the record can be traced to a section, table, figure or official implementation.
2. **Smoke passed:** the named configuration completes reset/step with finite rewards; versions and output are attached.
3. **Baseline reproduced:** full training/evaluation records support a comparison with a named reference under the same protocol.

These levels answer different questions. A smoke record with zero reward can still validate the interface; it cannot validate cooperation or a learning algorithm.

## Small, useful first comparison

Use one exact environment configuration, a baseline and the proposed change, matched training seeds and a fixed evaluation bank. Declare the primary outcome before widening the experiment. Keep any probe/adaptation or teacher-selection budget in the total budget.

For a small-budget pilot, report the uncertainty and the restricted scope. Do not rename a shortened training run as a reproduction of a full 20M-step benchmark.
