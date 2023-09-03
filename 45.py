'''https://math.stackexchange.com/questions/417486/probability-that-the-first-digit-of-2n-is-1 really useful post about the topic'''

import math

def nofdigits(x):
    ans=0
    while x>0:
        x//=10
        ans+=1
    return ans

def binpow(a,b):
    res=1
    while b>0:
        if b&1:
            res=(res*a)
        a=(a*a)
        b>>=1
    return res

#n=int(input())
#print(nofdigits(binpow(2,n))/n)

'''For n tends inf the answer will converge at log(2)'''

print(math.log10(2)*10**6)

'''Answer is : 301029'''
