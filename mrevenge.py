# sample test game for playing games yourself


import gym
from gym.utils.play import play
env = gym.make("MontezumaRevengeNoFrameskip-v4")
play(env, zoom=4)