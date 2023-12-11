from python.libraries.array import inbound

connections = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, 1), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(0, -1), (-1, 0)],
}


def handle_part_1(lines: list[str]) -> int:
    s = get_s(lines)
    st = get_shape_of_s(lines, s)
    lines = [list(l) for l in lines]
    lines[s[0]][s[1]] = st

    loop = get_loop(lines, s, st)
    return int(len(loop) / 2)


def handle_part_2(lines: list[str]) -> int:
    s = get_s(lines)
    st = get_shape_of_s(lines, s)
    lines = [list(l) for l in lines]
    lines[s[0]][s[1]] = st

    h = len(lines)
    w = len(lines[0])

    loop = get_loop(lines, s, st)
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if (r, c) in loop:
                continue

            lines[r][c] = '.'

    inside = set()
    cross_match = {'L': 'J', 'F': '7'}

    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if (r, c) in loop:
                continue

            if r == 0 or c == 0 or r == h - 1 or c == w - 1:
                continue

            crossings = 0
            non_pipe = ''
            for x in row[c + 1:]:
                if x == '-' or x == '.':
                    continue
                if x == '|':
                    crossings += 1
                    continue

                if non_pipe == '':
                    if x not in cross_match.keys():
                        crossings += 1
                        continue
                    non_pipe = x
                    continue

                if x != cross_match[non_pipe]:
                    crossings += 1
                non_pipe = ''

            if crossings % 2 == 1:
                inside.add((r, c))

    visualize(lines, inside, loop)

    return len(inside)


def get_s(lines):
    # find S
    s = (0, 0)
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == 'S':
                s = (r, c)
                break
    return s


def get_shape_of_s(lines, s):
    # Find shape of S
    st = ''
    for tube in connections.keys():
        n = 0
        for dr, dc in connections[tube]:
            c_r, c_c = (s[0] + dr, s[1] + dc)
            if not inbound(c_r, c_c, len(lines), len(lines[0])):
                continue
            connect = lines[c_r][c_c]
            if connect != '.' and (-1 * dr, -1 * dc) in connections[connect]:
                n += 1
        if n == 2:
            st = tube
            break
    return st


def get_loop(lines, start, start_shape):
    visited = set()
    to_visit = [start]
    while len(to_visit) > 0:
        nexts = []
        for r, c in to_visit:
            visited.add((r, c))
            for dr, dc in connections[lines[r][c]]:
                if not (r + dr, c + dc) in visited:
                    nexts.append((r + dr, c + dc))

        to_visit = nexts

    return visited

def visualize(lines, inside, loop):
    m = {
        '|': '┃',
        '-': '━',
        '7': '┓',
        'F': '┏',
        'L': '┗',
        'J': '┛',
    }
    for r, row, in enumerate(lines):
        for c, col in enumerate(row):
            if (r, c) in inside:
                lines[r][c] = '\x1b[92m+\x1b[39m'
                continue
            if (r, c) in loop:
                lines[r][c] = m[col]
                continue
            lines[r][c] = '-'

    for row in lines:
        print("".join(row))
