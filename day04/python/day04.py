from typing import List

from passport_rules import passport_rules


def parse_input(filename: str) -> List[dict]:
    passports = []
    passport = {}
    with open(filename) as file:
        for line in file:
            if line == '\n':
                passports.append(passport)
                passport = {}
            else:
                line = line.rstrip('\n')
                fields = line.split(' ')
                for field in fields:
                    key, value = field.split(':')
                    passport[key] = value
    
    passports.append(passport)
    return passports

def is_valid(passport: dict) -> bool:
    valid = True
    for key, validation_function in passport_rules.items():
        if not (key in passport.keys() and validation_function(passport[key])):
            valid = False
            break
    return valid

if __name__ == '__main__':
    passports = parse_input('day04/input.txt')
    all = list(map(is_valid, passports))
    print(sum(map(is_valid, passports)))