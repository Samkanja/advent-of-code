from typing import TextIO

WINS = ('A Y','B Z','C X')
LOSSES = ('A Z','B X','C Y')

def calculation(line:str) -> int:
    points = dict(X=1,Y=2,Z=3)
    total = 0
    if line in WINS:
        total = 6
    elif line in LOSSES:
        total = 0
    else:
        total = 3
    total += points[line[-1]]
    return total


def read_input(f:TextIO) -> str:
    total = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return total
        total += calculation(line)
    

with open('2022/day2/input.txt') as f:
    print(read_input(f))