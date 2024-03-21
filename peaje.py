print("Este programa servira como peaje para 3 tipos de vehiculo")
print("Para salir ingrese el numero 0")
print("Para Automovil ingrese el numero 1")
print("Para Bus ingrese el numero 2")
print("Para Caminon ingrese el numero 3")
Tvehiculo = int(input("Tipo de vehiculo es:  "))
if Tvehiculo == 1:
    preciopeaje = 4000
    
elif Tvehiculo == 2:
      precipeaje = 10.000
 
elif Tvehiculo == 3:
      preciopeaje = 12000

print("El vehiculo tiende que pagar:",preciopeaje)