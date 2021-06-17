# Problem: https://www.hackerrank.com/challenges/write-a-function/problem
# Score: 10

def is_leap(year):
    # Write your logic here
    if year <= 1900:
        return False
    
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False
