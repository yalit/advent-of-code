from python.libraries.array import inbound

# direction 0 equals going right, and + 90 turning clockwise (down, left, up)
change_of_dir = {
    '/' : {0 : [-90], 90 : [90], 180: [-90], 270: [90]},
    '\\': {0 : [90], 90 : [-90], 180: [90], 270: [-90]},
    '.' : {0 : [0], 90 : [0], 180: [0], 270: [0]},
    '|' : {0 : [-90, 90], 90 : [0], 180: [-90, 90], 270: [0]},
    '-' : {0 : [0], 90 : [-90, 90], 180: [0], 270: [-90, 90]},
}

delta_move = {0: (0,1), 90: (1, 0), 180: (0,-1), 270:(-1,0)}

def handle_part_1(cavern: list[str]) -> int:
    return find_nb_energized(cavern, (0,0,0))


def handle_part_2(cavern: list[str]) -> int:
    top = [(0, c, 90) for c in range(len(cavern[0]))]
    bottom = [(len(cavern) - 1, c, 270) for c in range(len(cavern[0]))]
    left = [(r, 0, 0) for r in range(len(cavern))]
    right = [(r, len(cavern[0]) - 1, 180) for r in range(len(cavern))]

    m = 0
    for start in top + bottom + left + right:
        m = max(find_nb_energized(cavern, start), m)

    return m


# start in shape of (row, col, direction)
# direction  = 0 (right) / 90 (down) / 180 (left) / 270 / (up)
def find_nb_energized(cavern, start):
    beams_positions = [start]
    energized = set()
    h = len(cavern)
    w = len(cavern[0])

    while len(beams_positions) > 0:
        row, col, direction = beams_positions.pop()
        for rotation_direction in change_of_dir[cavern[row][col]][direction]:
            new_direction = (direction + rotation_direction) % 360
            n_row, n_col = row + delta_move[new_direction][0], col + delta_move[new_direction][1]
            if inbound(n_row, n_col, h, w) and (n_row, n_col, new_direction) not in energized:
                beams_positions.append((n_row, n_col, new_direction))
        energized.add((row, col, direction))

    return len(set([(r, c) for r, c, _ in energized]))