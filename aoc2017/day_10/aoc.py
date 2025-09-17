from functools import reduce

def handle_part_1(lines: list[str]) -> int:
    lengths = list(map(int, lines[0].split(',')))
    l = list(range(5 if len(lengths) == 4 else 256)) # 4 for test purposes
    l, _, _ = knot(l, lengths)
    return l[0] * l[1]

def handle_part_2(lines: list[str]) -> str:
    lengths = list(lines[0].encode('utf-8')) + [17, 31, 73, 47, 23]
    pos,skip = 0, 0

    l = list(range(256))
    for _ in range(64):
        l, pos, skip = knot(l, lengths, pos, skip)

    hash = ""
    for i in range(16):
        sparse = l[16*i:16*(i+1)]
        dense = reduce(lambda h,x: h^x, sparse)
        hash += hex(dense)[2:].zfill(2)

    return hash


def knot(l, lengths, pos = 0, skip = 0) -> tuple[list[int], int, int]:
    for n in lengths:
        chunk = []
        if pos + n <= len(l):
            chunk = l[pos:pos+n]
        else: # near the end and need to circular bound
            end = len(l) - pos
            start = n-end
            chunk = l[pos:] + l[0:start]

        for i, x in enumerate(reversed(chunk)):
            l[(pos+i)%len(l)] = x

        pos = (pos + n + skip) % len(l)
        skip += 1

    return l, pos, skip