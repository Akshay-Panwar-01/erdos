'''We can see that there are total 62 such numbers with less than equal to 8 digits in it 
so for 27th number we'll use all the prime numbers upto 10**4 only'''

def sievespf(n):
    spf = [i for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if spf[p] == p:
            for i in range(p * p, n + 1, p):
                if spf[i] == i:
                    spf[i] = p
        p += 1 
    return list(set(spf))

def check(m,a,b):
    p,q,r=map(str,[m,a,b])
    a=[]
    b=[]
    if len(q)!=len(r):
        return False

    for i in p:
        a.append(i)
    for i in q+r:
        b.append(i)
    
    if len(a)!=len(b):
        return False
    if sorted(a)!=sorted(b):
        return False
    
    return True


spf=sorted(sievespf(10000))
x=len(spf)
count=0
sample=[]
for i in range(x):
    for j in range(i+1,x):
        if check(spf[i]*spf[j],spf[i],spf[j]):
#            print(spf[i]*spf[j],spf[i],spf[j],count+1)
            sample.append(spf[i]*spf[j])
            count+=1
sample.sort()
print(sample[26])

'''The answer is : 30189721'''
