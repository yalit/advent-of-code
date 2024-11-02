from python.libraries.array import visualize_grid_dict
from python.libraries.intCode.intCodeComputer import IntCodeComputer

def handle_part_1(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(",")))
    computer = IntCodeComputer(program)
    affected = 0
    for x in range(50):
        for y in range(50):
            computer.reset()
            computer.set_inputs([x, y])
            affected += computer.execute()[-1]
    return affected


def handle_part_2(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(",")))
    computer = IntCodeComputer(program)
    grid = {}
    y_stop = {a: True for a in range(580)}
    max_x = {}

    # range found by iteration
    r = range(1100, 1500)
    for y in r:
        found_on_line = False
        for x in range(0,1500):
            computer.reset()
            computer.set_inputs([x, y])
            # if no beam found on previous line for x but already found in the column, skip
            if x in y_stop and y_stop[x]:
                continue

            value = computer.execute()[-1]
            if value:
                found_on_line = True
                y_stop[x] = False
            else:
                if found_on_line:
                    # if beam already found in the column, stop for the line
                    break
                if x in y_stop:
                    y_stop[x] = True
                    continue

            grid[(x, y)] = '#' if value else '.'
        max_x[y] = max([a for a,b in grid.keys() if b == y and grid[(a,b)] == '#'])
        min_x = min([a for a, b in grid.keys() if b == y and grid[(a, b)] == '#'])
        if y-99 in max_x and min_x == max_x[y-99] - 99:
            return min_x * 10000 + y - 99

    return 0
