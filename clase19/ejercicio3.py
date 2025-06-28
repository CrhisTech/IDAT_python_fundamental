misProductos = {}
suma = 0.0
while True:
    introArti = input("Introduce un articulo: ")
    precio = float(input(f'Introduce el precio de {introArti}: '))
    misProductos[introArti] = precio
    
    yesNo = input("Quieres añadir articulos a la lista(y/n)? ")
    if yesNo == 'n':
        break

print("Lista de la compra")
for mi_dict in misProductos.items():
    #recuperamos los datos
    filtro = list(mi_dict)
    suma = suma + filtro[1]
    print(filtro[0], "\t", filtro[1])
print("Costo total: ", suma)
input("Press enter to exit")