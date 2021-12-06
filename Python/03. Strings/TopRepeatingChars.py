"""
print the most repeatable sequence of each given letters
i.e.: for "abcaabbb" print a:2,b:3,c:1
"""
some: str = "cddceeffccdddd"
cnt: int = 1
db: dict = {}

for i in range(len(some)):
    try:
        if some[i] == some[i+1]:
            cnt += 1
        else:
            if not some[i] in db.keys() or db[some[i]] < cnt:
                db[some[i]] = cnt
            cnt = 1
    except IndexError:
        if not some[i] in db.keys() or db[some[i]] < cnt:
            db[some[i]] = cnt
        break

print(db)