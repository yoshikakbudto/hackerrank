# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10

"""
I suggested that if the list is sorted, then every 1st element of the group should be equal to the next one. 
if not, then the 1st element is unique and it is a captains room number. 
If the captain's room is the last one in the list, then just print it when all groups went through
"""
groups_num, rooms = int(input()), input().split()
rooms.sort()

for i in range(len(rooms)//groups_num):
    if rooms[groups_num*i] == rooms[groups_num*i + 1]:
        continue
    else:
        print(rooms[groups_num*i])
        exit()
print(*rooms[-1:])