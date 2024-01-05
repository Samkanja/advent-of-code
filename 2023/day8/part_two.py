from pathlib import Path
from typing import TextIO
import argparse

ROOT = Path().absolute()
PATH = ROOT / '2023/day8'

parser = argparse.ArgumentParser()
parser.add_argument('-t','--text',help='pick a text to run', type=int, default=0)
args = parser.parse_args()

if args.text:
    FILENAME = 'input.txt'
else:
    FILENAME = 'sample_input.txt'

def read_input(f: TextIO):
    steps , _ ,*nodes = f.read().splitlines()
    network = {}
    for line in nodes:
        pos, node = line.split(' = ')
        network[pos] = node[1:-1].split(', ')

    current = [key for key in network if key[-1] == "A"]
    print(current)


with open(PATH /FILENAME, 'r') as f:
    print(read_input(f))