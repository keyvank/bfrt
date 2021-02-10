import re
from .common import Copy

def create_func(inps, temps, src):
    tokens = list(re.findall(r'(?:[\<\>\+\-\.\,\[\]]+|\w+)', src))
    code = "def F(circuit, {}):\n".format(', '.join(inps))
    for (temp, sz) in temps:
        code += "   {} = circuit.shared_var('_{}', {})[0]\n".format(temp, "CREATE_FUNC_" + str(hash((src, temp))), sz)
    for t in tokens:
        if t.isalnum():
            code += "   circuit.goto({})\n".format(t)
        else:
            code += "   circuit.emit('{}')\n".format(t)

    ldict = {}
    exec(code, None, ldict)
    return ldict['F']

def inplace_to_stable(inplace):
    def stable(*args):
        circuit = args[0]
        result = circuit.shared_var("INPLACE_TO_STABLE_" + str(hash(inplace)), 1)
        Copy(circuit, args[2], result)
        inplace(*[args[0], result, *args[3:]])
        Copy(circuit, result, args[1])
    return stable
