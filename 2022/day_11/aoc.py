import re


class Monkey:
    def __init__(self, input: str):
        inputs = input.split('\n')
        self.items = [int(x) for x in inputs[1][18:].split(', ')]
        self.op = inputs[2][19:]
        self.test = {'test': int(inputs[3][22:]), 'true': int(inputs[4][29:]), 'false': int(inputs[5][30])}


    def getItemsRecipients(self):
        recipients = {}
        for item in self.items:
            n = self.getNewValue(item)
            if n % self.test['test'] == 0:
                recipients[self.test['true']] = n
            else:
                recipients[self.test['false']] = n
        return recipients
    
    def getNewValue(self, v: int):
        data = re.compile(r'^(?P<one>\d+).(?P<op>[+.*/]).(?P<two>\d+)$').fullmatch(self.op.replace('old', str(v)))
        o = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}
        return o[data.groupdict()['op']](int(data.groupdict()['one']), int(data.groupdict()['two']))

    

def handle_part_1(lines: list[str]) -> int:
    monkeys = [Monkey(x) for x in '\n'.join(lines).split('\n\n')]
    print(monkeys[0].getItemsRecipients())
    return 0


def handle_part_2(lines: list[str]) -> int:
    return 0
