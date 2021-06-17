# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Score: 10

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([ [r1, r2, r3] for r1 in range(x+1) for r2 in range(y+1) for r3 in range(z+1) if r1+r2+r3 != n])