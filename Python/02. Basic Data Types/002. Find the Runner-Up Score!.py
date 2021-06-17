# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(list(dict.fromkeys(arr)))[-2])