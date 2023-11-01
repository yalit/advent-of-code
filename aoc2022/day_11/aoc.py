import re
from functools import reduce


class Monkey:
    def __init__(self, input: str):
        inputs = input.split('\n')
        self.items = [int(x) for x in inputs[1][18:].split(', ')]
        self.op = inputs[2][19:]
        self.test = {'test': int(inputs[3][21:]), 'true': int(inputs[4][29:]), 'false': int(inputs[5][30])}
        self.inspections = 0

    def treatItem(self, mod: int = 1):
        if len(self.items) == 0:
            return
        self.inspections += 1
        item = self.items[0]
        self.items = self.items[1:]
        n = self.handleWorryLevel(self.getNewValue(item), mod)
        recipient = self.test['true'] if n % self.test['test'] == 0 else self.test['false']
        return [recipient, n]

    def handleWorryLevel(self, v: int, mod: int = 1):
        return v // 3

    def addItem(self, item):
        self.items.append(item)

    def getNewValue(self, v: int):
        data = re.compile(r'^(?P<one>\d+).(?P<op>[+.*/]).(?P<two>\d+)$').fullmatch(self.op.replace('old', str(v)))
        o = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}
        return o[data.groupdict()['op']](int(data.groupdict()['one']), int(data.groupdict()['two']))


class UnManagedMonkey(Monkey):
    def handleWorryLevel(self, v: int, mod: int = 1):
        return v % mod


def handleInspections(monkeys: list[Monkey], nb: int, mod: int = 1):
    for _ in range(nb):
        for monkey in monkeys:
            for item in monkey.items:
                r = monkey.treatItem(mod)
                monkeys[r[0]].addItem(r[1])


def handle_part_1(lines: list[str]) -> int:
    monkeys = [Monkey(x) for x in '\n'.join(lines).split('\n\n')]
    handleInspections(monkeys, 20)
    return reduce(lambda a, b: a * b, sorted([m.inspections for m in monkeys])[-2:])


def handle_part_2(lines: list[str]) -> int:
    monkeys = [UnManagedMonkey(x) for x in '\n'.join(lines).split('\n\n')]
    fullModulo = reduce(lambda a, b: a*b, [m.test['test'] for m in monkeys], 1)
    handleInspections(monkeys, 10000, fullModulo)
    return reduce(lambda a, b: a * b, sorted([m.inspections for m in monkeys])[-2:])
