from python.libraries.intCode.instructionFactory import create_instruction
from python.libraries.intCode.intCodeMemory import IntCodeMemory


class IntCodeRunner:
    def __init__(self, program: list[int]):
        self.initial_program = program
        self.ongoing = False

    def execute(self, noun: int = None, verb: int = None, program_inputs: list[int] = None):
        memory = IntCodeMemory(self.initial_program[:], program_inputs)

        if noun is not None:
            memory.set(1, noun)
        if verb is not None:
            memory.set(2, verb)

        self.ongoing = True

        while self.ongoing:
            instruction = create_instruction(memory.get(memory.position, 1))
            # print(instruction)
            # print("Position: ",memory.position)
            # print("Program value:", memory.program[memory.position])
            # print("modes: ", instruction.modes)
            # print("Program: ", len(memory.program), memory.program)
            instruction.execute(memory)

            if memory.end:
                self.ongoing = False

        return memory.output
