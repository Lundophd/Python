numeros=[]
a=0
while a<10:
    num=int(input("dame un dato"))
    a=a+1
    numeros.append(num)

print(numeros)
buscar= int(input("\n \n dime el numero que deseas buscar en la lista "))
if (buscar in numeros):
    print("El numero que buscas si esta en la pisicion : ")
    print(numeros.index(buscar))
else: 
    print("El numero que buscas no esta en la lista")
