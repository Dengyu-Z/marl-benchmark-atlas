# Minimal environment checks / 最小运行示例

[Home](../README.md) · [验证记录](../docs/verification.md)

These scripts sample random actions. They check the installed API and never train or load a policy. Use Python 3.12 for the tested optional dependency pins; the catalog tools themselves use Python 3.10+.

## MPE2 and original LBF

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: replace the line above with .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements/smoke.txt
python examples/mpe_smoke.py --agents 3 --episodes 2 --output runs/mpe.json
python examples/mpe_smoke.py --continuous --output runs/mpe-continuous.json
python examples/lbf_smoke.py --episodes 2 --output runs/lbf.json
```

| Example | Configuration | Validation scope |
| --- | --- | --- |
| MPE2 discrete | `simple_spread_v3`, N=3, local_ratio=0.5, 25 cycles | 2 episodes passed |
| MPE2 continuous | Same task with `continuous_actions=True` | 2 episodes passed |
| Original LBF | `Foraging-8x8-2p-2f-v3`, registered package defaults | 2 episodes passed |
| Engine SMACv2 | Protoss 5v5 on `10gen_protoss` | API recipe only; not run |

MPE2 and the Python LBF package are different implementations from Sable's JaxMARL and Jumanji environments. The recipes are starting points, not exact Sable reproductions. MPE2 continuous actions in this version have shape `(5,)`; Sable's paper describes its continuous JaxMARL action interface differently. Check the actual action space printed in each record.

LBF returns a vector of per-agent rewards. Gymnasium's single-agent passive checker emits a warning about that reward type with the tested version; the smoke script handles the vector explicitly. The tested LBF package reports its 50-step episode endpoint through `terminated`; preserve that observed API behavior rather than silently rewriting it as `truncated`.

## Optional engine-based SMACv2

Install StarCraft II, the required SMACv2 maps and Python dependencies from the [official project instructions](https://github.com/oxwhirl/smacv2). Follow the game's license and upstream installation process. Set `SC2PATH` to your own game installation directory as described upstream.

```bash
python examples/smacv2_smoke.py --seed 0 --output runs/smacv2.json
```

The script uses the official `StarCraftCapabilityEnvWrapper` API and `10gen_protoss` map name with 5 friendly/enemy units. A label such as `protoss_5_vs_5` can be a training-framework alias rather than the upstream map filename. Random actions are sampled only from each agent's availability mask.

The current environment does not contain SC2, so this recipe remains **not run**. A successful installation on another machine must include its own run record before the catalog status is upgraded.

## Record format

With `--output`, each script writes JSON containing exact config, dependency versions, Python/platform, episode seeds, joint steps, returns and the limited claim being checked. New local records belong in `runs/`, which is ignored by Git. Contribute reviewed evidence under `validation/` with the corresponding ledger update.
