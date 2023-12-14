from icecream import ic
with open("testsample.txt", "r") as f:
    data = f.readlines()
total = 0
times = 1
for line in data:
    line = line.split(":")[1]
    line = line.split("|")
    win = line[0].split()
    options = line[1].split()
    while times!=0:
        found = 0
        times -= 1
        for i in win:
            if i in options:
                found += 1
                ic(i, found, times)
            if found:
                total += 1
        ic(total, found, times)
    times = found-1
ic(total)