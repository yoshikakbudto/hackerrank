# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Score: 20

from collections import defaultdict

d = defaultdict(list)

size_a, size_b = map(int, input().split())
for _ in range(size_a):
    d['set_a'].append(input())

for _ in range(size_b):
    key = input()
    if key in d['set_a']:
        print(*[i+1 for i,j in enumerate(d['set_a']) if j == key])
    else:
        print(-1)