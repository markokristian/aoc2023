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

def check(buf, g, mx, my):
    if not buf:
        return False
    adjs = set()
    for pos in buf:
        adjs.update(adj(pos, g, mx, my))
    adjs.difference_update(set(buf))
    return not all([g[a] == "." for a in adjs])

g, mx, my = input("03/input1")
sum = 0
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
                    if check(buf, g, mx, my):
                        sum += int("".join([g[pos] for pos in buf]))
                    break
            else:
                x += 1
                if check(buf, g, mx, my):
                    sum += int("".join([g[pos] for pos in buf]))
                break
print(sum)
