from typing import List
from collections import namedtuple
from functools import reduce

Step = namedtuple('Step', 'forward down')

def read_mountain(filename: str) -> List[str]:
    mountain = []
    with open(filename) as file:
        mountain = file.read().splitlines()
    return mountain

def count_trees(slope: List[str], step: Step) -> int:
    num_trees = 0
    x, y = 0, 0
    y_max = len(slope)
    x_max = len(slope[0])
    while y < y_max - 1:
        x += step.forward
        x %= x_max
        y += step.down
        if y >= y_max:
            y = y_max - 1
        if slope[y][x] == '#':
            num_trees += 1
    return num_trees

if __name__ == '__main__':
    mountain = read_mountain('day03/input.txt')
    print(count_trees(mountain, Step(3, 1)))
    all_counts = [count_trees(mountain, Step(f, d)) for f, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    print(all_counts)
    print(reduce(lambda x, y: x*y, all_counts))
