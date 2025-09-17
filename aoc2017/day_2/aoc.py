def handle_part_1(lines: list[str]) -> int:
    sum = 0

    for l in lines:
        n = [int(a) for a in l.split()]
        sum+= max(n) - min(n)

    return sum


def handle_part_2(lines: list[str]) -> int:
    sum = 0

    for l in lines:
        n = list(reversed(sorted([int(a) for a in l.split()])))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                if n[i]/n[j] == n[i]//n[j]:
                    sum += n[i]//n[j]

    return sum
