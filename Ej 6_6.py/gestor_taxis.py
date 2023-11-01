from taxis import *

class Gestor_taxis(Autos, Chofer):
    def __init__(self):
        self.lista_choferes : list[Chofer] = []
        self.lista_autos : list[Autos] = []

    def crear_chofer(self):
        nombre = input("Ingrese el nombre del nuevo chofer: ")
        apellido = input("Ingrese el apellido del auto del nuevo chofer: ")
        dni = int(input("Ingrese el dni del nuevo chofer: "))
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo chofer: ")
        residencia = input("Ingrese la residencia del nuevo chofer: ")
        nuevo_chofer = Chofer(nombre, apellido, dni, fecha_nacimiento, residencia)
        self.lista_choferes.append(nuevo_chofer)
    
    def crear_autos(self):
        nombre_chofer = input("Ingrese el nombre del chofer que va a manejar el nuevo auto: ")
        for choferes in self.lista_choferes:
            if choferes.nombre == nombre_chofer:
                patente = input("Ingrese la patente del nuevo auto: ")
                modelo = input("Ingrese el modelo del nuevo auto: ")
                año = int(input("Ingrese el año del nuevo auto: "))
                marca = input("Ingrese la marca del nuevo auto: ")
                nuevo_chofer = Autos(patente, modelo, año, marca, nombre_chofer)
                self.lista_autos.append(nuevo_chofer)
            else:
                print("El chofer no existe!")

    def listar_choferes(self):
        for i in self.lista_choferes:
            i.mostrar_choferes()
    def listar_autos(self):
        for i in self.lista_autos:
            i.mostrar_autos()

    
    def modificar_chofer(self):
        chofer = input("Ingrese el chofer que quiere cambiar: ")
        for choferes in self.lista_choferes:
            if choferes.nombre == chofer:
                nuevo_chofer = input("Ingrese el nombre del nuevo chofer: ")
                choferes.cambiar_chofer(nuevo_chofer)
                for chofer in self.lista_autos:
                    chofer.cambiar_chofer(nuevo_chofer)
            else:
                print("No existe el chofer!")

    def modificar_residencia(self):
        chofer = input("Ingrese el chofer que quiere cambiarle la residencia: ")
        for choferes in self.lista_choferes:
            if choferes.nombre == chofer:
                nueva_residencia = input("Ingrese la nueva residencia del chofer: ")
                choferes.cambiar_residencia(nueva_residencia)
            else:
                print("El chofer no existe!")


