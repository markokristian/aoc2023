with open("09/input1") as f:
    lines = f.readlines()
    lines = [list(map(int, l.split())) for l in lines]

s = 0
for series in lines:
    lasts = []
    series = list(reversed(series))
    while 1:
        lasts.append(series[-1])
        diffs = [
            series[n] - series[n-1]
            for n in range(1, len(series))
        ]
        if all([n == 0 for n in diffs]):
            break
        else:
            series = diffs

    s += sum(lasts)

print(s)