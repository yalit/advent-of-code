import re
from functools import reduce
from heapq import heapify, heappush, heappop

memoizePressures = {}

def findPaths(v, valves, interesting):
    visited = set()
    toVisit = [(0,v)]
    heapify(toVisit)
    paths = {}
    while toVisit:
        steps, previousPath = heappop(toVisit)
        steps += 1
        for x in valves[previousPath][1]:
            if x in visited:
                continue
            visited.add(x)
            if x in interesting and x != v:
                paths[x] = steps
            heappush(toVisit, (steps, x))

    return paths


def findMax(valves, paths, minutes=30, current='AA', opened=set()):
    maxPressure = 0
    if (current, minutes, '.'.join([*opened])) in memoizePressures:
        return memoizePressures[(current, minutes, '.'.join([*opened]))]

    for nextValve in paths[current]:
        if nextValve in opened:
            continue

        remainingMinutes = minutes - paths[current][nextValve] - 1
        if remainingMinutes <= 0:
            continue

        maxPressure = max(maxPressure, findMax(valves, paths, remainingMinutes, nextValve, {*opened, nextValve}) + (valves[nextValve][0] * remainingMinutes))

    memoizePressures[(current, minutes, '.'.join([*opened]))] = maxPressure
    return maxPressure


def handle_part_1(lines: list[str]) -> int:
    valves = {}
    for line in lines:
        d = re.compile(r'^Valve.(?P<v>[A-Z]{2}).has.flow.rate=(?P<rate>\d+);.tunnels?.leads?.to.valves?.(?P<neighbors>.*)$').fullmatch(line).groupdict()
        valves[d['v']] = (int(d['rate']), d['neighbors'].split(', '))
    interesting = set([k for k, v in valves.items() if v[0] > 0])
    allShortestPaths = {x: findPaths(x, valves, interesting) for x in valves}

    return findMax(valves, allShortestPaths)


def handle_part_2(lines: list[str]) -> int:
    valves = {}
    for line in lines:
        d = re.compile(r'^Valve.(?P<v>[A-Z]{2}).has.flow.rate=(?P<rate>\d+);.tunnels?.leads?.to.valves?.(?P<neighbors>.*)$').fullmatch(line).groupdict()
        valves[d['v']] = (int(d['rate']), d['neighbors'].split(', '))
    interesting = [k for k, v in valves.items() if v[0] > 0]
    allShortestPaths = {x: findPaths(x, valves, interesting) for x in valves}

    maxBothPressures = 0

    # Find all different partitions of interesting to split between the 2 (elephant and me)
    def allPartitions(e, elements):
        if len(elements) == 0:
            return [[e], []]

        partitions = []
        for p in allPartitions(elements[0], elements[1:]):
            partitions.append([e, *p])
            partitions.append(p)

        return partitions
    partitions = allPartitions(interesting[0], interesting[1:])

    # get the max for each of the splits
    for e in partitions:
        maxBothPressures = max(maxBothPressures, findMax(valves, allShortestPaths, minutes=26, opened=set(e)) + findMax(valves, allShortestPaths, minutes=26, opened=set([x for x in interesting if x not in e])))

    return maxBothPressures
