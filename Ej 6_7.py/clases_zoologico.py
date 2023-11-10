"""Ejercicio 6.7 (Zoologico)
Simular un programa de gestion de animales de un zoologico, que cuente con dos clases Animales y Empleados

La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (Nombre de objeto empleado))

Crear 3 clases que hereden de animal segun su sector del zoologico
Animales en jaulas.
Animales sueltos.
Animales en el agua
La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))"""


class Empleados:
    def __init__(self, legajo: int, nombre: str, apellido: str):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.lista_animales_a_cuidar = []
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def imprimir_info_empleados(self):
        print (f"El legajo es {self.legajo}, se llama {self.nombre} apellido {self.apellido} y cuida a: ")
        for i in self.lista_animales_a_cuidar:
            print (f"- {i}")

    def imprimir_nombre_empleados(self):
        print (f"- {self.nombre}")
    
    def asignar_animal(self, nombre):
        self.lista_animales_a_cuidar.append(nombre)
        

class Animales:
    def __init__(self, nombre: str, tipo_animal_: str, fecha_nacimiento: str, encargado_cuidar: Empleados):
        self.nombre = nombre
        self.tipo_animal = tipo_animal_
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar

    def imprimir_info_animales(self):
        print (f"El nombre es {self.nombre}, tipo de animal {self.tipo_animal} nacio el {self.fecha_nacimiento} y lo cuida {self.encargado_cuidar}")

    def imprimir_nombre_animales(self):
        print (f"- {self.nombre}")

    def __str__(self):
        return f"{self.nombre}"
    
    def cambiar_empleado(self, nombre):
        self.encargado_cuidar = nombre

class AnimalesJaula(Animales):
    def __init__(self, nombre: str, tipo_animal_: str, fecha_nacimiento: str, encargado_cuidar: Empleados):
        super().__init__(nombre, tipo_animal_, fecha_nacimiento, encargado_cuidar)
       

class AnimalesSueltos(Animales):
    def __init__(self, nombre: str, tipo_animal_: str, fecha_nacimiento: str, encargado_cuidar: Empleados):
        super().__init__(nombre, tipo_animal_, fecha_nacimiento, encargado_cuidar)

class AnimalesAgua(Animales):
    def __init__(self, nombre: str, tipo_animal_: str, fecha_nacimiento: str, encargado_cuidar: Empleados):
        super().__init__(nombre, tipo_animal_, fecha_nacimiento, encargado_cuidar)

