import random as rs
lista = [rs.randint(1, 50) for x in range(20)]
print("VECTOR GENERADO")
print(lista)
print("NUMEROS A BUSCAR EN LA LISTA")
cant_numIngr = 0
while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 1000:
        break
    elif numero in lista:
        posicion = lista.index(numero)
        print(f'El numero {numero} se encuentra en la posicion', posicion)
    else: 
        print("\nNumero buscado no se encuentra")
    cant_numIngr += 1
print("Cantidad de numeros ingresados para consulta es: ", cant_numIngr)