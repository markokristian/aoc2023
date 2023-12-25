from itertools import combinations
import numpy as np

def read():
    with open("11/input1") as f:
        y, g = 0, {}
        for line in f:
            x = 0
            for s in line.rstrip():
                g[(x, y)] = s
                x += 1
            y += 1
        mx, my = max(g)
        return g, mx + 1, my + 1

def col_is_blank(g, x, my):
    return all(g[(x, y)] == '.' for y in range(my))

def row_is_blank(g, y, mx):
    return all(g[(x, y)] == '.' for x in range(mx))

def expand(g, mx, my):
    # just move the #:es
    shift = 999_999
    blank_cols = set([x for x, _ in g.keys() if col_is_blank(g, x, my)])
    blank_rows = set([y for _, y in g.keys() if row_is_blank(g, y, mx)])
    # print(blank_cols, blank_rows)
    for blank_x in sorted(blank_cols, reverse=True):
        to_shift_right = [(x,y) for x, y in g.keys() if x > blank_x and g[(x, y)] == "#"]
        for oldx, oldy in to_shift_right:
            del g[(oldx, oldy)]
            g[(oldx + shift, oldy)] = "#"
    for blank_y in sorted(blank_rows, reverse=True):
        to_shift_down = [(x,y) for x, y in g.keys() if y > blank_y and g[(x, y)] == "#"]
        for oldx, oldy in to_shift_down:
            del g[(oldx, oldy)]
            g[(oldx, oldy + shift)] = "#"
    return g

grid = read()
g, mx, my = grid
g = expand(g, mx, my)

starts = [pos for pos in g.keys() if g[pos] == "#"]
s = 0
for s1, s2 in combinations(starts, 2):
    res = abs(np.array(s1) - np.array(s2))
    s += sum(res)
print(s)
