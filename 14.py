file1=open("14.txt","r+")
x=file1.readlines()

# print(max(x)) max value is coming 9999504

fib=[0,1,1]
while fib[-1]<9999504:
    fib.append(fib[-1]+fib[-2])

count=0
for i in x:
    j=int(i)
    if j in fib:
        count+=1
print(count)

'''Answer is : 24 '''
