# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20

from itertools import groupby

print(*[(len(tuple(k)), int(j)) for j, k in groupby(input())])
