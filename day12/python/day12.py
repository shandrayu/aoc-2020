from collections import namedtuple
from typing import List


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

if __name__ == '__main__':
    filename = 'day12/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(Command(line[0], int(line[1:])))

    print('Manhattan distance between that location and the ship\'s starting position is {}'.format(execute_commands(data)))