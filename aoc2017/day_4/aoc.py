from collections import Counter

def handle_part_1(lines: list[str]) -> int:
    s = 0
    for l in lines:
        c= Counter(l.split())
        if len(l.split()) == len(c):
            s+=1
    return s


def handle_part_2(lines: list[str]) -> int:
    s = 0
    for l in lines:
        words = l.split()
        c = set()
        for w in words:
            c.add("".join(sorted(w)))  
        if len(c) == len(words):
            s += 1
    return s
