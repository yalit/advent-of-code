from python.libraries.intCode.intInstruction import AddInstruction, MultiplyInstruction, EndInstruction, Instruction, \
    InputInstruction, OutputInstruction, JumpIfTrueInstruction, JumpIfFalseInstruction, LessThanInstruction, \
    EqualsInstruction

instructions = {
    1: AddInstruction,
    2: MultiplyInstruction,
    3: InputInstruction,
    4: OutputInstruction,
    5: JumpIfTrueInstruction,
    6: JumpIfFalseInstruction,
    7: LessThanInstruction,
    8: EqualsInstruction,
    99: EndInstruction
}

def create_instruction(instruction_code: int) -> Instruction:
    t = list(str(instruction_code))
    operation_code = int(''.join(t[-2:]))
    modes = list(map(int, list(reversed(t))[2:]))

    for _ in range(len(modes), 3):
        modes.append(0)

    try:
        return instructions[operation_code](modes)
    except:
        raise Exception(f'Operation code not handled : {operation_code}')
