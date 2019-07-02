Lista = []
Num = int(input("Ingrese un numero: "))
while Num < 0:
    print('Error. Ingresa un numero mayor que cero mamada, por favor :)\n')
    Num = int(input("Ingrese un numero: "))
while Num >= 1:
    Lista.append (Num)
    Num = int(input("Ingrese un numero: "))
print(Lista)
input("Pulse INTRO para finalizar...")
