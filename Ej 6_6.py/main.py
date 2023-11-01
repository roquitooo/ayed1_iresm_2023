
from gestor_taxis import Gestor_taxis
def menu():
    obj_gestor = Gestor_taxis()
    while True:
        menu = """
    1. Crear Chofer
    2. Crear Autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes 
    6. imprimir lista de autos
    7. SALIR
    Opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_chofer()
            case '2':
                obj_gestor.crear_autos()
            case '3':
                obj_gestor.modificar_chofer()
            case '4':
                obj_gestor.modificar_residencia()
            case '5':
                obj_gestor.listar_choferes()
            case '6':
                obj_gestor.listar_autos()
            case'7':
                print("Adios")
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()