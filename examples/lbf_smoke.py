#!/usr/bin/env python3
"""Original lb-foraging Gymnasium API smoke; not the Jumanji Sable configuration."""
import argparse
import math
from _record import save_record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--episodes', type=int, default=2)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--output')
    args = parser.parse_args()
    if args.episodes < 1:
        parser.error('episodes must be positive')
    try:
        import gymnasium as gym
        import lbforaging  # registers environment IDs
    except ImportError:
        parser.exit(2, 'Install the optional environment: python -m pip install lbforaging\n')
    env_id = 'Foraging-8x8-2p-2f-v3'
    env = gym.make(env_id)
    results = []
    try:
        for episode in range(args.episodes):
            seed = args.seed + episode
            obs, _ = env.reset(seed=seed)
            env.action_space.seed(seed)
            totals = None
            steps = 0
            while True:
                obs, rewards, terminated, truncated, info = env.step(env.action_space.sample())
                if totals is None:
                    totals = [0.0] * len(rewards)
                for i, reward in enumerate(rewards):
                    if not math.isfinite(float(reward)):
                        raise RuntimeError('Non-finite reward')
                    totals[i] += float(reward)
                steps += 1
                # Gymnasium termination/truncation may be joint bools or per-agent sequences.
                ended = bool(terminated) if isinstance(terminated, bool) else all(terminated)
                limited = bool(truncated) if isinstance(truncated, bool) else all(truncated)
                if ended or limited:
                    break
                if steps > 1000:
                    raise RuntimeError('Unexpectedly long episode; inspect the installed API')
            results.append(dict(seed=seed, joint_steps=steps, per_agent_return=totals,
                                terminated=ended, truncated=limited))
    finally:
        env.close()
    save_record(args.output, 'lbf', 'lb-foraging Gymnasium ' + env_id,
                dict(environment_id=env_id, spec_kwargs=env.spec.kwargs,
                     action_space=str(env.action_space), observation_space=str(env.observation_space)),
                results, ['lbforaging', 'gymnasium', 'numpy'])


if __name__ == '__main__':
    main()
