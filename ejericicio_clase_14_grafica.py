import tkinter as tk

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Resultado: " + str(result))
    except ValueError:
        result_label.config(text="Error: Entrada no válida")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Resultado: " + str(result))
    except ValueError:
        result_label.config(text="Error: Entrada no válida")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Resultado: " + str(result))
    except ValueError:
        result_label.config(text="Error: Entrada no válida")

def divide():
    try:
        result = float(entry1.get()) / float(entry2.get())
        result_label.config(text="Resultado: " + str(result))
    except ValueError:
        result_label.config(text="Error: Entrada no válida")
    except ZeroDivisionError:
        result_label.config(text="Error: No se puede dividir entre cero")

root = tk.Tk()
root.title("Calculadora Simple")

label1 = tk.Label(root, text="Número 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Número 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=2, column=0)
subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=2, column=1)
multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=3, column=0)
divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
