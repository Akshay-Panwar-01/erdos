import sympy 
import math

# def gen(p,q):
#     a=["a"]
#     while len(a[0])<(p+q):
#         temp=[]
#         for i in a:
#             if i.count("a")<p:
#                 if i.count("b")<q:
#                     temp.append(i+'b')
#                 temp.append(i+"a")
#             else:
#                 temp.append(i+"b")
#         a=temp
#     return a

# def check(n):
#     res={"a":0,"b":0}
#     for i in n:
#         res[i]+=1
#         if res["a"]<=res["b"]:
#             return False 
#     return True

# n=15
# ans=[]
# for i in range(n-1):
#     x=gen(n,i)
#     count=0
#     for i in x:
#         if check(i):
#             count+=1
#     ans.append(count)
# print(ans)

'''The result we get on comparison online is as follows '''

s=[1,2]
while len(s)<199:
    temp=[1]
    for i in range(1,len(s)+1):
        if i==len(s):
            temp.append(temp[-1]+s[-1])
        else:
            temp.append(temp[-1]+s[i])
    s=temp
print((s[100]*sympy.factorial(201)*sympy.factorial(101))/sympy.factorial(300))

'''The answer is : 6767'''
