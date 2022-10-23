import gym

# pip install gym[atari]
# pip install autorom[accept-rom-license]
env = gym.make("PongNoFrameskip-v4")
observation = env.reset()
env.render()



