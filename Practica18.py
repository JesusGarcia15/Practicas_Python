def Agrega_Una_Vez(lista, el):
    while True:
        try:
            if el in lista:
                raise ValueError
            else:
                lista.append(el)
            return el
        except ValueError:
            print ('Imposible añadir elementos duplicados', [el])
            break
print (Agrega_Una_Vez ([1],1))
input('Puse INTRO para continuar...')
