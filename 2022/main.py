import sys

runType = ''
day = ''

if len(sys.argv) == 3:
    day = sys.argv[2]
    print(f"Provided day is {day}")

if len(sys.argv) >= 2:
    runType = sys.argv[1]
    print(f"Provided runType is {runType}")

if len(sys.argv) < 2:
    while runType != 'run' and runType != 'test':
        print(f'Which type of run do you want to do : run | test ?')
        runType = input()
        print(f"Requested runType is {runType}")

if len(sys.argv) < 3:
    while day == '':
        print(f'Which day do you want to {runType} ?')
        day = input()
        print(f"Requested day is {day}")


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
