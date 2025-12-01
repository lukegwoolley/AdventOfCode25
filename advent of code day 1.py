import pathlib
import pandas as pd
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_1.txt") as f:
    instructions = f.read().strip().split("\n")
# instructions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82", "L32", "R500", "L441"]
dial = [50]
zeros = [0]

for instruction in instructions:
    zero = 0
    direction = instruction[0]
    distance = int(instruction[1:])
    if direction == "L":
        #if dial is 0, turning left makes it 99
        dial.append((dial[-1] - distance) % 100)
        # if it rotates through 0, count how many times
        for i in range(1, distance + 1):
            if (dial[-2] - i) % 100 == 0:
                zero += 1
    elif direction == "R":
        #if dial is 99, turning right makes it 0
        dial.append((dial[-1] + distance) % 100)
        # if it rotates through 0, count how many times
        for i in range(1, distance + 1):
            if (dial[-2] + i) % 100 == 0:
                zero += 1
    zeros.append(zero)


# add "Start" to instructions for first row
instructions.insert(0, "Start")
# Data Frame for debugging
df = pd.DataFrame(zip(instructions, zeros, dial), columns=["Instruction", "Zeros Crossed", "Dial Position"])

print("Number of times dial points to 0:", sum(zeros))