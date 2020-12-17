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

def get_range_with_sum(data: List[int], target_sum: int, min_window_size: int) -> (bool, int, int):
    assert(len(data) > min_window_size)
    range_start_idx = 0
    range_end_idx = range_start_idx + min_window_size
    current_sum = sum(data[range_start_idx:range_end_idx])
    while range_end_idx < len(data):
        numbers_in_range = range_end_idx - range_start_idx
        if numbers_in_range < min_window_size:
            range_end_idx += 1
            current_sum += data[range_end_idx - 1]
        elif current_sum == target_sum:
            break
        elif current_sum < target_sum:
            range_end_idx += 1
            current_sum += data[range_end_idx - 1]
        elif current_sum > target_sum:
            current_sum -= data[range_start_idx]
            range_start_idx += 1
        
    return current_sum == target_sum, range_start_idx, range_end_idx

def sum_smallest_and_largest_nums_in_range(data: List[int], target_sum: int, min_window_size: int) -> int:
    found, range_start_idx, range_end_idx = get_range_with_sum(data, target_sum, min_window_size)
    subrange = data[range_start_idx:range_end_idx]
    return sum([min(subrange), max(subrange)]) if found else -1

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
    print('Sum of smallest and biggest number in the range is {}'.format(sum_smallest_and_largest_nums_in_range(data, invalid_number, 2)))
