# before running gym ensure that you run: set DISPLAY=:0 with X ming installed


import gym
env = gym.make('CartPole-v1')
env.reset()
for step_index in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("Step {}:".format(step_index))
    print("action: {}".format(action))
    print("observation: {}".format(observation))
    print("reward: {}".format(reward))
    print("done: {}".format(done))
    print("info: {}".format(info))
    if done:
        break