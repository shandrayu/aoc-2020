from collections import namedtuple
from enum import Enum
from typing import List


class CommandType(Enum):
    ACC = 1
    JMP = 2
    NOP = 3

Command = namedtuple('Command', 'command_type value')

def get_type(command_str: str) -> CommandType:
    if command_str == 'acc':
        command = CommandType.ACC
    elif command_str == 'jmp':
        command = CommandType.JMP
    elif command_str == 'nop':
        command = CommandType.NOP
    return command

def read_command(line: str) -> Command:
    command_type_str, value_str = line.split(' ') 
    return Command(get_type(command_type_str), int(value_str))

def execute(program) -> int:
    acc = 0
    idx = 0
    while not program[idx][1]:
        command = program[idx][0]
        program[idx][1] = True
        if command.command_type == CommandType.ACC:
            acc += command.value
            idx += 1
        elif command.command_type == CommandType.NOP:
            idx += 1
        elif command.command_type == CommandType.JMP:
            idx += command.value
    return acc

if __name__ == '__main__':
    program = []
    with open('day08/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            command = read_command(line)
            program.append([command, False])
    
    print('Accumulator value before going into the infinite loop was {} '.format(execute(program)))