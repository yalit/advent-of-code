from python.libraries.intCode.intCodeComputer import IntCodeComputer


def handle_part_1(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))
    runner = IntCodeComputer(program)
    return runner.execute()[-1]


def handle_part_2(lines: list[str]) -> int:
    return handle_part_1(lines)
