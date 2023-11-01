class IntCodeMemory:
    def __init__(self, program: list[int]):
        self.program = program
        self.output = None
        self.end = False

    def get(self, pos: int, mode: int):
        match mode:
            case 1: #Immediate
                return self.program[pos]
            case 0: #Position
                return self.program[self.get(pos, 1)]
        raise Exception(f'Incorrect mode : ${str(mode)}')

    def set(self, pos: int, value: int):
        self.program[pos] = value