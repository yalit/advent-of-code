from python.libraries.intCode.intInstruction import AddInstruction, MultiplyInstruction, EndInstruction, Instruction, \
    InputInstruction, OutputInstruction, JumpIfTrueInstruction, JumpIfFalseInstruction, LessThanInstruction, \
    EqualsInstruction


def create_instruction(position: int, instruction_code: int, instruction_input: int = None) -> Instruction:
    t = list(str(instruction_code))
    operation_code = int(''.join(t[-2:]))
    modes = list(map(int, list(reversed(t))[2:]))

    match operation_code:
        case 1:
            for _ in range(len(modes), 3):
                modes.append(0)
            return AddInstruction(position, modes, instruction_input)

        case 2:
            for _ in range(len(modes), 3):
                modes.append(0)
            return MultiplyInstruction(position, modes, instruction_input)

        case 3:
            for _ in range(len(modes), 1):
                modes.append(0)
            if instruction_input is None:
                raise Exception("Instruction input should not be None")

            return InputInstruction(position, modes, instruction_input)

        case 4:
            for _ in range(len(modes), 1):
                modes.append(0)
            return OutputInstruction(position, modes, instruction_input)

        case 5:
            for _ in range(len(modes), 2):
                modes.append(0)
            return JumpIfTrueInstruction(position, modes, instruction_input)

        case 6:
            for _ in range(len(modes), 2):
                modes.append(0)
            return JumpIfFalseInstruction(position, modes, instruction_input)

        case 7:
            for _ in range(len(modes), 3):
                modes.append(0)
            return LessThanInstruction(position, modes, instruction_input)

        case 8:
            for _ in range(len(modes), 3):
                modes.append(0)
            return EqualsInstruction(position, modes, instruction_input)

        case 99:
            return EndInstruction(position, modes)

    raise Exception(f'Operation code not handled : ${operation_code}')