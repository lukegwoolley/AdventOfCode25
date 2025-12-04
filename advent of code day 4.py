import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_4.txt") as f:
    paper_rolls = f.read().strip().split("\n")

"""paper_rolls = ["..@@.@@@@.", 
               "@@@.@.@.@@", 
                "@@@@@.@.@@", 
                "@.@@@@..@.", 
                "@@.@@@@.@@", 
                ".@@@@@@@.@", 
                ".@.@.@.@@@",
                "@.@@@.@@@@",
                ".@@@@@@@@.",
                "@.@.@@@.@."]"""

accessible_count = 0

def test_adjacent_space(paper_rolls, x, y):
    if x > -1 and y > -1 and x < len(paper_rolls) and y < len(paper_rolls[0]):
        if paper_rolls[x][y] == '@':
            return 1
        else:
            return 0
    else:
        return 0

while True:
    paper_roll_removed = False
    for i in range(len(paper_rolls)):
        for j in range(len(paper_rolls[i])):
            adj_count = 0
            if paper_rolls[i][j] == '@':
                adj_count += test_adjacent_space(paper_rolls, i-1, j)  # Up
                adj_count += test_adjacent_space(paper_rolls, i+1, j)  # Down
                adj_count += test_adjacent_space(paper_rolls, i, j-1)  # Left
                adj_count += test_adjacent_space(paper_rolls, i, j+1)  # Right
                adj_count += test_adjacent_space(paper_rolls, i-1, j-1)  # Up-Left
                adj_count += test_adjacent_space(paper_rolls, i-1, j+1)  # Up-Right
                adj_count += test_adjacent_space(paper_rolls, i+1, j-1)  # Down-Left
                adj_count += test_adjacent_space(paper_rolls, i+1, j+1)  # Down-Right
            else:
                continue  # Skip if it's not a paper roll
            # Check it's not surrounded by at least 4 paper rolls
            if adj_count < 4:
                accessible_count += 1
                paper_rolls[i] = paper_rolls[i][:j] + '.' + paper_rolls[i][j + 1:] # Mark as removed
                paper_roll_removed = True
                break  # Break inner loop
        if paper_roll_removed:
            break  # Break outer loop to restart while
    if not paper_roll_removed:
        break  # Exit while loop if no roll was removed

print(accessible_count)
        