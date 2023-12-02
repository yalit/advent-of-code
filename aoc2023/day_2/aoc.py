from functools import reduce


def handle_part_1(lines: list[str]) -> int:
    max_cubes = {'red' : 12, 'green': 13, 'blue': 14}
    possible_games = []

    for line in lines:
        [game, info] = line.split(":")
        [_, game_id] = game.split(" ")
        possible = True
        for show in info.split(';'):
            for data in show.split(','):
                [n,color] = data.strip().split(' ')
                if possible and (color not in max_cubes or  int(n) > max_cubes[color]):
                    possible = False

        if possible:
            possible_games.append(int(game_id))
    return sum(possible_games)


def handle_part_2(lines: list[str]) -> int:
    min_cubes_power = []

    for line in lines:
        [game, info] = line.split(":")
        [_, game_id] = game.split(" ")
        min_colors = {}
        for show in info.split(';'):
            for data in show.split(','):
                [n,color] = data.strip().split(' ')
                if color not in min_colors:
                    min_colors[color] = int(n)
                else:
                    min_colors[color] = max(min_colors[color], int(n))

        min_cubes_power.append(reduce(lambda p, x: p * x, list(map(int, min_colors.values())), 1))

    return sum(min_cubes_power)
