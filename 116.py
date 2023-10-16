import sympy 
import math

'''Equataions were solved using wolframalpha and desmos .'''
x=(-9-10*math.sqrt(3*(15-math.sqrt(65))))/3
y=(-18+15*(math.sqrt(3*(15-math.sqrt(65))))+math.sqrt(195*(15-math.sqrt(65))))/6

a=(x,x+1)
b=(-9-x-y,-11-x-2*y)
c=(y,2*y+4)

area=(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2
#print(area)
# Area is 400

print(sympy.factorial(400))

'''The ans is : 91008'''
