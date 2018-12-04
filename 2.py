from aoc import get_input

data = get_input(2)
lines = data.split("\n")

line_counts = {}
twos = 0
threes = 0
for line in lines:
    counts = {}
    for char in line:
        try:
            counts[char] += 1
        except KeyError:
            counts[char] = 1
    has_twos = False
    has_threes = False
    for char, count in counts.items():
        if count == 2:
            has_twos = True
        if count == 3:
            has_threes = True
    if has_twos:
        twos += 1
    if has_threes:
        threes += 1

print(twos * threes)