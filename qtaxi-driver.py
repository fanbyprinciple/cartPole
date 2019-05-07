"""Training the agent"""

import gym
import colorama
colorama.init()
# for proper output formatting

from IPython.display import clear_output
from time import sleep

import numpy as np 

import random 
from IPython.display import clear_output # Ipython notebook command

env = gym.make("Taxi-v2").env

env.reset() # reset environment to a new, random state
# env.render()

q_table = np.zeros([env.observation_space.n, env.action_space.n])
# initializing a 500 * 6 matrix of zeroes


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

# Hyperparameter
alpha = 0.1 # training rate
gamma = 0.6 # discount factor: how imprtatnt are future rewards
epsilon = 0.1 # preventing action from taking same route again and again to avoid overfitting

# plotting metrics for notebook 
all_epochs = []
all_penalties = []

print("Training started")
# training 100000 traversals
for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward = 0,0,0
    done = False

    while not done:
        if random.uniform(0,1) < epsilon :
            action = env.action_space.sample() # explore action space
        else :
            action = np.argmax(q_table[state]) # use already learned values
        
        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1- alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] =  new_value

        if reward == -10 :
            penalties += 1

        state = next_state
        epochs += 1
    if(i % 100 == 0):
        clear_output(wait=True)
        print(f"Episode: {i}")
print("Training completed.")


# code without using Q learning

# while not done:
#     action = env.action_space.sample()
#     state, reward, done, info = env.step(action)

#     if reward == -10:
#         penalties += 1
    
#     # Put each rendered frame into dict for animation
    # frames.append({
    #     'frame': env.render(mode='ansi'),
    #     'state': state,
    #     'action': action,
    #     'reward': reward
    #     }
    # )

#     epochs += 1

    
# # print_frames(frames)
# # this is to show the actual taxi map working 
    
# print("Timesteps taken: {}".format(epochs))
# print("Penalties incurred: {}".format(penalties))

"""Evaluating after Q learning """

print("Evaluating after Q learning ")

total_epochs, total_penalties = 0,0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    epoch, penalties, reward = 0,0,0

    done = False
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

    
    frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
            })

    epoch += 1
    total_penalties += penalties
    total_epochs += epochs

print_frames(frames)

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")
    
    