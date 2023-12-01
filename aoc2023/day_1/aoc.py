import re

def handle_part_1(lines: list[str]) -> int:
    cnt = 0

    for line in lines:
        reg_first = re.compile(r'(\d)')
        f = reg_first.findall(line)
        cnt += int(f[0] + f[-1])

    return cnt


def handle_part_2(lines: list[str]) -> int:
    cnt = 0

    number_as_string = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in lines:
        reg_first = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
        f = reg_first.findall(line)
        number = number_as_string[f[0]] if f[0] in number_as_string.keys() else f[0]
        number += number_as_string[f[-1]] if f[-1] in number_as_string.keys() else f[-1]

        cnt += int(number)

    return cnt
