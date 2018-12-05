from aoc import get_input

data = get_input(5)

i = 0
while i+1 < len(data):
    char = data[i]
    if char.islower() and data[i+1] == char.upper() or char.isupper() and data[i+1] == char.lower():
        data = data[0:i] + data[i+2:]
        if i > 0:
            i -= 1
        continue
    i += 1

print(len(data))