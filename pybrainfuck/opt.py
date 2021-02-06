def optimize(code):
    while '<>' in code:
        code = code.replace('<>', '')
    while '><' in code:
        code = code.replace('><', '')
    return code
