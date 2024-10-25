from typing import List

from python.libraries.array import visualize_grid_dict
from python.libraries.intCode.intCodeComputer import IntCodeComputer

directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

def get_grid(computer: IntCodeComputer) -> dict:
    i = 0
    while not computer.end:
        computer.execute()
    scaffolds_input = computer.outputs
    grid = {}

    x = 0
    y = 0
    i = 0
    while i < len(scaffolds_input):
        if scaffolds_input[i] == 10:
            x = 0
            y += 1
        else:
            grid[(x, y)] = chr(scaffolds_input[i])
            x += 1
        i += 1
    return grid

def handle_part_1(lines: list[str]) -> int:
    computer = IntCodeComputer(list(map(int, lines[0].split(','))))
    grid = get_grid(computer)

    alignment_sum = 0
    for x,y in grid:
        if grid[(x,y)] != '#':
            continue

        if all([(x + dx, y + dy) in grid and grid[(x+dx, y+dy)] == '#' for dx, dy in directions.values()]):
            alignment_sum += x * y

    return alignment_sum


def handle_part_2(lines: list[str]) -> int:
    inp = list(map(int, lines[0].split(',')))
    inp[0] = 2

    def get_input(s: str) -> List[int]:
        return [ord(c) for c in s] + [10]

    # found the program manually
    # program = "L12,L12,L6,L6,R8,R4,L12,L12,L12,L6,L6,L12,L6,R12,R8,R8,R4,L12,L12,L12,L6,L6,L12,L6,R12,R8,R8,R4,L12,L12,L12,L6,L6,L12,L6,R12,R8"
    program = "A,B,A,C,B,A,C,B,A,C"
    a = "L,12,L,12,L,6,L,6"
    b = "R,8,R,4,L,12"
    c = "L,12,L,6,R,12,R,8"
    video = "n"

    inputs = get_input(program) + get_input(a) + get_input(b) + get_input(c) + get_input(video)
    print(f"Lengths: {len(get_input(program))}, {len(get_input(a))}, {len(get_input(b))}, {len(get_input(c))}, {len(get_input(video))}")

    computer = IntCodeComputer(inp,inputs)
    visualize_grid_dict(get_grid(computer))
    return computer.outputs[-1]
