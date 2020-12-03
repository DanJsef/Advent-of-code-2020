tree_map = list(item.replace('\n', '')
                for item in open('input.txt', 'r').readlines())


def calc_slopes(offset_down, offset_right, width=len(tree_map[0])):
    move_right = offset_right
    move_down = offset_down
    count = 0

    while move_down < len(tree_map):
        pos = tree_map[move_down][move_right % width]
        if pos == "#":
            count += 1
        move_right += offset_right
        move_down += offset_down

    return count


print(calc_slopes(1, 1) * calc_slopes(1, 3) *
      calc_slopes(1, 5) * calc_slopes(1, 7) * calc_slopes(2, 1))
