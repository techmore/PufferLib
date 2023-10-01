from pdb import set_trace as T

import pufferlib
import pufferlib.emulation
import pufferlib.registry
import pufferlib.wrappers


def env_creator():
    nle = pufferlib.registry.try_import('nle')
    return nle.env.NLE
 
def make_env():
    '''NetHack binding creation function'''
    env = env_creator()()
    env = pufferlib.wrappers.GymToGymnasium(env)
    return pufferlib.emulation.GymPufferEnv(env=env)