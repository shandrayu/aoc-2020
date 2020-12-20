from collections import namedtuple
from typing import List
import math


Command = namedtuple('Command', 'kind value')


def execute_commands(commands: List[Command]) -> int:
    directions = ('N', 'E', 'S', 'W')
    dir_idx = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    current_direction = 'E'
    for command in commands:
        if command.kind == 'L':
            idx = (dir_idx[current_direction] - int(command.value / 90)) % 4
            current_direction = directions[idx]
        elif command.kind == 'R':
            idx = (dir_idx[current_direction] + int(command.value / 90)) % 4
            current_direction = directions[idx]
        elif command.kind == 'F':
            position[current_direction] += command.value
        else:
            position[command.kind] += command.value

    return abs(position['N'] - position['S']) + abs(position['E'] - position['W'])


def rotate(point, direction, value):
    angle = value if direction == 'L' else -value

    s = int(math.sin(math.radians(angle)))
    c = int(math.cos(math.radians(angle)))

    # convert point to cartisian coordinates
    x = point['E'] - point['W']
    y = point['N'] - point['S']

    # rotate point
    xnew = x * c - y * s
    ynew = x * s + y * c

    # convert back to NESW coordinates
    rotated_point = {}
    if ynew > 0:
        rotated_point['N'] = ynew
        rotated_point['S'] = 0
    else:
        rotated_point['N'] = 0
        rotated_point['S'] = -ynew
    if xnew > 0:
        rotated_point['E'] = xnew
        rotated_point['W'] = 0
    else:
        rotated_point['E'] = 0
        rotated_point['W'] = -xnew

    return rotated_point


def execute_commands_2(commands: List[Command]) -> int:
    position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    way_point = {'N': 1, 'E': 10, 'S': 0, 'W': 0}

    for command in commands:
        if command.kind == 'F':
            for direction in way_point:
                position[direction] += command.value * way_point[direction]
        elif command.kind == 'L' or command.kind == 'R':
            way_point = rotate(way_point, command.kind, command.value)
        else:
            way_point[command.kind] += command.value

    return abs(position['N'] - position['S']) + abs(position['E'] - position['W'])


if __name__ == '__main__':
    filename = 'day12/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(Command(line[0], int(line[1:])))

    print('Manhattan distance between that location and the ship\'s starting position is {}'.format(
        execute_commands(data)))
    print('Manhattan distance between that location and the ship\'s starting position is {}'.format(
        execute_commands_2(data)))
