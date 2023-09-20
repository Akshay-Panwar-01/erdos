
def f(x):
    m=x%6
    return pow(5,x,10**m)

def s(x):
    res=0
    for i in range(1,x+1):
        res+=f(i)
    return res

#for i in range(24,int(input())+1,24):
#     print(f"The value of S({i}) is = ",s(i)/s(24))

'''On in depth investigation of the problem I came up with the approach that for any n=24k the s(n)=k*s(24)
and if n=24k+r then s(n)=k*s(24)+s(r)'''

n=10**18
r=(n%24) #this is 16
k=n//24
ans=(k*s(24))+s(r)
print(ans%(10**9+7))

'''The answer to the prblem is : 500280071'''
