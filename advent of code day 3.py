import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_3.txt") as f:
    joltages = f.read().strip().split("\n")
    joltages = [int(joltage) for joltage in joltages]

# joltages = [987654321111111, 811111111111119, 234234234234278, 818181911112111]
top_jolts = []

for jolts in joltages:
    # turn int into list of digits
    digits = [int(d) for d in str(jolts)]
    n = len(digits)
    k = 12
    # Greedy Algorithm: build the largest k digit number by picking the largest possible digit at each step
    result = []
    max_pos = 0
    for i in range(k):
        # The window is from max_pos to n - (k - i) inclusive
        end = n - (k - i) + 1
        # positive ints only so set max digit to -1
        max_digit = -1
        for j in range(max_pos, end):
            if digits[j] > max_digit:
                max_digit = digits[j]
                max_pos = j
        result.append(str(max_digit))
        max_pos += 1
    top_jolts.append(int(''.join(result)))

print(sum(top_jolts))

    

