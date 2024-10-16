from typing import List, Tuple, Dict

from python.libraries.array import visualize
from python.libraries.intCode.intCodeComputer import IntCodeComputer

class EmergencyHullPaintingRobot:
    def __init__(self, lines: List[int]):
        self.computer = IntCodeComputer(lines)

    def paint(self, panels: Dict[Tuple[int, int], int]):
        if len(panels) == 0:
            panel = (0,0)
        else:
            panel = list(panels.keys())[0]

        direction = 0  # 0 = up, 1 = right ...
        while not self.computer.end:
            input = 0 if panel not in panels else panels[panel]
            color = self.computer.execute(input)[-1]
            turn = -1 if self.computer.execute()[-1] == 0 else 1
            if panel not in panels:
                panels[panel] = 0
            panels[panel] = color

            direction = (direction + turn) % 4
            move = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
            panel = (panel[0] + move[direction][0], panel[1] + move[direction][1])

        return panels

def handle_part_1(lines: list[str]) -> int:
    robot = EmergencyHullPaintingRobot(list(map(int, lines[0].split(','))))
    return len(robot.paint({}))

def handle_part_2(lines: list[str]) -> int:
    robot = EmergencyHullPaintingRobot(list(map(int, lines[0].split(','))))
    panels = robot.paint({(0,0): 1})

    min_x = min([p[0] for p in panels])
    min_y = min([p[1] for p in panels])
    max_x = max([p[0] for p in panels])
    max_y = max([p[1] for p in panels])

    grid = [[' ' for _ in range(max_x + 1 - min_x)] for _ in range(max_y + 1 - min_y)]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x+1):
            if (x,y) in panels:
                grid[y][x] = '#' if panels[(x,y)] == 1 else ' '

    visualize(grid)
    return len(panels)
