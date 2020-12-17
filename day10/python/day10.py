from typing import List


def adapter_array_stats(adapters: List[int]) -> int:
    WINDOW_SIZE = 3
    stats = {}
    for i in range(1, WINDOW_SIZE + 1):
        stats[i] = 0
    
    sorted_adapters = sorted(adapters)
    previous_adapter = 0
    for adapter in sorted_adapters:
        difference = adapter - previous_adapter
        stats[difference] += 1
        previous_adapter = adapter

    # The last one
    stats[3] += 1
    return stats[1]*stats[3]

if __name__ == '__main__':
    filename = 'day10/input.txt'
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))

    print('The number of 1-jolt differences multiplied by the number of 3-jolt differences is {}'.format(adapter_array_stats(data)))