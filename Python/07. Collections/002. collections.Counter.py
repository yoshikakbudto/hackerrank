# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10

from collections import Counter
_, shoes = input(), Counter(input().split())

profit = 0
for i in range(int(input())):
    size, price = input().split()
    if shoes[size] > 0:
        profit += int(price)
        shoes[size] -= 1
print(profit)
