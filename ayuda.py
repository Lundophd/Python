#parcial practico de logica
print("hola!! es te programa te muestra un menu con las siguientes opciones")
print("Opcion 1---->Leer un número entero y determinar si tiene 3 dígitos.")
print("Opcion 2---->Leer un número entero y determinar si es negativo.")
print("Opcion 3---->Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par.")
print("Opcion 4---->Solicitar al usuario tres números y mostrar en pantalla al menor de los tres.")

def opcion1():
    num1 = print(int(input("digite un numero")))
    if (num1 > 99 and num1<1000) or (num1 < -99 and num1 > -1000):
        print("el numero" ,num1, " tiene 3 digitos")
    else:
        print("el" ,num1, " no contiene los 3 digitos que estamos buscando")
        
        
def opcion2(num2):
            num2= int(input("ingrese un numero para saber si es negativo"))
            print(num2)
            if num2 > 0:
                print("el numero" ,num2, "es positivo")
            else:
                print("el numero" ,num2, " es negativo")
                
def opcion3(num3,num4):
        num3= int(input("ingrese el primer numero"))
        num4= int(input("ingrese el segundo numero"))
        print("vamos ver si la suma de" ,num3, "y" ,num4, "es par ")
        resultado = num3 + num4
        print("el resultado de los dos numeros es" ,resultado,)
        if resultado % 2 == 0:
            print("El" ,resultado, " es par")
        else:
            print("El" ,resultado, "es impar")

def opcion4(num5,num6,num7):
        num5= int(input("ingrese el primer numero"))
        num6= int(input("ingrese el segundo numero"))
        num7= int(input("ingrese el tercer numero"))
        if num5 > num6 > num7:
            print("el numero" ,num7, " es el menor de todos")
        elif num5 > num7 > num6:
            print("el numero",num6, " es el menor de todos")
        else:
            print("el numero",num5," es el menor de todos")

opcion = (int(input("Por favor dame la opcion que deses")))
    
if opcion < 2:
    opcion1()
elif opcion <3: 
    opcion2()
elif opcion <4: 
    opcion3()
elif opcion <5:
    opcion4()
else:
    print("digite los opciones establecidas")
    
    
