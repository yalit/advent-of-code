def handle_part_1(lines: list[str]) -> int:
    lines = [[int(n) for n in l.split(" ")] for l in lines]
    s = 0

    for line in lines:
        sequences = [get_next_sequence(line)]
        while not all([True if n  == 0 else False for n in sequences[-1]]):
            sequences.append(get_next_sequence(sequences[-1]))

        sequences.reverse()
        for k, seq in enumerate(sequences):
            if k == 0:
                seq.append(0)
                continue
            seq.append(seq[-1] + sequences[k-1][-1])

        s += line[-1] + sequences[-1][-1]

    return s


def handle_part_2(lines: list[str]) -> int:
    lines = [[int(n) for n in l.split(" ")] for l in lines]
    s = 0

    for line in lines:
        sequences = [get_next_sequence(line)]
        while not all([True if n == 0 else False for n in sequences[-1]]):
            sequences.append(get_next_sequence(sequences[-1]))

        sequences.reverse()

        for k, seq in enumerate(sequences):
            if k == 0:
                sequences[k] = [0] + seq
                continue
            sequences[k] = [seq[0] - sequences[k-1][0]] + sequences[k]

        s += line[0] - sequences[-1][0]

    return s

def get_next_sequence(seq):
    s = []

    for i in range(1,len(seq)):
        s.append(seq[i] - seq[i-1])

    return s