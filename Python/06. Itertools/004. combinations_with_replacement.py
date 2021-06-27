# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Score: 10

from itertools import combinations_with_replacement

word, size = input().split()

print(*[ "".join(x) for x in list(combinations_with_replacement("".join(sorted(word)),int(size)))], sep="\n")