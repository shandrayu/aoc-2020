from collections import namedtuple


Rule = namedtuple('Rule', 'symbol lowest highest')

def validate_password(password: str, rule: Rule) -> bool:
    num_symbols = password.count(rule.symbol)
    return num_symbols >= rule.lowest and num_symbols <= rule.highest

def validate_password_updated(password: str, rule: Rule) -> bool:
    return (password[rule.lowest-1] == rule.symbol) ^ (password[rule.highest-1] == rule.symbol)

def parse_input(line: str) -> (str, Rule):
    limits, symbol, password = line.split(' ')
    lowest, highest  = [int(n) for n in limits.split('-')]
    symbol = symbol[0]
    rule = Rule(symbol, lowest, highest)
    return password, rule

if __name__ == '__main__':
    password_is_valid = []
    password_is_valid_updated = []
    with open('day02/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            password, rule = parse_input(line)
            password_is_valid.append(validate_password(password, rule))
            password_is_valid_updated.append(validate_password_updated(password, rule))
    
    print("First policy: Input data contains {} valid passwords".format(sum(password_is_valid)))
    print("Second policy: Input data contains {} valid passwords".format(sum(password_is_valid_updated)))
