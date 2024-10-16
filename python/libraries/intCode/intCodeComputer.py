from typing import List, Tuple

steps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 2}


class IntCodeComputer:
    def __init__(self, program: List[int]):
        self.program = program
        self.outputs = []
        self.relative_base = 0
        self.position = 0
        self.end = False

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

    def execute(self, entry = None) -> List[int]:
        while True:
            operation, modes = self.get_instructions()
            addresses = self.get_addresses(operation, modes)

            if operation == 1:
                self.set_value(addresses[2], self.get_value(addresses[0]) + self.get_value(addresses[1]))

            elif operation == 2:
                self.set_value(addresses[2], self.get_value(addresses[0]) * self.get_value(addresses[1]))

            elif operation == 3:
                if entry is not None:
                    self.set_value(addresses[0], entry)
                else:
                    self.set_value(addresses[0], int(input("Enter an input : ")))

            elif operation == 4:
                self.outputs.append(self.get_value(addresses[0]))
                self.position += steps[operation]
                return self.outputs

            elif operation == 5:
                if self.get_value(addresses[0]) != 0:
                    self.position = self.get_value(addresses[1])
                    continue

            elif operation == 6:
                if self.get_value(addresses[0]) == 0:
                    self.position = self.get_value(addresses[1])
                    continue

            elif operation == 7:
                if self.get_value(addresses[0]) < self.get_value(addresses[1]):
                    self.set_value(addresses[2], 1)
                else:
                    self.set_value(addresses[2], 0)

            elif operation == 8:
                if self.get_value(addresses[0]) == self.get_value(addresses[1]):
                    self.set_value(addresses[2], 1)
                else:
                    self.set_value(addresses[2], 0)

            elif operation == 9:
                self.relative_base += self.get_value(addresses[0])

            elif operation == 99:
                self.end = True
                break

            else:
                raise Exception("Not known operation")

            self.position += steps[operation]
        return self.outputs