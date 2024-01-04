from pathlib import Path
from typing import TextIO
import argparse


ROOT = Path().absolute()
PATH = ROOT / '2023/day7'

parser = argparse.ArgumentParser()
parser.add_argument('-t','--text',help='pick a text to run', type=int, default=0)
args = parser.parse_args()

if args.text:
    FILENAME = 'input.txt'
else:
    FILENAME = 'sample_input.txt'

letter_map = dict(T='A',J='B',Q='C',K='D',A="E")
def classify(hand):
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

def strength(hand):
    return (classify(hand),[letter_map.get(char, char) for char in hand])

def read_input(f:TextIO):
    plays = []
    lines = f.readlines()
    for line in lines:
        hand, bid = line.strip().split()
        plays.append((hand, int(bid)))
    
    plays.sort(key= lambda x : strength(x[0]))
    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid
    print(total)
        

with open(PATH/ FILENAME, 'r') as f:
    print(read_input(f))