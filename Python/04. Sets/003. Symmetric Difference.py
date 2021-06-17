# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
# Score: 10

if __name__ == '__main__':
    M = int(input())
    a = set(input().split())
    N = int(input())
    b = set(input().split())

    print('\n'.join(map(str, sorted(a^b, key=int))))