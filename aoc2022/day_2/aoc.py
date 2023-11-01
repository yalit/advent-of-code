import functools
from typing import Tuple, Any

# tuple for each (score, wins, draws, lose)
data = {'X': (1, "Z", "X", "Y"), 'Y': (2, "X", "Y", "Z"), 'Z': (3, "Y", "Z", "X")}
code_mapping = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def get_score_round(plays: tuple[str, str]) -> int:
    opponent = plays[0]
    me = plays[1]
    score = data[me][0]
    if opponent == me:
        score += 3
    if opponent == data[me][1]:
        score += 6
    return score


def map_play_data(plays: list[str]):
    return map(lambda a: (code_mapping[a[0]], a[1]), map(lambda a: a.split(' '), plays))


def handle_part_1(plays: list[str]) -> str:
    return str(sum(map(get_score_round, map_play_data(plays))))


def handle_part_2(plays: list[str]) -> str:
    plays = map_play_data(plays)

    def find_secret_play(plays: tuple[str, str]) -> tuple[str, str]:
        secret = plays[1]
        toPlay = ''
        if secret == "X":  # me lose, opponent wins
            toPlay = data[plays[0]][1]
        if secret == 'Y':  # me draw, opponent draw
            toPlay = data[plays[0]][2]
        if secret == 'Z':  # me win, opponent los
            toPlay = data[plays[0]][3]
        return plays[0], toPlay

    return str(sum(map(get_score_round, map(find_secret_play, plays))))
