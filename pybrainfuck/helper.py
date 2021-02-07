import re

def create_func(inps, temps, code):
    tokens = list(re.findall(r'(?:[\<\>\+\-\.\,\[\]]+|\w+)', code))
    code = "def F(circuit, {}):\n".format(', '.join(inps))
    for temp in temps:
        code += "   {} = circuit.shared_cell('_{}')\n".format(temp, temp.upper())

    for t in tokens:
        if t.isalnum():
            code += "   circuit.goto({})\n".format(t)
        else:
            code += "   circuit.emit('{}')\n".format(t)

    ldict = {}
    exec(code, None, ldict)
    return ldict['F']
