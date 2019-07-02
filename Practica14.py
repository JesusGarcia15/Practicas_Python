def Division(num,den):
    while True:
        try:
            return num/den
        except ZeroDivisionError:
            print ('Error. No se puede dividir entre cero')
            break
        except TypeError:
            print ('Esta pendejo, coloco una letra en vez de numero')
            break
print (Division(10,0))
input('Puse INTRO para continuar...')
