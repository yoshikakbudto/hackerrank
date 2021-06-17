# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Score: 10

n,m=input().split()
n=int(n)
m=int(m)

for y in range(0, int(n/2)):
    dotpipes=y*2 + 1
    dashes=int(m/2) - 1 - (y*3)
    print('-'*dashes + '.|.'*dotpipes + '-'*dashes)

dashes=int(m/2-3)
print('-'*dashes + 'WELCOME' + '-'*dashes)

for y in range(int(n/2)-1, -1, -1):
    dotpipes=y*2 + 1
    dashes=int(m/2) - 1 - (y*3)
    print('-'*dashes + '.|.'*dotpipes + '-'*dashes)

