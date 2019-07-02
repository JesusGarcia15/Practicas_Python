def Numeros (Num1, Num2):
    n = 0
    for n in range (Num1+1, Num2):
        print(n)
Num1 = int(input("Ingrese un numero: "))
Num2 = int(input("Ingrese un segundo numero: "))
print ("Los numeros que hay entre ", Num1, "y", Num2, "son: ")
print (Numeros(Num1,Num2))
