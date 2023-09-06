'''However the approach is so lame , it took a lot of time to calculate the final answer 
i'm working on a better approach to this '''

import sympy as s
import math as m

def ispal(s):
    if s[::-1]==s:
        return True
    return False

count=0
for i in range(1,10**9,2):
    x=bin(i)[2:]
    y=oct(i)[2:]
    z=hex(i)[2:]
    if ispal(x) and ispal(y) and ispal(z):
        print(i)
        count+=i
print(count,"ans")

'''
1
3    
5    
7    
9    
3951 
4095 
4097 
12291
20485
21845
28679
30039
36873
16187247
16777215
16777217
16781313
50331651
50343939
83886085
83894277
83906565
83914757
89458005
89466197
89478485
89486677
117440519
117448711
117460999
117469191
123012439
123020631
123032919
123041111
150994953
151031817
'''
'''The answer is 2124805300'''
