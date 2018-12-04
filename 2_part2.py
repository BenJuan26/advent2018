from aoc import get_input

data = get_input(2)
lines = data.split("\n")

for i in range(len(lines)):
    for j in range(len(lines)):
        word1 = lines[i]
        word2 = lines[j]
        diff = 0
        for n in range(len(word1)):
            if word1[n] != word2[n]:
                diff += 1
        if diff == 1:
            result = ""
            for n in range(len(word1)):
                if word1[n] == word2[n]:
                    result += word1[n]
            print(result)
            raise SystemExit