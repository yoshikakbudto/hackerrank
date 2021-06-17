# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50

n, m = input().split()
numbers = input().split()
A = set(input().split())
B = set(input().split())

happiness = 0
for i in numbers:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
        
print(happiness)