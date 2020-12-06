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


if __name__ == '__main__':
    counts = []
    with open('day06/input.txt') as f:
        lines = f.readlines()
    
    print('Sum of the counts is {}'.format(count_anyone_answered_yes(lines)))
