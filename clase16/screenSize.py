import tkinter as tk

def crear_ventana():
  ventana = tk.Tk()
  ventana.title("Posicionamiento de Ventana")

  # Define el ancho, alto y posición (x, y) de la ventana
  ancho = 400
  alto = 300
  x_pos = 100
  y_pos = 50

  # Aplica la geometría a la ventana
  ventana.geometry(f"{ancho}x{alto}+{x_pos}+{y_pos}")

  ventana.mainloop()

if __name__ == "__main__":
  crear_ventana()