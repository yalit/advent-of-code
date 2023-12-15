import functools
import re


def handle_part_1(lines: list[str]) -> int:
    return sum([hash_sequence(s) for s in lines[0].split(",")])


def handle_part_2(lines: list[str]) -> int:
    hashmap = {h:[] for h in range(256)}

    for step in lines[0].split(","):
        label, operation, lens = re.match(r'([a-zA-Z]+)([-=])([0-9]*)', step).groups()
        h = hash_sequence(label)

        idx = functools.reduce(lambda i, e : e[0] if i == -1 and e[1][0] == label else i, enumerate(hashmap[h]), -1)

        if operation == '-' and idx >= 0:
            hashmap[h].pop(idx)
        elif operation == '=':
            if idx >= 0:
                hashmap[h][idx] = (label, int(lens))
            else:
                hashmap[h].append((label, int(lens)))

    return sum([(idx_box + 1) * (idx + 1) * le for idx_box, box in hashmap.items() for idx, (la,le) in enumerate(box)])

def hash_sequence(s):
    return functools.reduce(lambda h,c: hash_character(c, h), list(s), 0)

def hash_character(c, v):
    return ((v + ord(c)) * 17) % 256