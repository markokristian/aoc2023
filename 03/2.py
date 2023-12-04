from collections import defaultdict
from math import prod

def input(file_name):
    with open(file_name) as f:
        y, g = 0, {}
        for line in f:
            x = 0
            for s in line.rstrip():
                g[(x, y)] = s
                x += 1
            y += 1
        mx, my = max(g)
        return g, mx, my

def adj(pos, g, mx, my):
    x, y = pos
    a = [
        None if x == 0 else (x - 1, y),
        None if y == my else (x, y + 1),
        None if y == 0 else (x, y - 1),
        None if x == mx else (x + 1, y),
        None if x == 0 or y == 0 else (x - 1, y - 1),
        None if x == 0 or y == mx else (x - 1, y + 1),
        None if y == 0 or x == mx else (x + 1, y - 1),
        None if y == my or x == mx else (x + 1, y + 1),
    ]
    return [pos for pos in a if pos is not None]

def gears(buf, g, mx, my):
    if not buf:
        return False
    adjs = set()
    for pos in buf:
        adjs.update(adj(pos, g, mx, my))
    adjs.difference_update(set(buf))
    return [a for a in adjs if g[a] == "*"]

g, mx, my = input("03/input1")
gnums = defaultdict(lambda:[])
for y in range(my + 1):
    x = 0
    while x <= mx:
        buf = []
        while x <= mx:
            if g[(x, y)].isnumeric():
                buf.append((x, y))
                x += 1
                # ahmagaad
                if x > mx:
                    gs = gears(buf, g, mx, my)
                    if gs:
                        num = int("".join([g[pos] for pos in buf]))
                        for gear in gs:
                            gnums[gear].append(num)
                    break
            else:
                x += 1
                gs = gears(buf, g, mx, my)
                if gs:
                    num = int("".join([g[pos] for pos in buf]))
                    for gear in gs:
                        gnums[gear].append(num)
                break
print(sum([
    prod(v) for v in gnums.values()
    if len(v) == 2
]))
