import numpy as np
from collections import deque

def read():
    with open("10/test2") as f:
        y, g = 0, {}
        for line in f:
            x = 0
            for s in line.rstrip():
                g[(x, y)] = s
                x += 1
            y += 1
        mx, my = max(g)
        return g, mx, my

deltas = {
    "-": [(-1, 0), (1, 0)],
    "|": [(0, -1), (0, 1)],
    "7": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
}

def adjacent(pos, g):
    x, y = pos
    c = g[pos]
    if c == "S":
        if y + 1 <= my and x + 1 <= mx and g[(x, y + 1)] in ["|", "L"] and g[(x + 1, y)] in ["-", "J"]:
            c = "F"
        elif y - 1 >= 0 and x + 1 <= mx and g[(x, y - 1)] in ["|", "F"] and g[(x + 1, y)] in ["-", "J"]:
            c = "L"
        elif y - 1 >= 0 and x - 1 >= 0 and g[(x, y - 1)] in ["|", "7"] and g[(x - 1, y)] in ["-", "L"]:
            c = "J"
        elif y - 1 >= 0 and x - 1 >= 0 and g[(x, y - 1)] in ["|", "J"] and g[(x - 1, y)] in ["-", "F"]:
            c = "7"
        elif x - 1 >= 0 and x + 1 <= mx and g[(x - 1, y)] in ["-", "L"] and g[(x + 1, y)] in ["-", "J"]:
            c = "-"
        elif x - 1 >= 0 and x + 1 <= mx and g[(x - 1, y)] in ["-", "F"] and g[(x + 1, y)] in ["-", "7"]:
            c = "-"
        elif y - 1 >= 0 and y + 1 <= my and g[(x, y - 1)] in ["|", "F"] and g[(x, y + 1)] in ["|", "L"]:
            c = "|"
        elif y - 1 >= 0 and y + 1 <= my and g[(x, y - 1)] in ["|", "7"] and g[(x, y + 1)] in ["|", "J"]:
            c = "|"
        else:
            print("bah")
            pass
    return [
        tuple(np.array(pos) + np.array(delta))
        for delta in deltas[c]
    ]

def find_s(g):
    for pos in g.keys():
        if g[pos] == "S":
            return pos

def bfs(start, g):
    visited = set()
    queue = deque([(start, 0)])
    steps = {start: 0}
    while queue:
        next, step = queue.popleft()
        if next not in visited:
            visited.add(next)
            # print("visit", g[next], steps)
            for adj in adjacent(next, g):
                if adj not in steps.keys():
                    steps[adj] = step + 1
                    queue.append((adj, step + 1))
    return max(steps.values())

g, mx, my = read()
start = find_s(g)
print(bfs(start, g))
