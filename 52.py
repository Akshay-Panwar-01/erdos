import math

mod=4776913109852041418248056622882488319
#print(int(math.sqrt(mod))) ----> 2185615041550556672 

m=2185615041550556672
y=739397
while (m*m)%mod !=y:
    m+=1
    if m%10000000==0:
        print("check")
print(m)

'''This process was quite annoying so just used wolframalpha instead 
and the answer was 1379758952143604540772248652640111683'''
