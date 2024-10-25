from math import ceil, lcm
from typing import List

from PIL.ImageChops import offset

base_pattern = [0, 1, 0, -1]

def handle_part_1(lines: list[str]) -> int:
    inp = list(map(int, lines[0]))

    phases = 0
    print(inp)
    while phases < 10:
        digit = 0
        new_inp = []
        while digit < len(inp):
            pattern = []
            for p in base_pattern:
                pattern += [p] * (digit + 1)
            pattern = pattern[1:] + pattern[:1]
            result = sum([inp[i] * pattern[i % len(pattern)] for i in range(len(inp))])
            new_inp.append(int(str(result)[-1]))
            digit +=1
        inp = new_inp
        print("".join(map(str, inp)))
        phases += 1

    return int("".join(map(str, inp[:8])))


def handle_part_2(lines: list[str]) -> int:
    inp = list(map(int, lines[0])) * 10000
    offset = int("".join(map(str, inp[:7])))
    phases = 0
    while phases < 100:
        new_inp = [inp[-1]]*len(inp)
        digit = len(inp) - 2
        while digit >= offset:
            new_inp[digit] = (inp[digit] + new_inp[digit + 1]) % 10
            digit -= 1

        phases += 1
        inp = new_inp

    return int("".join(map(str, inp[offset:offset+8])))


