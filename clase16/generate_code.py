#python.exe -m pip install --upgrade pip
#pip install python-barcode
#pip install ipython
#pip install Pillow
#OPCIONAL
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow

import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

user_data = input("Introduce el dato a codificar en el COdigo de Barras --> ")

code = barcode.get('code128', user_data, writer=ImageWriter())

filename = code.save(f"./images/{user_data}")

display(Image(filename=filename))
