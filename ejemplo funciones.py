#Ejemplo de Funciones

#Funcion para pedir datos al usuario
def pedirNum1 ():
    num1 = int(float(input("Dame el primer dato")))
    return num1

def pedirNum2():
    num2 = int(float(input("Dame el segundo dato")))
    return num2

def sumar ():
    A= pedirNum1()
    B= pedirNum2()
    suma = A+B
    return suma

print (f"El resultado de la suma es {sumar()}")