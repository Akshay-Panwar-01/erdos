'''The Question was quite simple and we could easily see that answer is tending to follow the formula 
(n//2)+2 for any integer n '''

s=[i for i in range(2,int(input("Enter the upper range:"))+1)]+[1]
x=True
while len(s)>1:
    if x:
        s.pop(0)
        x=False
    else:
        s.pop(-1)
        x=True
print(*s)

'''Answer for n =420420420 is 210210212'''
