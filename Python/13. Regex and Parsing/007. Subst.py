# Problem: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Score: 20

import re

def fmt_and(match_obj) -> str:
    """Substitute ' || ' and ' && ' with words."""
    if match_obj[0] == '||':
        return('or')
    else:
        return('and')

for _ in range(int(input())):
    input_string = input()
    res = re.sub( r'(?<= )(&&|\|\|)(?= )', fmt_and, input_string )
    print(res)
