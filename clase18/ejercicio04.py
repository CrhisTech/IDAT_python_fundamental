'''
Desarrollar un programa para gestionar un listado telefonico con los nombres y los telefonos de los clientes de una empresa. El programa debe incorporar las siguientes funciones: crear el fichero con el listado si no existe, consultar el telefono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de texto como listado.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.



'''
#paso1 crear el listado
lista_datos = [
        {
            "nombre": "Juan", "telefono": '3128239'},
        {
            "nombre": "Ana", "telefono": '3908179'},
        {
            "nombre": "Rodrigo", "telefono": '3607223'},
        {
            "nombre": "Luz", "telefono": '3218234'},
        {
            "nombre": "Pedro", "telefono": '3408235'}
]

#paso2 crear la funcion CrearFichero
def CrearFichero():#crear el archivo como ultimo paso luego de hacer los cambios
    fichero = open('./listado.txt','w')
    for  dic in lista_datos:
        fichero.write(f'{dic["nombre"]}, {dic["telefono"]}\n')
    fichero.close()
#paso3 consultar el telefono de un cliente
#si el cliente se encuentra 
def ConsultarNumero():
    consulta = input("Ingrese el numero a consultar: ")
    encontrado = False
    for dic in lista_datos:
        if str(dic["telefono"]) == consulta:
            print(f'Nombre del cliente: {dic["nombre"]}\nTelefono: {consulta}')
            encontrado = True
            break
    if not encontrado:
        while True:
            registrar = input("El numero en consulta no se encuentra, desea registrarlo? si/no -> (s/n): ")
            if registrar.lower() == 's':
                RegistrarNumero()
                break
            else:
                break

#paso4 añadir en los datos de un nuevo cliente
def RegistrarNumero():
    nombre = input("Ingrese el nombre del cliente: ").capitalize()
    numero = input("Ingrese el numero del cliente: ")
    lista_datos.append({"nombre": nombre, "telefono": numero})
    print("Registro exitoso.")

#paso5 eliminar el teléfono de un cliente
def EliminarNumero():
    telefono = input("Ingrese el numero que desea eliminar: ")
    encontrado = False
    for dic in lista_datos:
        if dic["telefono"] == telefono:
            lista_datos.remove(dic)
            encontrado = True
            break
    if not encontrado:
        print("El numero que desea eliminar no se encuentra en lista.")

def main():
    print("Bienvenido!")
    print("Que operacion deseas realizar:")
    while True:
        inicio = input("\nConsultar numero -> a\nRegistrar Numero -> b\nEliminar Numero -> c\nsalir ->d\nIngresa una letra correspondiente: ")
        try:
            if inicio.lower() == 'a':
                ConsultarNumero()
            elif inicio.lower() == 'b':
                RegistrarNumero()
            elif inicio.lower() == 'c':
                EliminarNumero()
            elif inicio.lower() == 'd':
                CrearFichero()
                break
        except ValueError:
            print("Ingrese una opcion valida.")
main()