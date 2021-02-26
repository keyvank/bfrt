from .opt import optimize
from pybrainfuck.bit8.common import Clear, Put
from pybrainfuck.bit32.common import Put32

class Var:
    def __init__(self, circuit, pos, size, log=True):
        if log:
            pass
            #print("#",pos, size)
            #print(''.join(["1" if b else "0" for b in mem[:20]]))
        self.circuit = circuit
        self.pos = pos
        self.size = size
        for i in range(pos, pos + size):
            self.circuit.mem[i] = True

    def __getitem__(self, ind):
        return Var(self.circuit, self.pos + ind, 1, False)

    def clear(self):
        for i in range(self.size):
            Clear(self.circuit, self[i])

    def free(self):
        for i in range(self.pos, self.pos + self.size):
            self.circuit.mem[i] = False

class Circuit:
    def __init__(self):
        self.pos = 0
        self.code = ""
        self.mem = [False for _ in range(30000)]

    def seek(self, offset):
        self.pos += offset

    def goto(self, cell):
        if self.pos > cell.pos:
            self.emit('<' * (self.pos - cell.pos))
        else:
            self.emit('>' * (cell.pos - self.pos))
        self.pos = cell.pos

    def emit(self, code):
        self.code += code

    def alloc_const8(self, val):
        m = self.alloc(1)
        Put(self, m, val)
        return m

    def alloc_const32(self, val):
        m = self.alloc(4)
        Put32(self, m, val)
        return m

    def alloc(self, size):
        back = self.pos
        back_sz = 0
        front = self.pos
        front_sz = 0
        while back_sz < size and front_sz < size:
            if back >= 0 and not self.mem[back]:
                back_sz += 1
            else:
                back_sz = 0
            if front < 30000 and not self.mem[front]:
                front_sz += 1
            else:
                font_sz = 0
            back -= 1
            front += 1
        if back_sz == size:
            var = Var(self, back + 1, size)
        else:
            var = Var(self, front - size, size)
        var.clear()
        return var

    def compile(self):
        return optimize(self.code)
