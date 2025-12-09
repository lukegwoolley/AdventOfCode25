import pathlib
from math import sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_9.txt") as f:
    coords = f.read().strip().split("\n")

"""coords = [
    "7,1",
"11,1",
"11,7",
"9,7",
"9,5",
"2,5",
"2,3",
"7,3",
]"""

max_area = 0
# find biggest rectangle that can fit between the coordinates and don't go outside of them
for i in range(len(coords)):
    x1, y1 = map(int, coords[i].split(","))
    for j in range(i, len(coords)):
        x2, y2 = map(int, coords[j].split(","))
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > max_area:
            max_area = area

print(max_area)


# find the biggest rectangle that can fit between the coordinates and don't go outside of them
max_area = 0
for i in range(len(coords)):
    x1, y1 = map(int, coords[i].split(","))
    for j in range(i, len(coords)):
        x2, y2 = map(int, coords[j].split(","))
        # check if more than two coordinates are inside the rectangle
        count = 0
        for k in range(len(coords)):
            x, y = map(int, coords[k].split(","))
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
            elif x2 <= x <= x1 and y2 <= y <= y1:
                count += 1
            elif x1 <= x <= x2 and y2 <= y <= y1:
                count += 1
            elif x2 <= x <= x1 and y1 <= y <= y2:
                count += 1
        if count <= 2:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > max_area:
                max_area = area

print(max_area)
