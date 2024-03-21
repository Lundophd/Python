

class Bebida:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getObtenerNombre(self):
        return f"la bebida es {self.__nombre}"

class Cerveza (Bebida):
    def __init__(self, nombre, marca, alhocol):
        super().__init__(nombre)
        
        self.__marca = marca
        self.__alhocol = alhocol
    
    def getObtenerNombre(self):
        return f"{super().getObtenerNombre()} de la marca {self.__marca} con grado de alhocol {self.__alhocol} "

cerveza = Cerveza("poker ", "babaria ", 4.0)
print(cerveza.getObtenerNombre())