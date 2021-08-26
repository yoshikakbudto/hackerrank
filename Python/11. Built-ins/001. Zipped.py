# Problem: https://www.hackerrank.com/challenges/zipped/problem
# Score: 10

_, subjects_num = map(int, input().split())

marks = zip(*[map(float, input().split()) for _ in range(subjects_num)])
print(*['{:.1f}'.format(sum(x)/subjects_num) for x in marks], sep='\n')
