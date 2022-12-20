from typing import TextIO


def is_subset(set_1:set,set_2:set) -> bool:
    return set_1.issubset(set_2) or set_2.issubset(set_1)


def read_input(f:TextIO) -> str:
    count = 0
    # line = f.readline().strip()
    # new = retrrive_range(line)
    # return new
    while True:
        line = f.readline().strip()
        
        if line == "":
            return count
        set_s = retrrive_range(line)
        if is_subset(*set_s):
            count += 1

 
    
    
        

def retrrive_range(line:str) -> list[set[int]]:
    new_line = line.split(',')
    assignment = [i.split('-')  for i in new_line]
    set_s = [set(range(int(a[0]), int(a[-1])+1)) for a in assignment]
    return set_s
   

with open('2022/day4/input.txt') as f:
    print(read_input(f))