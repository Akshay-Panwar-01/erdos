'''Pretty simple problem based on linearity of expectaions basially 
S1=4, S2=(4**4) ,S3=(4**4**4), Sn=(4**4**4**4........**4) n terms '''
import sympy 
import math 

mod=int(1e9+7)
a=4
ans=1
for i in range(1,1182014+1):
    ans=(ans*a)%mod
print(ans)

'''Ans is : 451583116'''
