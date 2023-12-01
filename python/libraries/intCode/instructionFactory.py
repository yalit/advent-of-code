from python.libraries.intCode.intInstruction import AddInstruction, MultiplyInstruction, EndInstruction, Instruction, \
    InputInstruction, OutputInstruction, JumpIfTrueInstruction, JumpIfFalseInstruction, LessThanInstruction, \
    EqualsInstruction


def create_instruction(instruction_code: int) -> Instruction:
    t = list(str(instruction_code))
    operation_code = int(''.join(t[-2:]))
    modes = list(map(int, list(reversed(t))[2:]))

    match operation_code:
        case 1:
            for _ in range(len(modes), 3):
                modes.append(0)
            return AddInstruction(modes)

        case 2:
            for _ in range(len(modes), 3):
                modes.append(0)
            return MultiplyInstruction(modes)

        case 3:
            for _ in range(len(modes), 1):
                modes.append(0)

            return InputInstruction(modes)

        case 4:
            for _ in range(len(modes), 1):
                modes.append(0)
            return OutputInstruction(modes)

        case 5:
            for _ in range(len(modes), 2):
                modes.append(0)
            return JumpIfTrueInstruction(modes)

        case 6:
            for _ in range(len(modes), 2):
                modes.append(0)
            return JumpIfFalseInstruction(modes)

        case 7:
            for _ in range(len(modes), 3):
                modes.append(0)
            return LessThanInstruction(modes)

        case 8:
            for _ in range(len(modes), 3):
                modes.append(0)
            return EqualsInstruction(modes)

        case 99:
            return EndInstruction(modes)

    raise Exception(f'Operation code not handled : ${operation_code}')
