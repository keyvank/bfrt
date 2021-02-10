from .opt import optimize
class Var:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def __getitem__(self, ind):
        return Var(self.pos + ind, 1)

class Circuit:
    def __init__(self):
        self.pos = 0
        self.next_cell = 0
        self.code = ""
        self.shared = {}

    def pc(self):
        return Var(self.pos)

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

    def new_var(self, size):
        cell = Var(self.next_cell, size)
        self.next_cell += size
        return cell

    def shared_var(self, name, size):
        if name not in self.shared:
            self.shared[name] = self.new_var(size)
        return self.shared[name]

    def compile(self):
        return optimize(self.code)
