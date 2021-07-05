# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
# Score: 20

from itertools import groupby

final=""
for j, k in groupby(input()):
    final+="({}, {}) ".format(len([x for x in k]), j)

print(final.rstrip())
