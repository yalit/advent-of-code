import functools


def get_elves_calories(lines: list[str]) -> list[int]:
    count = 0
    elves_calories = []
    for line in lines:
        if line == '':
            elves_calories.append(count)
            count = 0
        else:
            count += int(line)

    elves_calories.sort(reverse=True)
    return elves_calories


def handle_part_1(lines: list[str]) -> str:
    return str(get_elves_calories(lines)[0])


def handle_part_2(lines: list[str]) -> str:
    calories = get_elves_calories(lines)

    def sumCalories(a: int, b: int):
        return a + b

    return str(functools.reduce(sumCalories, calories[0:3]))
