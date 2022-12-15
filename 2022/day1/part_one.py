from typing import TextIO

def elf_with_the_most_carries(f:TextIO) -> int:
    total  = max_calories = 0
    while True:
        calory = f.readline()
        if calory == '':
            return max_calories
        elif calory == '\n':
            if total > max_calories:
                max_calories = total
            total = 0
        else:
            total += int(calory)
        

with open('2022/day1/input.txt') as f:
    print(elf_with_the_most_carries(f))

