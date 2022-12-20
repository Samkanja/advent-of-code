from typing import TextIO
import re
def read_input_file():
    file_input = open('2022/day5/sample_input.txt','r')
    read_file = file_input.read()
    parsed_input = read_file.split('\n')
    return parsed_input

def solve_problem():
    input = read_input_file()
    crates = []
    moves = []
    num_of_staks = 0
    # print(input)
    for line in input:
        # print(line)
        if '[' in line:
            crates.append(line)
        elif 'move' in line:
            moves.append(line)
        elif line != '':
            # print(line)
            num_of_staks = int(line[-2])

    stack_layout = {}
    for i in range(num_of_staks):
        stack_layout[i + 1] = []

    for row in reversed(crates):
        print(len(row))
        for i in range(num_of_staks):
            crate_letter_position = (i * 4) + 1
            crate_letter = row[crate_letter_position]
            if crate_letter != ' ':
                stack_layout[i  + 1].append(crate_letter)

    for move in moves: 
        move_values = re.findall(r'\d+',move)
        num_of_crates_to_move = int(move_values[0])
        crate_from = int(move_values[1])
        crate_to = int(move_values[2])
        crates_to_move = reversed(stack_layout[crate_from][-num_of_crates_to_move:])
        stack_layout[crate_from] = stack_layout[crate_from][:-num_of_crates_to_move]
        stack_layout[crate_to] += crates_to_move

    print(stack_layout)





    return None
res = solve_problem()
print(res)

# def grouping_items(line:list):
#     crates = []
#     instruction = []
#     num_of_stack = 0
#     if '[' in line:
#         crates.append(line)
#     elif 'move' in line:
#         instruction.append(line)
#     elif line != '':
#         num_of_stack = int(line[-2])
#     return crates, instruction, num_of_stack



# def read_input(f:TextIO) -> str:
#     # line = f.readline().split('\n')
#     while True:
#         line = f.readline()
#         if line == '':
#             break
#         print(line.split('\n'))
     

# with open('2022/day5/sample_input.txt') as f:
#     print(read_input(f))