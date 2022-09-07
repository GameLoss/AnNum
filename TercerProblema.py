import sympy as sp
import math
import numpy as np
from prettytable import PrettyTable

xi = 0
xa = 0
e = math.e
x = sp.Symbol('x')
fx = ((x**2)*3) - (e**x)
tablaNR = PrettyTable(["i", "xi", "xi+1", "Error"])
tablaSec = PrettyTable(["i", "xi-0", "xi", "xi+1", "Error"])

def ea(xra, xr):
    ea=abs((xr-xra)/xr) * 100
    return ea

f = sp.lambdify(x, fx, "numpy")
fp = sp.lambdify(x, fx.diff(x), "numpy")

def NR(a, i, tablaNR):
    xa=a
    xi=(-f(xa))/fp(xa)+xa
    i+=1
    err = ea(xa, xi)
    tablaNR.add_row([i, xa, xi, err])
    if(err<0.1):
        return "Resuelto en ", i, " iteraciones"
    else:
        return NR(xi, i, tablaNR)

def Sec(a, b, i, tablaSec):
    xa=a
    xac=b
    xi=(-f(xac)*(-xac+xa))/(-f(xac)+f(xa)) + xac
    i+=1
    err = ea(xac, xi)
    tablaSec.add_row([i, xa, xac, xi, err])
    if(err<0.1):
        return "Resuelto en ", i, " iteraciones"
    else:
        return Sec(xac, xi, i, tablaSec)

print("Newton Raphson: ")
print(NR(1, 0, tablaNR))
print(tablaNR)
i=0
print("Metodo de Secante: ")
print( Sec(0, 1, 0, tablaSec))
print(tablaSec)

