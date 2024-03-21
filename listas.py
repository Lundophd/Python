#listas
lista =["lunes","martes","miercoles","jueves","vienes", 2,True,2.45,[2,3,4,5,6,7]]
lista2=["manzana","mango","babano"]
print(lista[-6])#imprimir la posicion de la lista
print(lista[5])
print(lista[1:4])#imprimr seccion de la lista
print(lista[:4])#imprimir seccion de la lista de la posicion 0
print(lista[3:])#imprime desde la posicion 3 hasta el final
lista.append("sabado")#agragar un elemento a la lista
lista.append("domingo")
lista.extend([4,5,6])#Agregar varios elementos pero se tienen que agregar a una lista
print(lista)
lista3= lista+lista2
print(lista3)
print(34 in lista)
print(lista3.index(5))#Traer la posicion en la que se encuentra en la lista