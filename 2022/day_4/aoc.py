import re


def handle_part_1(lines: list[str]) -> int:
    def existsOverlap(line: str) -> bool:
        sectionRegex = re.compile(r'^(?P<min1>\d+)-(?P<max1>\d+),(?P<min2>\d+)-(?P<max2>\d+)$')
        sections = sectionRegex.fullmatch(line)
        return (int(sections.groupdict()['min1']) <= int(sections.groupdict()['min2'])
                and int(sections.groupdict()['max1']) >= int(sections.groupdict()['max2'])) \
            or (int(sections.groupdict()['min2']) <= int(sections.groupdict()['min1'])
                and int(sections.groupdict()['max2']) >= int(sections.groupdict()['max1']))

    return len(list(filter(existsOverlap, lines)))


def handle_part_2(lines: list[str]) -> int:
    def existsAtAllOverlap(line: str) -> bool:
        sectionRegex = re.compile(r'^(?P<min1>\d+)-(?P<max1>\d+),(?P<min2>\d+)-(?P<max2>\d+)$')
        sections = sectionRegex.fullmatch(line)
        return (int(sections.groupdict()['min1']) <= int(sections.groupdict()['min2']) <= int(sections.groupdict()['max1'])) \
            or (int(sections.groupdict()['min2']) <= int(sections.groupdict()['min1']) <= int(sections.groupdict()['max2']))

    return len(list(filter(existsAtAllOverlap, lines)))
