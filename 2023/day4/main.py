from typing import TextIO, Set
from pathlib import Path


ROOT = Path().absolute()
PATH = ROOT  /'2023/day4'
FILENAME = 'input.txt'

def func(x:int):
    total = 1
    if not x:
        return 0
    else:
        for i in range(len(x)):
            if i >= 1: 
                total *=2 
        else:
            return total


def compare_sets(set1: Set[int], set2: Set[int]) -> int:
    return len(set1 & set2)


def get_total(line: str) -> int:
    total = 1
    new_lst = line.strip().split(':')[1]
    winning, mine = new_lst.split('|')
    winning_set = set(int(num) for num in winning.split())
    mine_set = set( int(num) for num in mine.split())
    count = compare_sets(winning_set, mine_set) 
    return 2**(count-1) if count > 0 else 0



def read_input(f:TextIO) -> int:
    total = 0
    while True:
        line = f.readline()
        if line == '':
            return total
        total += get_total(line)


with open(PATH / FILENAME ,'r') as f:
    print(read_input(f))
