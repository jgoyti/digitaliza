import sys
import math


print(" ****CALCULADORA PHYTON**** \n 1)RAIZ CUADRADA \n 2)SUMA \n 3)RESTA \n 4)MULTIPLICACION \n 5)DIVISION \n 6)POTENCIA \n 7)SALIR  ")
print("MADE BY GOYTI")
opcion=int(input("Ingrese la opcion a calcular: "))

    
while(opcion != 7):

    if opcion >8 :
        print("No es una opcion valida , vuelve a intentarlo")
        opcion=int(input("Selecciona otra opcion: \n" ))
    if opcion == 1:
        numero =int(input("Dime el numero del que quieres saber la raiz: "))
        raiz_cuadrada = math.sqrt(numero)
        print("La raíz cuadrada de {} es {}".format(numero, raiz_cuadrada))
        opcion=int(input("Selecciona otra opcion: \n" ))
    n1=int(input("Dime el primer numero: "))
    n2=int(input("Dime el segundo numero: "))  
    if  opcion == 2 :
        suma=n1+n2
        print(" La suma es: " ,suma) 
        opcion=int(input("Selecciona otra opcion: \n" ))
    elif opcion == 3 : 
        resta=n1-n2
        print(" La resta es: " ,resta)
        opcion=int(input("Selecciona otra opcion: \n" ))
    elif opcion == 4 :
        multiplicacion=n1*n2
        print("La multiplicacion es: " ,multiplicacion)
        opcion=int(input("Selecciona otra opcion: \n" ))
    elif opcion == 5 :
        if n2<=0:
            print("ERROR , no se puede dividir entre 0 o numeros negativos")
        else:
            division=n1/n2
            print("La division es: " ,division)
            opcion=int(input("Selecciona otra opcion: \n" ))
    elif opcion == 6 :
        potencia=n1**n2
        print("El resultado de " +str(n1) +" elevado a "  +str(n2) +" es: " ,potencia)
        opcion=int(input("Selecciona otra opcion: \n" ))

else:
        print("HASTA LA PROXIMA!!")
        sys.exit()



        
