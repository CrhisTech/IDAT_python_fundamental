def mostrarLista():
    lista = []
    listaCuadrados = []
    for i in range(1, 11):
        lista.append(i)
    for i in range(len(lista)+1):
        cuadrados = pow(i, 2)
        listaCuadrados.append(cuadrados)
    return print(listaCuadrados)

mostrarLista()