'''All such numbers are of type 2**(n-1)*p where p is prime 
and also p+1=2**n and thus all the numbers where 2**n-1 is prime are the ones to be included in 
the answer such numbers takes the form of p*(p+1)//2 where p=2**n-1'''

import sympy 
import math as m

mod=10**9+7
ans=0
for i in range(2,119):
    p=2**i-1
    if sympy.isprime(p) and (p*(p+1))//2<=5*(10**35):
        ans+=(p*(p+1))//2
print(ans%mod)

'''Answer is : 61169540'''
