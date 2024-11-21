from collections import Counter


def maxCounter(c: dict[str, int]) -> str:
    m = 0
    letter = ""
    for k in c:
        if m < c[k]:
            letter = k
        m = max(m, c[k])
    return letter


def leastCounter(c: dict[str, int]) -> str:
    m = float("inf")
    letter = ""
    for k in c:
        if m > c[k]:
            letter = k
        m = min(m, c[k])
    return letter


def handle_part_1(lines: list[str]) -> str:
    words = [[line[i] for line in lines] for i in range(len(lines[0]))]

    return "".join([maxCounter(Counter(word)) for word in words])


def handle_part_2(lines: list[str]) -> str:
    words = [[line[i] for line in lines] for i in range(len(lines[0]))]

    return "".join([leastCounter(Counter(word)) for word in words])
