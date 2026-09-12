'''let z=2 then f(z)=zeta(2) and g(z)=1/zeta(2) , so x=1'''
import math
import sympy as sp

for k in range(1, 50):
    count=0
    for i in range(1, k + 1):
        if math.gcd(i, k) == 1:
            count += 1
    #print(f"{count},", end="")

'''Sum is Phi(k)'''

print(sp.totient(354216846978542365))  

# Answer is 266704449489725952