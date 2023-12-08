digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

directNeighbors = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

diagNeighbors = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
]

neighbors = directNeighbors + diagNeighbors

neighbors3d = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, -1],
    [0, -1, 0],
    [-1, 0, 0],
]

# ranges = (min,max)[]
def merge_ranges(ranges):
    if len(ranges) == 0:
        return ranges

    ranges = sorted(ranges, key=lambda r: r[0])
    merged = [tuple(ranges[0])]
    idx = 0
    for r in ranges[1:]:
        if r[0] < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
        else:
            merged.append(tuple(r))
    return merged

#r1 & r2 are tuple (start, end)
def intersect_range(r1, r2):
    if r1[0] > r2[1] or r1[1] < r2[0]:
        return None

    if r1[0] < r2[0]:
        return (r2[0], r1[1]) if r1[1] < r2[1] else r2

    return (r1[0], r2[1]) if r1[1] > r2[1] else r1

def lcm(*n):
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    p = abs(n[0]*n[1])//_pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p*x)//_pgcd(p, x)
    return p