


def read_input():
    l = []
    count = 0
    while True:
        line = f.readline()
        if line == '':
            break
        elif line and (len(l) <= 3 and count <= 3):
            l.append(line)
            count += 1
        else:
            l.clear()
            count = 0
    return l



with open('2022/day3/sample_input.txt') as f:
    print(read_input())
    