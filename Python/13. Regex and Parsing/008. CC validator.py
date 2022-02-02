# Problem: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# Score: 40
"""
► It must start with either 4,5,6
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""

import re

pattern = re.compile(r'(^[456]\d{15}$)|(^[456]\d{3}-\d{4}-\d{4}-\d{4}$)')

for _ in range(int(input())):
    cc = input()
    if pattern.match(cc) and not re.search(r'(\d)\1{3}', cc.replace('-','')):
        print('Valid')
    else:
        print('Invalid')

