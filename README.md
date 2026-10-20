<p align="center">
  <img src="assets/banner.svg" width="100%" alt="MARL Benchmark Atlas — choose an environment, trace its protocol, reproduce carefully" />
</p>

<p align="center">
  <strong>A source-backed field guide to multi-agent RL environments, datasets and evaluation protocols.</strong><br />
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="docs/environment-index.md">Environment index</a> ·
  <a href="docs/paper-index.md">Paper index</a> ·
  <a href="docs/sable-tasks.md">Sable's 45 tasks</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <img alt="Resource records: 18" src="https://img.shields.io/badge/resources-18-0f766e" />
  <img alt="Paper cards: 16" src="https://img.shields.io/badge/paper_cards-16-2563eb" />
  <img alt="Sable main tasks: 45" src="https://img.shields.io/badge/Sable_tasks-45-7c3aed" />
  <img alt="MIT license" src="https://img.shields.io/badge/license-MIT-64748b" />
</p>

Choose a benchmark for the question you want to answer. Find the implementation a paper actually used. Keep simulator changes from turning into misleading algorithm comparisons.

This atlas starts from **Sable's six-suite benchmark**, then connects it to a curated set of papers on exploration, role discovery, diversity, decentralized learning, credit assignment and safety. Online environments, paper-specific games and offline data resources have separate labels.

## Start here

| I want to… | Go to |
| --- | --- |
| Understand what the tasks actually are | [Visual overview / 中文图解](docs/environment-overview.zh-CN.md) |
| Match an algorithm to action and information requirements | [Algorithm compatibility](docs/algorithm-fit.md) |
| Pick an environment for a research question | [Selection guide](docs/selection-guide.md) / [中文选型指南](docs/selection-guide.zh-CN.md) |
| See the complete resource table | [Environment and dataset index](docs/environment-index.md) |
| Find a paper's environments and policy regime | [Paper → environment index](docs/paper-index.md) |
| Understand Sable's exact task set | [45-task list](docs/sable-tasks.md) / [中文详解](docs/sable-guide.zh-CN.md) |
| Run a small environment check | [MPE2, LBF and SMACv2 recipes](examples/README.md) |
| Check what has actually been run | [Verification ledger](docs/verification.md) |
| Avoid an invalid comparison | [Version and protocol traps](docs/comparability.md) |
| Reuse the data | [JSON/CSV catalog](data/README.md) and [offline CLI](#query-the-catalog-offline) |

## Understand the tasks first

![Conceptual sketches of six environment families, not simulator screenshots](assets/environments-at-a-glance.svg)

Warehouse robots deliver shelves; LBF agents jointly collect food; Connector agents draw paths without blocking each other; SMAX units coordinate attacks; MaBrax controllers share a robot's joints; MPE simple_spread particles divide up landmarks.

Start with **action type**, then check observation/history, cooperation/rewards, agent heterogeneity, training/execution information, data access and budget. [The compatibility guide](docs/algorithm-fit.md) explains why standard QMIX needs discrete actions while MAPPO, HAPPO and HARL HASAC support both through the appropriate implementations. Compatibility does not predict the best return.

## Sable at a glance

| Suite | Main tasks | Actions in Sable | Implementation used in the paper |
| --- | ---: | --- | --- |
| [RWARE](docs/environments/rware.md) | 15 | Discrete | Jumanji via Mava |
| [LBF](docs/environments/lbf.md) | 7 | Discrete | Jumanji via Mava |
| [Connector](docs/environments/connector.md) | 4 | Discrete | Jumanji via Mava |
| [SMAX](docs/environments/smax.md) | 11 | Discrete | JaxMARL via Mava |
| [MaBrax](docs/environments/mabrax.md) | 5 | Continuous | JaxMARL / Brax via Mava |
| [MPE simple_spread](docs/environments/mpe.md) | 3 | Continuous | JaxMARL via Mava |

**45 main tasks in total.** [NEOM](docs/environments/neom.md) and the extra large-population LBF settings belong to the scalability study. The source is the supplied Sable v5, Section 4, Appendix B and Appendix C; see the [paper card](papers/sable.md).

Three details that matter before copying a result:

- **SMAX, SMAC and SMACv2 are separate implementations.** Sable's `smacv2 ... units` labels are SMAX tasks.
- **RWARE collision semantics differ.** Sable describes episode termination on collision in its Jumanji implementation; the original Python environment resolves collisions differently.
- **MaBrax uses Brax physics.** A matching MA-MuJoCo joint partition does not establish score equivalence.

## What is covered

The [18 resource cards](docs/environment-index.md) include the six Sable suites, SMAC, SMACv2, MA-MuJoCo, VMAS, Google Research Football, Overcooked, CAMAR, didactic coordination games, open-system Wildfire, SUMO-RL, OG-MARL and NEOM.

The [16 paper cards](docs/paper-index.md) preserve environment mappings, on/off-policy labels, training/execution assumptions, source sections and unresolved details. One paper concerns reasoning-language-model RL and is explicitly marked **background only**. No uploaded PDF is redistributed.

## Query the catalog offline

Python **3.10+**; the catalog tools need no third-party packages.

```bash
git clone https://github.com/Dengyu-Z/marl-benchmark-atlas.git
cd marl-benchmark-atlas
python scripts/atlas.py --paper sable
python scripts/atlas.py --tag sparse-reward --action discrete
python scripts/atlas.py --kind offline-dataset --json
python scripts/validate_catalog.py
```

`--paper sable` also returns NEOM because it lists all linked Sable resources, including the separate scalability study. Use [sable_tasks.json](data/sable_tasks.json) for the 45-task main benchmark only. `--action continuous` includes resource families that support both action types.

## Run the first smoke check

Use an isolated environment. The smoke script samples random actions and writes a versioned run record.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: replace the line above with .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements/smoke.txt
python examples/mpe_smoke.py --output runs/mpe.json
python examples/mpe_smoke.py --continuous --output runs/mpe-continuous.json
python examples/lbf_smoke.py --output runs/lbf.json
```

**Verified in this edition:** MPE2 discrete/continuous and original LBF, 2 random-policy episodes per configuration on Linux / Python 3.12. Exact versions and records are in [the ledger](docs/verification.md). **SMACv2 is an unrun optional recipe** requiring StarCraft II and maps. No learning curves or reproduced baseline scores are claimed.

## Record an experiment so it can be compared

At minimum, preserve the simulator revision, task generator, observations, action space, reward definition, termination, training budget units, evaluation protocol and uncertainty across independent training seeds. The [protocol checklist](docs/reproducibility.md) and [run template](templates/reproduction-record.json) provide a starting point.

## Contribute a checked entry

Useful contributions include a missing implementation difference, an exact paper configuration, a reproducible installation fix, or a smoke record with package versions. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [roadmap](ROADMAP.md). Please attach evidence before upgrading an entry's verification level.

The original catalog and helper code use the [MIT license](LICENSE). Third-party papers, environments, datasets and trademarks retain their own licenses. Cite the original benchmark and method papers when you use them; this atlas is a navigation aid.
