from aoc import get_input

data = get_input(5)

maxlength = 1000000
localmax = 0
lastlocalmax = 1000000
while localmax != lastlocalmax:
    i = 0
    while i+1 < len(data):
        char = data[i]
        if char.islower():
            if data[i+1] == char.upper():
                data = data[0:i] + data[i+2:]
                continue
        if char.isupper():
            if data[i+1] == char.lower():
                data = data[0:i] + data[i+2:]
                continue
        i += 1
        if i > localmax:
            localmax = i
    print(localmax)
    if localmax < maxlength:
        maxlength = localmax
        lastlocalmax = localmax
        localmax = 0

print(len(data))
