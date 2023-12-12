from itertools import cycle
import networkx as nx

def input():
    with open("08/input1") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
        ops = cycle(list(lines[0]))
        nodes = {}
        for line in lines[1:]:
            n, nns = line.split(" = ")
            left, right = nns.split(", ")
            left = left.replace("(", "")
            right = right.replace(")", "")
            nodes[n] = [left, right]
        return ops, nodes

def bigraph(inputs):
    G = nx.DiGraph()
    for node, neighbors in inputs.items():
        G.add_node(node)
        G.add_edges_from((node, neighbor) for neighbor in neighbors)
    return G

def walk(g, start, ops):
    current, steps = start, 0
    while 1:
        op = next(ops)
        steps += 1
        neighbors = list(g.neighbors(current))
        current = neighbors[0] if op == "L" else neighbors[-1]
        if current == "ZZZ":
            return steps

ops, nodes = input()
G = bigraph(nodes)
steps = walk(G, "AAA", ops)
print(steps)
