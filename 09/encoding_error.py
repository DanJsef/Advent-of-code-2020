def find_bug(i, preamble_length, data):
    while i < len(data):
        possible = False
        hash_table = set()
        for n in range(1, preamble_length + 1):
            complement = data[i] - data[i-n]
            if complement in hash_table:
                possible = True
                break
            hash_table.add(data[i-n])
        if possible == False:
            return data[i]
        i += 1


def hack_bug(hack_sum, data):
    win_len = 2
    i = 2
    current_sum = sum(data[:win_len])
    while current_sum != hack_sum:
        if i == len(data) - win_len:
            i = win_len + 1
            win_len += 1
            current_sum = sum(data[:win_len])
        current_sum = current_sum + data[i] - data[i - win_len]
        i += 1
    hack_range = set(data[i-win_len:i])
    return min(hack_range) + max(hack_range)


data = [int(item) for item in open('input.txt', 'r').readlines()]

bug = find_bug(25, 25, data)

print(bug, hack_bug(bug, data))
