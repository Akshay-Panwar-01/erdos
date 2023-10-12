'''We have to find the number of strict partitions of the number , special mention to chatgpt for helping me in 
solving the problem and with this problem I've solved 100 problems on the platform , yaaay!'''
import sympy 
import math

def count_distinct_partitions(x, start=1, memo=None):
    if memo is None:
        memo = {}
    if (x, start) in memo:
        return memo[(x, start)]
    if x == 0:
        return 1
    
    count = 0
    for i in range(start, x + 1):
        count += count_distinct_partitions(x - i, i + 1, memo)

    memo[(x, start)] = count
    return count

x = 196
result = count_distinct_partitions(x)
print(f"The number of distinct strict partitions of {x} is {result}")

'''The number of distinct strict partitions of 196 is 382075868'''
