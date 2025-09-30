n_dirs = {
    (-1, 0): {  "left": (0, -1), "right": (0, 1), "reverse": (1, 0) },  # up
    (1, 0): {   "left": (0, 1),  "right": (0, -1), "reverse": (-1, 0) }, # down
    (0, -1): {  "left": (1, 0),  "right": (-1, 0), "reverse": (0, 1) }, # left
    (0, 1): {   "left": (-1, 0), "right": (1, 0), "reverse": (0, -1) }   # right
}

def handle_part_1(lines: list[str]) -> int:
    pos = (len(lines) // 2, len(lines[0]) // 2)
    direction = (-1, 0) # up

    infected = {(r,c) for r, row in enumerate(lines) for c, val in enumerate(row) if val == '#'}

    nb_infections = 0
    for _ in range(10000):
        if pos in infected:
            direction = n_dirs[direction]["right"]
            infected.remove(pos)
        else:
            direction = n_dirs[direction]["left"]
            infected.add(pos)
            nb_infections += 1
        pos = (pos[0] + direction[0], pos[1] + direction[1])

    return nb_infections


def handle_part_2(lines: list[str]) -> int:
    pos = (len(lines) // 2, len(lines[0]) // 2)
    direction = (-1, 0) # up

    weakened = set()
    infected = {(r,c) for r, row in enumerate(lines) for c, val in enumerate(row) if val == '#'}
    flagged = set()

    nb_infections = 0
    for _ in range(10000000):
        if pos in infected:
            direction = n_dirs[direction]["right"]
            infected.remove(pos)
            flagged.add(pos)
        elif pos in weakened:
            weakened.remove(pos)
            infected.add(pos)
            nb_infections += 1
        elif pos in flagged:
            direction = n_dirs[direction]["reverse"]
            flagged.remove(pos)
        else: # clean
            direction = n_dirs[direction]["left"]
            weakened.add(pos)
        pos = (pos[0] + direction[0], pos[1] + direction[1])

    return nb_infections
