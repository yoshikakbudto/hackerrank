# Problem: https://www.hackerrank.com/challenges/string-validators/problem
# Score: 10

def checkalnum(s):
    for i in s:
        if i.isalnum():
            return True
    return False

def checkalfa(s):
    for i in s:
        if i.isalpha():
            return True
    return False

def checkdigit(s):
    for i in s:
        if i.isdigit():
            return True
    return False

def checklocase(s):
    for i in s:
        if i.islower():
            return True
    return False

def checkuppercase(s):
    for i in s:
        if i.isupper():
            return True
    return False
    
if __name__ == '__main__':
    s = input()
    print(checkalnum(s))
    print(checkalfa(s))
    print(checkdigit(s))
    print(checklocase(s))
    print(checkuppercase(s))
