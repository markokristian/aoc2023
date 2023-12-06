import re
from collections import defaultdict

def input():
    with open("04/input1") as f:
        lines = f.readlines()
        cards = {}
        for line in lines:
            cardno, card = line.split(":")
            cardno = int(re.findall(r'\d+', cardno)[0])
            winners, mine = card.split("|")
            winners = {int(w) for w in winners.strip().replace("  ", " ").split(" ")}
            mine = {int(m) for m in mine.strip().replace("  ", " ").split(" ")}
            correct = len(winners.intersection(mine))
            cards[cardno] = correct
        return cards

def process(cards):
    copies = defaultdict(lambda: 0)
    for card, ncorrect in cards.items():
        copies[card] += 1
        for c in range(ncorrect):
            copies[card + c + 1] += copies[card]
    return sum(copies.values())
        
print(process(input()))
