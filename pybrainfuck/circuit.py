from .opt import optimize
class Cell:
    def __init__(self, pos):
        self.pos = pos

class Circuit:
    def __init__(self):
        self.pos = 0
        self.next_cell = 0
        self.code = ""
        self.shared = {}

    def pc(self):
        return Cell(self.pos)

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

    def new_cell(self):
        cell = Cell(self.next_cell)
        self.next_cell += 1
        return cell

    def new_cells(self, n):
        return [self.new_cell() for i in range(n)]

    def shared_cell(self, name):
        if name not in self.shared:
            self.shared[name] = self.new_cell()
        return self.shared[name]

    def shared_cells(self, name, n):
        if name not in self.shared:
            self.shared[name] = self.new_cells(n)
        return self.shared[name]

    def compile(self):
        return optimize(self.code)
