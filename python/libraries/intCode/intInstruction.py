from python.libraries.intCode.intCodeMemory import IntCodeMemory

class Instruction:
    def __init__(self, position: int, modes: list[int]):
        self.position = position
        self.modes = modes
        self.nb_moves = 4

    def execute(self, memory: IntCodeMemory) -> int:
        pass

    def get_next_position(self) -> int:
        return self.position + self.nb_moves


class AddInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        new_value = memory.get(self.position + 1, self.modes[0]) + memory.get(self.position + 2, self.modes[1])
        memory.set(memory.get(self.position + 3, 1), new_value) #Setting is always positional
        return self.get_next_position()


class MultiplyInstruction(Instruction):
    def execute(self, memory: IntCodeMemory):
        new_value = memory.get(self.position + 1, self.modes[0]) * memory.get(self.position + 2, self.modes[1])
        memory.set(memory.get(self.position + 3, 1), new_value) #Setting is always positional
        return self.get_next_position()

class EndInstruction(Instruction):
    def __int__(self, position: int, modes: list[int]):
        super().__init__(position, modes)
        self.nb_parameters = 1
        
    def execute(self, memory: IntCodeMemory):
        memory.output = memory.get(0,1)
        memory.end = True
        return self.get_next_position()
