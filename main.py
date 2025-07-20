class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."
alumno = Estudiante("Laura", 20, "Ingeniería de Sistemas")
print(alumno.presentarse())
print(alumno.estudiar())

