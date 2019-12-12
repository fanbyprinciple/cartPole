import retro

# not able to make it work in ubuntu

def main():
    env = retro.make(game='Airstriker-Genesis')
    obs = env.reset()

    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()
        
        env.close()
    

if __name__ == "__main__":
    main()

