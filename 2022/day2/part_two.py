from typing import TextIO

WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0

def calculation_of_total_points(line:str) -> int:
    LOSE = 'X'
    WIN = 'Z'
    DRAW = 'Y'
    loses = dict(A='C',B='A',C='B')
    wins = dict(A='B',C='A',B='C')
    draws = dict(A='A',B='B',C='C')
    points = dict(A=1,B=2,C=3)
    choice = line[-1]
    opponent_choice = line[0]
    if choice == LOSE:
        char = loses[opponent_choice]
        Char_point = points[char]
        total = LOSE_POINTS
    elif choice == WIN:
        char = wins[opponent_choice]
        Char_point = points[char]
        total = WIN_POINTS
    else:
        char = draws[opponent_choice]
        Char_point = points[char]
        total = DRAW_POINTS
    return Char_point + total

def read_input(f:TextIO) -> int:
    total = 0
    while True:
        line = f.readline().strip()
        if line == '':
            return total
        total += calculation_of_total_points(line)
        



with open('2022/day2/input.txt') as f:
    print(read_input(f))