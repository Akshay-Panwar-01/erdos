import math 

def f(x):
    l=int(pow(10,x))
    count=0
    for i in range(1,l//2):
        if math.gcd(i,l-i)==1:
            count+=1
    return count

for i in range(1,int(input("Enter the value of X:"))+1):
    print(f"The value of f(x) at {i} is ",f(i))

'''
The value of f(x) at 1 is  2   
The value of f(x) at 2 is  20  
The value of f(x) at 3 is  200 
The value of f(x) at 4 is  2000
The value of f(x) at 5 is  20000
The value of f(x) at 6 is  200000

so the formula for f(i)=2*(10**(i-1)) and thus answer forms a gp whose value
comes out to be 2*(10**10**10-1)/9 mod 10**9+7
'''
mod=10**9+7
s=pow(10,pow(10,10,mod-1),mod)
p=(2*(s-1))%mod
q_inv=pow(9,mod-2,mod)
print((p*q_inv)%mod)

'''The answer is : 45814514'''
