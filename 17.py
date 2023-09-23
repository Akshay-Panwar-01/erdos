'''As per given conditions c*(t+u+v)=20+10+9=39=3*13 thus c=3 and t+u+v=13
moreover (2,3) is v so we can only have one system of equation that leads the integral solution 
2*v+u=20 , 2*t+v=10 , 2*u+t=9 , implies that t=1 u=4 v=8
and the matrix is as follows
'''
a=[[8,1,4],[8,1,4],[4,8,1]]
ans=0
for i in range(3):
    for j in range(3):
        ans+=a[i][j]*(i+j+2)

print(ans)
'''The answer is : 145'''
