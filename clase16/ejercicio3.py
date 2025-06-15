'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
automatica el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene
4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
import winsound
from tkinter import *
from tkinter import messagebox

# Desactiva el pitido del sistema
winsound.PlaySound("*", winsound.SND_ALIAS)

def showData():
    try:
        age_value = int(age.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una edad válida.")
    if age_value < 4:
        messagebox.showinfo(
            "Bienvenido " + name.get() + "!",
            "Menores de 4 entran gratis, ¡que te diviertas!"
        )
    elif 4 <= age_value <= 18:
        messagebox.showinfo(
            "Bienvenido " + name.get() + "!",
            f"Tienes {age_value} años. El precio de la entrada es 5€."
        )
    else:
        messagebox.showinfo(
            "Bienvenido " + name.get() + "!",
            f"Tienes {age_value} años. El precio de la entrada es 10€."
        )

window = Tk()
# Screen size
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'400x250+800+440')
window.title("Bienvenido!")
window.resizable(width=False, height=False)
name = StringVar()
age = StringVar()
myVarCheck = BooleanVar()
Label(window, text='Nombre: ').place(x=80, y=80)
Label(window, text='Edad: ').place(x=80, y=110)
caseName = Entry(window, textvariable=name).place(x=190, y=80, width=130)
caseAge = Entry(window, textvariable=age).place(x=190, y=110, width=130)
button = Button(window, text="Pagar",bg="#007Bff", command=showData).place(x=110, y=180, width=180, height=30)







window.mainloop()