"""El programa debe:
*   Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
*   Debe comenzar con las siguientes peliculas y series en un diccionario:

```
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["Prision break", "La casa de papel" , "Los simpsons"]
        }
```


*   Contar con 5 funciones disponibles en el menu:
    1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2. Agregar nuevas peliculas o series (que no esten) en la base.
    3. Eliminar peliculas o series de la base.
    4. Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
    5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el")."""

base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["Prision break", "La casa de papel" , "Los simpsons"]
        }

def mostrar_lista():
    print ("--PELICULAS--")
    for i in base["peliculas"]:
        print(i)
    print("--SERIES--")
    for j in base["series"]:
        print (j)

def agregar_pelis ():
    pelicula_nueva = input("Ingrese la pelicula nueva: ")
    if pelicula_nueva not in base["peliculas"]:
        base["peliculas"].append(pelicula_nueva)
        print("La pelicula se agrego con exito!")
    else: 
        print("La pelicula ya se encuentra en la lista!")

def agregar_series ():
    serie_nueva = input("Ingrese la serie nueva: ")
    if serie_nueva not in base["series"]:
        base["series"].append(serie_nueva)
        print("La series se agrego con exito!")
    else: 
        print("La serie ya se encuentra en la lista!")

def eliminar_pelis():
    for i in base["peliculas"]:
        print (i)
    peli_a_eliminar = input("Ingrese la pelicula a eliminar: ")
    if peli_a_eliminar in base["peliculas"]:
        base["peliculas"].remove(peli_a_eliminar)
        print("La pelicula se elimino con exito!")
        mostrar_lista()
    else:
        print("La pelicula no existe!")

def eliminar_series():
    for i in base["series"]:
        print (i)
    series_a_eliminar = input("Ingrese la serie a eliminar: ")
    if series_a_eliminar in base["series"]:
        base["series"].remove(series_a_eliminar)
        print("La serie se elimino con exito!")
        mostrar_lista()
    else:
        print("La serie no existe!")

def lista_peliculas():
    inicio = int(input("Ingrese el punto inicial de donde quiere empezara a ver: "))
    final = int(input("Ingrese el punto final de donde quiere terminar de ver: "))
    if 0 <= inicio < final and final <= (len(base["peliculas"])):
        lista = base["peliculas"][inicio:final]
        for i in lista:
            print("Las peliculas dentro del rango son:")
            print (i)
    else:
        print("Esta fuera de rango!")

def buscar_peli():
    palabra = input("Elige una palabra que contenga la pelicula: ").capitalize()
    peliculas_coincidentes = []
    flag = False
    for pelicula in base["peliculas"]:
        if palabra in pelicula:
            peliculas_coincidentes.append(pelicula)
            print(pelicula)
            flag = True
    if flag == False:
        print("No se encontro ninguna pelicula")

def buscar_serie():
    palabra = input("Elige una palabra que contenga la serie: ").capitalize()
    series_coincidentes = []
    flag = False
    for serie in base["series"]:
        if palabra in serie:
            series_coincidentes.append(serie)
            print(serie)
            flag = True
    if flag == False:
        print("No se encontro ninguna serie")

def main():
    while True:
        menu = """menu:
    1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2. Agregar nuevas peliculas 
    3. Agregar nueva serie
    4. Eliminar peliculas
    5. Eliminar serie
    6. Mostrar lista de series desde un punto a otro
    7. Buscar peliculas que contenga una palabra en especifico
    8. Buscar serie que contenga una palabra en especifico
    9. SALIR
    Seleccion una opcion: """

        opcion = input(menu)
        if(opcion == "1"):
            mostrar_lista()
        elif(opcion == "2"):
            agregar_pelis()
        elif(opcion == "3"):
            agregar_series()
        elif(opcion == "4"):
            eliminar_pelis()
        elif(opcion == "5"):
            eliminar_series()
        elif (opcion =="6"):
            lista_peliculas()
        elif (opcion =="7"):
            buscar_peli()
        elif(opcion == "8"):
            buscar_serie()
        elif (opcion == "9"):
            print("ADIOS")
            break
        else:
            print('Opcion incorrecta')

main()