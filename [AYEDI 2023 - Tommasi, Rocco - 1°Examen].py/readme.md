'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: Simulacro Examen 1
 APELLIDO Y NOMBRE: Tommasi Rocco
 DNI: 46.216.436
 CARRERA: Analista de Sistemas
 AÑO: 2023 
 Se debe adjuntar archivos comprimidos en classroom con el siguiente nombre "[AYEDI 2023 - Apellido, Nombre - 1°Examen]" - No necesario
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión Videojuegos"

Introduccion: 
    El siguiente programa consiste en un software de gestion de videojuegos.
    El programa debe permitir agregar y quitar videojuegos al sistema junto con su informacion: 
    Nombre, Año, Categoria.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Permitir al usuario del programa agregar un nuevo videojuego (Indicando: Nombre - Año - Categoria)
       Verificando: Que el nombre no exista previamente, el año este entre 1990 y 2021 y que la categoria corresponda
       con una lista de categorias.(Ayuda: metodo in de list)
       IMPORTANTE: se debe crear una matriz para contener los datos, listas dentro de listas.
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    5. Eliminar una categoria del sistema, verificando previamente su existencia
    6. Salir
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio (minimo un archivo main y otro de funciones)
'''
categorias = ["Acción", "Deportivo", "Estrategia", "Simulación"]

video_juegos=[['fifa'],['Deportivo'],[2021]]

def main():
    while True:
        menu = """--Programa de Agenda--
    1. Agregar un nuevo videojuego
    2. Ver lista de videojuegos (Formato: Nombre - Año - Categoria)
    3. Editar la categoria de un video juego verificando que exista la categoria, se edita mediante el nombre.
    4. Agregar categorias al sistema, poniendo automaticamente la primera letra mayuscula (verificando que no exista previamente).
    5. Eliminar una categoria del sistema, verificando previamente su existencia
    6. Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            pass
        elif(opcion == "2"):
            pass
        elif(opcion == "3"):
            pass
        elif(opcion == "4"):
            pass
        elif(opcion == "5"):
            pass
        elif(opcion == "6"):
            return
        else:
            print('Opcion incorrecta')

if __name__ == "__main__":
    main()