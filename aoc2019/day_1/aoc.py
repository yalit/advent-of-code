import math

def get_fuel(mass: int) -> int:
    return math.floor(mass / 3) - 2

def handle_part_1(lines: list[str]) -> int:
    required_fuel = 0
    for mass in lines:
        required_fuel += get_fuel(int(mass))
    return required_fuel


def handle_part_2(lines: list[str]) -> int:
    required_fuel = 0
    for mass in lines:
        fuel = get_fuel(int(mass))
        required_fuel += fuel

        while get_fuel(fuel) >= 0:
            fuel = get_fuel(fuel)
            required_fuel += fuel

    return required_fuel

