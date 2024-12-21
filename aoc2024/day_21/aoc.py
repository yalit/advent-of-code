number_keypad_moves = {
    'A': {'0': ['<'], '9': ['^^^'], '1': ['^<<','<^<'], '4': ['<^<^', '^^<<', '<^^<', '^<<^', '^<^<'], '3': ['^']},
    '0': {'2': ['^'],'A': ['>']},
    '9': {'8': ['<'], 'A': ['vvv'], '6': ['v']},
    '1': {'7': ['^^'], '9': ['>>^^', '^>>^', '>^>^', '>^^>', '^>^>', '^^>>']},
    '4': {'5': ['>'],'0': ['>vv', 'v>v'], '8': ['>^', '^>'], 'A': ['>>vv', '>v>v', '>vv>', 'v>>v', 'v>v>']},
    '3': {'7': ['<<^^', '<^<^', '<^^<','^<<^', '^<^<', '^^<<'],'1': ['<<'], '4':['<<^', '<^<', '^<<']},
    '2': {'9': ['^^>', '^>^', '>^^']},
    '8': {'0': ['vvv'],'5': ['v'], '9': ['>']},
    '6': {'A': ['vv'],'4': ['<<']},
    '7': {'9': ['>>']},
    '5': {'6': ['>'],'A': ['vv>', 'v>v', '>vv']},
}

directional_keypad_moves = {
    'A': {'A': [''], '^': ['<'], '>': ['v'], '<': ['v<<','<v<'], 'v': ['v<', '<v']},
    '^': {'A': ['>'], '^': [''], 'v': ['v'], '<': ['v<'], '>': ['v>','>v']},
    'v': {'A': ['>^','^>'], 'v': [''], '^': ['^'], '<': ['<'], '>': ['>']},
    '<': {'A': ['>>^','>^>'], '<': [''], '^': ['>^'], 'v': ['>'], '>': ['>>']},
    '>': {'A': ['^'], '>': [''], '^': ['^<','<^'], 'v': ['<'], '<': ['<<']},
}

def find_shortest_moves(target: str, moves_from: dict[str, dict[str, list[str]]]) -> set[str]:
    current = 'A'
    possibles = {''}
    for next_digit in target:
        new_possibles = set()
        for possible in possibles:
            for move in moves_from[current][next_digit]:
                new_possibles.add(possible + move + 'A')
        possibles = new_possibles
        current = next_digit
    return possibles

def min_for_pattern(line: str, nb_rotation_needed: int) ->int :
    # find all the possibilities for the first robot moves on the number keypad for the target
    targets = find_shortest_moves(line, number_keypad_moves)

    memoization = {}

    # we need to find how to go from a place to another place with the least amount of moves after all the robots rotations
    # we need to return the length of the shortest moves after the robots have rotated nb_rotation_needed times
    def min_moves(current:str, target: str, nb_rotation_remaining: int) -> int:
        if nb_rotation_remaining == 0:
            return min(map(len, directional_keypad_moves[current][target])) + 1 #need to add 1 for the press on A

        if (current, target, nb_rotation_remaining) in memoization:
            return memoization[(current, target, nb_rotation_remaining)]

        min_nb_moves = float('inf')
        for pattern in directional_keypad_moves[current][target]:
            min_nb_moves = min(
                min_nb_moves,
                sum(
                    [min_moves(f,t,nb_rotation_remaining-1) for f,t in zip('A'+pattern+'A', pattern+'A')]
                )
            )


        memoization[(current, target, nb_rotation_remaining)] = min_nb_moves

        return min_nb_moves

    return min(
        sum([min_moves(f,t,nb_rotation_needed) for f,t in zip('A'+target, target)])
        for target in targets
    )


def handle_part_1(lines: list[str]) -> int:
    return sum(min_for_pattern(line, 1) * int(line[:-1]) for line in lines)

def handle_part_2(lines: list[str]) -> int:
    return sum(min_for_pattern(line, 24) * int(line[:-1]) for line in lines)



