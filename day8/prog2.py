from icecream import ic
from itertools import cycle
with open("sample.txt", "r") as f:
    data = f.readlines()

def all_ends_with_Z(curr) -> bool:
    return all(i.endswith("Z") for i in curr)

data = [x.strip().rstrip("\n") for x in data if x.strip() != ""]
path = data[0]
ways = {}
for line in data[1:]:
    line = [i.strip() for i in line.split("=")]
    ways[line[0]] = line[1].strip("()").split(",")
paths = cycle(path)
steps = 0 
curr = [i for i in ways if i.endswith("A")]
while not all_ends_with_Z(curr):
    direction = next(paths)
    if direction == "L":
        curr = [ways[i][0].strip() for i in curr]
        steps += 1
    elif direction == "R":
        curr = [ways[i][1].strip() for i in curr]
        steps += 1
    ic(curr)
ic(steps)


