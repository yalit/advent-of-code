from typing import Optional
from collections import deque


def handle_part_1(lines: list[str]) -> int:
    registers = {}
    sounds = []
    done = False
    i = 0

    def get_val(val: str):
        if val in registers:
            return registers[val]
        return int(val)
    
    while i < len(lines) and not done:
        line = lines[i]
        d = line.split()
        action = register = value = ""

        if len(d) == 2:
            action, register = d
        elif len(d) == 3:
            action, register, value = d

        if register not in registers:
            registers[register] = 0

        if action == "jgz":
            if registers[register] > 0:
                i += get_val(value)
                continue

        if action == 'snd':
            sounds.append(registers[register])

        if action == "rcv":
            if registers[register] > 0:
                sound = sounds.pop()
                print(sound)
                done = True

        if action == 'set':
            registers[register] = get_val(value)

        if action == 'add':
            registers[register] += get_val(value)

        if action == 'mul':
            registers[register] *= get_val(value)

        if action == 'mod':
            registers[register] = registers[register] % get_val(value)

        i += 1

    return 0


class Program:
    def __init__(self, id: int, code: list[list[str]]):
        self.id = id
        self.registers = {'p': id}
        self.code: list[list[str]] = code
        self.pos = 0
        self.queue: list[int] =deque([]) 
        self.target_program: Optional[Program] = None
        self.deadlock: bool = False
        self.nb_send = 0

    def set_target_program(self, program):
        self.target_program = program

    def next_action(self) -> bool:
        d = self.code[self.pos]
        action = register = value = ""

        if len(d) == 2:
            action, register = d
        elif len(d) == 3:
            action, register, value = d

        actions = {
            'add': self.add,
            'mul': self.mult,
            'set': self.set,
            'snd': self.send,
            'mod': self.mod,
            'rcv': self.receive,
            'jgz': self.jump
        }
 
        if actions[action](register, value):
            self.pos += 1
        return self.deadlock

    def send(self, value: str, register:str) -> bool:
        if not self.target_program:
            return True
        self.target_program.acquire(self.get_value(value))
        self.nb_send +=1
        return True
 
    def acquire(self, value: int):
        self.queue.append(value)
   
    def receive(self, register, value: str):
        if len(self.queue) == 0:
            self.deadlock = True
            return False
       
        self.set(register, str(self.queue.popleft()))
        self.deadlock = False
        return True
 
    def add(self, register: str, value: str) -> bool:
        self.registers[register] += self.get_value(value)
        return True
 
    def mult(self, register: str, value: str) -> bool:
        self.registers[register] *= self.get_value(value)
        return True
 
    def jump(self, register: str, value: str) -> bool:
        if self.get_value(register) > 0:
            self.pos += self.get_value(value)
            return False
        return True
 
    def mod(self, register: str, value: str) -> bool:
        self.registers[register] = self.registers[register] % self.get_value(value)
        return True
 
    def set(self, register: str, value: str) -> bool:
        self.registers[register] = self.get_value(value)
        return True
 
    def get_value(self, value:str):
        if value in self.registers:
            return self.registers[value]
        return int(value)

def handle_part_2(lines: list[str]) -> int:
    registers = {}
    program_A = Program(0, [l.split() for l in lines])
    program_B = Program(1, [l.split() for l in lines])
    program_A.set_target_program(program_B)
    program_B.set_target_program(program_A)
     
    deadlock = False
     
    while not deadlock:
        a_deadlock = program_A.next_action()
        b_deadlock = program_B.next_action()
        deadlock = a_deadlock and b_deadlock
     
    return program_B.nb_send
