"""El programa debe:

Contar con 3 funciones:

Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)

Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.IMPORANTE:deben ser palabras y no frases (verificar)

Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales

Contar con un menu donde debe pedir al usuario que operacion realizar

Pedir los parametros y devolver el resultado al usuario

Gestionar posibles errores"""

def contador_letras(palabra):
    acumulador = 0
    for i in(palabra):
        if i.isalpha():
            acumulador +=1
    return f"\tLa cantidad de letras que tiene {palabra} es: {acumulador}"


def comparador_palabras (palabra1, palabra2):
        if palabra1 > palabra2:
            return f"\tLa palabra '{palabra1}' es mayor a '{palabra2}', ya que la palabra '{palabra1}' tiene: {len(palabra1)}"
        elif palabra2 > palabra1:
            return f"\tLa palabra '{palabra2}' es mayor a '{palabra1}', ya que la palabra '{palabra2}' tiene: {len(palabra2)}"
        else: 
            return f"\tla palabra '{palabra1}' y la palabra '{palabra2}' son iguales"
        
def quitador_vocales (palabra_frase):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    palabra_sin_vocales = ""
    for letra in palabra_frase:
        if letra not in vocales:
            palabra_sin_vocales +=letra
    return f"\tLa palabra o frase {palabra_frase} sin vocales es: {palabra_sin_vocales}"

      
def pedir_palabra():
    while True: 
        try:
            argumento = (input("\tEscribe una palabra: "))
            return argumento
        except ValueError:
            print("No ingresaste un numero")

def menu():
    while True:
        menu = """
        MENU CONTADOR
        1- Contador de letras de una palabra
        2- Comparador de palabras
        3- Quitador de Vocales
        4- SALIR    
        Elige una opcion: """

        opcion = input(menu)
        match opcion:
            case "1": 
                a = pedir_palabra()
                print (contador_letras(a))
            case "2":
                a = pedir_palabra()
                b = pedir_palabra()
                print (comparador_palabras(a,b))
            case "3": 
                a = pedir_palabra()
                print (quitador_vocales(a))
            case "4":
                print ("Saliendo")
                return
            case default:
                print ("Opcion incorrecta")
menu()



