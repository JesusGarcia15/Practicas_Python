n = 0;
Numeros = []
Num = int(input("Ingrese un numero natural: "))
while Num < 1:
    print('Error. Ingresa un numero mayor que uno mamada, por favor :)\n')
    Num = int(input("Ingrese un numero natural: "))
for n in range (0, Num):
    Numeros.append(n)
print(Numeros)
input("Pulse INTRO para finalizar...")
