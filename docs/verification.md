# Verification ledger / 验证记录

[Home](../README.md) · [Machine-readable ledger](../data/validation.json)

Edition checked on **2026-10-20**. Runtime checks used Linux x86_64 and Python **3.12.14**. Catalog commands use the standard library; optional environment dependencies are isolated.

## Actual environment runs

| Configuration | Episodes / joint steps | Outcome | Evidence |
| --- | --- | --- | --- |
| MPE2 simple_spread, N=3, discrete, local_ratio=0.5 | 2 / 25 each | reset/step completed; finite rewards | [JSON](../validation/mpe-discrete.json) |
| MPE2 simple_spread, N=3, continuous, local_ratio=0.5 | 2 / 25 each | reset/step completed; finite rewards | [JSON](../validation/mpe-continuous.json) |
| Python LBF Foraging-8x8-2p-2f-v3 | 2 / 50 each | reset/step completed; finite rewards | [JSON](../validation/lbf.json) |
| Engine SMACv2, Protoss 5v5 on 10gen_protoss | 0 | Not run; SC2 not installed here | [Optional recipe](../examples/smacv2_smoke.py) |

Tested direct versions: `mpe2==1.1.1`, `lbforaging==2.0.0`, `pettingzoo==1.27.0`, `gymnasium==1.4.0`, `numpy==2.5.4`. The complete package manifest is [smoke-lock.txt](../requirements/smoke-lock.txt).

The MPE continuous action space is a `(5,)` Box in this version. LBF's per-agent reward vector produces a Gymnasium single-agent checker warning, handled explicitly by the script. Random LBF episodes collected zero food reward; that does not invalidate an interface smoke check and does not establish that the task has been learned.

These records establish **interface compatibility for these exact configurations**. They do not establish Sable reproduction, trained baseline performance, Windows compatibility, or validation of every configuration in a resource family. No policy was trained.

## Repository checks

- Catalog IDs, paper/resource mappings and source-hash formatting.
- The six-suite Sable task count (15+7+4+11+5+3=45), including duplicate checks.
- Local Markdown links, source-card existence and runtime-claim evidence links.
- Generated Markdown indexes and CSV consistency with canonical JSON.
- Python syntax, offline CLI filters and missing-dependency/help behavior.

The [GitHub Actions workflow](../.github/workflows/validate.yml) runs catalog checks without installing simulators or launching training. Environment runs above are recorded local checks, not a claim that Actions runs those simulators.

## Verification levels

| Label | What it establishes | Required evidence |
| --- | --- | --- |
| Literature checked | A claim is located in the supplied paper or official source | Paper section/table/page or primary URL |
| Smoke passed | A named environment configuration can reset and step | Exact config, versions, command and run record |
| Baseline reproduced | Training/evaluation match a specified reference protocol | Logs, budgets, independent training seeds, uncertainty and matched implementation |

`baseline_runs` is empty in this edition. Unsupported variants keep their unrun status even when a related implementation passes a smoke check.
