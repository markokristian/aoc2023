with open("01/input1") as f:
    lines = f.readlines()

def digits():
    ls = []
    for line in lines:
        l = []
        for c in line:
            if c.isnumeric():
                l.append(c)
        ls.append(l)
    return ls

print(sum([int(dgs[0] + dgs[-1]) for dgs in digits()]))
