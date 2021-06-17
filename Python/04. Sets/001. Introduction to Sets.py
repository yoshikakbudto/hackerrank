# Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Score: 10

def average(array):
    res = sum(set(array))/len(set(array))
    return(f"{res:.3f}")
