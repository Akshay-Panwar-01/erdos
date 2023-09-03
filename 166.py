import math 

def sumofdigits(x):
    ans=0
    while x>0:
        ans+=x%10
        x//=10
    return ans%9
'''
n=int(input())
for i in range(1,n+1):
    s=pow(2,i)
    x=pow(2,s)+1
    print(i,sumofdigits(x))
'''

'''We'll find that it is coming 5 for odd and 8 for even for every fermats number so'''
a=999999999999
odds=(a+1)//2
evens=a-odds
print(8*evens+5*odds)

'''Answer is : 6499999999992'''
