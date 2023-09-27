def pedir_un_str(texto_para_pedir):
    while True:
        variable_str= input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

def imprimir_base_frutas():
    print('-----BASE DE FRUTAS------')
    for i in range(len(base_frutas[0])):
        print(f"{base_frutas[0][i]} \t {base_frutas[1][i]}")
    
def imprimir_base_verduras():
    print('-----BASE DE VERDURAS------')
    for i in range(len(base_verduras[0])):
        print(f"{base_verduras[0][i]}\t {base_verduras[1][i]}")

base_frutas = [['Fruta'],['Stock']] #declaro una lista con dos columas
base_verduras = [["Verdura"],["Stock"]]

nueva_fruta = pedir_un_str('Ingrese una nueva fruta: ')
stock_de_la_fruta = pedir_un_int('Ingrese el stock fruta: ')
nueva_verdura = pedir_un_str('Ingrese una nueva verdura: ')
stock_de_la_verdura = pedir_un_int('Ingrese el stock verdura: ')

base_frutas[0].append(nueva_fruta)
base_frutas[1].append(stock_de_la_fruta)
base_verduras[0].append(nueva_verdura)
base_verduras[1].append(stock_de_la_verdura)


def agregar_stock ():
    opcion = input("Que alimento quieres agregar?\n Fruta o Verdura(f/v): ")
    while True:
        nuevo_alimento = pedir_un_str("Ingrese un nuevo alimento: ")
        if opcion == "f" and nuevo_alimento in base_frutas[0]:
            print ("Esta fruta ya esta en el inventario")
        if opcion == "v" and nuevo_alimento in base_verduras[0]:
            print("Esta verdura ya esta en el inventario")
        else:
            break
    nuevo_stock = pedir_un_int("Ingrese la cantidad de alimento que quiere agregar: ")
    if opcion =="f":
        base_frutas [0].append(nuevo_alimento)
        base_frutas [1].append(nuevo_stock)
    if opcion =="v":
        base_verduras [0].append(nuevo_alimento)
        base_verduras [1].append(nuevo_stock)


def eliminar_stock():
    opcion = input("Que alimento quieres eliminar?\n Fruta o Verdura(f/v): ")
    while True:
        if opcion == "f":
            imprimir_base_frutas()
            opcion2 = pedir_un_str("Que alimento de las frutas quieres eliminar: ")
            if opcion2 in base_frutas[0]:
                base_frutas[0].remove(opcion2)
                break
            else:
                print("El alimento no está en la lista de frutas.")
        elif opcion == "v":
            imprimir_base_verduras()
            opcion2 = pedir_un_str("Que alimento de las verduras quieres eliminar: ")
            if opcion2 in base_verduras[0]:
                base_verduras[0].remove(opcion2)
                break
            else:
                print("El alimento no está en la lista de verduras.")
        else:
            print("Opción no válida. Debes seleccionar 'f' o 'v'.")
            break

def consultar_stock():
    imprimir_base_verduras()
    imprimir_base_frutas()

def menu_general():
    while True:
        opcion = input('''
Eliga una opcion
      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock
Opcion: ''')
        if opcion == '1':
            agregar_stock()
        elif opcion == '2':
            consultar_stock()
        elif opcion == '3':
            eliminar_stock()
        else:
            print('opcion incorrecta')


    

