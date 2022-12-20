from typing import TextIO
def set_intersect(set_1:set,set_2:set) -> bool:
    return set_1.intersection(set_2)

def retrrive_range(line:str) -> list[set[int]]:
    new_line = line.split(',')
    assignment = [i.split('-')  for i in new_line]
    set_s = [set(range(int(a[0]), int(a[-1])+1)) for a in assignment]
    return set_s

def read_input(f:TextIO) -> int:
    count = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return count
        set_s = retrrive_range(line)
        if set_intersect(*set_s):
            count += 1
   

with open('2022/day4/input.txt') as f:
    print(read_input(f))