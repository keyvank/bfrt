import sys
import re

code = sys.stdin.read()
code = code.replace('w(*p){*p+=-1;}','*p=0;')

code = re.sub(r'w\(\*p\)\{\*p\+\=-1;p\+\=-(\d+);\*p\+\=1;p\+\=\1;\}',r'*(p-\1)+=*p;*p=0;', code)
code = re.sub(r'w\(\*p\)\{\*p\+\=-1;p\+\=(\d+);\*p\+\=1;p\+\=-\1;\}',r'*(p+\1)+=*p;*p=0;', code)

code = re.sub(r'w\(\*p\)\{p\+\=-(\d+);\*p\+\=1;p\+\=\1;\*p\+\=-1;\}',r'*(p-\1)+=*p;*p=0;', code)
code = re.sub(r'w\(\*p\)\{p\+\=(\d+);\*p\+\=1;p\+\=-\1;\*p\+\=-1;\}',r'*(p+\1)+=*p;*p=0;', code)

print(code)
