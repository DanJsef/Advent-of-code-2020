from copy import deepcopy


class Model():
    def __init__(self, data):
        self.layout_0 = self.parse(data)
        self.BORDERS = (len(self.layout_0), len(self.layout_0[0]))
        self.DIRECTIONS = 8
        self.DIRECTIONS_X = (1, -1, 1, -1, 0, 1, 0, -1)
        self.DIRECTIONS_Y = (1, -1, -1, 1, 1, 0, -1, 0)

    def parse(self, data):
        data = data.split('\n')
        for i, row in enumerate(data):
            data[i] = list(col for col in row)
        return data

    def display_grid(self):
        for row in self.layout_0:
            print(''.join(row))
        print()

    def transform(self):
        grid_0 = deepcopy(self.layout_0)
        for x in range(self.BORDERS[0]):
            for y in range(self.BORDERS[1]):
                if grid_0[x][y] == 'L':
                    adj = True
                    for n in range(self.DIRECTIONS):
                        a = x + self.DIRECTIONS_X[n]
                        b = y + self.DIRECTIONS_Y[n]
                        if a < (self.BORDERS[0]) and b < (self.BORDERS[1]) \
                                and a >= 0 and b >= 0:
                            item = grid_0[a][b]

                            while item == '.':
                                a = a + self.DIRECTIONS_X[n]
                                b = b + self.DIRECTIONS_Y[n]
                                if a < (self.BORDERS[0]) and b < (self.BORDERS[1]) \
                                        and a >= 0 and b >= 0:
                                    item = grid_0[a][b]
                                else:
                                    break

                            if item == '#':
                                adj = not adj
                                break
                    if adj:
                        self.layout_0[x][y] = '#'
                elif grid_0[x][y] == '#':
                    adj = 0
                    for n in range(self.DIRECTIONS):
                        a = x + self.DIRECTIONS_X[n]
                        b = y + self.DIRECTIONS_Y[n]
                        if a < (self.BORDERS[0]) and b < (self.BORDERS[1]) \
                                and a >= 0 and b >= 0:
                            item = grid_0[a][b]

                            while item == '.':
                                a = a + self.DIRECTIONS_X[n]
                                b = b + self.DIRECTIONS_Y[n]
                                if a < (self.BORDERS[0]) and b < (self.BORDERS[1]) \
                                        and a >= 0 and b >= 0:
                                    item = grid_0[a][b]
                                else:
                                    break

                            if item == '#':
                                adj += 1
                    if adj >= 5:
                        self.layout_0[x][y] = 'L'

    def count(self):
        count = 0
        for row in self.layout_0:
            for col in row:
                if col == '#':
                    count += 1
        return count


m = Model(open('input.txt').read())

i = 0
check = []
while m.layout_0 != check:
    check = deepcopy(m.layout_0)
    m.transform()
    i += 1
    # m.display_grid()

print(m.count())
