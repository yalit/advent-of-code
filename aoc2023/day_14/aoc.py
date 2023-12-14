from python.libraries.array import transpose

def handle_part_1(lines: list[str]) -> int:
    return handle_board("B".join(lines), ['N'], 1)


def handle_part_2(lines: list[str]) -> int:
    return handle_board("B".join(lines), ['N', 'W', 'S', 'E'], 1000000000)

def handle_board(board, cycle, n):
    tilt_functions = {
        'N' : tilt_board_north,
        'S' : tilt_board_south,
        'E' : tilt_board_east,
        'W' : tilt_board_west
    }

    total_steps = n * len(cycle)
    visited = {}
    remaining_cycles = n
    for x in range(n):
        found = False
        for idx, d in enumerate(cycle):
            i = (len(cycle) * x) + idx
            board = tilt_functions[d](get_board_from_string(board))
            if i % 4 == 0 and board in visited.keys():
                delta = i - visited[board]
                restart_cycle_index = i + (delta * int((total_steps-i)/delta))
                remaining_cycles = int((total_steps - restart_cycle_index)/len(cycle))
                found = True
                break
            if i % 4 == 0:
                visited[board] = i

        if found:
            break

    for y in range(remaining_cycles):
        for j, d, in enumerate(cycle):
            board = tilt_functions[d](get_board_from_string(board))

    board = get_board_from_string(board)
    return sum([sum([len(board)-i for x in row if x == 'O']) for i, row in enumerate(board)])

def sort_rock(r):
    return -1 if r == 'O' else 0

def sort_rock_reversed(r):
    return -1 if r == '.' else 0

def tilt_board_north(board):
    b = ["".join(row) for row in transpose(board)]
    b = ["#".join(["".join(list(sorted(list(r), key=sort_rock))) for r in row.split('#')]) for row in b]
    b = ["".join(row) for row in transpose(b)]
    return get_string_board(b)

def tilt_board_south(board):
    b = ["".join(row) for row in transpose(board)]
    b = ["#".join(["".join(list(sorted(list(r), key=sort_rock_reversed))) for r in row.split('#')]) for row in b]
    b = ["".join(row) for row in transpose(b)]
    return get_string_board(b)

def tilt_board_east(board):
    return get_string_board(["#".join(["".join(list(sorted(list(r), key=sort_rock_reversed))) for r in row.split('#')]) for row in board])

def tilt_board_west(board):
    return get_string_board(["#".join(["".join(list(sorted(list(r), key=sort_rock))) for r in row.split('#')]) for row in board])

def get_string_board(board):
    return "B".join(board)

def get_board_from_string(board):
    return board.split('B')