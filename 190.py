import sympy 
import math as m

def prime_factors(n):
    fac=[]
    while n%2==0:
        n//=2
        fac.append(2)
    for i in range(3,int(m.sqrt(n))+1,2):
        while n%i==0:
            n//=i
            fac.append(i)
    if n>2:
        if n not in fac:
            fac.append(n)
    return fac

ans=0
for i in range(1,10**6):
    if len(prime_factors(i))==2:
        ans+=i
print(ans,"ans")

'''The answer is : 9322298311255 , time taken is a lot  ie about 10 mins'''
