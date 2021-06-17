# Problem: https://www.hackerrank.com/challenges/py-set-add/problem
# Score: 10

N = int(input())
cards = set()
while N>0:
    cards.add(input())
    N-=1

print(len(cards))
