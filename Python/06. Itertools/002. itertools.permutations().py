# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Score: 10

from itertools import permutations

str, n = 'HACK', 2
for j in sorted(list(permutations(str, int(n)))):
    print("".join(j))