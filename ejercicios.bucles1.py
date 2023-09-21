"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

try:
    edad = int(input("Introduce tu edad: "))
    edad_inicial = 1
    for años in range(edad_inicial, edad + 1):
        edad_inicial = edad
        print (años)
except:
    print ("No introduciste un numero")