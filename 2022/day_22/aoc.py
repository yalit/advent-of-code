import re


def handle_part_1(lines: list[str]) -> int:
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
    x, y, sx, d = grid[0].index('.'), 0, 0, 'R'
    print('x', x, 'sx', sx, 'y', y, d)

    dir_moves = {'R': (1, 0), 'D': (0,1), 'L': (-1,0), 'T': (0,-1)}
    changeDir = {
        'R': {'R': 'D', 'D': 'L', 'L': 'T', 'T': 'R'},
        'L': {'R': 'T', 'D': 'R', 'L': 'D', 'T': 'L'}
    }

    for move in moves:
        if move in ['R', 'L']:
            d = changeDir[move][d]
            continue

        dx, dy = dir_moves[d]

        for s in range(1, move+1): # starts at 1 ends at move
            if dy == 0: # deplacement horizontal
                nsx = (sx + dx) % bounds[y][2]
                nx = nsx + bounds[y][0]
                if grid[y][nx] == '#':
                    break
                x, sx = nx, nsx
                continue

            else: # déplacement vertical
                ny = y + dy
                if ny < 0 or ny >= gh or grid[ny][x] == ' ':
                    fy = y - dy
                    while 0 <= fy < gh and grid[fy][x] != ' ':
                        fy -= dy
                    ny = fy + dy

                if grid[ny][x] == '#':
                    break
                y = ny
                sx = x - bounds[y][0]
                continue

    score = ['R', 'D', 'L', 'T']
    return (1000 * (y + 1)) + (4 * (x + 1)) + score.index(d)


def handle_part_2(lines: list[str]) -> int:
    return 0
