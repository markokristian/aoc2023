from math import prod

with open("02/input1") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

colors = {"blue": 0, "green": 1, "red": 2}
games = {}
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

def max_set(sets):
    maxes = [0]*3
    for s in sets:
        for i, n in enumerate(s):
            if n > maxes[i]:
                maxes[i] = n
    return maxes

print(sum([
    prod(max_set(sets))
    for sets in games.values()
]))
