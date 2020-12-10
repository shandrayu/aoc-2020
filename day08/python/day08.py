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

def reset(program):
    for command in program:
        command[1] = False

def execute(program) -> (int, bool):
    acc = 0
    idx = 0
    reset(program)

    while idx < len(program) and not program[idx][1]:
        command = program[idx][0]
        program[idx][1] = True
        if command.command_type == CommandType.ACC:
            acc += command.value
            idx += 1
        elif command.command_type == CommandType.NOP:
            idx += 1
        elif command.command_type == CommandType.JMP:
            idx += command.value

    has_terminated = idx == len(program)

    return acc, has_terminated

def get_mutated_program():
    idx = 0
    while idx < len(program):
        if program[idx][0].command_type == CommandType.JMP:
            program[idx][0] = Command(CommandType.NOP, program[idx][0].value)
            yield program
            program[idx][0] = Command(CommandType.JMP, program[idx][0].value)
        elif program[idx][0].command_type == CommandType.NOP:
            program[idx][0] = Command(CommandType.JMP, program[idx][0].value)
            yield program
            program[idx][0] = Command(CommandType.NOP, program[idx][0].value)
        idx += 1

if __name__ == '__main__':
    program = []
    with open('day08/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            command = read_command(line)
            program.append([command, False])
    
    accumlator_value, has_terminated = execute(program)
    print('Program execution terminated {}'.format(has_terminated))
    print('Accumulator value before going into the infinite loop was {} '.format(accumlator_value))

    program_mutator = get_mutated_program()
    accumulator = -1000
    current_program = program
    while current_program:
        accumulator, has_terminated = execute(current_program)
        if has_terminated:
            break
        current_program = next(program_mutator, False)
    
    print('Program has terminated {}'.format(has_terminated))
    print('Mutated program last accumulator value is {}'.format(accumulator))