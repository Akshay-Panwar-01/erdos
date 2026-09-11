''' first solve manually using GP well find an equaltion '''
import math as m

def num(x):
    return (x*(3*x+5))**2

def denom(x):
    return (4*(x+1)*(x+2))**2

p=num(112358)
q=denom(112358)

factor=m.gcd(p,q)

p//=factor
q//=factor

print(p*q)

'''The answer is : 228618086507850699690277616143553206022400'''
