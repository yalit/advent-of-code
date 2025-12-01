def handle_part_1(lines: list[str]) -> int:
    p = 50

    total = 0
    for line in lines:
        d = line[0]
        n = int(line[1:]) if d == 'R' else -1 * int(line[1:])

        p = (p+n) % 100

        print(d, n, p)
        if p == 0:
            total += 1

    return total


def handle_part_2(lines: list[str]) -> int:
    p = 50

    total = 0
    for line in lines:
        d = line[0]
        n = int(line[1:])

        if d == 'L':
            if n >= p:
                print(d, n, p)
                print(total, "before")
                total += (1 if p > 0 else 0 ) + (1 * (n-p) // 100)
                print(total, "after")
            p = (p-n) % 100

        elif d == 'R':
            if n >= 100 - p:
                print(d, n, p)
                total += 1 + (1 * (n - 100 + p) // 100) 
            p = (p+n) % 100


    return total

