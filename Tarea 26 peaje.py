# peaje Vehicular
bus=1
automovil=2
camion=3
vehiculo=float(input("Por favaor seleccione 1 si es un bus, selecione 2 si es automovil, y si es un camion selecione 3"))
if vehiculo<=1:
    print("El vehiculo selecionado fu un Bus")
    print("El valor del peaje a pagar es de 19.600")
elif vehiculo==2:
    print("El vehiculo selecionado fu un Automovil")
    print("El valor del peaje a pagar es de 13.300")
else:
    print("El vehiculo selecionado fu un Camion")
    print("El valor del peaje a pagar es de 35.500")