from python.libraries.intCode.intInstruction import AddInstruction, MultiplyInstruction, EndInstruction, Instruction

def create_instruction(position: int, instruction_code: int, instruction_input: int = None) -> Instruction:
    t = list(str(instruction_code))
    operation_code = int(''.join(t[-2:]))
    modes = list(map(int, list(reversed(t))[2:]))

    match operation_code:
        case 1:
            for _ in range(len(modes), 3):
                modes.append(0)
            return AddInstruction(position, modes)
        case 2:
            for _ in range(len(modes), 3):
                modes.append(0)
            return MultiplyInstruction(position, modes)
        case 99:
            return EndInstruction(position, modes)

    raise Exception(f'Operation code not handled : ${operation_code}')