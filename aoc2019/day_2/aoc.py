from aoc2019.intCode.intCodeComputer import IntCodeComputer


def handle_part_1(lines: list[str]) -> int:
    positions = list(map(int, lines[0].split(',')))

    computer = IntCodeComputer(positions)
    return computer.execute(12,2)


def handle_part_2(lines: list[str]) -> int:
    positions = list(map(int, lines[0].split(',')))
    target = 19690720

    computer = IntCodeComputer(positions)

    upper = 100 #if 100 > len(positions) else len(positions) - 1
    for noun in range(upper):
        for verb in range(upper):
            res = computer.execute(noun, verb)
            if res == target:
                return (100 * noun) + verb


    return 0
