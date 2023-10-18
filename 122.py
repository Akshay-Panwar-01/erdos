'''We can simply fold the thing up again using simple recurrence .'''

import sympy 
import math

def pqoff(x,p,q):
    return [q,q*x+p]

def f(x):
    p=1
    q=x
    x-=1
    while x>=1:
        p,q=pqoff(x,p,q)
        x-=1
    return [p,q]

p,q=f(1000)
print("The answer to the problem is:",(p*q)%1000000007)

'''The answer is : 544785687'''
