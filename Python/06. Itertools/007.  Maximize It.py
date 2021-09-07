# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50

from itertools import product
n, m = map(int, input().split())


l = [ tuple(map(lambda x: int(x)**2, input().split()[1:])) for _ in range(n) ]
print(max(tuple(map(lambda x: sum(x)%m, tuple(product(*l))))))
