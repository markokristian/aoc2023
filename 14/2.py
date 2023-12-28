import numpy as np
from collections import defaultdict

def read():
    with open("14/input1") as f:
        lines = f.read().split("\n")
        arr = []
        for line in lines:
            arr.append([c for c in line])
        return np.array(arr)

def pressure(line):
    return sum([
        len(line) - i
        for i, char in enumerate(line) if char == 'O'
    ])

def stones_to_left(matrix):
    arr = []
    for k in range(len(matrix)):
        s = "".join(matrix[k])
        parts = s.split('#')
        for i in range(len(parts)):
            zeros = parts[i].count('O')
            dots = parts[i].count('.')
            parts[i] = 'O' * zeros + '.' * dots
        s = '#'.join(parts)
        arr.append([c for c in s])
    return np.array(arr)

matrix = read()

pressures = defaultdict(lambda: 0)
N = 1000
for cycle in range(N):
    # counter clockwise once (north)
    matrix = np.rot90(matrix, k=-1, axes=(1,0))
    matrix = stones_to_left(matrix)
    # clockwise once (west) [at normal]
    matrix = np.rot90(matrix, k=1, axes=(1,0))
    matrix = stones_to_left(matrix)
    # clockwise once (south)
    matrix = np.rot90(matrix, k=1, axes=(1,0))
    matrix = stones_to_left(matrix)
    # clockwise once (east)
    matrix = np.rot90(matrix, k=1, axes=(1,0))
    matrix = stones_to_left(matrix)
    # counter clockwise twice (back to normal)
    matrix = np.rot90(matrix, k=-2, axes=(1,0))

    north = np.rot90(matrix, k=-1, axes=(1,0))
    p = 0
    for k in range(len(north)):
        line = north[k]
        p += pressure(line)
    
    if (cycle + 1) % 10 == 0:
        pressures[cycle + 1] = p

ys = defaultdict(lambda: [])
for x,y in pressures.items():
    ys[y].append(x)

import json
print(json.dumps(ys, indent=2))

print("basically a cycle that satisfies that its divisible by the periodicity which in my case was 110")
print((1000000000 - 890) % 110 == 0)
