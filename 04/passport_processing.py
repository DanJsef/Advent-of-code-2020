import re

data = open('input.txt', 'r').read().split('\n\n')
patterns = {'byr:(19[2-9][0-9]|200[0-2])',
            'iyr:(201[0-9]|2020)',
            'eyr:(202[0-9]|2030)',
            'hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)',
            'hcl:#([0-9]|[a-f]){6}([ |\n]|$)',
            'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
            'pid:[0-9]{9}([ |\n]|$)'}


def validate_passport(data, patterns):
    count = 0
    for passport in data:
        for i, pattern in enumerate(patterns):
            validity = re.search(pattern, passport)
            if validity == None:
                break
            elif i == len(patterns) - 1:
                count += 1
    return count


print(validate_passport(data, patterns))
