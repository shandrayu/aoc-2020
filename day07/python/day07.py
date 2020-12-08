from collections import deque  

def parse_rule(rule_str: str) -> (str, dict):
    rule_str = rule_str.strip('\n')
    rule_str = rule_str.strip('.')
    bag_name, bags_inside_str = rule_str.split(' contain ')
    bag_name = bag_name.replace(' bags', '')
    bags_inside_str = bags_inside_str.split(', ')
    bags_inside = {}

    if bags_inside_str[0] == 'no other bags':
        return bag_name, bags_inside

    for bag in bags_inside_str:
        quantity, name = bag.split(' ', 1)
        quantity = int(quantity)
        # Skip quantity for now, is does not matter for the first part
        bag_str = ' bag' if quantity == 1 else ' bags'
        name = name.replace(bag_str, '')
        bags_inside[name] = quantity
    return bag_name, bags_inside

def count_possible_colors(color: str, rules: dict) -> int:
    count = 0
    queue = deque([color])
    counted_colors = set()
    # Will work if there no recursion in bags :)
    while queue:
        current_color = queue.popleft()
        for color, bags_inside in rules.items():
            if current_color in bags_inside and color not in counted_colors:
                count += 1
                queue.append(color)
                counted_colors.add(color)
    return count

def count_bags_inside(color: str, rules: dict) -> int:
    count = 0
    for bag_color, quantity in rules[color].items():
        count += quantity + quantity * count_bags_inside(bag_color, rules)
    return count

if __name__ == '__main__':
    rules = {}
    with open('day07/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            bag_name, bags_inside = parse_rule(line)
            rules[bag_name] = bags_inside
    COLOR = 'shiny gold'
    print('Amount of bag colors that can contain {} bag is {}'.format(COLOR, count_possible_colors(COLOR, rules)))
    print('{} bag shall contain {} other bags'.format(COLOR, count_bags_inside(COLOR, rules)))
