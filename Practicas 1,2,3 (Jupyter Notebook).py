import this
print('Me llamo Larry y tengo 60')
print('hola')#te estoy saludando
print('10 por 3 son', 10*3)
nombre = 'Elver' #Guarda el nombre de la chica
edad = 19 #Guardo su edad

#Mueeestra su nombre:
print('Te llamas', nombre)

#A continuacion, muestra cuantos años tiene:
print('Tienes', edad, 'años')

edad = edad + 1 #Le pongo un año mas:

#Vuelvo a mostrar su edad :
print('Cumples', edad, 'años ¡Felicidades!')

input()#Hago una pausa hasta que el usario pulse la tecla INTRO.

comida_niños = 50 #Tengo 50 bandejas de comida para niños
comida_adultos = 30 #Tengo 30 bandejas de coomida para todos
#Muestro las bandejas que tengo:
print('Tienes', comida_niños, 'bandeja de comida para niños.')
print('Tienes', comida_adultos, 'bandeja de comida para adultos')
#Simulo que los clientes han hecho consumicion:
comida_niños = comida_niños -40
comida_adultos = comida_adultos -20
#Sumo las bandejas que tengo y las guardo en otra variable:
total_comida = comida_niños + comida_adultos
print('Ha habido venta. En total quedan', total_comida, 'bandeja de comida')
input("Prsione INTRO para finalizar...") #Hago una pausa hasta que el usario pulse la tecla INTRO.
