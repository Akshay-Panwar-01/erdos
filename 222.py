'''This is quite simpler problem I would say .'''
import math

n=10**6
total_possible=(n*(n-1))//2
favourable=0
for i in range(1,n//2+1):
    favourable+=((n//i)-1)

hcf=math.gcd(favourable,total_possible)
p=favourable//hcf
q=total_possible//hcf

print(p+q)

'''The answer is : 3246834221 '''
