#!/usr/bin/python3

import io
import sys

with io.open(sys.argv[1]) as f:
    code = f.read()

mappings = {
    ".": "putchar(*ptr);",
    ",": "*ptr=getchar();",
    "[": "while (*ptr) {",
    "]": "}"
}

with io.open(sys.argv[2], "w") as f:
    f.write("#include <stdlib.h>\n")
    f.write("#include <stdio.h>\n")
    f.write("int main() {")
    f.write("unsigned char *data = (unsigned char *)malloc(30000);");
    f.write("for(unsigned int i = 0; i < 30000; i++) data[i] = 0;")
    f.write("unsigned char *ptr = data;")
    moving = 0
    adding = 0
    for ch in code:
        if ch in ['<', '>']:
            if ch == '>':
                moving = moving + 1 if moving else 1
            else:
                moving = moving - 1 if moving else -1
        elif moving:
            f.write("ptr += {};".format(moving))
            moving = 0

        if ch in ['+', '-']:
            if ch == '+':
                adding = adding + 1 if adding else 1
            else:
                adding = adding - 1 if adding else -1
        elif adding:
            f.write("*ptr += {};".format(adding))
            adding = 0

        if ch in mappings:
            f.write(mappings[ch])

    f.write("}")
