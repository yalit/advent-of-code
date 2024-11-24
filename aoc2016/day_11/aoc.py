# Rules
# Elevator can only 1 or 2 elements + you
# Michrochip can't be left alone


from collections import deque


def key(d):
    return "-".join(list(map(lambda i: f"{i[0]}-{i[1]}", d.items())))


def displayState(s):
    for i in range(4, 0, -1):
        floor = getFullFloor(s, i)
        print(f"F{i}", *["{:<4}".format(k if k in floor else ".") for k in s.keys()])


def getFullFloor(state, floor: int):
    return [k for k in state if state[k] == floor]


def getFloor(state, floor: int):
    return [k for k in state if state[k] == floor if k != "E"]


def correctState(state) -> bool:
    minFloor = min([v for _, v in state.items()])
    maxFloor = max([v for _, v in state.items()])
    if not (1 <= minFloor <= maxFloor <= 4):
        return False

    for i in range(4):
        floor = getFloor(state, i)
        generators = [x for x in floor if x[-1] == "G"]
        microchips = [x for x in floor if x[-1] == "M"]
        # if no generators or no microchips, no problem
        if len(generators) == 0 or len(microchips) == 0:
            continue

        for m in microchips:
            if m[:2] + "G" not in generators:
                return False

    return True


def nextState(state, upOrDown: str, changed: list[str]):
    if upOrDown == "up":
        return dict(
            (k, v) if k not in changed else (k, v + 1) for k, v in state.items()
        )

    return dict((k, v) if k not in changed else (k, v - 1) for k, v in state.items())


def bfs(state):
    to_visit = deque([(0, state, [])])
    visited = set()

    while to_visit:
        moves, current_state, path = to_visit.popleft()

        k = key(current_state)
        if k in visited:
            continue

        if not correctState(current_state):
            continue

        if all([v == 4 for k, v in current_state.items() if k != "E"]):
            return moves

        floorLevel = current_state["E"]
        floor = getFloor(current_state, floorLevel)
        minFloor = min([v for _, v in current_state.items()])

        new_path = path + [current_state]
        for i, elem in enumerate(floor):
            for j, other_elem in enumerate(floor):
                if j <= i:
                    continue
                if (elem[-1] == "M" and other_elem != elem[:2] + "G") or (
                    other_elem[-1] == "M" and elem != other_elem[:2] + "G"
                ):
                    continue

                # append moves with 2 elements
                to_visit.append(
                    (
                        moves + 1,
                        nextState(current_state, "up", ["E", elem, other_elem]),
                        new_path,
                    )
                )

                if floorLevel > minFloor:
                    to_visit.append(
                        (
                            moves + 1,
                            nextState(
                                current_state,
                                "down",
                                ["E", elem, other_elem],
                            ),
                            new_path,
                        )
                    )

            # append moves with only one element
            to_visit.append(
                (moves + 1, nextState(current_state, "up", ["E", elem]), new_path)
            )
            if floorLevel > minFloor:
                to_visit.append(
                    (moves + 1, nextState(current_state, "down", ["E", elem]), new_path)
                )

        visited.add(k)
    return -1


def handle_part_1(lines: list[str]) -> int:
    state = {
        "E": 1,
        "PoG": 1,
        "PoM": 2,
        "ThG": 1,
        "ThM": 1,
        "PrG": 1,
        "PrM": 2,
        "RuG": 1,
        "RuM": 1,
        "CoG": 1,
        "CoM": 1,
    }

    test_state = {"E": 1, "HyG": 2, "HyM": 1, "LiG": 3, "LiM": 1}

    return bfs(state)


def handle_part_2(lines: list[str]) -> int:
    state = {
        "E": 1,
        "PoG": 1,
        "PoM": 2,
        "ThG": 1,
        "ThM": 1,
        "PrG": 1,
        "PrM": 2,
        "RuG": 1,
        "RuM": 1,
        "CoG": 1,
        "CoM": 1,
        "ElG": 1,
        "ElM": 1,
        "DiG": 1,
        "DiM": 1,
    }

    return bfs(state)
    return 0
