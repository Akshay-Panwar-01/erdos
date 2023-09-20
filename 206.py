import sympy 

for i in range(-12,12):
    p=(i+8)*(i+10)*(i+12)
    if sympy.isprime(p):
        print(i,p)

'''The only form that is possible is -1 1 3 to make p a prime number
thus the answer to the problem is 3'''
