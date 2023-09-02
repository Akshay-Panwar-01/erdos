'''This pseudo code for another banger problem just fits the problem perfectly.'''

MOD = 10**9 + 7

def solve(s):
    n=s+1
    a=[0,1,2]

    while len(a)<n+1:
        s=list(a)
        for j in range(2,len(a)):
            a[j]=(a[j-1]+s[j])
        a.append((2*a[-1]))
    return a[-1]

print(solve(2702))

'''Answer is : 126410606437752'''
