from python.libraries.intCode.instructionFactory import create_instruction
from python.libraries.intCode.intCodeMemory import IntCodeMemory


class IntCodeRunner:
    def __init__(self, program: list[int]):
        self.initial_program = program
        self.ongoing = False

    def execute(self, noun: int = None, verb: int = None, inputs: list[int] = None):
        memory = IntCodeMemory(self.initial_program[:])

        if noun is not None:
            memory.set(1, noun)
        if verb is not None:
            memory.set(2, verb)

        self.ongoing = True

        position = 0
        while self.ongoing:
            instruction = create_instruction(position, memory.get(position, 1), inputs)
            position = instruction.execute(memory)
            if memory.end:
                self.ongoing = False

        return memory.output