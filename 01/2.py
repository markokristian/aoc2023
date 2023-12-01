with open("01/input1") as f:
    lines = f.readlines()

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find(buf):
    for n in nums.keys():
        if n in buf:
            return nums[n]
    return None


def parse(line):
    first = ""
    last = ""
    buf = ""
    for c in line:
        if c.isnumeric():
            first = c
            break
        buf += c
        num = find(buf)
        if num:
            first = num
            break
    buf = ""
    for c in reversed(line):
        if c.isnumeric():
            last = c
            break
        buf += c
        num = find(buf[::-1])
        if num:
            last = num
            break
    return int(first + last)


print(sum([parse(line) for line in lines]))
