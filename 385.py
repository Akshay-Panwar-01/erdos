'''Young tableau counting problem answer is given by the hook-length formula'''

MOD = 1_000_000_007

n = int(input())

fact = 1

for i in range(1, 2 * n + 1):
    fact = fact * i % MOD

fn = 1
for i in range(1, n + 1):
    fn = fn * i % MOD

ans = fact * pow(fn, MOD - 2, MOD) % MOD
ans = ans * pow(n + 1, MOD - 2, MOD) % MOD
ans = ans * pow(fn, MOD - 2, MOD) % MOD

print(ans)

# answer is 70646122
