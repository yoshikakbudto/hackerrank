# Problem: https://www.hackerrank.com/challenges/python-lists/problem
# Score: 10

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        cmd = input().split()
        if cmd[0] == 'print':
            print(l)
        else:
            getattr(l, cmd[0])(*map(int, cmd[1:]))
        