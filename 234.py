from itertools import permutations
import math as m

def generate_perm(n):
    nums=[i for i in range(1,n+1)]
    res=list(permutations(nums,2))
    return res

perms=generate_perm(2019)
ex=0
for i in perms:
    ex+=(m.gcd(i[0],i[1]))/4074342
print(int(1000*ex))

'''The answer is 4374'''
