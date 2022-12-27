from typing import TextIO
from string import ascii_letters

def calculation_priority_char(line:str):
    n = len(line)
    set_a = set(line[:n//2])
    set_b = set(line[n//2:])
    char = list(set_a.intersection(set_b))[0]
    return ascii_letters.index(char) + 1


def read_input(f:TextIO) -> int:
    total = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return total
        total += calculation_priority_char(line)


with open('2022/day3/input.txt') as f:
    print(read_input(f))