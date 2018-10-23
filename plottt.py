import pandas as pd
import os
import json
import matplotlib.pyplot as plt
with open("raw_campus_trajectories.txt") as tt:
    source = tt.read()
aa = json.loads(source)

# plt.ion()
bb=aa["trajectories"]
for line in bb:
    x=[]
    y=[]
    for dot in line:
        # plt.plot(dot)
        # print(dot)

        x.append(dot["x"])
        y.append(dot["y"])
        # x = x+[dot["x"]]
    plt.plot(x,y,'r')
# plt.ioff()
    plt.show()
