#!/usr/bin/env python3

from matplotlib import pyplot as plt
from matplotlib.tri import Triangulation
import numpy as np

# https://stackoverflow.com/questions/66048529/how-to-create-a-heatmap-where-each-cell-is-divided-into-4-triangles

sizeBoard = 3

def getPieces():
    # Get the pieces from the TetraVex game
    file = open("./dataFiles/TetraVex_3x3_Solution.txt", "r")
    north = []
    east = []
    south = []
    west = []
    for line in file:
        sides = line.split(" ")
        north.append([int(sides[0])])
        east.append([int(sides[1])])
        south.append([int(sides[2])])
        west.append([int(sides[3])])
    return [north, east, south, west]

def triangulation_for_triheatmap(M, N):
    xv, yv = np.meshgrid(np.arange(-0.5, M), np.arange(-0.5, N))  # vertices of the little squares
    xc, yc = np.meshgrid(np.arange(0, M), np.arange(0, N))  # centers of the little squares
    x = np.concatenate([xv.ravel(), xc.ravel()])
    y = np.concatenate([yv.ravel(), yc.ravel()])
    cstart = (M + 1) * (N + 1)  # indices of the centers

    trianglesN = [(i + j * (M + 1), i + 1 + j * (M + 1), cstart + i + j * M)
                  for j in range(N) for i in range(M)]
    trianglesE = [(i + 1 + j * (M + 1), i + 1 + (j + 1) * (M + 1), cstart + i + j * M)
                  for j in range(N) for i in range(M)]
    trianglesS = [(i + 1 + (j + 1) * (M + 1), i + (j + 1) * (M + 1), cstart + i + j * M)
                  for j in range(N) for i in range(M)]
    trianglesW = [(i + (j + 1) * (M + 1), i + j * (M + 1), cstart + i + j * M)
                  for j in range(N) for i in range(M)]
    return [Triangulation(x, y, triangles) for triangles in [trianglesN, trianglesE, trianglesS, trianglesW]]


values = getPieces()
triangul = triangulation_for_triheatmap(sizeBoard, sizeBoard)
cmaps = 'tab10' # Color map based out of 10 colors
fig, ax = plt.subplots()
imgs = [ax.tripcolor(t, np.ravel(val), cmap=cmaps, vmin=0, vmax=9, ec='white')
            for t, val in zip(triangul, values)]

# TODO Add text (nog te fixen)
# for val, dir in zip(values, [(-1, 0), (0, 1), (1, 0), (0, -1)]):
#     for i in range(M):
#         for j in range(N):
#             v = val[j, i]
#             ax.text(i + 0.3 * dir[1], j + 0.3 * dir[0], f'{v:.2f}', color='k' if 0.2 < v < 0.8 else 'w', ha='center', va='center')
# cbar = fig.colorbar(imgs[0], ax=ax)

ax.set_xticks(range(sizeBoard))
ax.set_yticks(range(sizeBoard))
ax.invert_yaxis()
ax.margins(x=0, y=0)
ax.set_aspect('equal', 'box')  # square cells
plt.tight_layout()
plt.show()