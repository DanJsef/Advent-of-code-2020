def difference(data):
    diff = data[1] - data[0]
    i = 2
    diff_store = {
        1: 0,
        2: 0,
        3: 1
    }
    diff_store[diff] += 1
    diff_store[data[0]] += 1

    while i < len(data):
        diff = data[i] - (diff + data[i-2])
        i += 1
        diff_store[diff] += 1

    return diff_store[1] * diff_store[3]

# NOTE: Initially solved by backtracking and dividing branches. Came across this solution and had to try it.


def combinations(data):
    data.append(0)
    data.sort()
    summary = {data[-1]: 1}
    for item in reversed(data[:-1]):
        summary[item] = sum(summary.get(x, 0)
                            for x in [item+1, item+2, item+3])
    return summary[0]


data = [int(item) for item in open('input.txt', 'r').readlines()]
data.sort()

print(difference(data), combinations(data))
