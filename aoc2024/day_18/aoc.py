from python.libraries.array import dist


def get_min_cost(
    size: int,
    obstacles: set[tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[int, dict[tuple[int, int], tuple[int, int]]]:
    open = {(start)}
    g_score = {(r, c): size**4 for r in range(size) for c in range(size)}
    g_score[start] = 0

    f_score = {(r, c): size**4 for r in range(size) for c in range(size)}
    f_score[start] = dist(start, end)
    came_from = {}

    while open:
        current = sorted(open, key=lambda x: f_score[x])[0]
        if current == end:
            return g_score[end], came_from

        open.remove(current)
        r, c = current
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            neighbor = (nr, nc)

            if neighbor in obstacles:
                continue
            if not (0 <= nr < size and 0 <= nc < size):
                continue

            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + dist(neighbor, end)
                if neighbor not in open:
                    open.add(neighbor)

    raise Exception("Not found")


def get_path(
    came_from: dict[tuple[int, int], tuple[int, int]], end: tuple[int, int]
) -> set[tuple[int, int]]:
    path = set()
    current = end
    while current in came_from:
        path.add(current)
        current = came_from[current]
    return path


def handle_part_1(lines: list[str]) -> int:
    size, nb = list(map(int, lines[0].split(",")))

    bytes = set(
        [
            (int(line.split(",")[1]), int(line.split(",")[0]))
            for line in lines[1 : 1 + nb]
        ]
    )

    return get_min_cost(size, bytes, (0, 0), (size - 1, size - 1))[0]


def handle_part_2(lines: list[str]) -> str:
    size, nb = list(map(int, lines[0].split(",")))

    bytes = set(
        [
            (int(line.split(",")[1]), int(line.split(",")[0]))
            for line in lines[1 : 1 + nb]
        ]
    )
    start, end = (0, 0), (size - 1, size - 1)

    _, came_from = get_min_cost(size, bytes, start, end)
    path = get_path(came_from, end)
    for line in lines[nb + 1 :]:
        byte = (int(line.split(",")[1]), int(line.split(",")[0]))
        bytes.add(byte)

        if byte not in path:
            continue
        try:
            _, came_from = get_min_cost(size, bytes, start, end)
            path = get_path(came_from, end)
        except Exception:
            return f"{byte[1]},{byte[0]}"

    raise Exception("All bytes are ok")
