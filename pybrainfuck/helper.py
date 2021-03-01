import re

def create_func(inps, temps, src):
    tokens = list(re.findall(r'(?:[\<\>\+\-\.\,\[\]]+|\w+)', src))
    code = "def F(circuit, {}):\n".format(', '.join(inps))
    for (temp, sz) in temps:
        code += "   {} = circuit.alloc({})[0]\n".format(temp, sz)
    for t in tokens:
        if t.isalnum():
            code += "   circuit.goto({})\n".format(t)
        else:
            code += "   circuit.emit('{}')\n".format(t)
    for (temp, sz) in temps:
        code += "   {}.free()\n".format(temp)
    ldict = {}
    exec(code, None, ldict)
    return ldict['F']

def inplace_to_stable(inplace):
    from .bit8.common import Copy
    def stable(*args):
        circuit = args[0]
        result = circuit.alloc(1)
        Copy(circuit, result, args[2])
        inplace(*[args[0], result, *args[3:]])
        Copy(circuit, args[1], result)
        result.free()
    return stable
