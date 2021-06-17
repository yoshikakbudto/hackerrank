# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Score: 10

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
s_sorted=sorted(students, key = lambda s: s[1])

# skip 1st equal-graded students
idx=1
for i in s_sorted[1:]:
    if s_sorted[0][1] == i[1]:
        idx += 1
    else:
        break

s_last = [s_sorted[idx],]
for s in s_sorted[idx+1:]:
    if s[1] == s_last[0][1]:
        s_last.append(s)
    else:
        break
    
finale=sorted(s_last, key=lambda s: s[0])
for i in finale:
    print(i[0])
