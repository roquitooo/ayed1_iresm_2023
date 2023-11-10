from gestor_zoologico import GestorZoologico
def menu():
    obj_gestor = GestorZoologico()
    while True:
        menu = """
1. Crear instancias de animales (se puede elegir entre los tres sectores) y guardarlos en una lista
2. Crear instancia de Empleados y guardarlos en una lista
3. Asignar a un empleado un animal a cuidar
4. Cambiar de encargado un animal
5. imprmiir lista de animales (con toda su informacions)
6. imprimir lista de Empleados (con toda su informacions)
7. Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.cargar_animales()
            case '2':
                obj_gestor.cargar_empleado()
            case '3':
                obj_gestor.asignar_animal_al_empleado()
            case '4':
                obj_gestor.cambiar_encargado_del_animal()
            case '5':
                obj_gestor.listar_animales()
            case '6':
                obj_gestor.listar_empleados()
            case '7':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()