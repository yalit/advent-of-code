import functools

from python.libraries.array import transpose

def handle_part_1(lines: list[str]) -> int:
   return handle(lines, find_mirror)


def handle_part_2(lines: list[str]) -> int:
    return handle(lines, find_mirror_with_smudge)

def handle(lines, fn):
    lines = "//".join(lines)
    lines = lines.split("////")

    nb_rows = 0
    nb_cols = 0
    for i, m in enumerate(lines):
        r = fn(m.split("//"))
        c = fn(transpose(m.split("//")))

        nb_rows += r if r else 0
        nb_cols += c if c else 0

    return nb_cols + (100 * nb_rows)

def find_mirror(lines: list[str]):
    l = len(lines)
    for i in range(1, l):
        m = min(i, l-i)
        if list(reversed(lines[i-m:i])) == lines[i:i+m]:
            return i

def find_mirror_with_smudge(lines: list[str]):
    l = len(lines)
    for i in range(1, l):
        m = min(i, l-i)
        count_diff = 0
        for t, b in zip(list(reversed(lines[i-m:i])), lines[i:i+m]):
            count_diff += functools.reduce(lambda d, c: d + 1 if c[0] != c[1] else d, zip(t,b), 0)
            if count_diff > 1:
                break
        if count_diff == 1:
            return i