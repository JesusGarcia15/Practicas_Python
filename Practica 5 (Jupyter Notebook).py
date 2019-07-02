nombre = str(input("Como te llamas: "))
if nombre == "Laura":
    print ('Hola', nombre)
else:
    print('no te conozco')


#1) COMPARAR NUMEROS
Num = int(input("Ingrese el primer valor: "))
Num1 = int(input("Ingrese el seundo valor: "))#Pedimos los valores para comparar
#Comparamos los valores
#Decimos que si el pimer valor es mayor al segundo imprima el mensaje
if Num > Num1:
    print('El numero mayor es: ', Num)
#Sino entonces imprime que el segundo es mayor
else:
    print('El numero mayor es: ', Num1)

input('Presione Intro para finalizar')#La pausa
#2) VERIFICAR EDAD
Age = int(input("Ingrese su edad: "))#Pedimos la edad del usuario
#Comparamos la edas, si es igual o mayor a 18 realizara...
if Age >= 18:
    print('Eres violador. Congratulations')
#Si el usuario se equivoca imprime un mensaje de error
elif Age <= 0:
    print('¿Eres idiota? Como vas a tener edad negativa o edad 0.')
#Si no es mayor a 18 realiza...
else:
    print('Eres un morrito nalgas miadas. F para ti')
input('Presione Intro para finalizar')#La pausax2
#3) CALIFICACIÓN
Cal = int(input("Ingrese su calificación: "))#Pido al usuario una calificación entera
#Comparo su calificacion, dependiendo que valor me de sera el mensaje que me dara
if Cal < 0:
    print('Error. Estas bien pendejo e idiota, metiste un numero negativo.')
elif Cal < 5:
    print('suspenso. si no sabes que significa es que estas bien pendejo y reprobaste, echale ganas')
elif Cal == 5:
    print('Suficiente. Reprobaste cagada, echale ganas, apoco quieres recursar')
elif Cal == 6:
    print('Aprovado. Por la minima cabron, siguete esforzando, no quieres ver el mensaje si repruebas')
elif Cal == 7:
    print('Notable. Pues sigues valiendo madres, puedes mejorar, pero si te vale madres la materia Congratulations')
elif Cal >= 8:
    print('Sobresaliente. Felicidades campeón, aunque todos sabemos que pasaste por barbero con el profesor')
input('Presione Intro para finalizar')#La pausax3
