# Problem: https://www.hackerrank.com/challenges/text-wrap/problem
# Score: 10



def wrap(string, max_width):
    news = ''
    i = 0
    for s in string:
        if i == max_width:
            news += '\n'
            i = 0
        news += s
        i+=1
        
    return news

