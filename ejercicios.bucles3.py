"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

numero = int(input("Introduce numero entero posiivo: "))
cont = -1
for i in range(numero, cont, -1):
    print (i, end=",")
