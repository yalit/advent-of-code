class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def pop(self):
        if self.len() == 0:
            return None

        popped = self.stack[-1]
        self.stack = self.stack[0:-1]
        return popped

    def len(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]