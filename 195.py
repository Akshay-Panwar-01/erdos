import math

def solve(n):
    x=[-1]+[0 for i in range(n)]
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            if x[j]:
                x[j]=0
            else:
                x[j]=1
    return x.count(0)

i=1
while i<101:
    print(i,i-solve(i))
    i+=1


'''So the number of ones coming as per the euation int(sqrt(a))'''

no_1=111111111
print(12345678987654321-111111111)

'''ANswer is : 12345678876543210'''
