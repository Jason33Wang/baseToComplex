'''
1、reset(self):重置环境的状态，返回观察。

2、step(self,action):推进一个时间步长，返回observation，reward，done，info

3、render(self,mode=’human’,close=False):重绘环境的一帧。默认模式一般比较友好，如弹出一个窗口。
'''



# import gym
# env = gym.make('CartPole-v0')
# env.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample())

import numpy as np

o = np.array([1,2,3])
o=o[np.newaxis,:]
