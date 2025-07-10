from ast import Tuple
from math import exp
import random as rd # importando el modulo aleatorio

def validaEntero():
    while True:
        numero = input("Ingrese un numero entero positivo: ")
        if numero.strip().isdigit():
            numero = int(numero)
            if numero > 0:
                return numero
            elif numero == 0:
                print("No ha introducido un numero entero positivo. Por favor, vuelva a intentarlo\n")
        else:
            try:
                if type(int(numero)) is int:
                    if int(numero)< 0:
                        print("No ha introducido un numero entero positivi. Por favor, vuelva a intentarlo\n")
            except:
                try:
                    if type(float(numero)) is float:
                        print("No ha introducido un numero entero. Por favor, vuelva a intentarlo\n")
                except:
                    print("El dato introducido no es numero. Por favor, vuelva a intentarlo\n")

while True:
    print("Sorteo de loteria")

    tupla = tuple([rd.randint(1, 100) for x in range(15)])
    numero = validaEntero()
    print("\nLista de numeros ganadores del sorteo")
    print(tupla)
    print("Numero de ganador más pequeño es:", min(tupla))
    print("Número de ganador más grande es:", max(tupla))
    if numero in tupla:
        if tupla.count(numero) == 1:
            # con f-format podemos usar variables y operaciones dentro de un string con llaves{}
            print(f"Felicitaciones! Su número: {numero} se encuentra dentro de la \n lista de ganadores.\nHa ganado un total de 15€")
        elif tupla.count(numero) > 1:
            print(f"Felicitaciones! Su número: {numero} se encuentra dentro \n de la lista de ganadores y además se ha repetido {tupla.count(numero)} veces. \n Ha ganado un total de {15+(5*(tupla.count(numero)-1))}€")
            break
    else:
        while True:
            opcion = input("Lo sentimos. Su numero no ha resultado premiado\n.\
                Desea volver a intentarlo? si o no: ").strip().lower()
            if opcion == "no" or opcion == "si":
                break
            else:
                print("\nNo hemos logrado entender su respuesta. Repítala,\
                    por favor\n Indique la respuesta con si o no")
        if opcion == "no":
                break