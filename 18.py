'''We can easily calculate the chance of winning of varun which is 
equal to 0.83056640625 and hence the problem proceeds as follows '''

total_money=2000
varuns_winning_probability=(81*42)/(4**6)
x=int(total_money*varuns_winning_probability)
y=total_money-x

#print(x,y) 1661 339
print(pow(x,y,10**9+7))

'''The answer to the problem is : 440052480'''
