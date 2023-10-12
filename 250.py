import sympy 
import math

def gen(x):
    a=[0.2,0.3,0.5,0.7]
    i=2
    while i<x:
        temp=[]
        div=10**(-i)
        for j in a:
            temp.append(j+(2*div))
            temp.append(j+(3*div))
            temp.append(j+(5*div))
            temp.append(j+(7*div))
        a=temp
        i+=1
    return a
res=gen(10)
print(sum(res)/len(res))

'''We're getting closer and closer to 0.4722222222222... which is 17/36'''
'''there's another way of doing the same question for any x digit number the expected value at any nth decimal place would be (2+5+3+7)*4**(n-1)/4**(n) that is 
17/4 so the expected value may be written as (17/40)+(17/400)+(17/4000)+(17/40000)+.....
which comes out to be 17/36 thus answer is 17+36=53'''
