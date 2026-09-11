count=0

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if (a ^ b ^ c ^ d) != 0:
                    count += 1
                    print(a, b, c, d)
print(count)
