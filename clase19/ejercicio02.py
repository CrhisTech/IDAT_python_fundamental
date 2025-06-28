def evaluarDigito(clave):
    retorno = False
    for x in clave:
        if x.isdigit():
            retorno = True
            break
    return retorno

def evaluarMayuscula(clave):
    contador = 0
    for x in clave:
        if x.isupper():
            contador += 1
    if contador >= 3:
        return True
    else:
        return False
    
clave = input("Ingrese clave: ")

digito = evaluarDigito(clave)
mayuscula = evaluarMayuscula(clave)

if len(clave) >= 5 and digito == True and mayuscula == True:
    print("OK")
else:
    print("ERROR")