from typing import List


def get_closest_bus(bus_ids: List[int], target_time: int) -> (int, int):
    times = [id - target_time % id for id in bus_ids]
    waiting_time = min(times)
    bus_id = bus_ids[times.index(waiting_time)]
    return bus_id, waiting_time


def parse_bus_ids(line: str) -> List[int]:
    bus_ids = line.strip('\n')
    bus_ids = bus_ids.split(',')
    bus_ids = [int(s) for s in bus_ids if s != 'x']
    return bus_ids


if __name__ == '__main__':
    filename = 'day13/input.txt'
    with open(filename) as f:
        lines = f.readlines()
        earliest_timestamp = int(lines[0])
        bus_ids = parse_bus_ids(lines[1])

    bus_id, waiting_time = get_closest_bus(bus_ids, earliest_timestamp)
    print('The earliest bus you can take to the airport is {}'.format(bus_id))
    print('The number of minutes you\'ll need to wait for that bus is {}'.format(
        waiting_time))
    print('Multiplication {}'.format(bus_id * waiting_time))
