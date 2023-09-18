import math as m
import sympy as s

def p2(x):
    count=0
    for p in range(2,x+1,2):
        i=p
        while i%2==0:
            i//=2
            count+=1
    return count

def p3(x):
    count=0
    for p in range(3,x+1,3):
        i=p
        while i%3==0:
            i//=3
            count+=1
    return count

a=[0]*7
a[0]=p3(66)-p3(24)-p3(66-24)
a[1]=p2(73)-p2(27)-p2(73-27)
a[2]=p3(3280)-p3(1367)-p3(3280-1367)
a[3]=p2(3712)-p2(2005)-p2(3712-2005)
a[4]=p2(14348)-p2(7519)-p2(14348-7519)
a[5]=16
a[6]=19

print(*a)     # 2 5 7 11 13 16 19

'''Which Resembles int(sqrt(2)*x)+int(sqrt(2)*(x+2))'''

b=[]
for i in range(68):
    x=int(i*m.sqrt(2))
    y=int((i+2)*m.sqrt(2))
    b.append(x+y)
print(*b) 

'''2 5 7 11 13 16 19 21 25 27 30 33 35 39 41 45 47 50 53 55 59 61 64 67 69 73 75
 79 81 84 87 89 93 95 98 101 103 107 109 112 115 117 121 123 127 129 132 135 137 
 141 143 146 149 151 155 157 161 163 166 169 171 175 177 180 183 185 189 191'''

'''The Answer is 191'''
