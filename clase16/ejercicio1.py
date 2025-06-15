from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def mostrarDatos():
    messagebox.showinfo("Datos Ingresados", "Usuario: " + usuario.get()
                        + "\nClave: " + clave.get() + "\nTipo de Usuario: " + varCombo.get()
                        + "\nRecordar Credenciales: "+ str(myVarCheck.get()))

ventana = Tk()
# otro = Tk()
ventana.geometry("512x512")
ventana.title("Login")
# fondo_imagen = PhotoImagen(file="mi_imagen.png")
varCombo = StringVar()
#fondo = Label(ventana, image=fondo_imagen).place(x=0,y=0)
combo = ttk.Combobox(ventana, values=[
    "Usuario", "Administrador"], state="readonly", textvariable=varCombo)
combo.place(x=210, y=30)
combo.current(0)
usuario = StringVar()
clave = StringVar()
myVarCheck = BooleanVar()
Label(ventana, text='Usuario: ').place(x=100, y=100)
Label(ventana, text="Clave: ").place(x=100, y=130)
cajaUsuario = Entry(ventana, textvariable=usuario).place(x=210, y=100, width=150)
cajaClave = Entry(ventana, textvariable=clave, show='*').place(x=210, y=130, width=150)
miCheck = Checkbutton(ventana, text="Recordar Credenciales", variable=myVarCheck).place(x=210,y=180)

boton = Button(ventana, text="Ingresar", bg="#007BFF", command=mostrarDatos).place(x=150, y=260, width=200, height=40)
ventana.mainloop()