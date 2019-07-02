Mese_año = [0,"Janury", "February", "March", "April", "May", "Jun", "July", "Agust", "September", "October", "November", "December"]
n = int(input("Ingrese un mes en numero: "))
while n > 12:
    print('Error, ese no es un mes del año pendejo de shit')
    n = int(input("Ingrese un mes en numero: "))
while n < 0:
    print('Error, ese no es un mes del año')
    n = int(input("Ingrese un numero: "))
#Verificamos la longitud de la lista con .len()
if n <= len(Mese_año):
    #Si estra en el rango imprime el mes del año en numero
    print (Mese_año [n])
input("Pulse INTRO para finalizar...")
