#saludos de navidad de una empresa
print ("Buenos dias, por las bisperas de años nuevo te estaremos enviando unos mensajes de navidad")
print ("1) categoria 1 Socios con una antiguedad de 5 años e inversion de 10 millones")
print ("2) categoria 2 Socios con una antiguedad de 5 años he inversion inferior a 10 millones ")
print ("3) categoria 3 Socios con una inversion mayor a 10 millones pero una antiguiedad inferior a 5 años")
print ("4) categoria 4 no tiene inversion (Trabajadores)")
Tipoe = int(input("su categoria es  "))
def saludon1 ():
    if Tipoe ==1:
        print ("¡Feliz Navidad! Gracias por todo lo que hemos compartido este año. ¡Sigamos volando alto! ¡Agradecer a tus clientes nunca está de más!")
        print (" tu reagalo sera una ancheta navideña llegara a tu casa en estos dias")
    elif Tipoe ==2:
        print ("¡Feliz Navidad! Gracias por todo lo que hemos compartido este año. ¡Sigamos volando alto! ¡Agradecer a tus clientes nunca está de más!")
    return saludon1
print (saludon1)
def saludn2 ():
    if Tipoe ==3:     
        print("tu reagalo sera una ancheta navideña llegara a tu casa en estos dias")
    elif Tipoe ==4: 
        print("A tu correo llego un email, deseandote feliz navidad, por politicas de la empresa el 1 de enero trabajara con horario normal")
    else: 
        print("Usted no tiene categoria")
    return saludn2