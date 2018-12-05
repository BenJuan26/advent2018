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

    i = 0
    while i+1 < len(data):
        char = data[i]
        if char.islower() and data[i+1] == char.upper() or char.isupper() and data[i+1] == char.lower():
            data = data[0:i] + data[i+2:]
            if i > 0:
                i -= 1
            continue
        i += 1

    if len(data) < best_count:
        best_count = len(data)
        best_letter = letter

print("{}: {}".format(best_letter, best_count))
