digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

directNeighbors = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

diagNeighbors = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
]

neighbors = directNeighbors + diagNeighbors

neighbors3d = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, -1],
    [0, -1, 0],
    [-1, 0, 0],
]