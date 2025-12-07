import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
with open(filepath+"/input_day_6.txt") as f:
    homework = f.read().strip().split("\n")
# missing space at end of line
homework[-1] += " "

"""homework = ["123 328  51 64 ",
  " 45 64  387 23 ",
  "  6 98  215 314",
  "*   +   *   +  "]"""

# reverse the order to translate to cephalopod math
reversed_homework = []
for line in homework:
    reversed_homework.append(line[::-1])


# pivot the rows to columns
homework_pivoted = []
for i in range(len(reversed_homework[0])):
    new_row = []
    for row in reversed_homework:
        new_row.append(row[i])
    homework_pivoted.append(new_row)

# translate to cephalopod math
result = []
calc = []
for col in homework_pivoted:
    col_str = "".join(col).strip()
    # if empty column just skip
    if col_str == "":
        continue
    if col_str[-1] == "+":
        calc.append(int(col_str[:-1]))
        result.append(sum(calc))
        calc = []
    elif col_str[-1] == "*":
        calc.append(int(col_str[:-1]))
        prod = 1
        for num in calc:
            prod *= num
        result.append(prod)
        calc = []
    else:
        calc.append(int(col_str))

print(sum(result))



        