
def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i
        while j > 0 and actual < lista[j-1]:
            lista[j]=lista[j-1]
            j-=1
        lista[j]=actual
    
inei = {
    "Molina": 175237, "Callao": 426649, "Victoria": 174958,
    "Comas": 532403, "Agustino": 194474, "Carabayllo": 305963,
    "Olivos": 377532, "Cieneguilla": 47860, "Lince": 51054,
    "Independencia": 220654, "Jesus Maria": 73439, "Ate": 638345,
    "Camen Legua": 43156, "Mi Peru": 52722, "Ventanilla": 356040,
    "Lima": 276861, "Ancon": 43951, "Barranco": 30698,
    "Bellavista": 78489, "La Perla": 64111, "Brena": 77291,
    "Chaclacayo": 44271, "Chorrillos": 330483, "Lince": 51054
}

poblacion = []
for pueblo in inei.values():
    poblacion.append(pueblo)

insercion(poblacion)

print("Pobracion ordenada:", poblacion[::-1])

print("Poblacion mas alta: ", poblacion[len(poblacion)-1])
print("Poblacion mas baja: ", poblacion[0])

input("press to finished...")