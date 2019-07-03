import numpy as np
def f(x):
    return x - 3
a = -2
b = 4
error = 0.1
while error > 1e-8:
    c = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fc = f(c)
    if fc == 0:
        raiz = c
        break
    elif fa * fc < 0:
        b = c
    elif fb * fc < 0:
        a = c
    raiz = c
    error = abs(fc)
print(raiz)
