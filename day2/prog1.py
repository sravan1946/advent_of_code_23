from icecream import ic
with open("sample.txt", "r") as f:
    data = f.readlines()

games = {}

for index, line in enumerate(data, start=1):
    games[index] = True
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
            if color == "red" and num > 12:
                games[index] = False
                break
            if color == "green" and num > 13:
                games[index] = False
                break
            if color == "blue" and num > 14:
                games[index] = False
                break
total = sum(i for i, value in games.items() if value)
print(total)