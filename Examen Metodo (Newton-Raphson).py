import numpy as np
def f(x):
    return x**4 - 10*x**3 + 3*x**2 + x + 23
def Df(x):
    return 4*x**3 - 30*x**2 + 6*x + 1
x0 = 9#se realiza un cambio para encontrar el primer punto
i = 1
error = ((x0 - x0+1))/ x0
while error < 1e-8:
    x1 = x0 - f(x0) / Df(x0)
    x0 = x1
    print('Interacion', i, "raiz aproximada: ", x0)
    i +=1
    break
