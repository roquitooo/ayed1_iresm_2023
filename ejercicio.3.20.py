"""El programa debe:

Pedir al usuario una cantidad de tramos de un viaje
pedir al usuario la duracion en minutos de cada tramo
calcular el tiempo total de viaje
no deben generar errores"""
try:
    while True: 
        tramo = int(input("Ingrese la cantidad de tramos: "))
        break

   
    total = 0
    for i in range(tramo):
        minutos = int(input(f"Ingrese la cantidad de minutos de cada tramo, {i+1} :"))
        total += minutos
        print (total)
except Exception as e:
     print (e)