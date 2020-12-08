class Interpret():

    def __init__(self, data):
        self.instructions = self.parse(data)
        self.def_instructions = self.parse(data)
        self.accumulator = 0

    def parse(self, data):
        return [item.split(' ') for item in data.split('\n')]

    def execute(self):
        position = 0
        executed = set()
        while position not in executed:
            executed.add(position)
            opcode = self.instructions[position]
            if opcode[0] == 'acc':
                self.accumulator += int(opcode[1])
                position += 1
            elif opcode[0] == 'jmp':
                position += int(opcode[1])
            elif opcode[0] == 'nop':
                position += 1
        return self.accumulator

    def repair(self):
        for i, opcode in enumerate(self.instructions):
            if opcode[0] != 'acc' and int(opcode[1]) != 0:
                self.instructions = self.def_instructions[:]
                if opcode[0] == 'nop':
                    opcode[0] = 'jmp'
                elif opcode[0] == 'jmp':
                    opcode[0] = 'nop'
                self.instructions[i] = opcode
                try:
                    self.accumulator = 0
                    self.execute()
                except:
                    return self.accumulator


ex = Interpret(open('input.txt', 'r').read())

print(ex.execute(), ex.repair())
