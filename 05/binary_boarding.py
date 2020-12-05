data = open('input.txt', 'r').readlines()

transtable = {66: 49, 70: 48, 82: 49, 76: 48}


def translate(value, table=transtable):
    return value.strip('\n').translate(table)


def calc_id(value):
    return int(value, 2)


def get_ids(data):
    seat_ids = []
    for seat in data:
        seat_ids.append(calc_id(translate(seat)))
    seat_ids.sort()
    return seat_ids


def find_seat(seats):
    i = 0
    while (seats[i] + 1) == seats[i+1]:
        i += 1
    return seats[i] + 1


print(find_seat(get_ids(data)))
