class IntCodeMemory:
    def __init__(self, program: list[int], instruction_inputs: list[int] = []):
        self.program = program
        self.position = 0
        self.output = None
        self.end = False
        self.instruction_inputs = instruction_inputs 
        self.input_requested = 0

    def get(self, pos: int, mode: int):
        match mode:
            case 1: #Immediate
                return self.program[pos]
            case 0: #Position
                return self.program[self.get(pos, 1)]
        raise Exception(f'Incorrect mode : ${str(mode)}')

    def set(self, pos: int, value: int):
        self.program[pos] = value

    def get_instruction_input(self):
        instruction_input = self.instruction_inputs[self.input_requested]
        self.input_requested += 1
        return instruction_input

    def move_position(self, nb_moves: int):
        self.position += nb_moves

    def add_instruction_input(self, instruction_input: int):
        self.instruction_inputs.append(instruction_input)

