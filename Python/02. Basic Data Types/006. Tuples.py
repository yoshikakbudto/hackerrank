# Problem: https://www.hackerrank.com/challenges/python-tuples/problem
# Score: 10


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))