while True:
    try:
        colores = {'rojo':'red', 'verde':'green', 'negro':'black'}
        print(colores['blanco'])
    except KeyError:
        print('Ese color no se encuentra en el rango de la lista, intente con un color que este en la lista')
        break
input('Puse INTRO para continuar...')
