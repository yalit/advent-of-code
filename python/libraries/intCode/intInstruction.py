from python.libraries.intCode.intCodeMemory import IntCodeMemory

class Instruction:
    def __init__(self, modes: list[int]):
        self.modes = modes

    def execute(self, memory: IntCodeMemory) -> int:
        pass

    def is_output(self) -> bool:
        return False

class AddInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        new_value = memory.get(memory.position + 1, self.modes[0]) + memory.get(memory.position + 2, self.modes[1])
        memory.set(memory.get(memory.position + 3, 1), new_value) #Setting is always positional
        memory.move_position(4)


class MultiplyInstruction(Instruction):
    def execute(self, memory: IntCodeMemory):
        new_value = memory.get(memory.position + 1, self.modes[0]) * memory.get(memory.position + 2, self.modes[1])
        memory.set(memory.get(memory.position + 3, 1), new_value) #Setting is always positional
        memory.move_position(4)

class InputInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        memory.set(memory.get(memory.position + 1, 1), memory.get_instruction_input())
        memory.move_position(2)

class OutputInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        memory.output = memory.get(memory.position + 1, self.modes[0])
        memory.move_position(2)
    
    def is_output(self) -> bool:
        return True

class JumpIfTrueInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if 0 != memory.get(memory.position + 1, self.modes[0]):
            memory.position = memory.get(memory.position + 2, self.modes[1])
        memory.move_position(3)

class JumpIfFalseInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if 0 == memory.get(memory.position + 1, self.modes[0]):
            memory.position = memory.get(memory.position + 2, self.modes[1])
        memory.move_position(3)

class LessThanInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if memory.get(memory.position + 1, self.modes[0]) < memory.get(memory.position + 2, self.modes[1]):
            memory.set(memory.get(memory.position + 3, 1) ,1)
        else:
            memory.set(memory.get(memory.position + 3, 1), 0)
        memory.move_position(4)

class EqualsInstruction(Instruction):
    def execute(self, memory: IntCodeMemory) -> int:
        if memory.get(memory.position + 1, self.modes[0]) == memory.get(memory.position + 2, self.modes[1]):
            memory.set(memory.get(memory.position + 3, 1) ,1)
        else:
            memory.set(memory.get(memory.position + 3, 1), 0)
        memory.move_position(4)

class EndInstruction(Instruction):
    def execute(self, memory: IntCodeMemory):
        if memory.output is None:
            memory.output = memory.get(0,1)
        memory.end = True
