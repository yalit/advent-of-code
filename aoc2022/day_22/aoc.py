import re

directions = ['R', 'D', 'L', 'T']
dir_moves = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'T': (0, -1)}
changeDir = {
    'R': {'R': 'D', 'D': 'L', 'L': 'T', 'T': 'R'},
    'L': {'R': 'T', 'D': 'R', 'L': 'D', 'T': 'L'}
}


def move(lines, wrapCallback):
    grid = lines[:-2]
    gw = max(map(len, grid))
    grid = [line.ljust(gw, ' ') for line in grid]
    gh = len(grid)
    # bounds for each line : start, end, length
    bounds = []
    for line in grid:
        f = [m for m in re.finditer(r'[\.#]', line)]
        bounds.append((f[0].start(), f[-1].start(), f[-1].start() - f[0].start() + 1))

    m_num = list(map(int, re.findall(r'\d+', lines[-1])))
    m_dir = re.findall(r'[RL]', lines[-1])
    moves = [i for z in zip(m_num, m_dir) for i in z]
    moves.append(m_num[-1])

    # x, y coordinate relative to the full length of the  grid
    # sx coordinate relative to the length of the shape for each line
    x, y, d = grid[0].index('.'), 0, 'R'
    print('x', x, 'y', y, d)

    for move in moves:
        if move in ['R', 'L']:
            d = changeDir[move][d]
            continue

        print(d, move)
        for s in range(1, move + 1):  # starts at 1 ends at move
            nx, ny, nd = wrapCallback(grid, gh, gw, x, y, d)

            try:
                if grid[ny][nx] == '#':
                    break
            except:
                print("Error", x, y, nx, ny, d)
                raise KeyError((nx, ny, nd))
            x, y, d = nx, ny, nd
            print(x, y, d)

    print(x, y)
    return (1000 * (y + 1)) + (4 * (x + 1)) + directions.index(d)


def handle_part_1(lines: list[str]) -> int:
    def wrapCallback(grid, gh, gw, x, y, direction):
        dx, dy = dir_moves[direction]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= gw or grid[y][nx] == ' ' or ny < 0 or ny >= gh or grid[ny][x] == ' ':
            fx, fy,  = x - dx, y - dy
            while 0 <= fx < gw and grid[y][fx] != ' ' and 0 <= fy < gh and grid[fy][x] != ' ':
                fx, fy = fx - dx, fy - dy
            nx, ny = fx + dx, fy + dy
        return nx, ny, direction

    return move(lines, wrapCallback)


