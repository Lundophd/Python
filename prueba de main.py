#ejercicio en clase
print("Hola usuario bienvenido a la tienda f.s.e")
nombre=print(input("para empezar dame tu nombre"))
print("opcion 1---> blusas")
print("opcion 2---> camisas")
print("opcion 3---> pantalones")
print("opcion 4---> cachuchas")
opcion=(int(input("dame una opcion")))

if opcion <1:
    def main():
        precio=("la blusa vale 30.000 por unidad")
        cantidad=print(int(input(nombre," por favor dame el numero de prendas que deseas")))
        if cantidad == 1:
            print(nombre," el valor de la camisa es de $30000")
        else:
            resultado=cantidad*30000   
            print(nombre," el total a pagar es de ",resultado)
    
    if __name__ == "__main__":    
        main()

elif opcion <3: 
    def main():
        precio2=print("la blusa vale 45.000 por unidad")
        cantidad=print(int(input(" por favor dame el numero de prendas que deseas")))
        if cantidad == 1:
            print(nombre," el valor de la camisa es de $45000")
        else:
            resultado=cantidad*45000    
            print(nombre," el total a pagar es de ",resultado)
        if __name__=="__camisas__":
            main()
            
elif opcion <4: 
    def main():
        precio3=print("la blusa vale 50.000 por unidad")
        cantidad=print(int(input(nombre," por favor dame el numero de prendas que deseas")))
        if cantidad ==1:
            print(nombre," el valor de la camisa es de $50000")
        else:
            resultado=cantidad*50000    
            print(nombre," el total a pagar es de ",resultado) 
        if __name__=="__pantalones__":
            main()

elif opcion <5:
    def main():
        precio4=print("la blusa vale 2.000 por unidad")
        cantidad=print(int(input(nombre," por favor dame el numero de prendas que deseas")))
        if cantidad ==1:
            print(nombre," el valor de la camisa es de $2000")
        else:
            resultado=cantidad*2000    
            print(nombre," el total a pagar es de ",resultado)
        if __name__=="__cachuchas__":
            main()
else:
    print("digite los opciones establecidas")