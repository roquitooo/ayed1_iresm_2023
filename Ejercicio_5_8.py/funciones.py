base_taxis = [["IRM-200","ABC-123","LOI-555"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def pedir_un_str(texto_para_pedir):
    while True:
        variable_str = input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()

def imprimir_base_taxis(base_taxis):
    print ("\nAUTO -  CHOFER  - RECORRIDO")
    for i in range(len(base_taxis[0])):
        print (f"{base_taxis[0][i]} - {base_taxis[1][i]} - {base_taxis[2][i]}km")

def recorrido_a_realizar ():
    recorrido = pedir_un_int("Indique el recorrido en KM que desea realizar: ")
    print ("Posibles choferes:")
    for i in range(len(base_taxis[0])):
        if recorrido <= base_taxis[2][i]:
            print ((base_taxis[1][i]),(base_taxis[2][i]))
        else:
            print ("No puedes realizar el viaje")
        break
    
def modificar_nombre():
    imprimir_base_taxis(base_taxis)
    auto_a_cambiar = input("Elige la PATENTE del auto del chofer nuevo: ").upper()
    if auto_a_cambiar in base_taxis[0]:
        nombre_nuevo = input("Elige el nombre nuevo del chofer del auto seleccionado: ")
        index = base_taxis[0].index(auto_a_cambiar)
        base_taxis[1][index] = nombre_nuevo
        return base_taxis
    else:
        print("No elegiste ningun auto")

def modificar_recorrido():
    imprimir_base_taxis(base_taxis)
    nombre_chofer = input("Elige el NOMBRE del chofer del recorrido nuevo: ")
    if nombre_chofer in base_taxis[1]:
        recorrido_nuevo = pedir_un_int("Elige el nuevo recorrido del chofer seleccionado: ")
        index = base_taxis[1].index(nombre_chofer)
        base_taxis[2][index] = recorrido_nuevo
        return base_taxis
    else:
        print("No elegiste ningun auto")

def nuevo_auto(base_taxis):
    nueva_patente = input("Indique la patente del nuevo auto: ").upper()
    if nueva_patente not in base_taxis[0]:
        base_taxis[0].append(nueva_patente)
        nuevo_chofer = pedir_un_str("Indique el nombre del nuevo chofer: ")
        if nuevo_chofer not in base_taxis[1]:
            base_taxis[1].append(nuevo_chofer)
            nuevo_recorrido = pedir_un_int ("Ingrese el recorrido maximo del nuevo chofer: ")
            base_taxis[2].append(nuevo_recorrido)
            print ("\nBase de taxis actualizada!")  
        else:
            print("El chofer ya esta registrado en la base de taxis!")
    else:
        print("La patente ya esta registrada!")

def informacion_chofer ():
    chofer = pedir_un_str("Ingrese el nombre del chofer para acceder a su informacion: ")
    if chofer in base_taxis[1]:
        index  = base_taxis[1].index(chofer)
        auto = base_taxis[0][index]
        nombre = base_taxis[1][index]
        recorrido = base_taxis[2][index]
        print (f"La patente de chofer es {auto}, el nombre es {nombre} y el recorrido maximo que puede realizar es: {recorrido}")
    else:
        print ("El chofer no existe!")

def eliminar_chofer (base_taxis):
    print("---LISTA DE CHOFERES---")
    for i in range(len(base_taxis[1])):
        print (base_taxis[1][i])
    chofer_a_eliminar = input("Eliga el chofer a eliminar: ")
    if chofer_a_eliminar in base_taxis[1]:
        index = base_taxis[1].index(chofer_a_eliminar)
        base_taxis[1].pop(index)
        print(f"\nEl chofer {chofer_a_eliminar} ha sido eliminado con exito!")
        return base_taxis
    else:
        print ("\nEl chofer no existe!")
   
def menu_general():
    while True:
        opcion = input('''
Eliga una opcion
                       
    1. Realizar un viaje segun su recorrido deseado
    2. Modificar nombre del chofer
    3. Modificar el recorrido del auto.
    4. Mostrar Base de Taxis
    5. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo. 
    6. Observar informacion de un chofer
    7. Eliminar un chofer
    8. Salir

Opcion: ''')
        if opcion == '1':
            recorrido_a_realizar()
        elif opcion == '2':
            modificar_nombre()
        elif opcion == '3':
            modificar_recorrido()
        elif opcion == '4':
            imprimir_base_taxis(base_taxis)
        elif opcion == '5':
            nuevo_auto(base_taxis)
        elif opcion == '6':
            informacion_chofer()
        elif opcion =='7':
            eliminar_chofer(base_taxis)
        elif opcion == '8':
            print("Adios")
            break
        else:
            print('opcion incorrecta')