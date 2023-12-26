from icecream import ic
from itertools import cycle
with open("sample.txt", "r") as f:
    data = f.readlines()
data = [x.strip().rstrip("\n") for x in data if x.strip() != ""]
path = data[0]
ways = {}
for line in data[1:]:
    line = [i.strip() for i in line.split("=")]
    ways[line[0]] = line[1].strip("()").split(",")
paths = cycle(path)
steps = 0 
curr = "AAA"
while curr != "ZZZ":
    direction = next(paths)
    ic(direction)
    if direction == "L":
        curr = ways[curr][0].strip()
        steps += 1
    elif direction == "R":
        curr = ways[curr][1].strip()
        steps += 1
ic(steps)
