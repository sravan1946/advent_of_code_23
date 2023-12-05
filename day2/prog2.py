from icecream import ic
with open("sample.txt", "r") as f:
    data = f.readlines()

games = {}

for index, line in enumerate(data, start=1):
    games[index] = {"red": 1, "green": 1, "blue": 1}
    colors = line[7:]
    colorgroups = colors.split("; ")
    for group in colorgroups:
        group = group.strip().split(", ")
        for color in group:
            color = color.split()
            if len(color) == 3:
                color = color[1:]
            num = int(color[0])
            color = color[1]
            if color == "red" and games[index]["red"] < num: 
                games[index]["red"] = num
            ic(group, games[index], num, color)
            if color == "green" and games[index]["green"] < num:
                games[index]["green"] = num
            if color == "blue" and games[index]["blue"] < num:
                games[index]["blue"] = num
total = 0
for i in games:
    prod = games[i]["red"] * games[i]["green"] * games[i]["blue"]
    total += prod
print(total)
