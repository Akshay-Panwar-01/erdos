'''Incorrect statement, It's actually substring rather than subsequence.'''
import sympy as sp

def f(n):
    s = str(n)

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            x = int(s[i:j])

            if sp.isprime(x):
                return False

    return True

ans = 0

for n in range(10000, 100000):
    if f(n):
        ans += n

print(ans)

# Answer is 158165924 