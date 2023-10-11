'''The answer would be the number of different ways wwe can write 5000-2500 in
that is , the partiton of number 2500'''
import sympy 
import math 

def partition(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

number = 2500
result = partition(number)%(10**9+7)
print(f"The partition function p({number}) is {result}")

'''The answer is : 729287017'''
