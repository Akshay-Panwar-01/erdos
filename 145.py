'''Create all permutaions using itertools and then use conditions on them'''
from itertools import permutations


def generate_arrangements():
    numbers = list(range(6))
    arrangements = list(permutations(numbers, 6))
    return arrangements


arrangements = generate_arrangements()
count=0
for arrangement in arrangements:
    for i in range(1,6):
        if arrangement[i-1]==i or arrangement[-1]==1:
            break
    else:
        count+=1
        print(arrangement,"acc")

print(count)
'''The answer is : 256'''
