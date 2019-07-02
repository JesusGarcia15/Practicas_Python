def Factorial (N):
    fac = 1
    for n in range(1, N + 1):
        fac = fac * n
    return fac
N = int(input("Ingrese un numero: "))
print(Factorial(N))
