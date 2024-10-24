from python.libraries.intCode.intCodeComputer import IntCodeComputer


class InputRequestIntCodeComputer(IntCodeComputer):
    def input(self, addresses):
        if self.entry is not None:
            self.set_value(addresses[0], self.entry)
            self.entry = None
        else:
            return "Input"