"""El programa debe:

Pedir al usuario una palabra
Verificar que sea una palabra y no un numero
Mostrar por pantalla las letras una a una
No producir errores"""

try:
    while True:
        palabra = input("Escribe una palabra: ")
        if (palabra).isalpha():
            break
        else:
            print ("no introduciste una palabra")
            
    for letra in (palabra):
        print (letra)

except Exception as e:
    print (e)