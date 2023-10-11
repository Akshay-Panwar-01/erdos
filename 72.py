import sympy 
import math 

def gen(n):
    a=[i for i in "github"]
    while len(a[0])<n:
        temp=[]
        for i in a:
            if i[-1]=="g":
                temp.append(i+"t")
                temp.append(i+"u")
                temp.append(i+"b")
                temp.append(i+"g")
            elif i[-1]=="b":
                temp.append(i+"g")
                temp.append(i+"i")
                temp.append(i+"t")
                temp.append(i+"u")
                temp.append(i+"b")
            elif i[-1]=="t" or i[-1]=="u":
                temp.append(i+"g")
                temp.append(i+"i")
                temp.append(i+"h")
                temp.append(i+"u")
                temp.append(i+"b")
            else:
                temp.append(i+"g")
                temp.append(i+"i")
                temp.append(i+"t")
                temp.append(i+"h")
                temp.append(i+"u")
                temp.append(i+"b")
        a=temp
    return a

def ispal(a):
    if a==a[::-1]:
        return 1
    return 0

# c=[]
# for i in range(2,11,2):
#     s=gen(i)
#     count=0
#     for j in s:
#         if ispal(j):
#             count+=1
#     print("YES")
#     c.append(count)
# print(*c)    
'''series comes out to be 5 23 105 479 2185 which is 
a(n)=5*a(n-1)-2*a(n-2)'''

mod=10**9+7
a=[5,23,105]
while 2*len(a)<7162534:
    a.append((5*a[-1]-2*a[-2])%mod)
print(a[-1])

'''The answer is :401849953'''
