"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

numero = int(input("Escribe un numero entero positivo: "))
inicio = 1
for i in range(inicio, numero, 2):
    inicio += numero
    print (i, end=",")