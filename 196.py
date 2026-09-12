from math import gcd

count = 0
wins = 0

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if a + b + c + d == 3:
                    count += 3
                    wins += (a >= b) + (a >= c) + (a >= d)

g = gcd(wins, count)
#print(wins // g, count // g)
print(pow(wins//g,count//g, 10**9 + 7))

#Answer is 53945879