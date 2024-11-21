import re


def nbTriangles(triangles: list[list[int]]) -> int:
    return len(
        [
            t
            for t in triangles
            if all([t[0] + t[1] > t[2], t[0] + t[2] > t[1], t[1] + t[2] > t[0]])
        ]
    )


def handle_part_1(lines: list[str]) -> int:
    triangles = [
        sorted([int(x) for x in [s for s in re.split(r"\s", line) if s != ""]])
        for line in lines
    ]

    return nbTriangles(triangles)


def handle_part_2(lines: list[str]) -> int:
    triangles = []
    s = [[int(x) for x in re.split(r"\s", line) if x != ""] for line in lines]
    for i in range(0, len(s), 3):
        triangles.append([s[i][0], s[i + 1][0], s[i + 2][0]])
        triangles.append([s[i][1], s[i + 1][1], s[i + 2][1]])
        triangles.append([s[i][2], s[i + 1][2], s[i + 2][2]])

    return nbTriangles(triangles)
