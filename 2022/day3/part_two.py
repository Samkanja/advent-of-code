from typing import List,TextIO
import string

def total_of_three_rucksanks(l:List[str]) ->int:
    char = list(set(l[0]) & set(l[1]) & set(l[2]))[0]
    return string.ascii_letters.index(char) +1


def read_input(f:TextIO) -> int:
    l = []
    p = []
    total = 0
    count = 3
    max_total = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return max_total
        elif len(l) == 3 and count == 0:
            total = total_of_three_rucksanks(l)
            l = []
        elif line and count == 3:
            l.append(line)
            count -= 1
        max_total += total
        total = 0
        
            
        
with open('2022/day3/input.txt') as f:
    print(read_input(f))
