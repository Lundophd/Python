def sumar(a,b):
    suma=a+b
    return suma

def main():
    print("Hola mundo")
    num1=int(input("Dame un numero"))
    num2=int(input("Dame otro numero"))
    #suma=num1+num2
    #print("El resultado de la suma de los numeros dados es ",suma)
    d=sumar(num1,num2)
    print(f"la suma es",d)
    print(f"la suma es {sumar(num1,num2)}")
    if d%2 ==0:
        print("es par")
    else:
        print("no es par")

if __name__ == "__main__":
    main()
    

