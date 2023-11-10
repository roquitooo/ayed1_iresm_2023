"""un empleado puede cuidar animales de diferentes sectores
Contar con 6 funciones disponibles en el menu (estas funciones deben estar incluidas en una clase llamada GestorZoologico):

Crear instancias de animales (se puede elegir entre los tres sectores) y guardarlos en una lista
Crear instancia de Empleados y guardarlos en una lista
Los empleados se les pueden asignar animales luego, los animales al crearlos en el sistema tienen q contar siosi con un encargado
Asignar a un empleado un animal a cuidar
Cambiar de encargado un animal
imprmiir lista de animales (con toda su informacions)
imprimir lista de Empleados (con toda su informacions)
Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes"""

from clases_zoologico import *

class GestorZoologico:
    def __init__(self):
        self.lista_animales_agua: list[AnimalesAgua] = []
        self.lista_animales_sueltos: list[AnimalesSueltos] = []
        self.lista_animales_jaula: list[AnimalesJaula] = []
        self.lista_animales : list[Animales] = []
        self.lista_empleados: list[Empleados] = []
    
    def cargar_empleado(self):
        legajo = int(input("Ingrese el legajo: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        nuevo_empleado = Empleados(legajo, nombre, apellido)
        self.lista_empleados.append(nuevo_empleado)

    def lugar_animal(self):
        while True:
            print('------ Lugar que pondra al animal ------')
            lista_tipos = []
            for i in Animales.__subclasses__():
                print(f'- {i.__name__}')
                lista_tipos.append(i.__name__)
            tipo_clase = input('Indique el lugar para el animal: ')
            if tipo_clase in lista_tipos:
                return tipo_clase
            else:
                print('Esa clase no existe')

    def verificar_encargado(self):
        print ("--LISTA EMPLEADOS--")
        while True:
            for j in self.lista_empleados:
                j.imprimir_nombre_empleados()
            nombre_encargado = input("Ingrese el encargado que cuidara al animal: ")
            for empleado in self.lista_empleados:
                if empleado.nombre == nombre_encargado:
                    return empleado
            print("El encargado no existe!")

    def verificar_existencia_animal(self):
        print ("--LISTA ANIMALES--")
        while True:
            for j in self.lista_animales:
                j.imprimir_nombre_animales()
            nombre_animal = input("Ingrese el nombre del animal: ")
            for animal in self.lista_animales:
                if animal.nombre == nombre_animal:
                    return animal
                else:
                    print("El animal no existe!")
                

    def cargar_animales(self):
        lugar_animal = self.lugar_animal()
        nombre = input("Ingrese el nombre del animal: ")
        tipo_animal = input("Ingrese el tipo de animal: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        encargado_a_cuidar = self.verificar_encargado()
        if lugar_animal == "AnimalesAgua":
            animal_nuevo = AnimalesAgua(nombre, tipo_animal, fecha_nacimiento, encargado_a_cuidar)
            self.lista_animales_agua.append(animal_nuevo)
            self.lista_animales.append(animal_nuevo)
            encargado_a_cuidar.asignar_animal(nombre)
        if lugar_animal == "AnimalesJaula":
            animal_nuevo = AnimalesJaula(nombre, tipo_animal, fecha_nacimiento, encargado_a_cuidar)
            self.lista_animales_jaula.append(animal_nuevo)
            self.lista_animales.append(animal_nuevo)
            encargado_a_cuidar.asignar_animal(nombre)
        if lugar_animal == "AnimalesSueltos":
            animal_nuevo = AnimalesSueltos(nombre, tipo_animal, fecha_nacimiento, encargado_a_cuidar)
            self.lista_animales_sueltos.append(animal_nuevo)
            self.lista_animales.append(animal_nuevo)
            encargado_a_cuidar.asignar_animal(nombre)

    def asignar_animal_al_empleado(self):
        empleado = self.verificar_encargado()
        animal = self.verificar_existencia_animal()
        empleado.asignar_animal(animal)
        animal.cambiar_empleado(nombre= empleado)

    def cambiar_encargado_del_animal(self):
        animal = self.verificar_existencia_animal()
        empleado = self.verificar_encargado()
        animal.cambiar_empleado(empleado)
        empleado.asignar_animal(animal)


    def listar_animales(self):
        print ("--LISTA ANIMALES AGUA--")
        for i in self.lista_animales_agua:
            i.imprimir_info_animales()
        print ("--LISTA ANIMALES JAULA--")
        for j in self.lista_animales_jaula:
            j.imprimir_info_animales()
        print ("--LISTA ANIMALES SUELTOS--")
        for k in self.lista_animales_sueltos:
            k.imprimir_info_animales()

    def listar_empleados(self):
        for i in self.lista_empleados:
            i.imprimir_info_empleados()
    



        


    
