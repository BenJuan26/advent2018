from aoc import get_input

data = get_input(1)

result = 0
past_results = {}
while True:
    for line in data.split("\n"):
        num = int(line[1:])
        if line[0] == "+":
            result = result + num
        else:
            result = result - num
        try:
            if past_results[result] == True:
                print(result)
                raise SystemExit
        except KeyError:
            past_results[result] = True
