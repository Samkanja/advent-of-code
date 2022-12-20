from typing import TextIO
def find_start_packet(line:str) -> int:
    d = {}
    l = 0
    for r in range(len(line)):
        if len(set(line[r:r+14])) == len(line[r:r+14]):
            return r+14
       

def read_input(f:TextIO):
    line = f.readline().strip()
    return find_start_packet(line)

with open('2022/day6/input.txt') as f:
    print(read_input(f))