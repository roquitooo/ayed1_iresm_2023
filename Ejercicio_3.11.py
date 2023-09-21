"""El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores."""

flag = True
while flag:
    try:
        dato1 = (input("Escribe un numero entero: "))
        dato2 = (input("Escribe otro numero entero: "))
        dato3 = (input("Escribe otro numero entero: "))
        dato4 = (input("Escribe otro numero entero: "))
        dato5 = (input("Escribe otro numero entero: "))
        if (dato1.isdigit() and dato2.isdigit() and dato3.isdigit() and dato4.isdigit() and dato5.isdigit()):
            dato1 = int(dato1)
            dato2 = int(dato2)
            dato3 = int(dato3)
            dato4 = int(dato4)
            dato5 = int(dato5)
            flag = False
            print ("EL promedio de estos numeros enteros es: ", (dato1 + dato2 + dato3 + dato4 + dato5)/5)
        else:
            print("No ingresaste numeros enteros") 
    except Exception as e:
        print (e)
