from collections import deque


def mix(a: int, b: int) -> int:
    return a ^ b

def prune(a: int) -> int:
    return a % 16777216

def get_next_secret_number(secret: int) -> int:
    ## 1st operation:
    next_secret = prune(mix(secret * 64, secret))

    ## 2nd operation:
    next_secret = prune(mix(next_secret // 32, next_secret))

    ## 3rd operation:
    return prune(mix(next_secret * 2048, next_secret))

class Pricer:
    prices: list[int]

    def __init__(self, initializer: int):
        self.prices = [initializer]

    def add_price(self, price: int):
        self.prices.append(price)
        if len(self.prices) > 5:
            self.prices.pop(0)

    def is_matching_deltas(self, deltas: tuple[int]):
        return  deltas == [a - b for a,b in zip(self.prices[1:], self.prices)]

    def get_deltas(self) -> tuple[int]:
        return tuple([a-b for a,b in zip(self.prices[1:], self.prices)])

    def get_price(self):
        return self.prices[-1]


def handle_part_1(lines: list[str]) -> int:
    secrets = list(map(int, lines))
    nb_transformations = 2000

    total = 0
    for secret in secrets:
        for i in range(nb_transformations):
            secret = get_next_secret_number(secret)
        total += secret
    return total


def handle_part_2(lines: list[str]) -> int:
    secrets = list(map(int, lines))
    nb_transformations = 2000

    secret_deltas_max = {}
    for secret in secrets:
        original_secret = secret
        secret_deltas_max[original_secret] = {}
        pricer = Pricer(int(str(original_secret)[-1:]))

        for i in range(nb_transformations):
            secret = get_next_secret_number(secret)
            pricer.add_price(int(str(secret)[-1:]))
            if pricer.get_deltas() not in secret_deltas_max[original_secret]:
                secret_deltas_max[original_secret][pricer.get_deltas()] = pricer.get_price()

    max_for_deltas = {}

    for secret in secret_deltas_max:
        for deltas, maximum in secret_deltas_max[secret].items():
            if deltas not in max_for_deltas:
                max_for_deltas[deltas] = 0
            max_for_deltas[deltas] += maximum

    return max(m for m in max_for_deltas.values())
