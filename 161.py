import math 
def func(a):
    p=list(a)
    a=[]
    for i in p:
        if len(i)>0 and i[-1]=='1':
            a.append(i+'0')
        else:
            a.append(i+'0')
            a.append(i+'1')
    return a

a=[""]
while len(a[0])<30:
    a=func(a)

#print(len(a)) this comes out to be 2178309 so sum of digit is 30
x=a[29]
print(x.count('0'))

'''The Answer to the problem is : 28'''
