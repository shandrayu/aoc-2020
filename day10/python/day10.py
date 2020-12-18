from typing import List


def adapter_array_stats(sorted_adapters: List[int]) -> int:
    WINDOW_SIZE = 3
    stats = {}
    for i in range(1, WINDOW_SIZE + 1):
        stats[i] = 0
    
    previous_adapter = 0
    for adapter in sorted_adapters:
        difference = adapter - previous_adapter
        stats[difference] += 1
        previous_adapter = adapter

    # The last one
    stats[3] += 1
    return stats[1]*stats[3]

def get_num_adapter_combinations(sorted_adapters: List[int], window_size: int) -> int:    
    adapters = [0]
    adapters.extend(sorted_adapters)

    num_adapters = len(adapters)
    paths = [0] * num_adapters
    paths[0] = 1

    for idx in range(1, num_adapters):
        neighbour_idx = idx - 1
        while neighbour_idx >= 0 and adapters[idx] - adapters[neighbour_idx] <= window_size:
            paths[idx] += paths[neighbour_idx]
            neighbour_idx -= 1
    
    return paths[num_adapters - 1]

if __name__ == '__main__':
    filename = 'day10/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))

    sorted_adapters = sorted(data)
    print('The number of 1-jolt differences multiplied by the number of 3-jolt differences is {}'.format(adapter_array_stats(sorted_adapters)))
    print('The number different combinations is {}'.format(get_num_adapter_combinations(sorted_adapters, 3)))