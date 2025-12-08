import pathlib
from math import sqrt
import random
import matplotlib.pyplot as plt
import numpy as np
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_8.txt") as f:
    junction_boxes = f.read().strip().split("\n")

junction_boxes = ["162,817,812",
"57,618,57",
"906,360,560",
"592,479,940",
"352,342,300",
"466,668,158",
"542,29,236",
"431,825,988",
"739,650,466",
"52,470,668",
"216,146,977",
"819,987,18",
"117,168,530",
"805,96,715",
"346,949,466",
"970,615,88",
"941,993,340",
"862,61,35",
"984,92,344",
"425,690,689"]

# get distance array
distances_array = []
for box in junction_boxes:
    box_coords = list(map(int, box.split(",")))
    distances = []
    for other_box in junction_boxes:
        other_box_coords = list(map(int, other_box.split(",")))
        distance = sqrt((box_coords[0]-other_box_coords[0])**2 + (box_coords[1]-other_box_coords[1])**2 + (box_coords[2]-other_box_coords[2])**2)
        distances.append(distance)
    distances_array.append(distances)

import pandas as pd
data = pd.DataFrame(distances_array, columns=junction_boxes, index=junction_boxes)

circuit = []
boxes_left = True
while boxes_left:
    min_distance = float("inf")
    for i in range(len(distances_array)):
        for j in range(len(distances_array[i])):
            if distances_array[i][j] < min_distance and distances_array[i][j] != 0:
                min_distance = distances_array[i][j]
                min_j = j
                min_i = i
    # if both junction boxes are already in the circuit, skip
    if any(junction_boxes[min_i] in pair for pair in circuit) and any(junction_boxes[min_j] in pair for pair in circuit):
        #set the distance to inf so it is not chosen again
        distances_array[min_i][min_j] = float("inf")
        distances_array[min_j][min_i] = float("inf")
        continue  
    circuit.append((junction_boxes[min_i], junction_boxes[min_j]))
    #set the distance to inf so it is not chosen again
    distances_array[min_i][min_j] = float("inf")
    distances_array[min_j][min_i] = float("inf")
    # Check for any junction_boxes not in circuit
    boxes_in_circuit = set()
    for pair in circuit:
        boxes_in_circuit.update(pair)
    boxes_left = [box for box in junction_boxes if box not in boxes_in_circuit]


"""circuit = []
# find the closest junction box for each junction box
for box in junction_boxes:
    other_boxes = junction_boxes.copy()
    other_boxes.remove(box)
    distances = []
    for other_box in other_boxes:
        box_coords = list(map(int, box.split(",")))
        other_box_coords = list(map(int, other_box.split(",")))
        distance = sqrt((box_coords[0]-other_box_coords[0])**2 + (box_coords[1]-other_box_coords[1])**2 + (box_coords[2]-other_box_coords[2])**2)
        distances.append((distance, other_box))
    distances.sort(key=lambda x: x[0])
    closest_box = distances[0][1]
    circuit.append((box, closest_box))"""

# plot the junction boxes and their connections
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for box in junction_boxes:
    box_coords = list(map(int, box.split(",")))
    ax.scatter(box_coords[0], box_coords[1], box_coords[2], c='b', marker='o')
for pair in circuit:
    box1_coords = list(map(int, pair[0].split(",")))
    box2_coords = list(map(int, pair[1].split(",")))
    xs = [box1_coords[0], box2_coords[0]]
    ys = [box1_coords[1], box2_coords[1]]
    zs = [box1_coords[2], box2_coords[2]]
    ax.plot(xs, ys, zs, c='r')
plt.show()

# count connected boxes
strings = []
for pair in circuit:
    box1 = pair[0]
    box2 = pair[1]
    if strings == []:
        strings.append([box1, box2])
    else:
        missing = True
        for string in strings:
            if box1 in string and box2 not in string:
                string.append(box2)
                missing = False
            elif box2 in string and box1 not in string:
                string.append(box1)
                missing = False
            elif box1 in string and box2 in string:
                missing = False
        if missing:
            strings.append([box1, box2])

print(strings)

lengths = []
for string in strings:
    lengths.append(len(string))
lengths.sort()
# multiply the top 3 lengths
result = lengths[-1] * lengths[-2] * lengths[-3]
print(result)