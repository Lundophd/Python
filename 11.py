#precio de un helado
print("El helado corresponde al numero 1\nEl helado mas una oreo es 2\nEl helado mas chispas de chocolate es 3\nEl helado mas chocolate es 4\nEl helado mas salsa es 5\nEl helado mas una oreo y chispas de chocolate es 6\nEl helado mas una oreo y chocolate es 7\nEl helado mas una oreo y salsa es 8\nEl helado mas chispas de chocolate y chocolate es 9\nEl helado mas chispas de chocolate y salsa es 10\nEl helado mas chocolate y salsa es 11\nEl helado mas una oreo, chispas de chocolate y chocolate es 12\nEl helado mas una oreo,chispas de chocolate y salsa es 13\nEl helado mas chispas de chocolate,chocolate y salsa es 14\nEl helado mas chocolate,salsa y oreo es 15\nEl helado con todo es 16")
thelado=int(input("Dime que tipo de helado quieres: "))
helado=1500
if thelado==1:
  helados=(helado)
if thelado==2:
  helados=(helado)+1000
if thelado==3:
  helados=(helado)+1100
if thelado==4:
  helados=(helado)+1200
if thelado==5:
  helados=(helado)+500
if thelado==6:
  helados=(helado)+2100
if thelado==7:
  helados=(helado)+2200
if thelado==8:
  helados=(helado)+1500
if thelado==9:
  helados=(helado)+2300
if thelado==10:
  helados=(helado)+1600
if thelado==11:
  helados=(helado)+1700
if thelado==12:
  helados=(helado)+3400
if thelado==13:
  helados=(helado)+2600
if thelado==14:
  helados=(helado)+2800
if thelado==15:
  helados=(helado)+2700
if thelado==16:
  helados=(helado)+3800
else:
  print("No hay mas opciones disponibles")

print("El precio del helado que escogiste es: ",helados)