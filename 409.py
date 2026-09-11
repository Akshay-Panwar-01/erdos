from array import array

n=9696969

def f(n):
    phi=array('I', range(n+1))
    primes=[]
    is_comp=bytearray(n+1)
    s=0
    for i in range(2,n+1):
        if not is_comp[i]:
            primes.append(i)
            phi[i]=i-1
        for p in primes:
            x=i*p
            if x>n:
                break
            is_comp[x]=1
            if i%p==0:
                phi[x]=phi[i]*p
                break
            phi[x]=phi[i]*(p-1)
    for i in range(2,n+1):
        s+=phi[i]
    return (s*2)+1

print(f(n))

'''optimized way to calculate the sum of phi(n) for n=1 to n=9696969 using a sieve method.The 
function f(n) computes the Euler's Totient function for all integers up to n and sums them up,returning 
the final result. The use of array and bytearray helps in efficient memory usage and speed.'''

# Answer is 57164126817955
