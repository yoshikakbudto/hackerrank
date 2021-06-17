# Problem: https://www.hackerrank.com/challenges/py-set-union/problem
# Score: 10

_ = input()
a = set(input().split())
_ = input()
b = set(input().split())
print(len(a|b))
