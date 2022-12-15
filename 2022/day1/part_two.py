from typing import TextIO

def total_of_the_top_three_with_most_calories(f:TextIO) -> int:
    total = 0
    l = []
    while True:
        calory = f.readline()
        if calory == '':
            return sum(sorted(l)[-3:])
        elif calory == '\n':
            l.append(total)
            total = 0
        else:
            total += int(calory)

       
with open('2022/day1/input.txt') as f:
    print(total_of_the_top_three_with_most_calories(f))
