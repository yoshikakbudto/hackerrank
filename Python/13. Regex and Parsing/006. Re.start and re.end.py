# Problem: https://www.hackerrank.com/challenges/re-start-re-end/problem
# Score: 20

import re

s,k=input(), re.compile(input())
#s, k = 'a', re.compile('b')

"""
iterate through the string
"""
start_pos = -1

while(True):
    m = k.search(s, start_pos)
    if start_pos < 0 and not m:
        print((-1, -1))
        break
    elif m:
        print((m.start(), m.end()-1))
        start_pos = m.start() + 1
    else:
        break
