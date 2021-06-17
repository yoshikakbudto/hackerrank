# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10

def count_substring(string, sub_string):
    i = 0
    c = 0
    while i != -1:
        i = string.find(sub_string, i + c)
        if i > -1:
            c += 1
    return c