# Machine-readable catalog

[Home](../README.md)

| File | Contents | Maintained how |
| --- | --- | --- |
| [environments.json](environments.json) | Resource types, actions, implementations, tags, upstreams, caveats and paper links | Canonical JSON |
| [algorithms.json](algorithms.json) | Action compatibility, on/off-policy regime, implementation scope and primary sources for 7 methods | Canonical JSON |
| [papers.json](papers.json) | Paper metadata, policy regime, training/execution paradigm, mappings and source locators | Canonical JSON |
| [sable_tasks.json](sable_tasks.json) | 45 main-benchmark paper labels with suite and action type | Canonical JSON |
| [source_manifest.json](source_manifest.json) | Supplied PDF names, SHA-256 hashes and evidence locators | Provenance |
| [validation.json](validation.json) | Links to checked-in runtime evidence and validation scope | Verification ledger |
| [environments.csv](environments.csv) | Flat resource export | Generated |
| [papers.csv](papers.csv) | Flat paper export | Generated |
| [sable_tasks.csv](sable_tasks.csv) | Flat Sable task export | Generated |

## Semantics

- `id`: stable local identifier, not an upstream environment ID.
- `kind`: `online`, `paper-specific` or `offline-dataset`.
- `action_space`: `discrete`, `continuous`, `both` or unresolved `unknown`; it is family-scoped unless the entry says otherwise.
- `policy`: paper-method regime (`on-policy`, `off-policy`, `mixed` or `background`), not an intrinsic property of an environment.
- `source_version`: the specific supplied document or checked primary record.
- `year: null` and URL `null`: not established in this edition. Never interpret null as an unavailable or nonexistent project.
- `evidence_status`: `literature_checked` establishes a source check only.
- `runtime_status`: `not_run`, `smoke_passed` or `baseline_reproduced`. For `smoke_passed`, inspect the ledger: it applies only to the named implementation/configuration, not every variant in that family.
- `paper_task_label`: a paper table label with normalized typography, not a tested API registration string.
- `checked_on`: the curation date. Package versions of actual runs live in the validation records.
- `beginner`: who the agents are, their goal, concrete actions, scoped reward timing, and candidate baselines explained in Chinese.
- `beginner.reward_density`: descriptive and task-scoped, never a measured difficulty score. `config-dependent` and `unknown` preserve unresolved details.
- Algorithm candidate filters check an intersection of supported action types and the requested variant; they are not predictions of learning performance or completed integrations.

Regenerate indexes and CSV after JSON changes:

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
python scripts/build_catalog.py --check
```

Markdown environment/paper cards contain curated explanations and are maintained alongside the JSON. Review both when changing a factual record; the generator only rebuilds the three indexes and three CSV files.
