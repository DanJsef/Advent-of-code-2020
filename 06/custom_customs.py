data = open('input.txt', 'r').read().split('\n\n')


def count(data):
    count = 0
    for group in data:
        answers = {}
        group = group.split('\n')
        for person in group:
            if answers == {}:
                answers = set(person)
            else:
                # NOTE: change intersection to union for first problem
                answers = answers.intersection(set(person))
        count += len(answers)
    return count


print(count(data))
