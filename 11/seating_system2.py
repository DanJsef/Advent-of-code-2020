from copy import deepcopy

data = open('dum.txt').read()


def parse(data):
    data = data.split('\n')
    for i, row in enumerate(data):
        data[i] = list(col for col in row)
    return data


layout_0 = parse(data)
# layout_1 = parse(data)
BORDERS = (len(layout_0[0]), len(layout_0[1]))
DIRECTIONS = 8
DIRECTIONS_X = (1, -1, 1, -1, 0, 1, 0, -1)
DIRECTIONS_Y = (1, -1, -1, 1, 1, 0, -1, 0)


def display_grid():
    for row in layout_0:
        print(row)
    print()


def transform():
    grid_0 = deepcopy(layout_0)
    for x in range(BORDERS[0]):
        for y in range(BORDERS[1]):
            if grid_0[x][y] == 'L':
                adj = True
                for n in range(DIRECTIONS):
                    a = x + DIRECTIONS_X[n]
                    b = y + DIRECTIONS_Y[n]
                    if a < (BORDERS[0]) and b < (BORDERS[1])
                            and a >= 0 and b >= 0:
                        item=grid_0[a][b]
                        if item == '#':
                            adj=not adj
                            break
                if adj:
                    layout_0[x][y]='#'
            elif grid_0[x][y] == '#':
                adj=0
                for n in range(DIRECTIONS):
                    a=x + DIRECTIONS_X[n]
                    b=y + DIRECTIONS_Y[n]
                    if a < (BORDERS[0]) and b < (BORDERS[1])
                            and a >= 0 and b >= 0:
                        item=grid_0[a][b]
                        if item == '#':
                            adj += 1
                if adj >= 4:
                    layout_0[x][y]='L'


i=0
while i < 6:
    transform()
    i += 1
    display_grid()







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
            print(row)
        print()

    def transform(self):
        grid_0 = deepcopy(self.layout_0)
        for x in range(self.BORDERS[0]):
            for y in range(self.BORDERS[1]):

                adj = 0
                for n in range(self.DIRECTIONS):
                    a = x + self.DIRECTIONS_X[n]
                    b = y + self.DIRECTIONS_Y[n]
                    if a < (self.BORDERS[0]) and b < (self.BORDERS[1]) \
                            and a >= 0 and b >= 0:

                        item = grid_0[a][b]

                        if grid_0[x][y] == 'L':
                            adj = True
                            if item == '#':
                                adj = not adj
                                break
                        elif grid_0[x][y] == '#':
                            if item == '#':
                                adj += 1
                            if adj >= 4:
                                self.layout_0[x][y] = 'L'
                if adj == True:
                    self.layout_0[x][y] = '#'

    def count(self):
        count = 0
        for row in self.layout_0:
            for col in row:
                if col == '#':
                    count += 1
        return count


m = Model(open('dum.txt').read())

i = 0
check = []
while m.layout_0 != check:
    check = deepcopy(m.layout_0)
    m.transform()
    i += 1
    # m.display_grid()

print(m.count())
