import numpy as np

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

def matrix_pressure(matrix):
    p = 0
    for k in range(len(matrix)):
        s = "".join(matrix[k])
        parts = s.split('#')
        for i in range(len(parts)):
            zeros = parts[i].count('O')
            dots = parts[i].count('.')
            parts[i] = 'O' * zeros + '.' * dots
        p += pressure('#'.join(parts))
    return p

matrix = read()
matrix = np.rot90(matrix, 1)
print(matrix_pressure(matrix))
