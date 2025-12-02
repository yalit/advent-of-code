from collections import Counter

def handle_part_1(lines: list[str]) -> int:
    ranges = sorted([(int(r.split('-')[0]), int(r.split('-')[1])) for r in lines[0].split(',')])

    total = 0
    for s,e in ranges:
        for x in range(s, e+1):
            sx = str(x)
            l = len(sx)
            if l % 2 == 1:
                continue

            if sx[:l//2] == sx[l//2:]:
                total+=x

    return total

def handle_part_2(lines: list[str]) -> int:
    ranges = sorted([(int(r.split('-')[0]), int(r.split('-')[1])) for r in lines[0].split(',')])

    total = 0
    for s,e in ranges:
        for x in range(s, e+1):
            sx = str(x)
            l = len(sx)

            found = False
            for n in range(1, l//2+1):
                elems = [sx[i:i+n] for i in range(0, l, n)]
                if not found and all(x == elems[0] for x in elems):
                    total += x
                    found = True

    return total
