# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Score: 40

from itertools import combinations

_, el, grp_size = input(), input().replace(" ",""), int(input())
 
combs = tuple(combinations(el, grp_size))

# True assumed as 1 when being sumed
matches = sum(map(lambda x: 'a' in x, combs))

print(matches/len(combs))