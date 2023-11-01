from python.libraries.intCode.intCodeMemory import IntCodeMemory

class Instruction:
    def __init__(self, position: int, modes: list[int], instruction_input: int = None):
        self.position = position
        self.modes = modes
        self.instruction_input = instruction_input

    def execute(self, memory: IntCodeMemory) -> int:
        pass

    def get_next_position(self, nb_moves) -> int:
        return self.position + nb_moves


class AddInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        new_value = memory.get(self.position + 1, self.modes[0]) + memory.get(self.position + 2, self.modes[1])
        memory.set(memory.get(self.position + 3, 1), new_value) #Setting is always positional
        return self.get_next_position(4)


class MultiplyInstruction(Instruction):
    def execute(self, memory: IntCodeMemory):
        new_value = memory.get(self.position + 1, self.modes[0]) * memory.get(self.position + 2, self.modes[1])
        memory.set(memory.get(self.position + 3, 1), new_value) #Setting is always positional
        return self.get_next_position(4)

class InputInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        memory.set(memory.get(self.position + 1, 1), self.instruction_input)
        return self.get_next_position(2)

class OutputInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        memory.output = memory.get(self.position + 1, self.modes[0])
        return self.get_next_position(2)

class JumpIfTrueInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if 0 != memory.get(self.position + 1, self.modes[0]):
            return memory.get(self.position + 2, self.modes[1])
        return self.get_next_position(3)

class JumpIfFalseInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if 0 == memory.get(self.position + 1, self.modes[0]):
            return memory.get(self.position + 2, self.modes[1])
        return self.get_next_position(3)

class LessThanInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if memory.get(self.position + 1, self.modes[0]) < memory.get(self.position + 2, self.modes[1]):
            memory.set(memory.get(self.position + 3, 1) ,1)
        else:
            memory.set(memory.get(self.position + 3, 1), 0)
        return self.get_next_position(4)

class EqualsInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if memory.get(self.position + 1, self.modes[0]) == memory.get(self.position + 2, self.modes[1]):
            memory.set(memory.get(self.position + 3, 1) ,1)
        else:
            memory.set(memory.get(self.position + 3, 1), 0)
        return self.get_next_position(4)

class EndInstruction(Instruction):
    def execute(self, memory: IntCodeMemory):
        if memory.output is None:
            memory.output = memory.get(0,1)
        memory.end = True
        return self.get_next_position(0)
