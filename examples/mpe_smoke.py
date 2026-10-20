#!/usr/bin/env python3
"""MPE2 simple_spread random-policy smoke; not Sable's JaxMARL configuration."""
import argparse
import math
from _record import save_record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agents', type=int, default=3)
    parser.add_argument('--episodes', type=int, default=2)
    parser.add_argument('--max-cycles', type=int, default=25)
    parser.add_argument('--continuous', action='store_true')
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--output')
    args = parser.parse_args()
    if min(args.agents, args.episodes, args.max_cycles) < 1:
        parser.error('agents, episodes and max-cycles must be positive')
    try:
        from mpe2 import simple_spread_v3
    except ImportError:
        parser.exit(2, 'Install the optional environment: python -m pip install mpe2\n')
    env = simple_spread_v3.parallel_env(N=args.agents, local_ratio=0.5,
          max_cycles=args.max_cycles, continuous_actions=args.continuous, render_mode=None)
    results = []
    try:
        for episode in range(args.episodes):
            seed = args.seed + episode
            obs, _ = env.reset(seed=seed)
            if not obs:
                raise RuntimeError('Reset returned no agent observations')
            totals = {agent: 0.0 for agent in env.agents}
            for i, agent in enumerate(env.agents):
                env.action_space(agent).seed(seed * 1000 + i)
            steps = 0
            while env.agents:
                actions = {agent: env.action_space(agent).sample() for agent in env.agents}
                obs, rewards, terminations, truncations, infos = env.step(actions)
                for agent, reward in rewards.items():
                    if not math.isfinite(float(reward)):
                        raise RuntimeError('Non-finite reward')
                    totals[agent] += float(reward)
                steps += 1
                if steps > args.max_cycles:
                    raise RuntimeError('Episode did not respect max_cycles')
            results.append(dict(seed=seed, joint_steps=steps, per_agent_return=totals))
    finally:
        env.close()
    save_record(args.output, 'mpe', 'MPE2 simple_spread_v3 Parallel API',
                dict(N=args.agents, local_ratio=0.5, max_cycles=args.max_cycles,
                     continuous_actions=args.continuous,
                     action_spaces={a: str(env.action_space(a)) for a in env.possible_agents},
                     observation_spaces={a: str(env.observation_space(a)) for a in env.possible_agents}), results,
                ['mpe2', 'pettingzoo', 'gymnasium', 'numpy', 'pygame-ce'])


if __name__ == '__main__':
    main()
