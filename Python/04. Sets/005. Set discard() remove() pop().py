# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Score: 10

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    inpt = input().split()
    cmd = inpt[0]
    try:
        arg = inpt[1]
    except IndexError:
        arg=''
    eval(f's.{cmd}({arg})')
print(sum(s))
