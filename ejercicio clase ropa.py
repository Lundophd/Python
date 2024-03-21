print("Hola usuario bienvenido a la tienda f.s.e ")
nombre=(input("para empezar dame tu nombre"))
print("opcion 1---> blusas")
print("opcion 2---> camisas")
print("opcion 3---> pantalones")
print("opcion 4---> cachuchas")
opcion = int(input("Dame una opcion"))

if opcion <2:
    def valorunidad (a,b):
        multi=a*b
        return multi

    def main():
        valoru=30000
        print(f"el valor por unidad de los pantalones es de {valoru}")
        num2=int(input("dime cuantos pantalones deseas comprar"))
        print(f"{nombre} la cantidad de prendas que deseas comprar es {num2}")
        final1=valorunidad(valoru,num2)
        print(nombre," el valor a pagar por los pantalones es de ",final1)
    
    if __name__ == "__main__":
         main()


elif opcion <3:
        
    def valorc(a,b):
        multi=a*b
        return multi

    def main():
    
        precio2=45000
        print(f"{nombre} el valor por unidad de las camisas es de {precio2}")
        num2=int(input("dime cuantas camisas deseas comprar"))
        print(f"{nombre} la cantidad de prendas que deseas comprar es {num2}")
        final=valorc(precio2,num2)
        print(f"el valor de las camisas es de {final}")
    
    if __name__ == "__main__":
            main()
elif opcion <4:
        
    def valorzapatos (a,b):
        multi=a*b
        return multi

    def main():
        num1=78900
        num2=int(input("dime cuantos pares de zapatos deseas comprar"))
        print(f"{nombre} el valor por par de los zapatos es de {num1}")
        print(f"la cantidad de prendas que deseas comprar es {num2}")
        final3=valorzapatos(num1,num2)
        print(f"{nombre}el valor a pagar por los pares de zapatos es de {final3}")
    
    if __name__ == "__main__":
            main()

elif opcion <5:
    
        
    def valormedias (a,b):
        multi=a*b
        return multi

    def main():
        medias=20000
        print(f"el valor por par de medias es de {medias}")
        mediasop=int(input("dime cuantos pares de medias deseas comprar"))
        print(f"la cantidad de prendas que deseas comprar es {mediasop}")
        print(f"el valor por par de medias es de {medias}")
        final=valormedias(medias,mediasop)
        print(f"{nombre} el valor a pagar por los pares de medias es de {final}")
    
    if __name__ == "__main__":
        main()
