def get_hikes(grid: list[list[int]], starts: list[tuple[int,int]], rating: bool) -> set:
    hikes = set()
    for start in starts:
        to_visit = [((start),)]

        while to_visit:
            path = to_visit.pop()
            r, c = path[-1]
            level = grid[r][c]
            if level == 9:
                if rating:
                    hikes.add(path)
                else:
                    hikes.add((start, path[-1]))
                continue

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == level + 1 and (nr, nc) not in path:
                    to_visit.append(path+((nr, nc),))
    return hikes

def get_grid_and_starts(lines: list[str]) -> tuple[list[list[int]], list[tuple[int,int]]]:
    grid = []
    starts = []
    for r, line in enumerate(lines):
        grid.append([])
        for c, char in enumerate(line):
            grid[r].append(int(char))
            if char == '0':
                starts.append((r, c))
    return grid, starts

def handle_part_1(lines: list[str]) -> int:
    grid, starts = get_grid_and_starts(lines)
    return len(get_hikes(grid, starts, False))


def handle_part_2(lines: list[str]) -> int:
    grid, starts = get_grid_and_starts(lines)
    return len(get_hikes(grid, starts, True))
