import re
from functools import reduce

def handle_part_1(lines: list[str]) -> int:
    s = 0
    for line in lines:
        good = [int(x) for x in re.findall(r'(\d+)',line.split(": ")[1].split(" | ")[0])]
        tomatch = [int(n) for n in (re.findall(r'(\d+)',line.split(": ")[1].split(" | ")[1]))]
        st = 0
        n = 1
        for m in tomatch:
            if m in good:
                if n == 1:
                    st += 1
                if n > 1:
                    st *= 2
                n += 1
        s += st

    return s


def handle_part_2(lines: list[str]) -> int:
    cards = [1 for _ in lines]

    for i, line in enumerate(lines):
        good = [int(x) for x in re.findall(r'(\d+)',line.split(": ")[1].split(" | ")[0])]
        tomatch = [int(n) for n in (re.findall(r'(\d+)',line.split(": ")[1].split(" | ")[1]))]
        n = 0
        for m in tomatch:
            if m in good:
                n += 1
                
        if n > 0:
            for a in range(1,n + 1):
                cards[i+a] = cards[i+a] + cards[i]
        print(i+1, n, cards)
    print(cards)
    return sum(cards)
