from aoc import get_input

data = get_input(1)

result = 0
for line in data.split("\n"):
    num = int(line[1:])
    if line[0] == "+":
        result = result + num
    else:
        result = result - num

print(result)