def decrypt(lines, decryptionKey, times):
    numbers = list(enumerate(map(lambda x: int(x) * decryptionKey, lines)))
    n = len(numbers)
    original = numbers[:]

    for _ in range(times):
        for x in original:
            numbers.pop(i := numbers.index(x))
            numbers.insert((i + x[1]) % (n - 1), x)

    i = [x[1] for x in numbers].index(0)

    return sum([numbers[(i + 1000) % n][1], numbers[(i + 2000) % n][1], numbers[(i + 3000) % n][1]])


def handle_part_1(lines: list[str]) -> int:
    return decrypt(lines, 1, 1)


def handle_part_2(lines: list[str]) -> int:
    return decrypt(lines, 811589153, 10)
