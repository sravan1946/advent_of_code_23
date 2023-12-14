from icecream import ic
with open("sample.txt", "r") as f:
    data = f.readlines()

times = data[0].split()[1:]
distances = data[1].split()[1:]
time = int("".join(times))
distance = int("".join(distances))
total = 1
distances_travelled = []
for sec in range(time):
    speed = sec
    ic(speed)
    time_to_travel = time - sec
    distance_travelled = speed * time_to_travel
    distances_travelled.append(distance_travelled)
distances_travelled = [d for d in distances_travelled if d > distance]
ic(distances_travelled)
total *= len(distances_travelled)
ic(total)

