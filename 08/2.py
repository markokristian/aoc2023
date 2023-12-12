import math
from itertools import cycle
import networkx as nx

def read_input():
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

def walk(g, starts, ops):
    ss = []
    for current in starts:
        steps = 0
        while 1:
            op = next(ops)
            steps += 1
            neighbors = list(g.neighbors(current))
            current = neighbors[0] if op == "L" else neighbors[-1]
            if current.endswith("Z"):
                ss.append(steps)
                break
    return ss

def lcm(steps):
    lc = steps[0]
    for num in steps[1:]:
        lc = lc * num // math.gcd(lc, num)
    return lc

ops, nodes = read_input()
G = bigraph(nodes)
starts = [node for node in G.nodes if node.endswith("A")]
steps = walk(G, starts, ops)
print(lcm(steps))
