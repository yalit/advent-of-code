def is_safe(deltas):
    return (
        min(list(map(abs, deltas))) >= 1
        and max(list(map(abs, deltas))) <= 3
        and (all(x > 0 for x in deltas) or all(x < 0 for x in deltas))
    )


def handle_part_1(lines: list[str]) -> int:
    safe = 0

    for line in lines:
        ns = list(map(int, line.split()))
        deltas = [a - b for a, b in zip(ns[:-1], ns[1:])]
        safe += 1 if is_safe(deltas) else 0
    return safe


def handle_part_2(lines: list[str]) -> int:
    safe = 0

    for line in lines:
        ns = list(map(int, line.split()))
        deltas = [a - b for a, b in zip(ns[:-1], ns[1:])]
        if is_safe(deltas):
            safe += 1
            continue
        for i in range(len(ns)):
            t_ns = ns[:i] + ns[i + 1 :]
            deltas = [a - b for a, b in zip(t_ns[:-1], t_ns[1:])]
            if is_safe(deltas):
                safe += 1
                break

    return safe
