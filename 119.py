import sympy 
import math

def min_cubes_sum(x):
    max_cube_root = int(x ** (1/3))
    dp = [float('inf')] * (x + 1)
    dp[0] = 0
    for i in range(1, max_cube_root + 1):
        cube = i**3
        for j in range(cube, x + 1):
            dp[j] = min(dp[j], dp[j - cube] + 1)

    return dp

a=min_cubes_sum(10**6+1)
print(sum(a)-2)

'''The answer is : 4178421'''
