# Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Score: 20

import re

patt = re.compile(r'[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]', re.IGNORECASE)
s = 'abeeciidoofuue'
s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
s= 'match a single character not present in the list below'
i=0
l=[]

while(True):
    r=patt.search(s[i:])
    try:
        i += r.end() - 1
        l.append(r.groups()[0])
    except AttributeError:
        break

if l:
    print(*l,sep='\n')
else:
    print(-1)