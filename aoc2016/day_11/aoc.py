# Rules
# Elevator can only 1 or 2 elements + you
# Microchip can't be left alone

from queue import PriorityQueue


def display_state(state):
    for i in range(4, 0, -1):
        d = [f"F{i}"]
        d.append("E" if state[0] == i else ".")
        for e, v in state[1]:
            d.append(e if v == i else ".")
        print(*["{:<3}".format(a) for a in d])


def display_path(came_from, final):
    path = [final]

    c = final
    while c in came_from:
        path.append(came_from[c])
        c = came_from[c]

    for i, s in enumerate(reversed(path)):
        print(f"---- Turn {i} ----")
        display_state(s)
        print("")


def correct_state(state) -> bool:
    minFloor = min([v for _, v in state[1]])
    maxFloor = max([v for _, v in state[1]])

    if not (1 <= minFloor <= maxFloor <= 4):
        return False

    for i in range(minFloor, maxFloor + 1):
        microchips = [x for x, v in state[1] if x[-1] == "M" and v == i]
        generators = [x for x, v in state[1] if x[-1] == "G" and v == i]

        if len(generators) == 0:
            continue

        for m in microchips:
            if m[:2] + "G" not in generators:
                return False

    return True


def next_state(state, upOrDown: str, changed: list[str]):
    floorLevel = state[0]

    if upOrDown == "up":
        return (
            floorLevel + 1,
            tuple(
                (
                    (e, f + 1) if f == floorLevel and e in changed else (e, f)
                    for e, f in state[1]
                )
            ),
        )

    return (
        floorLevel - 1,
        tuple(
            (
                (e, f - 1) if f == floorLevel and e in changed else (e, f)
                for e, f in state[1]
            )
        ),
    )


def heuristic(state):
    distances = {}
    for e, v in state[1]:
        if e[:2] not in distances:
            distances[e[:2]] = v
        else:
            distances[e[:2]] = abs(distances[e[:2]] - v)
    return sum([x for x in distances.values()]) + sum([4 - v for _, v in state[1]])


def is_goal(state):
    return all(v == 4 for _, v in state[1])


def get_neighbors(state):
    floorLevel = state[0]
    floor = [e for e in state[1] if e[1] == floorLevel]
    minFloor = min([v for _, v in state[1]])

    up = []
    down = []
    for i, e in enumerate(floor):
        for j, oe in enumerate(floor):
            if floorLevel < 4:
                if i < j:
                    n = next_state(state, "up", [e[0], oe[0]])
                    if correct_state(n):
                        up.append(n)

                if len(up) == 0:
                    n = next_state(state, "up", [e[0]])
                    if correct_state(n):
                        up.append(n)

            if floorLevel > minFloor:
                n = next_state(state, "down", [e[0]])
                if correct_state(n):
                    down.append(n)

                if len(down) == 0 and i < j:
                    n = next_state(state, "down", [e[0], oe[0]])
                    if correct_state(n):
                        down.append(n)

    return up + down


def a_star(start) -> int:
    open = PriorityQueue()
    open.put((heuristic(start), start))

    g_score = {}
    g_score[start] = 0
    f_score = {}
    f_score[start] = heuristic(start)
    came_from = {}

    while open.queue:
        current = open.get()[1]

        if is_goal(current):
            # display_path(came_from, current)
            return g_score[current]

        for n in get_neighbors(current):
            t_g_score = g_score[current] + 1
            if n not in g_score or t_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = t_g_score
                f_score[n] = t_g_score + heuristic(n)
                if len(list(filter(lambda e: e == n, open.queue))) == 0:
                    open.put((heuristic(n), n))

    return -1


def handle_part_1(lines: list[str]) -> int:
    state = (
        1,
        (
            ("ThM", 1),
            ("ThG", 1),
            ("RuM", 1),
            ("RuG", 1),
            ("CoM", 1),
            ("CoG", 1),
            ("PoM", 2),
            ("PoG", 1),
            ("PrM", 2),
            ("PrG", 1),
        ),
    )

    state_test = (1, (("HyG", 2), ("HyM", 1), ("LiG", 3), ("LiM", 1)))

    return a_star(state)


def handle_part_2(lines: list[str]) -> int:
    state = (
        1,
        (
            ("ThM", 1),
            ("ThG", 1),
            ("RuM", 1),
            ("RuG", 1),
            ("CoM", 1),
            ("CoG", 1),
            ("DiM", 1),
            ("DiG", 1),
            ("PoM", 2),
            ("PoG", 1),
            ("PrM", 2),
            ("PrG", 1),
            ("ElM", 1),
            ("ElG", 1),
        ),
    )

    return a_star(state)
