import tensorflow as tf
from maze_env2 import Maze
from DQN_brain import DeepQNetwork
import time



if __name__ == '__main__':
    env = Maze()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
    RL.load_model()
    RL.epsilon=1
    observation = env.reset()
    while True:
        # fresh env
        env.render()
        time.sleep(1)
        # RL choose action based on observation
        action = RL.choose_action(observation)
        print(observation*4)
        # RL take action and get next observation and reward
        observation_, reward, done = env.step(action)
        observation = observation_
        # break while loop when end of this episode
        if done:
            break

