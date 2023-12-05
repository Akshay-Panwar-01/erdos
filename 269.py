'''The most optimal way to escape the cliff is to choose the perpendicular direction to the current radial direction 
so sqrt(1^2+2^2+......+n^2)=r is the form for n be the answer of r radius circle '''
import sympy
import math 

'''Sum of first n natural squares is '''
def cs(n):
    return (n*(n+1)*(2*n+1))//6

i=1
while cs(i)<(10**9)**2:
    i+=1
print(i)

'''The answer is : 1442250'''
