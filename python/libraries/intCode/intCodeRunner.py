from python.libraries.intCode.instructionFactory import create_instruction
from python.libraries.intCode.intCodeMemory import IntCodeMemory


class IntCodeRunner:
    def __init__(self, program: list[int]):
        self.initial_program = program
        self.ongoing = False

    def execute(self, noun: int = None, verb: int = None, program_inputs: list[int] = None):
        memory = IntCodeMemory(self.initial_program[:], program_inputs)
        instruction_input = None if program_inputs is None else program_inputs[0]

        if noun is not None:
            memory.set(1, noun)
        if verb is not None:
            memory.set(2, verb)

        self.ongoing = True

        position = 0
        while self.ongoing:
            print(memory.position, memory.program[memory.position:memory.position+5])
            instruction = create_instruction(memory.get(memory.position, 1))
            instruction.execute(memory)

            if memory.end:
                self.ongoing = False

        return memory.output
