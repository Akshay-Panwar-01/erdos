import sympy 
import math

'''X-a should be divisible by q according to the equation of line .'''

a,b=-10101099,127898755387
c,d=1137947000140424,1607032990556

# my=d-b
# mx=c-a
# common=(math.gcd(my,mx))

# p=my//common
# q=mx//common
# print(my,mx,common)
# print(p,q) 
#1299827 1000000009

mod=1000000009
n=((c+a)//mod)+1
print(n)

def count(m,i):
    res=0
    while i%m==0:
        res+=1
        i//=m
    return res

c2=0
c5=0
for i in range(1,n+1):
    c2+=count(2,i)
    c5+=count(5,i)
print(min(c2,c5))

# n , zeroes in n! are 1137947 284481

print(pow(284481,1137947,1000000007))

'''The answer is : 876339089'''
