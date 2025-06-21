'''
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un numero de kilos y muestre por pantalla el precio de ese numero de kilos de fruta. si la fruta no esta en el diccionario debe mostrar un mensaje informando de ello
'''
#crear diccionario
lista_frutas = [
    {'nombre': 'platano', 'precio': 1.35},
    {'nombre': 'manzana', 'precio': 0.80},
    {'nombre': 'pera', 'precio': 0.85},
    {'nombre': 'naranja', 'precio': 0.70}
]

# consultar precio

def calcularPrecio(fruta, cantidad):
    for dic in lista_frutas:
        if dic['nombre'] == fruta:
            precio_total = cantidad * dic['precio']
            return precio_total
        
print("Bienvenido!")
for dic in lista_frutas:
    print(dic['nombre'])

nombre = input("Ingrese la fruta que desea comprar: ")
cantidad = input("Ingrese la cantidad x KG que desea comprar: ")
cantidad = float(cantidad)
encontrado = False
for dic in lista_frutas:
    if dic['nombre'] == nombre:
        print(f'El precio total es: S/', calcularPrecio(nombre, cantidad))
        encontrado = True
        break
if not encontrado:
    print("La fruta no se encuentra en lista.")