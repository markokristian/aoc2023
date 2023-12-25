from itertools import combinations
from concurrent.futures import ThreadPoolExecutor, as_completed
import networkx as nx

def read():
    with open("11/test1") as f:
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

def expand(grid):
    g, mx, my = grid
    updated, shift_x = {}, 0

    for x in range(mx):
        for y in range(my):
            updated[(x + shift_x, y)] = g[(x, y)]
        if col_is_blank(g, x, my):
            shift_x += 1
            for y in range(my):
                updated[(x + shift_x, y)] = '.'
    
    final, shift_y = {}, 0
    new_max_x = mx + shift_x
    for y in range(my):
        for x in range(new_max_x):
            final[(x, y + shift_y)] = updated[(x, y)]
        if row_is_blank(updated, y, new_max_x):
            shift_y += 1
            for x in range(new_max_x):
                final[(x, y + shift_y)] = '.'

    return final, new_max_x, my + shift_y

def grid_as_graph(g):
    G = nx.Graph()
    for pos in g.keys():
        x, y = pos
        G.add_node((x, y))
        if x > 0:
            G.add_edge((x, y), (x-1, y))
        if y > 0:
            G.add_edge((x, y), (x, y-1))
    return G

grid = read()
g, mx, my = expand(grid)
starts = [pos for pos in g.keys() if g[pos] == "#"]
G = grid_as_graph(g)
sum = 0
with ThreadPoolExecutor(max_workers=len(starts)) as executor:
    future_to_pair = {
        executor.submit(nx.shortest_path_length, G, pair[0], pair[1]):
        pair for pair in combinations(starts, 2)
    }
    for future in as_completed(future_to_pair):
        pair = future_to_pair[future]
        distance = future.result()
        sum += distance
print(sum)
