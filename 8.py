'''As all the primes are quite impossible to calculate in a considerable time so i just downloaded a file of all such primes
from the website http://www.primos.mat.br/2T_en.html '''
file1=open("prime_numbers.txt","r+")
primes=file1.readlines()

def sofd(x):
    res=0
    for i in x:
        if i!="\n" and i!="\t":
            res+=int(i)
    return res

ans=0
for i in primes:
    ans+=sofd(i)
print(ans)

'''The answer is 2076414728 and the time taken was about 4 minutes '''
