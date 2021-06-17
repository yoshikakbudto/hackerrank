# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Score: 10

a=set(map(int,input().split()))
for _ in range(int(input())):
    if not a.issuperset(set(map(int,input().split()))):
        print(False)
        exit()
print(True)