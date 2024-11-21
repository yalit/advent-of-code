from hashlib import md5


def handle_part_1(lines: list[str]) -> str:
    id = lines[0]

    i = 0
    password = ""
    while len(password) < 8:
        h = md5((id + str(i)).encode("utf-8")).hexdigest()
        if "00000" == "".join(h[:5]):
            password += h[5]
        i += 1

    return password


def handle_part_2(lines: list[str]) -> str:
    id = lines[0]

    i = 0
    password = {}
    targetIndexes = list(map(str, range(8)))
    while len(password) < 8:
        h = md5((id + str(i)).encode("utf-8")).hexdigest()
        if "00000" == "".join(h[:5]) and h[5] in targetIndexes and h[5] not in password:
            password[h[5]] = h[6]
        i += 1

    return "".join([password[str(x)] for x in range(8)])
