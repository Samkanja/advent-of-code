
from pathlib import Path
from typing import TextIO

ROOT = Path().absolute()
PATH = ROOT / '2023/day7'
FILENAME = 'input.txt'

letter_map = dict(T='A',J='.',Q='C',K='D',A="E")

def score(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0
def replacements(hand):
    if hand == "":
        return [""]
    return [x +y for x in ("23456789TQKA" if hand[0] == 'J' else hand[0]) for y in replacements(hand[1:])]

def classify(hand):
    return max(map(score, replacements(hand)))

def strength(hand):
    return (classify(hand),[letter_map.get(char, char) for char in hand])


def read_input(f:TextIO):
    plays = []
    lines = f.readlines()
    for line in lines:
        hand, bid = line.strip().split()
        plays.append((hand, int(bid)))
    # print(plays)
    plays.sort(key=lambda x: strength(x[0]))
    total = 0
    for rank, (hand, bid) in enumerate(plays,start=1):
        total += rank * bid
    return total

with open(PATH/ FILENAME, 'r') as f:
    print(read_input(f))