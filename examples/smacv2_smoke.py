#!/usr/bin/env python3
"""Optional SC2-engine SMACv2 smoke. Requires a separately installed SC2 and maps."""
import argparse
import random
from _record import save_record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--output')
    args = parser.parse_args()
    try:
        from smacv2.env.starcraft2.wrapper import StarCraftCapabilityEnvWrapper
    except ImportError:
        parser.exit(2, 'Install SC2, SMACv2 and maps using the upstream instructions first.\n')
    config = dict(map_name='10gen_protoss', seed=args.seed,
        conic_fov=False, obs_own_pos=True, use_unit_ranges=True, min_attack_range=2,
        capability_config=dict(n_units=5, n_enemies=5,
            team_gen=dict(dist_type='weighted_teams', unit_types=['stalker', 'zealot', 'colossus'],
                          weights=[0.45, 0.45, 0.1], observe=True),
            start_positions=dict(dist_type='surrounded_and_reflect', p=0.5,
                                 n_enemies=5, map_x=32, map_y=32)))
    env = StarCraftCapabilityEnvWrapper(**config)
    rng = random.Random(args.seed)
    try:
        info = env.get_env_info()
        env.reset()
        total, steps = 0.0, 0
        while True:
            actions = []
            for i in range(info['n_agents']):
                available = [a for a, valid in enumerate(env.get_avail_agent_actions(i)) if valid]
                if not available:
                    raise RuntimeError('No available action for agent ' + str(i))
                actions.append(rng.choice(available))
            reward, terminated, step_info = env.step(actions)
            total += float(reward)
            steps += 1
            if terminated:
                break
            if steps > info['episode_limit']:
                raise RuntimeError('Episode exceeded its configured limit')
        result = [dict(seed=args.seed, joint_steps=steps, team_return=total,
                       battle_won=bool(step_info.get('battle_won', False)))]
    finally:
        env.close()
    save_record(args.output, 'smacv2', 'StarCraft II engine / SMACv2', config, result,
                ['smacv2', 'pysc2', 'numpy'])


if __name__ == '__main__':
    main()
