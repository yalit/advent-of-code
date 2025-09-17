def handle_part_1(lines: list[str]) -> int:
    stream = lines[0]
    score = 0
    level = 0
    pos = 0

    while pos < len(stream):
        if stream[pos] == "{":
            level += 1
        elif stream[pos] == "}":
            score += level
            level -= 1
        elif stream[pos] == "<":
            pos, _ = skip_garbage(stream, pos)
        pos +=1

    return score


def handle_part_2(lines: list[str]) -> int:
    stream = lines[0]
    pos = 0
    nb_garbage = 0

    while pos < len(stream):
        if stream[pos] == "<":
            pos, local_garbage = skip_garbage(stream, pos)
            nb_garbage += local_garbage
        pos +=1

    return nb_garbage

def skip_garbage(stream: str, pos: int) -> tuple[int, int]:
    ended = False
    nb = 0
    while not ended:
        if stream[pos] == '>':
            nb -= 1
            ended = True
            continue
        if stream[pos] == '!':
            nb -= 1
            pos +=1
        nb+=1
        pos +=1
        
    return pos, nb