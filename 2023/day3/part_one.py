from pathlib import Path
from typing import TextIO


ROOT = Path().absolute()
PATH = ROOT / '2023/day3'
FILENAME = 'input.txt'

P = complex
adj = [
        P(-1,1) , P(0,1), P(1,1),
        P(-1,0) ,         P(1,0),
        P(-1,-1), P(0, -1), P(1,-1),
    ]

def get_num(grid, pos):
    if pos not in grid or not grid[pos].isnumeric():
        return None
    while pos-1 in grid and grid[pos-1].isnumeric():
        pos -= 1 
    start = pos
    num = ''
    while pos in grid and grid[pos].isnumeric():
        num += grid[pos]
        pos +=1 

    return start, int(num)


def getAdjParts(grid, pos):
    parts = set()
    for d in adj:
        parts.add(get_num(grid,pos +d))
  
    return parts - {None}


def get_total(grid, symbols):
    parts = set()
    for s in symbols:
        parts |= getAdjParts(grid, s)
    total = 0
    for val in parts:
        total += val[1]
    # return total
    
def part_two(grid, symbols):
    total  = 0
    for val in symbols:
        if grid[val] != '*': continue
        parts = getAdjParts(grid, val)
        print(parts)
    

def read_input(f:TextIO):
    grid = {}
    symbols = []
    lines = f.readlines()
    for y, line in enumerate(lines):
        for x , char in enumerate(line.strip()):
            if char != '.':
                grid[P(x,y)] = char
                if not char.isnumeric():
                    symbols.append(P(x,y))

    print(get_total(grid,symbols))
    print(part_two(grid, symbols))
   
    return None
    


with open(PATH / FILENAME, 'r') as f:
    print(read_input(f))