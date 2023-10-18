import sympy 
import math

k=0
ans=0
while 2**k<10**9:
    s=4*(2**(k+1)-1)
    t=9*2**k-(4*(2**(k+1)-1))
    if s%t==0:
        p=s//t
        if sympy.isprime(p) and p%2!=0:
            ans+=3*p*2**k
    k+=1
print(ans)

'''The answer is : 792'''
