from typing import List


def count_anyone_answered_yes(lines: List[str]) -> int:
    counts = []
    current_questions = set()
    for line in lines:
        if line == '\n':
            counts.append(len(current_questions))
            current_questions = set()
        else:
            line = line.strip('\n')
            current_questions.update(set(line))
    # last set of questions
    counts.append(len(current_questions))
    return sum(counts)

def count_everyone_answered_yes(lines: List[str]) -> int:
    counts = []
    current_questions = set()
    is_first_person = True
    for line in lines:
        if line == '\n':
            counts.append(len(current_questions))
            current_questions = set()
            is_first_person = True
        else:
            line = line.strip('\n')
            answers = set(line)
            if is_first_person:
                current_questions = answers
                is_first_person = False
            else:
                current_questions = current_questions.intersection(answers)
    # last set of questions
    counts.append(len(current_questions))
    return sum(counts)

if __name__ == '__main__':
    counts = []
    with open('day06/input.txt') as f:
        lines = f.readlines()
    
    print('Anyone: Sum of the counts is {}'.format(count_anyone_answered_yes(lines)))
    print('Everyone: Sum of the counts is {}'.format(count_everyone_answered_yes(lines)))
