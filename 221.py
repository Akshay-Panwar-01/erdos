import sympy 
import math

count=0
for i in range(2,91):
    x=2*(i-1)
    if 360%x==0:
        count+=1
print(count)
print(count*89) 
'''Total values hw can shoot at is 89 and so answer will be count*89
which comes out to be : 16*89 = 1424'''
