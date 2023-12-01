from python.libraries.intCode.intCodeRunner import IntCodeRunner
from itertools import permutations

def handle_part_1(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))

    runner = IntCodeRunner(program)

    max_signal = 0
    for a in permutations(range(5)):
        output = 0
        for inp in a:
            output = runner.execute(program_inputs=[inp, output])

        max_signal = max(max_signal, output)

    return max_signal


def handle_part_2(lines: list[str]) -> int:
    return 0
