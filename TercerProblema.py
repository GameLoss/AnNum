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

def Sec(a, b, i):
    print("a")
    xa=a
    xac=b
    xi=(-f(xac)*(-xac+xa))/(-f(xac)+f(xa)) + xac
    i+=1
    err = ea(xac, xi)
    print("xi+1= ", xi)
    print("Error Aproximado= ", err)
    if(err<0.1):
        return "Resuelto en ", i, " iteraciones"
    else:
        return Sec(xac, xi, i)

print("Newton Raphson: ")
print(NR(1, 0))
i=0
print("Metodo de Secante: ")
print( Sec(0, 1, 0))

