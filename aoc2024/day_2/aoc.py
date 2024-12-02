def is_safe(line):
    deltas = [a-b for a,b in zip(line, line[1:])]
    return (
        min(list(map(abs, deltas))) >= 1
        and max(list(map(abs, deltas))) <= 3
        and (all(x > 0 for x in deltas) or all(x < 0 for x in deltas))
    )


def handle_part_1(lines: list[str]) -> int:
    safe = 0

    for line in lines:
        ns = list(map(int, line.split()))
        safe += 1 if is_safe(ns) else 0
    return safe


def handle_part_2(lines: list[str]) -> int:
    safe = 0

    for line in lines:
        ns = list(map(int, line.split()))
        if any(is_safe(ns[:i]+ns[i+1:]) for i in range(len(ns))):
            safe += 1

    return safe
