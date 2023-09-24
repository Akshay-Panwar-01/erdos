import math

def check(x):
    if x>999 or x<100:
        return False
    y=str(x)
    if y[0]==y[2] and y[0]!=y[1]:
        return True
    return False

def dbug(x):
    y=int(x*10000)
    count=0
    if x!=(y/9999):
        return False
    s=str(y)
    for i in s:
        if s.count(i)>1:
            return False
    return True


def all_different(a,b,x):
    s=str(a)+str(b)+str(x)
    p=set()
    for i in s:
        p.add(i)
    if len(p)==8:
        return True
    else:
        return False

a=[]
qs=[101*i for i in range(1,10)]

for i in range(100,1000):
    if check(i):
        for j in qs:
            x=int((i/j)*10000)
            if dbug(i/j) and all_different(i,j,x) and i<j:
                if (i/j) not in a:
                    #print(i,j)
                    a.append(i/j)

'''The only pairs are 212 606 and 242 303 '''
#print(a) ======> [0.34983498349834985, 0.7986798679867987]

res=0
for i in a:
    res+=int(i*10000)

hcf=math.gcd(res,9999)
p=res//hcf
q=9999//hcf
print(p*q)

'''The answer to the problem is : 11716'''
