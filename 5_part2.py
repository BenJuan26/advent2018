from aoc import get_input

best_count = 10000000
best_letter = ""
for letter in "abcdefghijklmnopqrstuvwxyz":
    data = get_input(5)
    i = 0
    while i+1 < len(data):
        if data[i].lower() == letter:
            data = data[0:i] + data[i+1:]
            continue
        i += 1
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
        if localmax < maxlength:
            maxlength = localmax
            lastlocalmax = localmax
            localmax = 0

    if len(data) < best_count:
        best_count = len(data)
        best_letter = letter

print("\n{}: {}".format(best_letter, best_count))
