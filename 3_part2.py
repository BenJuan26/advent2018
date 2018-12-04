from aoc import get_input

data = get_input(3)

sheet = [0] * 1000
for i in range(1000):
    sheet[i] = [0] * 1000

claims = data.split("\n")
for claim in claims:
    clauses = claim.split(" ")
    claim_id = clauses[0][1:]
    coords = clauses[2].split(",")
    x = int(coords[0])
    y = int(coords[1][:-1])
    size = clauses[3].split("x")
    w = int(size[0])
    h = int(size[1])

    for col in range(w):
        for row in range(h):
            sheet[col+x][row+y] = sheet[col+x][row+y] + 1

for claim in claims:
    clauses = claim.split(" ")
    claim_id = clauses[0][1:]
    coords = clauses[2].split(",")
    x = int(coords[0])
    y = int(coords[1][:-1])
    size = clauses[3].split("x")
    w = int(size[0])
    h = int(size[1])

    success = True
    for col in range(w):
        for row in range(h):
            if sheet[col+x][row+y] > 1:
                success = False
    
    if success:
        print(claim_id)
