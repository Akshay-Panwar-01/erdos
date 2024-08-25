'''identify 2 to the power 1,2,3,4,5,6 and their sums as the pattern and then '''
import sympy as sp

k=182721378
s=0
mod=10**9+7
for i in range(27):
    s+=4**i
    s=(s%mod)
s+=(48503651**2)%mod
print(s%mod)

# 604988641 is the answer
