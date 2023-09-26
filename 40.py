'''Let's dive into the theory of the question so basically on simplifying f(n) we get 
f(n)=(8/n**2)*(n**2+(n-2)**2+(n-4)**4+.......+1 or 2 ) so in that way we can put the values in G(n)
so we got G(n)= sqrt(4*(n+1)/n) and thus the argument of the function Z becomes : 50000/(sqrt(10**10+10)-10**5)'''

denom=(10**10+10)**(0.5)-10**5
print(50000/denom) #999999952.502551 this is due to inaccuracies actually it is 10**9

'''now z(n) is actually summation of Y(n) from 2 to n and thus we can calculate this using '''

z=0
for i in range(1,10**9+1):
    z+=i*((10**9//i)-1)
print(z)

'''The answer is : 322467033612360628
Time taken = 5 minutes almost '''
