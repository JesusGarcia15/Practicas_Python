while True:
    try:
        resultado = 15 + "20"
        print (resultado)
    except TypeError:
        print('Coloco un caracter de tipo str, coloque los des numeros de tipo int')
        break
input('Puse INTRO para continuar...')
