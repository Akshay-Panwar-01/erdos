'''a(n) is C(2n,n) and sum is a(1) to a(60)'''
import math

ans = sum(math.comb(2*n, n) for n in range(1, 61))
print(ans)

# answer is 129183848197921031950947240904648220
