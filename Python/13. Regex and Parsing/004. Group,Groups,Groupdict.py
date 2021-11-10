# Problem: https://www.hackerrank.com/challenges/re-group-groups/problem
# Score: 20

import re
try:
    print(re.search(r'([0-9a-zA-Z])\1', input()).group()[0])
except AttributeError:
    print(-1)