import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_5.txt") as f:
    ingredients = f.read().strip().split("\n")

# ingredients = ["3-5", "10-14", "16-20", "12-18", "1", "5", "8", "11", "17", "32"]

# split list into ranges and single numbers
ranges = []
singles = []
for item in ingredients:
    if "-" in item:
        ranges.append(item)
    # skip empty lines
    elif item.strip() == "":
        continue
    else:
        singles.append(int(item))

def is_in_range(number, range_str):
    start, end = map(int, range_str.split("-"))
    return start <= number <= end

fresh = 0

#part 1
for single in singles:
    for range_str in ranges:
        in_any_range = is_in_range(single, range_str)
        if in_any_range:
            fresh += 1
            break

print(fresh)

total_fresh = 0

#part 2
sorted_ranges = sorted(ranges, key=lambda x: int(x.split("-")[0]))
for i in range(len(sorted_ranges) - 1):
    range_1 = sorted_ranges[i]
    range_2 = sorted_ranges[i + 1]
    start_1, end_1 = map(int, range_1.split("-"))
    start_2, end_2 = map(int, range_2.split("-"))
    if end_1 >= start_2:
        # merge ranges
        new_range = f"{start_1}-{max(end_1, end_2)}"
        sorted_ranges[i + 1] = new_range
        sorted_ranges[i] = None

for range_str in sorted_ranges:
    if range_str is None:
        continue
    start, end = map(int, range_str.split("-"))
    total_fresh += (end - start + 1)

print(total_fresh)

        