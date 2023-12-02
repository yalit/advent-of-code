import re
from python.libraries.array import product

data_pattern = re.compile(r'(\d+) (red|green|blue)')

def handle_part_1(lines: list[str]) -> int:
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []

    for line in lines:
        [game, info] = line.split(":")
        possible = True
        for (n, color) in data_pattern.findall(info):
            if possible and int(n) > max_cubes[color]:
                possible = False

        if possible:
            possible_games.append(int(game.split(" ")[1]))

    return sum(possible_games)


def handle_part_2(lines: list[str]) -> int:
    min_cubes_power = 0

    for line in lines:
        min_colors = {}
        for (n, color) in data_pattern.findall(line.split(":")[1]):
            min_colors[color] = int(n) if color not in min_colors else max(min_colors[color], int(n))

        min_cubes_power += product(list(map(int, min_colors.values())))

    return min_cubes_power
