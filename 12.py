import sympy
file1=open("12.txt","r+")
x=file1.readlines()

a=[]
for i in x:
    if sympy.isprime(int(i)):
        a.append(int(i))

'''only two primes 492227 492113'''

print(a[0]-a[1])

'''Answer is : 114'''
