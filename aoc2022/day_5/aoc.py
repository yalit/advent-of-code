import re
from libraries.stack import Stack


def find_indices_stacks(list_to_check):
    return [idx for idx, value in enumerate(list_to_check) if value != ' ' and value != '[' and value != ']']


def init_stacks(stacks_data: list[str]) -> dict[int, Stack]:
    stacks_id = stacks_data[-1]
    stacks_id_map: dict[int, int] = {i: int(stacks_id[i]) for i in find_indices_stacks(stacks_id)}

    stacks: dict[int, Stack] = {}
    stacks_cranes_data = reversed(list(stacks_data[0:-1]))
    for data in stacks_cranes_data:
        for idx in find_indices_stacks(data):
            stack_idx = stacks_id_map[idx]
            if stack_idx not in stacks.keys():
                stacks[stack_idx] = Stack()
            stacks[stack_idx].add(data[idx])

    return stacks


class MoveInput:
    nb: int
    moveFrom: int
    moveTo: int

    def __init__(self, moveData: str):
        moveRegex = re.compile(r'^move.(?P<nb>\d+).from.(?P<from>\d+).to.(?P<to>\d+)$')
        moveInputs = moveRegex.fullmatch(moveData)
        self.nb = int(moveInputs.groupdict()['nb'])
        self.moveFrom = int(moveInputs.groupdict()['from'])
        self.moveTo = int(moveInputs.groupdict()['to'])


class CargoCrane9000:
    def __init__(self, lines: list[str]):
        self.stacks: dict[int, Stack] = init_stacks(lines[0:lines.index("")])
        self.moves: list[MoveInput] = [MoveInput(moveInput) for moveInput in lines[lines.index("") + 1:]]

    def handleMoves(self):
        for move in self.moves:
            for i in range(0,move.nb):
                self.moveCrate(move)

    def moveCrate(self, move: MoveInput):
        self.stacks[move.moveTo].add(self.stacks[move.moveFrom].pop())

    def getTopCrates(self):
        return ''.join([self.stacks[stack_idx].peek() for stack_idx in sorted(self.stacks.keys())])


class CargoCrane9001(CargoCrane9000):
    def handleMoves(self):
        for move in self.moves:
            self.moveCrate(move)

    def moveCrate(self, move: MoveInput) :
        for crate in reversed([self.stacks[move.moveFrom].pop() for _ in range(0,move.nb)]):
            self.stacks[move.moveTo].add(crate)


def handle_part_1(lines: list[str]) -> str:
    crane = CargoCrane9000(lines)
    crane.handleMoves()
    return crane.getTopCrates()


def handle_part_2(lines: list[str]) -> str:
    crane = CargoCrane9001(lines)
    crane.handleMoves()
    return crane.getTopCrates()
