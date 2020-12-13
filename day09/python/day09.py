from typing import Deque
from typing import List
from collections import deque


def is_number_valid(number: int, preamble: Deque[int]) -> bool:
    is_valid = False
    for preabmle_num in preamble:
        difference = number - preabmle_num
        if difference in preamble and difference != preabmle_num:
            is_valid = True
            break
    return is_valid

def get_first_invalid_number(data: List[int], preamble_size: int) -> (int, bool):
    first_invalid_number = -1
    found = False
    preamble = deque(data[0:preamble_size])
    for number in data[preamble_size:]:
        if not is_number_valid(number, preamble):
            first_invalid_number = number
            found = True
            break
        preamble.popleft()
        preamble.append(number)
    return first_invalid_number, found

if __name__ == '__main__':
    filename = 'day09/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))

    invalid_number, found = get_first_invalid_number(data, 25)
    print('Found {}'.format(found))
    print('First number in the list which does not follow the rules is {}'.format(invalid_number))
