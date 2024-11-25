from hashlib import md5
import re


trioRegex = r"([a-z0-9])\1\1"
quentaRegex = r"([a-z0-9])\1\1\1\1"


def get_keys(salt, hash):
    index = 0
    keys = []
    trios = {}
    while len(keys) <= 80:
        h = hash(salt + str(index))  #
        t = re.findall(trioRegex, h)
        q = re.findall(quentaRegex, h)
        if len(t) > 0:
            if index == 534:
                print(534, t)
            trios[index] = (t[0], h)
        if len(q) > 0:
            for elem in q:
                found = [
                    (a, trios[a])
                    for a in trios.keys()
                    if a < index < a + 1000 and a != index and trios[a][0] == elem
                ]
                if len(found) > 0:
                    keys += found
        index += 1

    return sorted(keys)


def handle_part_1(lines: list[str]) -> int:
    salt = lines[0]

    def hash_simple(s):
        return md5(s.encode("utf-8")).hexdigest()

    return get_keys(salt, hash_simple)[63]


def handle_part_2(lines: list[str]) -> int:
    salt = lines[0]

    def stretched_hash(s):
        h = md5(s.encode("utf-8")).hexdigest()
        for _ in range(2016):
            h = md5(h.encode("utf-8")).hexdigest()
        return h

    return get_keys(salt, stretched_hash)[63]
