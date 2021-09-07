# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50
"""
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

206
"""

from itertools import product
n, m = map(int, input().split())


l = [ tuple(map(lambda x: int(x)**2, input().split()[1:])) for _ in range(n) ]

print(list(l))
#print(max(tuple(map(lambda x: sum(x)%m, tuple(product(*l))))))
