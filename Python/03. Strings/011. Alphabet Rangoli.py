# Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Score: 20

def print_rangoli(size):
    # your code goes here
    START_LETTER_ASCII_NUM=97
    assert(0<size<27)

    fullset=[chr(x) for x in range(START_LETTER_ASCII_NUM, START_LETTER_ASCII_NUM+size)]
    rang_width=(size+(size-1)*3)

    for i in range(size-1, -size, -1):
        idx = abs(abs(i)-size) - 1
        raw = fullset[size-idx:][::-1] + fullset[size-(idx+1):]
        print("-".join(raw).center(rang_width,'-'))

