from collections import defaultdict
from sortedcontainers import SortedDict
from collections import Counter

def input():
    with open("07/input1") as f:
        lines = f.readlines()
        for line in lines:
            hand, bid = line.split(" ")
            handn = []
            cm = {"A": "F", "K": "E", "Q": "C", "J": "0", "T": "A"}
            for card in hand:
                if card.isnumeric():
                    handn.append(card)
                else:
                    handn.append(cm[card])
            yield handn, int(bid.strip())
hands = list(input())

def check(hand):
    # replace joker with the most common card type
    if "0" in hand:
        nojokers = [c for c in hand if c != "0"]
        if not nojokers:
            hand = "00000"
        else:
            cnt = Counter(nojokers)
            most_common = cnt.most_common(1)[0][0]
            hand = [most_common if c == '0' else c for c in hand]

    counter = Counter(hand)
    counts = counter.values()

    if 5 in counts:
        return 0
    if 4 in counts:
        return 1
    if 3 in counts and 2 in counts:
        return 2
    if 3 in counts:
        return 3
    if sum(count == 2 for count in counts) == 2:
        return 4
    if 2 in counts:
        return 5
    if sum(count == 1 for count in counts) == 5:
        return 6
    return None

# put each hand in a bucket of wintype
wintypes = defaultdict(lambda: SortedDict())

for hand, bid in hands:
    wintype = check(hand)
    hex = int(''.join(hand), 16)
    wintypes[wintype].update({
        hex: bid
    })

# sort each bucket by rank
rank = 1
keys_sorted = reversed(sorted(wintypes.keys()))
winnings = 0
for wt in keys_sorted:
    v = wintypes[wt]
    for hand in v:
        winnings += rank * v[hand]
        rank += 1
print(winnings)
