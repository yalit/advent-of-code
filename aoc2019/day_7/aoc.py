from itertools import permutations
from python.libraries.intCode.intCodeComputer import IntCodeComputer


def handle_part_1(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))

    max_signal = 0
    for a in permutations(range(5)):
        computers = [IntCodeComputer(program) for _ in range(5)]
        output = 0
        for i, inp in enumerate(a):
            computers[i].set_inputs([inp, output])
            output = computers[i].execute()[-1]

        max_signal = max(max_signal, output)

    return max_signal


def handle_part_2(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))

    max_signal = 0
    for a in permutations(range(5, 10)):
        computers = [IntCodeComputer(program) for _ in range(5)]
        output = 0
        # Set phase settings
        for i, inp in enumerate(a):
            computers[i].set_inputs([inp, output])
            output = computers[i].execute()[-1]
        while not computers[4].end:
            for i in range(5):
                computers[i].set_inputs([output])
                output = computers[i].execute()[-1]

        max_signal = max(max_signal, output)

    return max_signal
