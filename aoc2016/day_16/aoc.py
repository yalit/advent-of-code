def handle_part_1(lines: list[str]) -> str:
    disk_size = int(lines[0])
    seed = list(map(int, list(lines[1])))

    data = generate_data(seed)
    while len(data) < disk_size:
        data = generate_data(data)

    data = data[:disk_size]
    return "".join(map(str, get_checksum(data)))


def handle_part_2(lines: list[str]) -> str:
    lines[0] = "35651584"
    return handle_part_1(lines)


def generate_data(d: list[int]) -> list[int]:
    e = [1 - d[x] for x in range(len(d) - 1, -1, -1)]
    return d + [0] + e


def get_checksum(data) -> list[int]:
    checksum = [1 if data[x] == data[x + 1] else 0 for x in range(0, len(data), 2)]

    while len(checksum) % 2 == 0:
        checksum = [
            1 if checksum[x] == checksum[x + 1] else 0
            for x in range(0, len(checksum), 2)
        ]
    return checksum
