from pathlib import Path
from typing import TextIO,Dict,Tuple, List

ROOT = Path().absolute()
PATH = ROOT / '2023/day3'
FILENAME = 'input.txt'


P = complex
ADJACENT = [
        P(-1,1) , P(0,1), P(1,1),
        P(-1,0) ,         P(1,0),
        P(-1,-1), P(0, -1), P(1,-1),
    ]

def get_num(grid: Dict[complex, str], pos: complex) -> Tuple[complex, int]:
    if pos not in grid or not grid[pos].isnumeric():
        return None
    while pos-1 in grid and grid[pos-1].isnumeric():
        pos -= 1

    start = pos
    num = ''
    while pos in grid and grid[pos].isnumeric():
        num += grid[pos]
        pos += 1
    return start, int(num)

def get_adj_parts(grid, pos):
    parts = set()
    for val in ADJACENT:
        parts.add(get_num(grid, pos + val))

    return parts - {None}


def get_all_point(grid: Dict[complex, str], symbols: List[complex]):
    total = 0
    for val in symbols:
        if grid[val] != '*': continue
        parts = list(get_adj_parts(grid, val))
        print(parts)
        if len(parts) == 2:
            total += parts[0][1] * parts[1][1]
    return total





def read_input(f: TextIO) -> None:
    grid = {}
    symbols = []
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            if char != '.':
                grid[P(j,i)] = char
                if not char.isnumeric():
                    symbols.append(P(j,i))

    print(get_all_point(grid, symbols))

    


with open(PATH / FILENAME , 'r') as f:
    print(read_input(f))