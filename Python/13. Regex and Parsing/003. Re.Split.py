# Problem: https://www.hackerrank.com/challenges/re-split/problem
# Score: 20

regex_pattern = r"[,. ]"

import re
print("\n".join(re.split(regex_pattern, input())))