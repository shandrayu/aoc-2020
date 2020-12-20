from typing import List

def count_neighborhood(data: List[List[str]], x: int, y: int) -> int:
    height = len(data)
    assert height
    width = len(data[0])
    assert 0 < x < height - 1
    assert 0 < y < width - 1
    neighbour_idx = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                     (x, y - 1), (x, y + 1), 
                     (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    s = 0
    for x_n, y_n in neighbour_idx:
        s += 1 if data[x_n][y_n] == '#' else 0
    return s

def count_neighborhood_in_rays(data: List[List[str]], x: int, y: int) -> int:
    height = len(data)
    assert height
    width = len(data[0])
    assert 0 < x < height - 1
    assert 0 < y < width - 1

    directions = [(-1, -1), (-1,  0), (-1, +1),
                  ( 0, -1), ( 0, +1),
                  (+1, -1), (+1,  0), (+1, +1)]
    s = 0
    ray = lambda s : s == '.'
    for x_delta, y_delta in directions:
        x_ray = x + x_delta
        y_ray = y + y_delta
        while ray(data[x_ray][y_ray]):
            x_ray += x_delta
            y_ray += y_delta
        s += 1 if data[x_ray][y_ray] == '#' else 0
    return s 

def is_occupied(s: str) -> bool:
    return s == '#'

def update_seating(data: List[List[str]], tolerance: int, neighbourhood_function) -> (List[List[str]], bool):
    height = len(data)
    assert height
    width = len(data[0])
    new_matrix = [['-'] * width for _ in range(height)]
    
    is_updated = False
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            num_occupied = neighbourhood_function(data, x, y)
            if is_occupied(data[x][y]) and num_occupied >= tolerance:
                new_matrix[x][y] = 'L'
                is_updated = True
            elif data[x][y] =='L' and num_occupied == 0:
                new_matrix[x][y] = '#'
                is_updated = True
            else:
                new_matrix[x][y] = data[x][y]    
    return new_matrix, is_updated

def count_occupied_seats(data: List[List[str]]) -> int:
    occupied_seats = 0
    for row in data:
        occupied_seats += sum([is_occupied(symbol) for symbol in row]) 
    return occupied_seats

def first_part(data: List[List[str]]) -> int:
    is_updated = True
    new_seating = data
    while is_updated:
        new_seating, is_updated = update_seating(new_seating, 4, count_neighborhood)

    return count_occupied_seats(new_seating)

def second_part(data: List[List[str]]) -> int:
    is_updated = True
    new_seating = data
    while is_updated:
        new_seating, is_updated = update_seating(new_seating, 5, count_neighborhood_in_rays)

    return count_occupied_seats(new_seating)

if __name__ == '__main__':
    filename = 'day11/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        # Add a border around data
        width = len(lines[0].strip('\n')) + 2
        data.append(['-'] * width)
        for line in lines:
            line = line.strip('\n')
            line = ['-'] + list(line) + ['-']
            data.append(line)
        data.append(['-'] * width)

    print('First part: Number of occupied seats is {}'.format(first_part(data)))
    print('Second part: Number of occupied seats is {}'.format(second_part(data)))