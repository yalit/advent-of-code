def handle_part_1(lines: list[str]) -> int:
    mem = Memory()

    for l in lines:
        instructions = l.split()

        if instructions[1] == 'inc':
            mem.inc(instructions[0], int(instructions[2]), instructions[4:])        
        
        if instructions[1] == 'dec':
            mem.dec(instructions[0], int(instructions[2]), instructions[4:])

    return mem.get_max()


def handle_part_2(lines: list[str]) -> int:
    mem = Memory()
    maximum = 0

    for l in lines:
        instructions = l.split()

        if instructions[1] == 'inc':
            mem.inc(instructions[0], int(instructions[2]), instructions[4:])        
        
        if instructions[1] == 'dec':
            mem.dec(instructions[0], int(instructions[2]), instructions[4:])
        maximum = max(maximum, mem.get_max())
    return maximum

class Memory:
    def __init__(self) -> None:
        self.registers = {}

    def __str__(self) -> str:
        return " / ".join([a+":"+str(n) for a, n in self.registers.items()])
    
    def get_max(self):
        return max([n for _,n in self.registers.items()])

    def check_if_exists(self, register):
        if register not in self.registers:
            self.registers[register] = 0

    def inc(self, register, value, condition_data):
        self.check_if_exists(register)
        if self.can_operate(condition_data[0], condition_data[1], condition_data[2]):
            self.registers[register] += value
    
    def dec(self, register, value, condition_data):
        self.check_if_exists(register)
        
        if self.can_operate(condition_data[0], condition_data[1], condition_data[2]):
            self.registers[register] -= value
    
    def get(self, register):
        self.check_if_exists(register)
        return self.registers[register]
    
    def can_operate(self, register, condition, value):
        self.check_if_exists(register)

        if condition == '<':
            return self.registers[register] < int(value)
        
        if condition == '<=':
            return self.registers[register] <= int(value)
        
        if condition == '>=':
            return self.registers[register] >= int(value)

        if condition == '>':
            return self.registers[register] > int(value)
        
        if condition == '==':
            return self.registers[register] == int(value)

        if condition == '!=':
            return self.registers[register] != int(value)
