cont = 1
res = 0
Num = int(input("Ingrese el numero que quiere la tabla de multiplicar: "))
while Num < 0:
    print('Error. No se si estas pendejo, idiota o tienes un retraso, mete un puto numero positivo')
while cont <= 10:
    res = Num * cont
    print(Num, "*", cont, '=', res)
    cont +=1
    input("Pulse INTRO para continuar...")
input("Pulse INTRO para finalizar...")
