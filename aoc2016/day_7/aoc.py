import re


def isABBA(s: str) -> bool:
    return len(s) == 4 and s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def nbABBA(s: str) -> int:
    n = 0
    for i in range(len(s)):
        if isABBA(s[i : i + 4]):
            n += 1

    return n


def handle_part_1(lines: list[str]) -> int:
    n = 0

    for line in lines:
        hypernets = [
            w.replace("]", "").replace("[", "") for w in re.findall(r"\[\w+\]", line)
        ]
        supernets = [
            w.replace("]", "").replace("[", "")
            for w in re.findall(r"\]?\w+\[", line) + re.findall(r"\]\w+\[?", line)
        ]

        outsideABBA = 0
        for w in supernets:
            outsideABBA += nbABBA(w)

        hypernetsABBA = 0
        for w in hypernets:
            hypernetsABBA += nbABBA(w)

        if outsideABBA >= 1 and hypernetsABBA == 0:
            n += 1
    return n


def isABA(s: str) -> bool:
    return len(s) == 3 and s[0] == s[2] and s[0] != s[1]


def handle_part_2(lines: list[str]) -> int:
    n = 0
    for line in lines:
        abas = set()
        hypernets = [
            w.replace("]", "").replace("[", "") for w in re.findall(r"\[\w+\]", line)
        ]
        supernets = [
            w.replace("]", "").replace("[", "")
            for w in re.findall(r"\]?\w+\[", line) + re.findall(r"\]\w+\[?", line)
        ]

        for w in supernets:
            for i in range(len(w)):
                if isABA(w[i : i + 3]):
                    abas.add(w[i : i + 3])

        supportsSSL = any(
            any("".join([aba[1], aba[0], aba[1]]) in h for h in hypernets)
            for aba in abas
        )
        if supportsSSL:
            n += 1

    return n
