from math import gcd

def phi(n):
    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result


def tower_mod(a, m):
    """
    Infinite power tower:
        a^(a^(a^...)) mod m

    Uses Euler's theorem recursively.
    """

    if m == 1:
        return 0

    if gcd(a, m) == 1:
        return pow(a, tower_mod(a, phi(m)), m)

    ph = phi(m)
    e = tower_mod(a, ph)

    return pow(a, e + ph, m)


a = 321298371289423
M = 7908922576125228087

print(tower_mod(a, M))
