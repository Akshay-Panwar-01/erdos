from numpy import gcd
import sympy as sp


def s(x, y):
    z = 0
    for i in range(y):
        z += (x * i) % y
    return z


points = []
for x in range(1, 10):
    for y in range(1, 10):
        if gcd(x, y) != 1:
            points.append(((x, y), s(x, y)))


ys = sorted({y for (_, y), _ in points})
zs = [next(z for (_, yy), z in points if yy == y) for y in ys]

Y = sp.symbols('Y')
interp = sp.expand(sp.interpolate(list(zip(ys, zs)), Y))
print("Simplified coprime interpolation:", sp.simplify(interp))

x, y = sp.symbols('x y', positive=True)

'''Its y(y-d)/2 for d=gcd(x, y) which is 35 here '''

print(((42082520835355*(42082520835355-35))//2)%1000000007)

# Answer is 284211919
