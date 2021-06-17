# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10

for _ in range(int(input())):
    _, a, _, b = input(), set(input().split()), input(), set(input().split())
    print(len(b-a) == len(b) - len(a))