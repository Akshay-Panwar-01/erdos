import sympy 
import math 

def generate():
    s=[[1],[2]]
    x=[4,5,6,7,7,8]
    k=0
    while len(s[0])<7 and k<6:
        res=[]
        for i in range(1,x[k]+1):
            for j in s:
                res.append(j+[i])
        s=res
        k+=1
    return s

# print(len(generate())) ====> 94080

unique=[]
for i in generate():
    perm=sorted(i)
    if perm not  in unique:
        unique.append(perm)
print(len(unique))

'''The answer is : 1879'''
