import sympy as sp
import math

mod=10**9+7

a=7654567
b=7653567
#print(math.gcd(a,b))        --> 1

s=0
points=[]
for n in range(1,10):
    for i in range(1,n+1):
        for x in range(0,i):
            for y in range(0,i):
                s+=((a*x+b*y)%i)
#    print(s,end=",") #0,2,13,48,133,308,630,1176,2046
    points.append((n,s))

m=sp.symbols('x')
poly = sp.interpolate(points,m)
# print(sp.factor(poly))
# x*(x - 1)*(x + 1)*(x + 2)*(3*x + 4)/120

x=10**7
ans=((x*(x-1)*(x+1)*(x+2)*(3*x+4))//120)
print(ans%mod)

#Answer is 641893433
