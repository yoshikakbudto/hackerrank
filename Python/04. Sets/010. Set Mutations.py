# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Score: 10

_, A = input(), set(map(int, input().split()))
for _ in range(int(input())):
    op, B = input().split()[0], set(map(int, input().split()))
    eval('A.{}(B)'.format(op))
    
print(sum(A))
