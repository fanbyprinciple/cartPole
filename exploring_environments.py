import gym

#env = gym.make('MountainCarContinuous-v0')
#env = gym.make('Pendulum-v0')
env = gym.make('LunarLander-v2')
#env = gym.make('CarRacing-v0')
#env = gym.make('BipedalWalker-v2')
#env = gym.make('Centipede-v0')
#env = gym.make('FetchPush-v1') # can't be done without mujoco

observation = env.reset()

for t in range(1000):
    env.render()
    print(observation)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(observation, reward, done, info)
    if done:
        print("Finished after {} timesteps".format(t+1))
        break