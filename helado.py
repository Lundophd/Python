#Este Programa te dice los precios y complementos de un heladp
valor_del_Helado=1500
el_adicional_de_oreo=1000
el_adicional_de_chispas_de_chocolate=1100
el_adicional_de_chocolate=1200
el_adicional_de_salsa=500

C_Helado = int(input("ingrese la cantidad de helado: "))
C_adicional_de_oreo= int(input("ingrese la cantida de oreos que desea tener "))
C_adicional_de_chipas_de_chocolate=int(input("ingrese la cantidad de chispas de chocolate que desea tener "))
C_adicional_de_chocolate=int(input("ingrese la cantidad de chocolate que desea tener "))
C_adicional_de_salsa=int(input("ingrese la cantidad de salsa que desea tener "))

total= (C_Helado*valor_del_Helado)  + (C_adicional_de_oreo*el_adicional_de_oreo) + (C_adicional_de_chipas_de_chocolate*el_adicional_de_chispas_de_chocolate) + (C_adicional_de_chocolate*el_adicional_de_chocolate) + (C_adicional_de_salsa*el_adicional_de_salsa)

print ('el valor a pagar es:', total)

