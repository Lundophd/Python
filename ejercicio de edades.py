print("buenos dias este es un progrma para calcular la edad actual del usuario en meses dias y años  ")
numero=input("porfavor ingrese su  año de nacimiento ")
numero=(int(numero))
numero2=input("por favor ingrese su mes de nacimiento, en numeros donde enero es 1, febrero  2, marzo 3, abril 4, mayo 5, juniio 6, juulio 7, agosto 8,septiembre 9, octubre 10, noviembre 11 y diciembre es 12  ")
numero2=(int(numero2))
numero3=input("porfavor ingrese el dia de su nacmiento")
numero3=(int(numero3))
numero4=input("porfavor ingrese el numero del dia  actual")
numero4=(int(numero4))  
numero5=input("porfavor ingrese  el numero del  mes actual")
numero5=(int(numero5))    
año=(int(2023))   
resta=año-numero
mes=(int(12))
mes2=(int(2))
resta2=mes-numero2
suma2=(resta2+numero5)
dia=(int(30))
resta3=dia-numero3
suma=resta3+numero4
print("tu edad actual es",resta)
print("años, con ",suma2)
print("meses y ",suma)
print("dias")

