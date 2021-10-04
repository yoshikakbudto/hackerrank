# Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Score: 20

import numpy as np

def fibonacci(n):
    """Return n fibonacci numbers. Solved with matrixes magic.

    we'll use matrix exponentiation to solve the Fibonacci number by its position.
        we just need to raise the given matrix into its place number.
    """
    matrix = np.array([[0,1],[1,1]])
    return(list(map(lambda x: np.linalg.matrix_power(matrix, x+1)[0][0], range(n))))


def fibonacci0(n):
    """Return n fibonacci numbers.
    """
    # pre-cache 1st numbers wich are always the same
    fibonacis = [0, 1, 1]
    for x in range(3, n):
        fibonacis.append(sum(fibonacis[x-2:x]))

    return(fibonacis[:n])


cube = lambda x: x ** 3

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))