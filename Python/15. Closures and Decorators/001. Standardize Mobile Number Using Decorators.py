# Problem: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# Score: 30

def wrapper(f):
    def fun(l):
        new_list = []
        for str_num in l:
            num = int(str_num.replace('+',''))
            if num > 9999999999: # 91 prefixed
                num -= 910000000000
            new_list.append(f'+91 {num//100000} {num-(num//100000)*100000}')
        f(new_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)