from python.libraries.array import visualize
from python.libraries.intCode.intCodeComputer import IntCodeComputer

def handle_part_1(lines: list[str]) -> int:
    computer = IntCodeComputer(list(map(int,lines[0].split(","))))

    nb_blocks = 0
    grid = set()
    while not computer.end:
        computer.execute()
        computer.execute()
        x,y,tile = computer.execute()[-3:]
        if tile == 2:
            nb_blocks += 1
        grid.add((x,y,tile))

    min_x = min(x for x, y, t in grid)
    min_y = min(y for x, y, t in grid)
    max_x = max(x for x, y, t in grid)
    max_y = max(y for x, y, t in grid)

    display = [[" " for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    tiles = {0: " ", 1: "W", 2: "#", 3: "_", 4: "O"}
    for x,y,tile in grid:
        display[y - min_y][x - min_x] = tiles[tile]

    visualize(display)
    return nb_blocks


class OwnIntCodeComputer(IntCodeComputer):
    def input(self, addresses):
        if self.entry is not None:
            self.set_value(addresses[0], self.entry)
            self.entry = None
        else:
            return "Input"

def handle_part_2(lines: list[str]) -> int:
    code = list(map(int, lines[0].split(",")))
    code[0] = 2
    computer = OwnIntCodeComputer(code)

    ball = (-1, -1)
    paddle = (-1, -1)
    entry = None
    score = 0
    while not computer.end:
        output = computer.execute(entry)
        entry = None
        if output == "Input":
            if ball[0] < paddle[0]:
                entry = -1
            elif ball[0] > paddle[0]:
                entry = 1
            else:
                entry = 0
        if len(output) % 3 == 0:
            x, y, tile = output[-3:]
            if tile == 3:
                paddle = (x, y)
            elif tile == 4:
                ball = (x, y)

            if x == -1 and y == 0:
                score = tile

    return score
