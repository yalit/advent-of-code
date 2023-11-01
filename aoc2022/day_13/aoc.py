import functools
import json
from functools import reduce


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return right - left

    left = [left] if isinstance(left, int) else left
    right = [right] if isinstance(right, int) else right

    ordered = reduce(lambda t, i: compare(left[i], right[i]) if t == 0 else t, range(min(len(left), len(right))), 0)

    return ordered if ordered != 0 else len(right) - len(left)


def handle_part_1(lines: list[str]) -> int:
    lines = '\n'.join(lines)
    return reduce(lambda t, pair:  t + pair[0] if compare(*pair[1]) >= 0 else t, [(k + 1, list(map(json.loads, pairs.split('\n')))) for k, pairs in enumerate(lines.split('\n\n'))], 0)


def handle_part_2(lines: list[str]) -> int:
    lines.append("[[2]]")
    lines.append("[[6]]")
    s = sorted(list(map(json.loads, filter(lambda a: a != '', lines))), key=functools.cmp_to_key(compare), reverse=True)
    return (s.index([[2]]) + 1) * (s.index([[6]]) + 1)
