import math as m
def f(x):
    return (x**6+8*(x**4)-6*(x**2)+8)

def iscuberoot(x):
    y=m.ceil(x**(1/3))
    if y**3==x:
        return True
    return False

for i in range(1000):
    if iscuberoot(f(i)):
        x,y2=i,m.ceil(f(i)**(1/3))

print(3345*x+4321*y2)
'''The answer to the problem is : 57566'''
