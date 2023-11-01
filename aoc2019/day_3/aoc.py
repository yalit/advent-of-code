import re
def get_all_positions(movements: list[str]) -> set[complex]:
    pos = 0+0j
    positions = set()

    movement_regex = '([RULD])(\d+)'

    for move in movements:
        [(m, dist)] = re.findall(movement_regex, move)
        for a in range(int(dist)):
            match m:
                case 'R':
                    pos = pos + 1j
                case 'L':
                    pos = pos - 1j
                case 'U':
                    pos = pos + 1
                case 'D':
                    pos = pos - 1
            positions.add(pos)

    return positions

def get_all_positions_with_steps(movements: list[str]) -> list[tuple]:
    pos = (0,0,0)
    positions = []

    movement_regex = '([RULD])(\d+)'
    for move in movements:
        [(m, dist)] = re.findall(movement_regex, move)
        for a in range(int(dist)):
            match m:
                case 'R':
                    pos = (pos[0], pos[1] + 1)
                case 'L':
                    pos = (pos[0], pos[1] - 1)
                case 'U':
                    pos = (pos[0] + 1, pos[1])
                case 'D':
                    pos = (pos[0] - 1, pos[1])
            positions.append(pos)

    return positions

def handle_part_1(lines: list[str]) -> int:
    w1 = lines[0].split(',')
    w2 = lines[1].split(',')

    same= get_all_positions(w1).intersection(get_all_positions(w2))
    distances = [int(abs(x.real) + abs(x.imag)) for x in same]

    return min(distances)


def handle_part_2(lines: list[str]) -> int:
    w1 = lines[0].split(',')
    w2 = lines[1].split(',')

    pw1 = get_all_positions_with_steps(w1)
    pw2 = get_all_positions_with_steps(w2)

    same = set(pw1).intersection(set(pw2))

    return min([pw1.index(x) + pw2.index(x) + 2 for x in same])
