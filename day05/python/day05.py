from collections import namedtuple
from typing import List


Seat = namedtuple('Seat', 'row column')

def seat_id(seat: Seat) -> int:
    return seat.row * 8 + seat.column

def binary_search(data: str, range: int, lower: str, upper: str) -> int:
    idx = 0
    left = 0
    right = range
    while idx < len(data):
        half_range = (right - left) // 2 + 1
        if data[idx] == lower:
            right -= half_range
        elif data[idx] == upper:
            left += half_range
        idx += 1
    return left

def seat_column(seat_column_str: str) -> int:
    return binary_search(seat_column_str, 7, 'L', 'R')

def seat_row(seat_row_str: str) -> int:
    return binary_search(seat_row_str, 127, 'F', 'B')

def find_one_missing_id(ids: List[int]) -> int:
    sorted_ids = sorted(ids)
    id = -1
    for idx in range(len(sorted_ids) - 1):
        if sorted_ids[idx + 1] - sorted_ids[idx] == 2:
            id = sorted_ids[idx] + 1
    return id

if __name__ == '__main__':
    seats = []
    with open('day05/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            seat_row_str = line[0:7]
            seat_column_str = line[7:]
            seat = Seat(seat_row(seat_row_str), seat_column(seat_column_str))
            # Debug
            # print('Seat: row {}, column {}'.format(seat.row, seat.column))
            seats.append(seat_id(seat))
    
    print('The highest seat ID on a boarding pass is {}'.format(max(seats)))
    print('Your seat ID is {}'.format(find_one_missing_id(seats)))