def handle_part_2(lines: list[str]) -> int:

    def wrapCallbackTestInput(grid, gh, gw, x, y, direction):
        l = 4

        #       1
        #   1 2| |6
        # 3| | | |7
        #   4 5| | |6
        #       4 3

        # 1 top to 1 bottom
        if 2 * l <= x < 3 * l and y == 0 and direction == 'T':
            return (3 * l) - 1 - x, l, 'D'
        # 1 bottom to 1 top
        if x < l and y == l and direction == 'T':
            return (3 * l) - 1 - x, 0, 'D'
        # 2 top to bottom
        if x == 2 * l and y < l and direction == 'L':
            return y + l, l, 'D'
        # 2 bottom to 2 top
        if l <= x < 2 * l and y == l and direction == 'T':
            return 2 * l, x - l, 'R'
        # 3 top to 3 bottom:
        if x == 0 and l <= y < 2 * l and direction == 'L':
            return (5 * l) - 1 - y, gh - 1, 'T'
        # 3 bottom to 3 top
        if 3 * l <= x < gw and y == gh - 1 and direction == 'D':
            return 0, (5 * l) - 1 - x, 'R'
        # 4 top to 4 bottom
        if x < l and y == 2 * l - 1 and direction == 'D':
            return (3 * l) - 1 - x, gh - 1, 'T'
        # 4 bottom to 4 top
        if 2 * l <= x < 3 * l and y == gh - 1 and direction == 'D':
            return (3 * l) - 1 - x, 2 * l - 1, 'T'
        # 5 top to 5  bottom
        if l <= x < 2 * l and y == 2 * l - 1 and direction == 'D':
            return 2 * l, (4 * l) - 1 - x, 'R'
        # 5 bottom to 5 top
        if x == 2 * l and 2 * l <= y < gh and direction == 'L':
            return (4 * l) - 1 - x, 2 * l, 'T'
        # 6 top to 6 bottom
        if x == 3 * l - 1 and y < l and direction == 'R':
            return gw - 1, gh - 1 - y, 'L'
        # 6 bottom to 6 top
        if x == gw - 1 and 2 * l <= y < gh and direction == 'R':
            return 3 * l - 1, gh - 1 - y, 'R'
        # 7 top to 7 bottom
        if x == 3 * l - 1 and l <= y < 2 * l and direction == 'R':
            return (5 * l) - 1 - y, 2 * l, 'D'
        # 7 bottom to 7 top
        if 3 * l <= x < gw and y == 2 * l and direction == 'T':
            return 3 * l - 1, l + gw - 1 - x, 'L'

        dx, dy = dir_moves[direction]
        return x + dx, y + dy, direction

    def wrapCallBackFullInput(grid, gh, gw, x, y, direction):
        l = 50
        #     3 4
        #   1|_|_|7
        #   2|_|6
        # 1|_|_|7
        # 3|_|5
        #   4

        # 1 top to 1 bottom
        if x == l and y < l and direction == 'L':
            return 0, (3 * l) - 1 - y, 'R'
        # 1 bottom to 1 top
        if x == 0 and 2 * l <= y < 3 * l and direction == 'L':
            return l, (3 * l) - 1 - y, 'R'
        # 2 top to 2 bottom
        if x == l and l <= y < 2 * l and direction == 'L':
            return y - l, 2 * l, 'D'
        # 2 bottom to 2 top
        if x < l and y == 2 * l and direction == 'T':
            return l, l + x, 'R'
        # 3 top to 3 bottom
        if l <= x < 2 * l and y == 0 and direction == 'T':
            return 0, (2 * l) + x, 'R'
        # 3 bottom to 3 top
        if x == 0 and 3 * l <= y < gh and direction == 'L':
            return y - (2 * l), 0, 'D'
        # 4 top to 4 bottom
        if 2 * l <= x < gw and y == 0 and direction == 'T':
            return x - (2 * l), gh - 1, 'T'
        # 4 bottom to 4 top
        if x < l and y == gh - 1 and direction == 'D':
            return (2 * l) + x, 0, 'D'
        # 5 top to bottom
        if l <= x < 2 * l and y == (3 * l) - 1 and direction == 'D':
            return l - 1, x + (2 * l), 'L'
        # 5 bottom to 5 top
        if x == l - 1 and 3 * l <= y < gh and direction == 'R':
            return y - (2 * l), (3 * l) - 1, 'T'
        # 6 top to 6 bottom
        if 2 * l <= x < 3 * l and y == l - 1 and direction == 'D':
            return (2 * l) - 1, x - l, 'L'
        # 6 bottom to top
        if x == (2 * l) - 1 and l <= y < 2 * l and direction == 'R':
            return y + l, l - 1, 'T'
        # 7 top to bottom
        if x == gw - 1 and y < l and direction == 'R':
            return (2 * l) - 1, (3 * l) - 1 - y, 'L'
        # 7 bottom to top
        if x == (2 * l) - 1 and 2 * l <= y < 3 * l and direction == 'R':
            return gw - 1, (3 * l) - 1 - y, 'L'

        dx, dy = dir_moves[direction]
        return x + dx, y + dy, direction

    if len(lines) > 14: # full input
        return move(lines, wrapCallBackFullInput)
    return move(lines, wrapCallbackTestInput)
