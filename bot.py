import gym


env =gym.make('CartPole-v0')

for i_episode in range(20):
	observartion = env.reset()

	for t in range(100):
		env.render()
		print(observartion)
		action = env.action_space.sample()
		#reinforcement learning
		observartion, reward, done, info = env.step(action)

		if done:
				print("episode finished after {} timesteps")
				break

