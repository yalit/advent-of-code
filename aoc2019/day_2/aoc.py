from python.libraries.intCode.intCodeComputer import IntCodeComputer


def handle_part_1(lines: list[str]) -> int:
    positions = list(map(int, lines[0].split(',')))

    positions[1] = 12
    positions[2] = 2
    computer = IntCodeComputer(positions)
    return computer.execute()


def handle_part_2(lines: list[str]) -> int:
    positions = list(map(int, lines[0].split(',')))
    target = 19690720

    upper = 100 #if 100 > len(positions) else len(positions) - 1
    for noun in range(upper):
        for verb in range(upper):
            positions[1] = noun
            positions[2] = verb
            computer = IntCodeComputer(positions)
            res = computer.execute()
            if res == target:
                return (100 * noun) + verb

    return 0
