import re
import time


def handle_part_1(lines: list[str]) -> int:
    seeds = [(int(n), int(n)) for n in re.findall(r'(\d+)', lines[0])]
    return get_min_location(lines[2:], seeds)


def handle_part_2(lines: list[str]) -> int:
    ranges = [r.split(' ') for r in re.findall(r'(\d+ \d+)', lines[0])]
    seeds = []
    for (start, n) in ranges:
        seeds.append((int(start), int(start) + int(n) -1))
    return get_min_location(lines[2:], seeds)


def get_min_location(lines, seed_ranges):
    maps = []
    for x, line in enumerate(lines):
        if 'map' in line:
            [f, t] = re.match(r'([a-z]+)-to-([a-z]+) map:', line).groups()
            print("Start de ", f, " => ", t)
            maps = []
            continue
        elif line != '':
            [target, source, n] = re.findall(r'(\d+)', line)
            maps.append(((int(source), int(source) + int(n) - 1), (int(target), int(target) + int(n) - 1)))
        else:
            seeds = []
            for a, seed_range in enumerate(seed_ranges):
                m_ranges = mapped_ranges(seed_range, maps)
                seeds += m_ranges
            seed_ranges = seeds

    return min([min(r) for r in seed_ranges])

# a range is a tuple of (start, end) and targer_ranges is a list (source_range, target_range)
# returns a list of ranges split per "mapped" to targetRanges
def mapped_ranges(range1, target_ranges):
    (start, end) = range1
    for ((s_start, s_end), (t_start, t_end)) in target_ranges:
        #around start
        if start < s_start <= end <= s_end:
            return[(start, s_start - 1), (t_start, t_start + end - s_start)]

        #around full range
        if start < s_start <= s_end < end:
            return [(start, s_start - 1), (t_start, t_end), (s_end+ 1, end)]

        #around end
        if s_start <= start <= s_end < end:
            return [(t_start + start - s_start, t_end + end - s_end), (s_end+1, end)]

        #inside
        if s_start <= start <= end <= s_end:
            return [(t_start + start - s_start, t_start + end - s_start)]

        #fully around
        if start < s_start <= s_end < end:
            return [
                (start, s_start-1),
                (t_start, t_end),
                (s_end+1, end)
            ]

    return [range1]