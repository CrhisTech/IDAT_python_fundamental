# Hacer un programa que permita el registro de una agenta telefonico
# considerando los apellidos nombres y celulares
# de las personas. Debe permitir la busqueda por el apellido o celular
nombre = []
apellido = []
celular = []
while True:
    print("1) Registrar personas")
    print("2) Buscar personas Registradas")
    print("3) Salir")
    opcion = input("Seleccione: ").strip()
    if opcion == "1":
        name = input("Ingresar nombre: ").strip()
        lastName = input("Ingresar apellido: ").strip()
        celphone = input("Ingresar celular: ").strip()
        nombre.append(name)
        apellido.append(lastName)
        celular.append(celphone)
    elif opcion == "2":
        if len(celular) == 0:
            print('\nNo hay ningun registro realizado')
        else:
            print("1) Buscar por apellido")
            print("2) Buscar por celular")
            buscar = input("Seleccione: ").strip()
            if buscar == "1":
                ape = input("Ingrese un apellido a buscar: ").strip()
                if ape in apellido:
                    print("\nNombre:", nombre[apellido.index(ape)])
                    print("Apellido:", apellido[apellido.index(ape)])
                    print("celular:", celular[apellido.index(ape)])
                else:
                    print("No se ha encontrado\n")
            elif buscar == "2":
                cel = input("Ingrese un numero de celular a buscar: ").strip()
                if cel in celular:
                    print("\nNombre:", nombre[celular.index(cel)])
                    print("Apellido:", apellido[celular.index(cel)])
                    print("Celular:", celular[celular.index(cel)])
                else:
                    print("No se ha encontrado\n")
            else:
                print("Opcion incorrecta\n")
    elif opcion == "3":
        fichero = open("agendaTelefonica.txt", "w")
        for i in range(len(nombre)):
            fichero.write(f"{nombre[i]},{apellido[i]},{celular[i]}\n")

            
        break #sirve para salir del while
    else:
        print("Opcion incorrecta")