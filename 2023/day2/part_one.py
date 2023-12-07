from pathlib import Path
from functools import reduce
from typing import TextIO


ROOT = Path().absolute()
DATA = ROOT / '2023/day2'

FILENAME = 'input.txt'


def highest_values_of_color(line: str):
    d = {}
    new_str = line.split(':')[1]
    for new_line in new_str.split(';'):
        for n_color in new_line.split(','):
            num , color = n_color.split()
            if color in d and d[color] > int(num):
                continue
            d[color] = int(num)

    return reduce(lambda x, y: x *y, d.values())
    

def getting_game_id(line: str) -> int:
    d = dict(green=13,blue=14,red=12)
    game_id = 0
    good = True
    new_str = line.split(':')[1]
    for new_line in new_str.split(';'):
        for n_color in new_line.split(','):
            num, color = n_color.split()
            if int(num) > d[color]:
                good = False

    if good:
        game_id = int(line.split(':')[0][5:])
    
    return game_id 


def find_total(f: TextIO):
    total = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return total 
        total += highest_values_of_color(line)


with open(DATA / FILENAME) as f:
    print(find_total(f))
