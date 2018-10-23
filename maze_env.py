import numpy as np
import time
import sys
import tkinter as tk
import random


UNIT = 40   # pixels
MAZE_H = 7  # grid height
MAZE_W = 7  # grid width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.n_features = 2
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # 画网格
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # 定义中心点
        origin = np.array([20, 20])

        # 障碍物1
        hell1_center = origin + np.array([UNIT * 4, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        # 障碍物2
        hell2_center = origin + np.array([UNIT*2, UNIT * 4])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')
        # 障碍物3
        hell3_center = origin + np.array([UNIT * 3, UNIT * 4])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell2_center[1] + 15,
            fill='black')

        # create oval
        oval_center = origin + np.array([UNIT * 3,0])
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')

        # create red rect
        agent_center = origin + np.array([UNIT*3,UNIT*6])
        self.rect = self.canvas.create_rectangle(
            agent_center[0] - 15, agent_center[1] - 15,
            agent_center[0] + 15, agent_center[1] + 15,
            fill='red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.1)
        self.canvas.delete(self.rect)
        agent = np.array([20, 20])
        agent = agent + np.array([UNIT*3,UNIT*6])
        self.rect = self.canvas.create_rectangle(
            agent[0] - 15, agent[1] - 15,
            agent[0] + 15, agent[1] + 15,
            fill='red')
        # return observation
        return (np.array(self.canvas.coords(self.rect)[:2])-np.array(self.canvas.coords(self.oval)[:2]))/(MAZE_H*UNIT)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
                reward = 1
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        next_coords = self.canvas.coords(self.rect)  # next state

        # reward function
        if next_coords == self.canvas.coords(self.oval):
            reward = 10
            done = True
            print("成功到达终点")
        elif next_coords in [self.canvas.coords(self.hell1),self.canvas.coords(self.hell2),self.canvas.coords(self.hell3)]:
            reward = -10
            done = True
            print("撞到障碍物游戏结束！！！")
        else:
            reward = 0
            done = False
        s_ = (np.array(next_coords[:2]) - np.array(self.canvas.coords(self.oval)[:2])) / (MAZE_H * UNIT)
        return s_, reward, done

    def render(self):
        time.sleep(0.1)
        self.update()


# def update():
#     for t in range(10):
#         s = env.reset()
#         while True:
#             env.render()
#             a = random.randint(0,3)
#             s, r, done = env.step(a)
#             if done:
#                 break

# if __name__ == '__main__':
#     env = Maze()
#     env.after(100, update)
#     env.mainloop()