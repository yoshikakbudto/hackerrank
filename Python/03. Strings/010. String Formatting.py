# Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Score: 10

def print_formatted(number):
    # your code goes here
    pads=len(f"{number:b}")
    for n in range(1,number+1):
        print(f"{n:{pads}d} {n:>{pads}o} {n:>{pads}X} {n:>{pads}b}")

