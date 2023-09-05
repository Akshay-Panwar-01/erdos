'''the summation becomes sum of (x+1)*(x+1)!-x*x! so
on doing further summation we got (n+2)!-(n-1)!-1 where
n=10**12 and by analysis we can prove that both (n+2)! and 
(n+1)! are divisible by 3**20 as 61! is divisible by 3**20
and thus answer becomes -1 mod 3**20 that is 3**20-1'''

print(3**20-1)

'''The answer is : 3486784400'''
