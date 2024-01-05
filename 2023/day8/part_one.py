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



def read_input(f:TextIO):
    steps , _ , *nodes = f.read().splitlines()
    network = {}
  
    for node in nodes:
        pos, targets = node.split(' = ')
        network[pos] = targets[1:-1].split(', ')
    # print(network)
    current = "AAA"
    step_count = 0
    while current != "ZZZ":
    
        step_count += 1
        

        current = network[current][steps[0] =='R']
        steps = steps[1:] + steps[0]

    return step_count
         
with open(PATH / FILENAME, 'r') as f:
    print(read_input(f))
