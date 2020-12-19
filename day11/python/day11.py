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

def is_occupied(s: str) -> bool:
    return s == '#'

def update_seating(data: List[List[str]]) -> (List[List[str]], bool):
    height = len(data)
    assert height
    width = len(data[0])
    new_matrix = [['.'] * width for _ in range(height)]
    
    is_updated = False
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            num_occupied = count_neighborhood(data, x, y)
            if is_occupied(data[x][y]) and num_occupied >= 4:
                new_matrix[x][y] = 'L'
                is_updated = True
            elif data[x][y] =='L' and num_occupied == 0:
                new_matrix[x][y] = '#'
                is_updated = True
            else:
                new_matrix[x][y] = data[x][y]    
    return new_matrix, is_updated

def count_occupied_seats(data: List[List[str]]) -> int:
    is_updated = True
    new_seating = data
    while is_updated:
        new_seating, is_updated = update_seating(new_seating)

    occupied_seats = 0
    for row in new_seating:
        occupied_seats += sum([is_occupied(symbol) for symbol in row]) 
    return occupied_seats

if __name__ == '__main__':
    filename = 'day11/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        # Add a border of floor around data
        width = len(lines[0].strip('\n')) + 2
        data.append(['.'] * width)
        for line in lines:
            line = line.strip('\n')
            line = ['.'] + list(line) + ['.']
            data.append(line)
        data.append(['.'] * width)

    print('Number of occupied seats is {}'.format(count_occupied_seats(data)))
