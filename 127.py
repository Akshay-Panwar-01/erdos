for i in range(1,30):
    s=[]
    for j in range(i,0,-1):
        if j*2 not in s:
            s.append(j)
    # print(len(s),end=",")
#1,1,2,3,4,4,5,5,6,6,7,8,9,9,10,11,12,12,13,14,15,15,16,16,17,17,18,19,20
# Find on oeis a(2n)=2n-a(n) and a(2n+1)=2n+1-a(n)

def a(n):
    if n==0:
        return 0
    else:
        return n-a(n//2)

print(a(4444444444))