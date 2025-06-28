import random

dado1 = 0
dado2 = 0
dado3 = 0
contador = 0
print("Lanzando dados")
while True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    print("-"*10)
    print("dado1", dado1)
    print("dado2", dado2)
    print("dado3", dado3)
    print("-"*10)
    contador += 1
    if dado1 == 6 and dado2 == 6 and dado3 == 6:
        break
print("fueron necesarios ", contador, " lanzamientos")

#----------pruebas de codigo
msg = b'hola mundo\n'
print(msg[0:len(msg)-1])
print("mensaje")