
"""El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores."""
try:

    while True:
        dato = input("ingrese un dato: ")
        if dato == "python":
            print("Correcto")
            break
        else:
            print("Palabra Incorrecta")
except Exception as e:
    print (e)



