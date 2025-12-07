import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_7.txt") as f:
    tachyon = f.read().strip().split("\n")

"""tachyon = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"..............."
]"""

split = 0
i = 0
paths = []
paths.append([0]*len(tachyon[0]))
while i < len(tachyon)-1:
    row = tachyon[i]
    paths.append([0]*len(row))
    j = 0
    while j < len(row):
        step = row[j]
        if step == "S":
            paths[i][j] = 1
            if tachyon[i+1][j] == "^":
                tachyon[i+1] = tachyon[i+1][:j-1] + "|" + tachyon[i+1][j:]
                paths[i+1][j-1] = 1
                tachyon[i+1] = tachyon[i+1][:j+1] + "|" + tachyon[i+1][j+2:]
                paths[i+1][j+1] = 1
                split += 1
            else:
                tachyon[i+1] = tachyon[i+1][:j] + "|" + tachyon[i+1][j+1:]
                paths[i+1][j] = 1
            break
        elif step == "|":
            if tachyon[i+1][j] == "^":
                if tachyon[i+1][:j-1] == "|" and tachyon[i+1][j+1:] == "|":
                    pass
                elif tachyon[i+1][:j-1] == "|" and tachyon[i+1][j+1] != "|":
                    paths[i+1][j-1] = paths[i+1][j-1] + paths[i][j]
                elif tachyon[i+1][:j-1] != "|" and tachyon[i+1][j+1:] == "|":
                    paths[i+1][j+1] = paths[i+1][j+1] + paths[i][j]
                else:
                    paths[i+1][j-1] = paths[i+1][j-1] + paths[i][j]
                    paths[i+1][j+1] = paths[i+1][j+1] + paths[i][j]
                tachyon[i+1] = tachyon[i+1][:j-1] + "|" + tachyon[i+1][j:]
                tachyon[i+1] = tachyon[i+1][:j+1] + "|" + tachyon[i+1][j+2:]
                split += 1
            else:
                tachyon[i+1] = tachyon[i+1][:j] + "|" + tachyon[i+1][j+1:]
                paths[i+1][j] = paths[i+1][j] + paths[i][j]
        j += 1
    i += 1

for row in paths:
    print(row)
print("Number of splits:", split)
print("Total paths to bottom:", sum(paths[-1]))

        