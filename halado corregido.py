#precio de un helado
print("Hola bienvenido a laheladeria virtual ")
print("1) Valor del helado sin nada adicional 1500 ")
print("2) El adicional de oreo cuesta 1000. ")
print("3) El adicional de chispas de chocolatye cuesta 1100 ")
print("4) El adicional de chocolate cuesta 1200 ")
print("5) El adicional de salsa cuesta 500   ")
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