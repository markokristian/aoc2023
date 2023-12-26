with open("15/input1") as f:
    line = f.readline()
    cmds = line.split(",")

def hash(cmd):
    v = 0
    for c in cmd:
        v += ord(c)
        v *= 17
        v %= 256
    return v

print(sum([hash(cmd) for cmd in cmds]))
