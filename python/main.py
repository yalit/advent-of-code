import sys, os
import time


def import_module(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

runType = sys.argv[1]
year = sys.argv[2]
day = sys.argv[3]

sys.path.append(os.path.abspath(os.path.join('..')))

dayScript = import_module(f'aoc{year}.day_{day}.aoc')

if runType == 'test':
    print(f'Running day {day} --- TEST')
    file = open(f'../aoc{year}/day_{day}/input_test.txt', "r")
else:
    print(f'Running day {day}')
    file = open(f'../aoc{year}/day_{day}/input.txt', "r")

lines = [x.strip('\n') for x in file.readlines()]

if len(sys.argv) == 4 or sys.argv[4] == '1':
    start = time.time()
    print("Solution part 1 : ", dayScript.handle_part_1(lines))
    print("Execution time : ", time.time() - start, 'seconds')

if len(sys.argv) == 4 or sys.argv[4] == '2':
    start = time.time()
    print("Solution part 2 : ", dayScript.handle_part_2(lines))
    print("Execution time : ", time.time() - start, 'seconds')
