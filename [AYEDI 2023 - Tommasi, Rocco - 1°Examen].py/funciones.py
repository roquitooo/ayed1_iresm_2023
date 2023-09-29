categorias = ["Accion", "Deportivo", "Estrategia", "Simulacion"] 
video_juegos=[['Fifa'],['Deportivo'],[2021]]

def pedir_un_str (texto_a_pedir):
    while True:
        variable_str = input(texto_a_pedir)
        if (variable_str).isalpha():
            break
        else:
            print("Debes escribir una palabra, no numeros")
    return variable_str.lower()

def pedir_un_int (texto_a_pedir):
    while True:
        try:
            variable_int = int(input(texto_a_pedir))
            break
        except Exception as e:
            print(e)
    return variable_int
        
def agregar_juego():
    juego = pedir_un_str("Ingrese el nombre del videojuego: ").capitalize()
    if juego not in video_juegos[0]:
        año_juego = pedir_un_int("Ingrese el año del juego: ")
        if 1990 < año_juego < 2021:
            categoria_del_juego = pedir_un_str("Ingrese la categoria del juego: ").capitalize()
            if categoria_del_juego in categorias:
                video_juegos[0].append(juego)
                video_juegos[1].append(categoria_del_juego)
                video_juegos[2].append(año_juego)
                print ("\nEl juego ha sido agregado con exito!")
                return
            else:
                print("\nEl juego no se encuentra dentro de las categorias!")
        else:
            print("\nEl juego debe estar entre el año 1990 y 2021!")
    else:
        print("\nEl juego ya se encuentra en los videojuegos!")

def lista_videojuegos(video_juegos):
    print ("NOMBRE  - AÑO -  CATEGORIA ")
    for i in range(len(video_juegos[0])):
        print(f"{video_juegos[0][i]} - {video_juegos[1][i]} - {video_juegos[2][i]}")
    
def editar_categoria():
    print ("NOMBRE")
    for i in range(len(video_juegos[0])):
        print(f"{video_juegos[0][i]}")
    juego_a_editar = pedir_un_str("Seleccione el juego a editar la categoria: ").capitalize()
    if juego_a_editar in video_juegos[0]:
        categoria_nueva = pedir_un_str("\n -Accion \n Deportivo \n -Estrategia \n -Simulacion \n Ingrese la categoria nueva para el juego: ").capitalize()
        if categoria_nueva in categorias:
            index = video_juegos[0].index(juego_a_editar)
            video_juegos[1][index] = categoria_nueva      
            print("\nLa categoria se edito con exito!")
        else:
            print("\nLa categoria no existe!")
    else:
        print("\nEl juego no existe!")
    
def agregar_categorias():
    categoria_nueva = pedir_un_str("Ingrese la categoria nueva: ").capitalize()
    if categoria_nueva not in categorias:
        categorias.append(categoria_nueva)
        print ("\nLa categoria se agrego con exito!")
    else:
        print ("\nLa categoria ya existe!")

def eliminar_categorias():
    categoria_a_eliminar = pedir_un_str("Ingrese la categoria a eliminar: ").capitalize()
    if categoria_a_eliminar in categorias:
        index = categorias.index(categoria_a_eliminar)
        categorias.pop(index)
        print ("\nLa categoria se elimino con exito!")
    else:
        print ("\nLa categoria no existe!")

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
            agregar_juego()
        elif(opcion == "2"):
            lista_videojuegos(video_juegos)
        elif(opcion == "3"):
            editar_categoria()
        elif(opcion == "4"):
            agregar_categorias()
        elif(opcion == "5"):
            eliminar_categorias()
        elif(opcion == "6"):
            print ("Adios")
            break
        else:
            print('Opcion incorrecta')
