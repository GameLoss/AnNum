import sympy as sp
import math
import numpy as np

xi = 0
xa = 0
e = math.e
x = sp.Symbol('x')
fx = ((x**2)*3) - (e**x)

def ea(xra, xr):
    ea=abs((xr-xra)/xr) * 100
    return ea

f = sp.lambdify(x, fx, "numpy")
fp = sp.lambdify(x, fx.diff(x), "numpy")

def NR(a, i):
    xa=a
    xi=(-f(xa))/fp(xa)+xa
    i+=1
    err = ea(xa, xi)
    print("xi= ", xi)
    print("Error Aproximado= ", err)
    if(err<0.1):
        return "Resuelto en ", i, " iteraciones"
    else:
        return NR(xi, i)

print(NR(1, 0))

