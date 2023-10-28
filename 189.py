import sympy 
import math

def factors(x):
    res=[]
    for i in range(1,x+1):
        if x%i==0:
            res.append(i)
    return res

for x in range(1,25):
    s=x
    a=[0]+[1]*x
    count=0
    while x>1 and len(list(set(a)))>1:
        if a[x]==1:
            p=factors(x)
            a[x]=0
            for i in p:
                a[i]=0
            count+=1
        x-=1
    if count!= (s+1)//2:
        print("YES", count, s)
    else:
        print(count)

'''Comes out that for n ans would be int value of the fraction (n+1)/2'''
print((123456789+1)//2)

'''Answer is  : 61728395'''
