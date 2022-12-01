import sys

# Run it like python main.py test|run <day>
if len(sys.argv) != 3:
    raise ValueError('Please provide a type of run (test or main) and a day to run')

runType = sys.argv[1]
day = sys.argv[2]
dayScript = __import__(f'day_{day}.aoc')

if runType == 'test':
    print(f'Running day {day} --- TEST')
    file = open(f'./day_{day}/input_test.txt', "r")
else:
    print(f'Running day {day}')
    file = open(f'./day_{day}/input.txt', "r")

lines = [x.strip('\n') for x in file.readlines()]

print("Solution part 1 : ", dayScript.aoc.handle_part_1(lines))
print("Solution part 2 : ", dayScript.aoc.handle_part_2(lines))
