width = 50
height = 6


def display_screen(screen):
    for y in range(height):
        print("".join(["#" if screen[(x, y)] else "." for x in range(width)]))


def rectangle(screen, X: int, Y: int):
    for x in range(X):
        for y in range(Y):
            screen[(x, y)] = 1


def rotateRow(screen, Y, B):
    row = [screen[(x, Y)] for x in range(width)]
    for i, r in enumerate(row):
        screen[((i + B) % width, Y)] = r


def rotateColumn(screen, X, B):
    col = [screen[(X, y)] for y in range(height)]
    for i, c in enumerate(col):
        screen[(X, (i + B) % height)] = c


def getSwipedScreen(lines: list[str]) -> dict[tuple[int, int], int]:
    screen = {}
    for x in range(width):
        for y in range(height):
            screen[(x, y)] = 0

    for line in lines:
        command = line.split(" ")
        if command[0] == "rect":
            X, Y = command[1].split("x")
            rectangle(screen, int(X), int(Y))

        if command[0] == "rotate" and command[1] == "column":
            _, Y = command[2].split("=")
            rotateColumn(screen, int(Y), int(command[4]))

        if command[0] == "rotate" and command[1] == "row":
            _, Y = command[2].split("=")
            rotateRow(screen, int(Y), int(command[4]))

    return screen


def handle_part_1(lines: list[str]) -> int:
    screen = getSwipedScreen(lines)
    return len([x for x in screen if screen[x]])


def handle_part_2(lines: list[str]) -> int:
    display_screen(getSwipedScreen(lines))
    return 0
