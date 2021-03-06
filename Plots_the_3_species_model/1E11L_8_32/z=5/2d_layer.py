#Author: Yuding Ai
#2015-July-15
#Visualize 3D hard rod

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# DrawRods(dim,plane,layer)
# a function that draws the rods:
# with 3 parameters:
#     dim is the dimention:
#         3 ------------- 3D
#         2 ------------- 2D
#     plane indicates with plane we want to draw: choice: 
#         0 ------------- x,y plane
#         1 ------------- y,z plane
#         2 ------------- z,x plane
#     layer indicates the # of layers we want to see on a specific plane

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')

# ================================ Draw Ver Rods ===========================
a = 0
with open("3dplotv.txt", "r") as file:
    for line in file:
        a= a+1
xpos = np.zeros(a)
ypos = np.zeros(a)

i = 0
with open("3dplotv.txt", "r") as file:
    for line in file:
        words = line.split()
        wx = words[0]
        wy = words[1]
        xpos[i] = wx
        ypos[i] = wy
        i = i+1

dx = np.ones(a)
dy = np.ones(a)

for y in range(0,a):
    dy[y] = 8

    ax.add_patch(
        patches.Rectangle(
            (xpos[y], ypos[y]),
            dx[y],
            dy[y],
            facecolor="red"
        )
    )


# ================================ Draw Hor Rods ===========================
a = 0
with open("3dploth.txt", "r") as file:
    for line in file:
        a= a+1
xpos = np.zeros(a)
ypos = np.zeros(a)

i = 0
with open("3dploth.txt", "r") as file:
    for line in file:
        words = line.split()
        wx = words[0]
        wy = words[1]
        xpos[i] = wx
        ypos[i] = wy
        i = i+1

dx = np.ones(a)
dy = np.ones(a)

for y in range(0,a):
    dx[y] = 8

    ax.add_patch(
        patches.Rectangle(
            (xpos[y], ypos[y]),
            dx[y],
            dy[y],
        )

    )
        
plt.axis('equal')
fig.savefig('2dplot.png', dpi=90, bbox_inches='tight')
plt.show()


