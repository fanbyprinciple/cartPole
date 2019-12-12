import gym


env = gym.make('BreakoutDeterministic-v4')

frame = env.reset()

env.render()

is_done = False

while not is_done :
    env.render()
