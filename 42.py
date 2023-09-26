'''The number of ways of arranging n identical things over n identical places is equal to
the partitions of that number n that is p(n) , https://brilliant.org/wiki/identical-objects-into-identical-bins/'''
def partition(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

number = 10000
result = partition(number)%(10**9+7)
print(f"The partition function p({number}) is {result}")

'''The answer is : 17783467'''
