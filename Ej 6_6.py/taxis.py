""" 1. Crear instancias de choferes y guardarlos en una lista de choferes
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    4. Modificar el lugar de residencia del chofer indicando su nombre
    5. imprmiir lista de choferes (con toda su informacion)
    6. imprimir lista de autos (con toda su informacions)"""

class Autos:
    def __init__(self, patente, modelo , año, marca, nombre_Chofer):
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.nombre_Chofer = nombre_Chofer

    def cambiar_chofer(self, nuevo_chofer):
        self.nombre_Chofer = nuevo_chofer
    
    def mostrar_autos(self):
        print(f"La patente del auto es {self.patente} de modelo {self.modelo} del año {self.año} marca {self.marca} y el chofer que lo maneja es {self.nombre_Chofer}")


class Chofer:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia

    def cambiar_residencia(self, nueva_residencia):
        self.residencia = nueva_residencia

    def cambiar_chofer(self, nuevo_chofer):
        self.nombre = nuevo_chofer

    def mostrar_choferes(self):
        print(f"El nombre del chofer es {self.nombre} de apellido {self.apellido} dni {self.dni} nacio el {self.fecha_nacimiento} y vive en {self.residencia}")
    
    def cambiar_residencia(self, nueva_residencia):
        self.residencia = nueva_residencia




