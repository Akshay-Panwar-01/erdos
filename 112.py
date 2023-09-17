'''Here all the terms of the form (a+b*sqrt(5))**(1/c) are equal to (sqrt(5)+1)/2 
and of the form of (a-b*sqrt(5))**(1/c) equals (sqrt(5)-1)/2 so'''

import math as m
x=(m.sqrt(5)+1)/2
y=(m.sqrt(5)-1)/2
ans=(x+x+x-y-y+x+y+x-y-y-y)
print(int(ans*1000000000))

'''The answer to the problem is 5618033988'''
