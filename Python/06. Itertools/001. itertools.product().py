# Problem:  https://www.hackerrank.com/challenges/itertools-product/problem
# Score: 10

from itertools import product

a, b = map(int, input().split()), map(int, input().split())
print(*list(product(a, b)))
