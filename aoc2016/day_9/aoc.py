def handle_part_1(lines: list[str]) -> int:
    seq = lines[0]

    size = 0
    i = 0
    while i < len(seq):
        if seq[i] == "(":
            next = seq.index(")", i)
            n, r = seq[i + 1 : next].split("x")
            t = int(n) * int(r)
            size += t
            i += next - i + int(n) + 1
        else:
            size += 1
            i += 1

    return size


def decompress(s: str) -> int:
    if "(" not in s:
        return len(s)

    i = s.index("(")
    next = s.index(")", i)
    n, r = list(map(int, s[i + 1 : next].split("x")))
    return (
        i + decompress(s[next + 1 : next + 1 + n] * r) + decompress(s[next + 1 + n :])
    )


def handle_part_2(lines: list[str]) -> int:
    seq = lines[0]

    size = 0
    i = 0
    while i < len(seq):
        if seq[i] == "(":
            next = seq.index(")", i)
            n, _ = list(map(int, seq[i + 1 : next].split("x")))
            s = decompress(seq[i : next + 1 + n])
            size += s
            i += next - i + n + 1
            continue

        size += 1
        i += 1

    return size
