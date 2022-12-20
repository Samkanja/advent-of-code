from typing import TextIO
import string

def find_priory_digit_of_characters(line:str) -> int:
    n = len(line)
    set_a = set(line[:n//2])
    set_b = set(line[n//2:])
    char = list(set_a.intersection(set_b))[0]
    return string.ascii_letters.index(char) + 1

def read_inputs(f:TextIO) -> int:
    total = 0
    while True:
        line = f.readline()
        if line == '':
            return total
        total += find_priory_digit_of_characters(line)

with open('2022/day3/input.txt') as f:
    print(read_inputs(f))