#condicionales adicionales

edad = int(input("Dame tu edad"))

if edad>0 and edad<110:
    print("Digitaste una edad correcta")
    if edad >=18:
        print("Es mayor de edad")
    else:
        print("es menor de edad")
else:
    print("Digitaste mal la edad")  