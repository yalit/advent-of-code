from libraries.array import visualize


def handle_part_1(lines: list[str]) -> int:
    currentStep, totalStrength, signal = 0, 0, 1
    steps = [220, 180, 140, 100, 60, 20]
    for k, l in enumerate(lines):
        for _ in range(1 if l[0:4] == 'noop' else 2):
            currentStep += 1
            if len(steps) > 0 and currentStep >= steps[-1]:
                totalStrength += signal * steps[-1]
                steps.pop()

        signal += int(l[5:]) if l[0:4] == 'addx' else 0

    return totalStrength


def handle_part_2(lines: list[str]) -> int:
    crt = [['🎄'  for _ in range(40)] for _ in range(6)]
    currentStep, signal = 0, 1
    steps = [220, 180, 140, 100, 60, 20]

    for k, l in enumerate(lines):
        if currentStep >= 240:
            break
        for _ in range(1 if l[0:4] == 'noop' else 2):
            crt[currentStep // 40][currentStep % 40] =  '🎅' if currentStep % 40 in [signal - 1, signal, signal + 1] else '🎄'
            currentStep += 1

        signal += int(l[5:]) if l[0:4] == 'addx' else 0

    visualize(crt)
    return 0
