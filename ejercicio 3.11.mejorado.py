"""El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores."""

def promedio (a,b,c,d,e):
    suma = (a + b + c + d + e) / 5
    print (f"El promedio de los numeros {a, b, c, d, e} es: ",{suma})

numeros = 5
for i in range(numeros):
 a = int(input("Escribe el primer numero "))
 b = int(input("Escribe el s numero "))
 c = int(input("Escribe el t numero "))
 d = int(input("Escribe el c numero "))
 e = int(input("Escribe el q numero "))
 
 print ()