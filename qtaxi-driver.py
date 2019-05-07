"""Training the agent"""

import gym
import colorama
colorama.init()
# for proper output formatting

from IPython.display import clear_output
from time import sleep

import numpy as np 
q_table = np.zeros([env.observation_space.n, env.action_space.n])
# initializing a 500 * 6 matrix of zeroes



env = gym.make("Taxi-v2").env

env.reset() # reset environment to a new, random state
# env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])#.getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)


env.s = 328  # set environment to illustration's state

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1
    
    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
        }
    )

    epochs += 1

    
# print_frames(frames)
# this is to show the actual app working 
    
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))