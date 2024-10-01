from python.libraries.intCode.intCodeRunner import IntCodeRunner


def handle_part_1(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))
    print(program)
    runner = IntCodeRunner(program)

    return runner.execute(program_inputs=[1])


def handle_part_2(lines: list[str]) -> int:
    program = list(map(int, lines[0].split(',')))

    runner = IntCodeRunner(program)

    return runner.execute(program_inputs=[5])
