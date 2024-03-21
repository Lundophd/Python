print("buen dia por favor indique su tiempo en la empresa y su inversion ")

print("1| si llevas mas de 5 años de antiguedad y una inversion mayor de 10 palos")
print("2| llevas 5 años de antiguedad pero una inversion menor a 10 palos ")
print("3| tu antiguedad es menor a 5 años pero tu inversion es mayor a 10 palos ")
print("4| no cumples ningun requisito")
NOpcion = int(input("indique la opcion segun los requisitos que cumple "))

cadena1 = "buen dia reciba un cordial saludo, deseandole una feliz navidad y prospero año"
cadena2 = "para comentarle que a su reccepcion le llegara un detalle de parte de la empresa"



if NOpcion <2:
   print(cadena1)
   print(cadena2)
elif NOpcion <3: 
    print(cadena1)
elif NOpcion <4: 
    print(cadena2)
elif NOpcion <5:
    print('feliz navidad :)')
else:
    print("opcion invalida porfavor seguir el menu")