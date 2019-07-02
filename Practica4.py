n = 0;
i = 0;
Num = int(input("Dame un numero: "))
while Num < 1:
    print('Error. Pon un puto numero positivo')
    Num = int(input("Dame un numero: "))
if Num == 2:
    print('Es primo', Num)
else:
    for n in range(1,Num):
        primo = True
        for i in range(2,n):
          if n % i == 0:
              primo = False
        if primo is True:
            print('Es primo ', n)
#http://diagramas-de-flujo.blogspot.com/2013/01/calcular-los-n-primeros-numeros-primos-en-Java.html
