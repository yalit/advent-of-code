def swap(s, a, b):
    temp = s[a]
    s[a] = s[b]
    s[b] = temp
    return s


def reverse(s, a, b):
    return s[:a] + list(reversed(s[a : b + 1])) + s[b + 1 :]


def rotate(s, dir, a):
    if dir == "left":
        return s[a:] + s[:a]
    return s[len(s) - a :] + s[: len(s) - a]


def move(s, a, b):
    temp = s[a]
    if a < b:
        return s[:a] + s[a + 1 : b + 1] + [temp] + s[b + 1 :]
    if a > b:
        return s[:b] + [temp] + s[b:a] + s[a + 1 :]
    return s


h1 = []
h2 = []


def handle_part_1(lines: list[str]) -> str:
    operations = [line.split(" ") for line in lines[1:]]
    password = list(lines[0])  # list(lines[0])

    for op in operations:
        old = [x for x in password]
        if op[0] == "swap" and op[1] == "position":
            password = swap(password, int(op[2]), int(op[5]))

        if op[0] == "swap" and op[1] == "letter":
            password = swap(password, password.index(op[2]), password.index(op[5]))

        if op[0] == "reverse":
            password = reverse(password, int(op[2]), int(op[4]))

        if op[0] == "rotate" and op[1] != "based":
            password = rotate(password, op[1], int(op[2]))

        if op[0] == "rotate" and op[1] == "based":
            steps = password.index(op[6])
            password = rotate(password, "right", steps + 2 if steps >= 4 else steps + 1)

        if op[0] == "move":
            password = move(password, int(op[2]), int(op[5]))

        h1.append((" ".join(op), "".join(old), "".join(password)))
    return "".join(password)


def handle_part_2(lines: list[str]) -> str:
    operations = [line.split(" ") for line in lines[1:]]
    password = list("fbgdceah")

    for op in reversed(operations):
        old = [x for x in password]
        if op[0] == "swap" and op[1] == "position":
            password = swap(password, int(op[2]), int(op[5]))

        if op[0] == "swap" and op[1] == "letter":
            password = swap(password, password.index(op[2]), password.index(op[5]))

        if op[0] == "reverse":
            password = reverse(password, int(op[2]), int(op[4]))

        if op[0] == "rotate" and op[1] != "based":
            password = rotate(
                password, "left" if op[1] == "right" else "right", int(op[2])
            )

        if op[0] == "rotate" and op[1] == "based":
            current_index = password.index(op[6])
            steps_back = {0: 1, 1: 1, 2: 6, 3: 2, 4: 7, 5: 3, 6: 0, 7: 4}
            password = rotate(password, "left", steps_back[current_index])

        if op[0] == "move":
            password = move(password, int(op[5]), int(op[2]))

        h2.append((" ".join(op), "".join(password), "".join(old)))

    return "".join(password)
