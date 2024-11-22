import re


def giveValueTo(d, target, value):
    if target not in d:
        d[target] = []

    d[target] = sorted(d[target] + [value])


def handle_part_1(lines: list[str]) -> int:
    bots = {}
    outputs = {}
    instructions = {}

    for line in lines:
        if line.startswith("value"):
            r = re.match(r"value (\d+) goes to bot (\d+)", line).groups()
            giveValueTo(bots, int(r[1]), int(r[0]))
        else:
            r = re.match(
                r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
                line,
            ).groups()
            instructions[int(r[0])] = ((r[1], int(r[2])), (r[3], int(r[4])))

    while len([x for x in bots if len(bots[x]) == 2]) > 0:
        bot = [x for x in bots if len(bots[x]) == 2][0]
        low, high = instructions[bot]

        if bots[bot] == [17, 61]:
            return bot

        if high[0] == "output":
            giveValueTo(outputs, high[1], bots[bot][1])
        else:
            giveValueTo(bots, high[1], bots[bot][1])

        if low[0] == "output":
            giveValueTo(outputs, low[1], bots[bot][0])
        else:
            giveValueTo(bots, low[1], bots[bot][0])
        bots[bot] = []

    return 0


def handle_part_2(lines: list[str]):
    bots = {}
    outputs = {}
    instructions = {}

    for line in lines:
        if line.startswith("value"):
            r = re.match(r"value (\d+) goes to bot (\d+)", line).groups()
            giveValueTo(bots, int(r[1]), int(r[0]))
        else:
            r = re.match(
                r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
                line,
            ).groups()
            instructions[int(r[0])] = ((r[1], int(r[2])), (r[3], int(r[4])))

    while len([x for x in bots if len(bots[x]) == 2]) > 0:
        bot = [x for x in bots if len(bots[x]) == 2][0]
        low, high = instructions[bot]

        if high[0] == "output":
            giveValueTo(outputs, high[1], bots[bot][1])
        else:
            giveValueTo(bots, high[1], bots[bot][1])

        if low[0] == "output":
            giveValueTo(outputs, low[1], bots[bot][0])
        else:
            giveValueTo(bots, low[1], bots[bot][0])
        bots[bot] = []

    return outputs[0][0] * outputs[1][0] * outputs[2][0]
