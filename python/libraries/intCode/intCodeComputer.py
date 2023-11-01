class IntCodeComputer:
    def __init__(self, program: list[int], ):
        self.initialProgram = program

    def execute(self, noun: int, verb: int):
        program = self.initialProgram[:]
        program[1] = noun
        program[2] = verb

        c_pos = 0
        action = program[c_pos]
        while action != 99:
            if action == 1:
                program[program[c_pos + 3]] = program[program[c_pos + 1]] + program[program[c_pos + 2]]
            else:
                program[program[c_pos + 3]] = program[program[c_pos + 1]] * program[program[c_pos + 2]]
            c_pos += 4
            action = program[c_pos]

        return program[0]