# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10

from itertools import combinations

word, size = input().split()
for n in range(1,int(size)+1):
    print(*[ "".join(x) for x in list(combinations("".join(sorted(word)),n))], sep="\n")