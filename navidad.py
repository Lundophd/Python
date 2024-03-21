#saludos de navidad de una empresa
print ("Buenos dias, por las bisperas de años nuevo te estaremos enviando unos mensajes de navidad")
print ("1) categoria 1 Socios con una antiguedad de 5 años e inversion de 10 millones")
print ("2) categoria 2 Socios con una antiguedad de 5 años he inversion inferior a 10 millones ")
print ("3) categoria 3 Socios con una inversion mayor a 10 millones pero una antiguiedad inferior a 5 años")
print ("4) categoria 4 no tiene inversion (Trabajadores)")
navidad = int(input("indigue en que categoria se encuentra "))
c1 = "¡Feliz Navidad! Gracias por todo lo que hemos compartido este año. ¡Sigamos volando alto! ¡Agradecer a tus clientes nunca está de más!"
c2 = "para comentarle que a su reccepcion le llegara un detalle de parte de la empresa"

if navidad <2:
   print(c1)
   print(c2)
elif navidad <3: 
    print(c1)
elif navidad <4: 
    print(c2)
elif navidad <5:
    print('feliz navidad gracias por trabajr con nostros')
else:
    print("no tienes categoria")
    
