def handle_part_1(lines: list[str]) -> int:
    return get_severity(lines, 0)

def handle_part_2(lines: list[str]) -> int:
    start = 0

    while get_severity(lines, start, True) > 0:
        start +=1
    
    return start


def get_severity(lines, start, caught_only = False):
    ranges = {int(l.split(": ")[0]): int(l.split(": ")[1]) for l in lines}
    size = max(ranges.keys())
    severity = 0

    for depth in range(size + 1):
        pico = depth + start
        if depth in ranges and pico % ((ranges[depth]-1)*2) == 0:
            severity += depth * ranges[depth] if not caught_only else 1

    return severity