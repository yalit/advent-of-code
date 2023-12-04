import re
from functools import reduce

def handle_part_1(lines: list[str]) -> int:
    s = 0
    for line in lines:
        cards = line.split(": ")[1].split(" | ")
        good = [int(x) for x in re.findall(r'(\d+)',cards[0])]
        tomatch = [int(n) for n in re.findall(r'(\d+)',cards[1])]
        st = 0
        n = 0
        for m in tomatch:
            if m in good:
                st = st + 1 if n == 0 else st * 2
                n += 1
        s += st

    return s


def handle_part_2(lines: list[str]) -> int:
    cardNumbers = [1 for _ in lines]

    for i, line in enumerate(lines):
        cards = line.split(": ")[1].split(" | ")
        good = [int(x) for x in re.findall(r'(\d+)',cards[0])]
        tomatch = [int(n) for n in re.findall(r'(\d+)',cards[1])]
        n = 0
        for m in tomatch:
            if m in good:
                n += 1
                
        if n > 0:
            for a in range(1,n + 1):
                cardNumbers[i+a] = cardNumbers[i+a] + cardNumbers[i]

    return sum(cardNumbers)
