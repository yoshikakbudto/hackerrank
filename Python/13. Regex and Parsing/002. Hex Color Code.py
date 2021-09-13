# Problem: https://www.hackerrank.com/challenges/hex-color-code/problem
# Score: 30

import re

code=''

for _ in range(int(input())):
    code += input()
    pattern = re.compile('[:, ](#[0-9A-Fa-f]{6})|[:, ](#[0-9A-Fa-f]{3})')

result=re.findall(pattern, code)

for x in result:
    print('{}{}'.format(x[0],x[1]))