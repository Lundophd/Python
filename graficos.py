import tkinter

ventana = tkinter.Tk() #Contenedor grafico
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text="hola mundo", bg="green")
etiqueta.pack(fill = tkinter.X)#colocar el label en 
def saludo(num1,num2):
    print("hola programadores")
    print(num1*num2)

cajanumero1 = tkinter.Entry(ventana, font="Helvetica 20")
cajanumero1.pack()
cajanumero2 = tkinter.Entry(ventana, font="Helvetica 20")
cajanumero2.pack()

def numerocajas():
    numero1 = int(cajanumero1.get())
    numero2 = int(cajanumero2.get())
    resultmult = numero1 * numero2
    etiquetaresult ["text"] = resultmult
    #print("El resultado es: " , resultmult)
    

boton = tkinter.Button(ventana, text="presionar", bg="white", command=lambda: saludo(3,2))
boton.pack()
etiquetaresult= tkinter.Label(ventana, bg="blue")
etiquetaresult.pack(fill = tkinter.X)#colocar el label en 

ventana.mainloop()

