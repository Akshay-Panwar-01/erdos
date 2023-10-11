'''Largest positive integer n for which n! can be expressed as the product of n-a consecutive positive integers is (a+1)! - 1'''
import sympy 
import math 

'''And if n>= p then n!-1 mod p === -1 mod p so '''
x=38980715857-1
ans=x%8037517
print(ans)

'''The ans is :6795923'''
