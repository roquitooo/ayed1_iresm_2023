"""El programa debe:
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores"""

def celsius_fahrenheit (a):
    suma = (a * (9/5)) + 32
    return f"\n\t{a} °C pasados a fahrenheit es: {round((suma),2)}°F"

def cm3_litros (a):
    suma = a / 1000
    return f"\n\t{a} cm3 pasados a litros es: {round((suma),2)}L"


def litros_cm3 (a):
    suma = a * 1000
    return f"\n\t{a} litros pasados a cm3 es: {round((suma),2)} cm3"

def pesos_dolares (a):
    suma = a / 717
    return f"\n\t${a} pesos pasados a dolares es ${round((suma),2)} USD"

def pedir_numero():
    while True: 
        try:
            argumento = float(input("\tEscribe un numero: "))
            return argumento
        except ValueError:
            print("No ingresaste un numero")

def menu():
    while True:
        menu = """
        MENU CONVERSIONES
        1- Convertir Grados Celsius a Fahrenheit
        2- Convertir CM3 a Litros
        3- Convertir Litros a CM3
        4- Convertir Pesos ARS a $ DOLARES
        5- SALIR    
        Elige una opcion: """

        opcion = input(menu)
        if opcion in ["1", "2", "3", "4"]:
            a = pedir_numero ()
        match opcion:
            case "1": 
                print(celsius_fahrenheit(a))
            case "2":
                print(cm3_litros(a))
            case "3": 
                print(litros_cm3(a))
            case "4":
                print(pesos_dolares(a))
            case "5":
                print ("Saliendo")
                return
            case default:
                print ("Opcion incorrecta")
menu()



        



