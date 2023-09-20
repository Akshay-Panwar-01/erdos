import math as m
def phi(n):
    res=n
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            while (n % i) == 0:
                n//=i
            res-=(res//i)
    if n>1:
        res-=(res//n)
    return res

result=0
for i in range(1,1001):
    result+=(phi(i)/(2020**i-1))
print(result)

# result comes out to be 0.0004955400171868978 represented in p/q form as 

p=2020
q=4076361
mod=10**9+7
q_inv=pow(q,mod-2,mod)
print((p*q_inv)%mod)

'''The answer is : 524928733'''
