import pathlib
import re
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_2.txt") as f:
    ids = f.read().strip().split(",")

"""ids = ["11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224",
        "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659",
        "824824821-824824827", "2121212118-2121212124"]"""

invalid_ids = []

for id in ids:
    id_halves = id.split("-")
    # Iterate through the ranges
    for i in range(int(id_halves[0]), int(id_halves[1]) + 1):
        # Use regex to check if same group repeats more than once
        match = re.match(r"^(.+)\1+$", str(i))
        if match:
            invalid_ids.append(i)
print(sum(invalid_ids))
    

