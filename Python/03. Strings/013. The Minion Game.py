# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem
# Score: 40

"""
 Iterations:
 1. At 1st i try to simply string.count() method, but it
     doesnt respect overlapping substrings.
 2. sum(1 for i in range(len(string))if string.startswith(pattern, i))
    up to 2sec on small dataset
 3. as above, but use numpy's startwith
    up to 20sec on small dataset
 4. Switched to pypy3 and the speed sky rocketed up to 0.4 sec.
     But the time limit for pypy3 is 4 secs, when for python3 is 10
 5. with c-style: 1.5 secs
 6. with regex: 4 secs

 7. I gave up on going deeper to learning algorithms. And picked the better solution
     the maths rule as someone said. I'm not a math so a failed. The solution
     uses just one loop and looks simple. But i couldt get WHY does it working -
     it just a mistic-kind for me. so simple but far from understanding to simple sysadmin.
     It took a half of hour to get the point.

"""

def minion_game(s):
    vowels = "AEIOU"
    kevin_score = 0   # vowels
    stuart_score = 0   # consonants
    strlen = len(s)

    for i in range(strlen):
        if s[i] in vowels:
            kevin_score += (strlen-i)
        else:
            stuart_score += (strlen-i)

    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print("Draw")

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)
