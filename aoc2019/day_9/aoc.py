from python.libraries.intCode.intCodeComputer import IntCodeComputer

def handle_part_1(lines: list[str]) -> int:
    computer = IntCodeComputer(list(map(int, lines[0].split(','))))
    return computer.execute()[-1]
    

def handle_part_2(lines: list[str]) -> int:
    return handle_part_1(lines)
