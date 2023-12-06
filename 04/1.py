with open("04/input1") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    cardno, card = line.split(":")
    winners, mine = card.split("|")
    winners = {int(w) for w in winners.strip().replace("  ", " ").split(" ")}
    mine = {int(m) for m in mine.strip().replace("  ", " ").split(" ")}
    correct = len(winners.intersection(mine))
    sum += correct if correct in [0, 1] else 2**(correct - 1)
print(sum)
