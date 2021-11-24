# Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Score: 20
# The re-worked version. After i've learned of a positive/negative lookbehind/lookahead assertions in regex

import re

cns = 'qwrtypsdfghjklzxcvbnm'

patt=re.compile('(?<=['+cns+'])([aeiou]{2,})(?=['+cns+'])', re.I)
result = patt.findall(input())
print("\n".join(result or ['-1']))