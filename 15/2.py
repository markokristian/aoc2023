from collections import defaultdict

def hash(cmd):
    v = 0
    for c in cmd:
        v += ord(c)
        v *= 17
        v %= 256
    return v

def read():
    with open("15/input1") as f:
        for cmd in f.readline().split(","):
            if cmd[-1] == "-":
                lbl = cmd[:-1]
                yield hash(lbl), lbl, "-", None
            else:
                lbl, fl = cmd.split("=")
                yield hash(lbl), lbl, "=", int(fl)

cmds = read()
boxes = defaultdict(lambda: {})
for boxnum, lbl, op, fl in cmds:
    box = boxes[boxnum]
    if op == "-" and lbl in box:
        del box[lbl]
    if op == "=":
        box[lbl] = fl

s = 0
for id, box in boxes.items():
    for lenspos, (_, fl) in enumerate(box.items()):
        s += (id + 1) * (lenspos + 1) * fl
print(s)
