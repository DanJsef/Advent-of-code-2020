input_file = open('input.txt', 'r')
lines = input_file.readlines()

# NOTE: First problem solution
# def pass_validation(lines):
#     count = 0

#     for line in lines:
#         data = line.split(' ')
#         occurrence = data[2].count(data[1][0])
#         params = data[0].split('-')
#         if int(params[0]) <= int(occurrence) <= int(params[1]):
#             count += 1

#     return count


def pass_validation(lines):
    count = 0

    for line in lines:
        data = line.split(' ')
        params = data[0].split('-')
        pos1 = position_valid(int(params[0])-1, data[2], data[1][0])
        pos2 = position_valid(int(params[1])-1, data[2], data[1][0])
        if (pos1 == True or pos2 == True) and (pos1 == None or pos2 == None):
            count += 1

    return count


def position_valid(position, word, value):
    if word[position] == value:
        return True


print(pass_validation(lines))
