'''The powers included in the term at k th place may be given as the binary 
form of that number k when reversed for example at 13th place bin(13)=1101  powers of a that
are present are 0 2 3 that is (a**3+a**2+1) '''

n=423732713
powers=bin(n)[2:][::-1]

x=13
ans=0
for i in range(len(powers)):
    if powers[i]=='1':
        ans+=pow(13,i,4222236787)
print(ans%4222236787)

'''The answer is : 3477823026'''
