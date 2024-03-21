#saludos de navidad de una empresa
def categoria1():
    print("feliz navidad gracias por estar con nostros todos estos años que sean muchos mas")
    print("y aca tu regalo")
    
def categoria2():
    print("feliz navidad gracias por estar con nostros todos estos años que sean muchos mas")

def categoria3():
    print("y aca tu regalo")
    
def categoria4():
    print('feliz navidad gracias por trabajr con nostros')
    
print ("Buenos dias, por las bisperas de años nuevo te estaremos enviando unos mensajes de navidad")
print ("1) categoria 1 Socios con una antiguedad de 5 años e inversion de 10 millones")
print ("2) categoria 2 Socios con una antiguedad de 5 años he inversion inferior a 10 millones ")
print ("3) categoria 3 Socios con una inversion mayor a 10 millones pero una antiguiedad inferior a 5 años")
print ("4) categoria 4 no tiene inversion (Trabajadores)")
navidad = int(input("indigue en que categoria se encuentra "))
   
if navidad <2:
    categoria1()
elif navidad <3: 
    categoria2()
elif navidad <4: 
    categoria3()
elif navidad <5:
    categoria4()
else:
    print("no tienes categoria")