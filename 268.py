'''The expected value of the dice will be (n+1)/2'''
n=1234567
ex=(n+1)//2

'''Now we'll use the linearity of expectations here ie E(x+y)=E(x)+E(y)'''
print((ex+1)*ex)

'''The answer is: 381040153940'''
