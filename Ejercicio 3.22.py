"""El programa debe:
*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    No deben generar errores"""


try:
    while True: 
        cantidad_personas = input("Ingrese la cantidad de personas: ")
        if cantidad_personas.isdigit():
            cantidad_personas = int(cantidad_personas)
            break
        else:
            print("No ingresaste un numero")
except Exception as e:
    print (e)

edad_mayor = 0

while True:
    try:
        for i in range(cantidad_personas):
            edad = int(input(f"Ingrese la edad de la persona numero {i+1}: "))
            if edad > edad_mayor:
                edad_mayor = edad
        print (f"La edad mas alta es:", edad_mayor)
        break
    except ValueError:
        print ("Debe ingresar un numero")



