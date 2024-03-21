class Persona:
    total_personas = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1
        
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    total_estudiantes = 0
    
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
    
    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")


class Profesor:
    total_profesores = 0
    
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        Profesor.total_profesores += 1
    
    def presentarse(self):
        print(f"Profesor: {self.nombre}, Edad: {self.edad}, Especialidad: {self.especialidad}")


class EstudianteProfesor(Estudiante, Profesor):
    def __init__(self, nombre, edad, carrera, especialidad):
        Estudiante.__init__(self, nombre, edad, carrera)
        Profesor.__init__(self, nombre, edad, especialidad)
    
    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad} años. Soy estudiante de {self.carrera} y también profesor de {self.especialidad}.")


# Ejemplo de uso
persona1 = Persona("Juan", 30)
persona1.saludar()

estudiante1 = Estudiante("Maria", 20, "Ingeniería")
estudiante1.saludar()
estudiante1.mostrar_info()

profesor1 = Profesor("Pedro", 40, "Matemáticas")
profesor1.presentarse()

estudiante_profesor1 = EstudianteProfesor("Ana", 25, "Biología", "Ecología")
estudiante_profesor1.saludar()
estudiante_profesor1.mostrar_info()
estudiante_profesor1.presentarse()

print(f"Total de personas: {Persona.total_personas}")
print(f"Total de estudiantes: {Estudiante.total_estudiantes}")
print(f"Total de profesores: {Profesor.total_profesores}")
