import sympy 
import math

'''the probability of x be the minimum value obtained when m faced dice rolled n times is  ((m-x+1)**n-(m-x)**n)/m**n so'''

def a(i):
    res=(101-i)**20-(100-i)**20
    return res/(100**20)

x=[0]
for i in range(1,101):
    x.append(a(i))

exval=0
for i in range(101):
    exval+=i*x[i]
print(exval*1000000)

'''The answer is : 5278561'''
