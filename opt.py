import sys
import re

code = sys.stdin.read()
code = code.replace('while (*ptr) {*ptr += -1;}','*ptr = 0;')

code = re.sub(r'while \(\*ptr\) \{\*ptr \+\= -1;ptr \+\= -(\d+);\*ptr \+\= 1;ptr \+\= \1;\}', r'*(ptr - \1) += *ptr; *ptr = 0;', code)
code = re.sub(r'while \(\*ptr\) \{\*ptr \+\= -1;ptr \+\= (\d+);\*ptr \+\= 1;ptr \+\= -\1;\}', r'*(ptr + \1) += *ptr; *ptr = 0;', code)

code = re.sub(r'while \(\*ptr\) \{ptr \+\= -(\d+);\*ptr \+\= 1;ptr \+\= \1;\*ptr \+\= -1;\}', r'*(ptr - \1) += *ptr; *ptr = 0;', code)
code = re.sub(r'while \(\*ptr\) \{ptr \+\= (\d+);\*ptr \+\= 1;ptr \+\= -\1;\*ptr \+\= -1;\}', r'*(ptr + \1) += *ptr; *ptr = 0;', code)

print(code)
