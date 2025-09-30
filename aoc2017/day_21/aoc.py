from python.libraries.array import rotate_right, flip_horizontal, flip_vertical
from python.libraries.utils import split_every_n

grid = [".#.", "..#", "###"]

def get_book(lines: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    book = {}
    rotations = {}

    def rotate(arr):
        return ["".join(row) for row in rotate_right(arr)]

    for line in lines:
        inp, out = map(lambda x: x.strip().split("/"), line.split(" => "))
        book[tuple(inp)] = out

        # Generate all rotations and flips
        # Original
        rotations[tuple(inp)] = tuple(inp)

        # 3 rotations to the right
        rotations[tuple(rotate(inp))] = tuple(inp)
        rotations[tuple(rotate(rotate(inp)))] = tuple(inp)
        rotations[tuple(rotate(rotate(rotate(inp))))] = tuple(inp)

        # Flip horizontally and generate rotations
        base = flip_horizontal(inp)
        rotations[tuple(base)] = tuple(inp)
        rotations[tuple(rotate(base))] = tuple(inp)
        rotations[tuple(rotate(rotate(base)))] = tuple(inp)
        rotations[tuple(rotate(rotate(rotate(base))))] = tuple(inp)

        #flip vertically and generate rotations
        base = flip_vertical(inp)
        rotations[tuple(base)] = tuple(inp)
        rotations[tuple(rotate(base))] = tuple(inp)
        rotations[tuple(rotate(rotate(base)))] = tuple(inp)
        rotations[tuple(rotate(rotate(rotate(base))))] = tuple(inp)

    return book, rotations


def iterate(grid: list[str], book: dict[tuple[str], str], rotations: dict[tuple[str], tuple[str]]) -> list[str]:
    size = len(grid)
    if size % 2 == 0:
        step = 2
    else:
        step = 3

    n_size = size//step + size
    new_grid = ["" for _ in range(n_size)]

    for r in range(0, size, step):
        for c in range(0, size, step):
            block = []
            for i in range(step):
                block.append(grid[r+i][c:c+step])
            evolved = book[rotations[tuple(block)]]
            n_step = step + 1
            for i, b in enumerate(evolved):
                new_grid[(r//step)*n_step + i] += b

    return new_grid

def handle_part_1(lines: list[str]) -> int:
    book, rotations = get_book(lines)
    grid = [".#.", "..#", "###"]

    for i in range(5):
        grid = iterate(grid, book, rotations)

    return sum([row.count("#") for row in grid])


def handle_part_2(lines: list[str]) -> int:
    book, rotations = get_book(lines)
    grid = [".#.", "..#", "###"]

    for i in range(18):
        grid = iterate(grid, book, rotations)

    return sum([row.count("#") for row in grid])
