from typing import List, Tuple

steps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 2}

class IntCodeComputer:
    def __init__(self, program: List[int], inputs: List[int] = []):
        self.program = program
        self.outputs = []
        self.relative_base = 0
        self.position = 0
        self.end = False
        self.entry = None
        self.inputs = inputs
        self.actions = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base,
            99: self.finish
        }

    def get_instructions(self) -> Tuple[int, Tuple[int, int, int]]:
        t = str(self.get_value(self.position)).zfill(5)
        return int(t[-2:]), (int(t[2]), int(t[1]), int(t[0]))

    def get_addresses(self, operation, modes) -> List[int]:
        addresses = []
        for i in range(1, steps[operation]):
            mode = modes[i - 1]
            if mode == 0:
                addresses.append(self.get_value(self.position + i))
            elif mode == 1:
                addresses.append(self.position + i)
            elif mode == 2:
                addresses.append(self.get_value(self.position + i) + self.relative_base)
        return addresses

    def get_value(self, address: int) -> int:
        if address >= len(self.program):
            for _ in range(len(self.program), address + 1):
                self.program.append(0)
        return self.program[address]

    def set_value(self, address: int, value: int) -> None:
        if address >= len(self.program):
            for _ in range(len(self.program), address + 1):
                self.program.append(0)
        self.program[address] = value

    def add(self, addresses):
        self.set_value(addresses[2], self.get_value(addresses[0]) + self.get_value(addresses[1]))
        return None

    def multiply(self, addresses):
        self.set_value(addresses[2], self.get_value(addresses[0]) * self.get_value(addresses[1]))

    def input(self, addresses):
        if self.entry is not None:
            self.set_value(addresses[0], self.entry)
        elif self.inputs:
            self.set_value(addresses[0], self.inputs.pop(0))
        else:
            self.set_value(addresses[0], int(input("Enter an input : ")))

    def output(self, addresses):
        self.outputs.append(self.get_value(addresses[0]))
        self.position += steps[4]
        return self.outputs

    def jump_if_true(self, addresses):
        if self.get_value(addresses[0]) != 0:
            self.position = self.get_value(addresses[1])
            return "jump"

    def jump_if_false(self, addresses):
        if self.get_value(addresses[0]) == 0:
            self.position = self.get_value(addresses[1])
            return "jump"

    def less_than(self, addresses):
        if self.get_value(addresses[0]) < self.get_value(addresses[1]):
            self.set_value(addresses[2], 1)
        else:
            self.set_value(addresses[2], 0)

    def equals(self, addresses):
        if self.get_value(addresses[0]) == self.get_value(addresses[1]):
            self.set_value(addresses[2], 1)
        else:
            self.set_value(addresses[2], 0)

    def adjust_relative_base(self, addresses):
        self.relative_base += self.get_value(addresses[0])

    def finish(self, addresses):
        self.end = True
        return "end"

    def execute(self, entry = None) -> List[int]:
        self.entry = entry
        while True:
            operation, modes = self.get_instructions()
            addresses = self.get_addresses(operation, modes)

            if operation in self.actions:
                answer = self.actions[operation](addresses)
            else:
                raise ValueError(f"Unknown operation : {operation}, modes : {modes}")

            if answer == "jump":
                continue
            elif answer == "end":
                break
            elif answer is not None:
                return answer
            else:
                pass

            self.position += steps[operation]
        return self.outputs