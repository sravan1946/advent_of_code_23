from icecream import ic 
with open("sample.txt", "r") as f:
    data = f.readlines()
total = 0

for line in data:
    line = line.split(":")[1]
    line = line.split("|")
    win = line[0].split()
    options = line[1].split()
    found = 0
    ic(win)
    for i in win:
        if i in options:
            found += 1
    if found:
        total += 2**(found-1) 
ic(total)