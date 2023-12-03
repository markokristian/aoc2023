import numpy as np

with open("02/input1") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

colors, games = {"blue": 0, "green": 1, "red": 2}, {}
for line in lines:
    s = line.split(":")
    gid = int(s[0].split(" ")[1])
    sets = s[1].split(";")
    parsed = []
    for set in sets:
        s = set.split(",")
        items = [0]*3
        for d in s:
            n, color = d.lstrip().split(" ")
            items[colors[color]] = int(n)
        parsed.append(items)
    games[gid] = parsed

def works(s):
    return np.all([14, 13, 12] - np.array(s) >= 0)

def is_possible(sets):
    return all([works(s) for s in sets])

print(sum([
    gid for gid, sets in games.items()
    if is_possible(sets)
]))
