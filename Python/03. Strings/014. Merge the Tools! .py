# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Score: 40

def merge_the_tools(s, k):
    for j in [ s[i:i+k] for i in range(0, len(s), k) ]:
        print("".join(list(dict.fromkeys(j))))