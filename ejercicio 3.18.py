"""El programa debe:

Pedir al usuario un número entero positivo y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

try: 
    num = int(input("Ingrese un numero: "))
    for i in range(num, 0, -1):
        print (i, end=",")
except Exception as e:
    print(e)