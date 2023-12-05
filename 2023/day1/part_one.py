from pathlib import Path
from typing import List, TextIO

ROOT = Path().absolute()
DATA = ROOT / '2023/day1'

FILENAME = 'input.txt'

d = dict(one='1', two='2', three='3', four='4', five='5', six='6', seven='7', eight='8', nine='9')


def find_total_1(line: str):
    lst = []
    for i , ele in enumerate(line):
        if ele.isdigit():
            lst.append(ele)
        for char in list(d.keys()):
            if line[i:].startswith(char):
                lst.append(d[char])
    return int(lst[0] + lst[-1])


def find_total(line: str) -> int: 
    lst = []
    for char in line:
        if char.isdigit():
            lst.append(char)

    return int(lst[0] + lst[-1])


def read_input(f: TextIO) -> int:
    total = 0

    while True:
        line = f.readline().strip()
        if line == '':
            return total
        total += find_total_1(line)


with open(DATA / FILENAME, 'r') as f:
    print(read_input(f))



