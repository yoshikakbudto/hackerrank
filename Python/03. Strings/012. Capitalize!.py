# Problem:  https://www.hackerrank.com/challenges/capitalize/problem
# Score: 20

def solve(s):
    return re.sub(r"(^|\s)([a-z])",lambda x: "{}{}".format(x.group(1),x.group(2).upper()),s)