import sympy 
import math

'''We get maximum value for upper triangular matrix type of board
so xi=(n+1-i) and yi=i'''

n=13579
ans=0
for i in range(1,n+1):
    xi=(n+1-i)
    yi=i
    ans+=xi*(n-yi)
print(ans)

'''The answer is : 834607163320'''
