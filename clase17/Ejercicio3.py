# monto *(1 + 0.18)
'''
Escribir una funcion que calcule el total de una factura tras aplicarle el IGV
. La funcion debe recibir la cantidad sin IGV y el porcentaje de IGV a aplicar, y devolver el total de la 
factura. Si se invoca la funcion sin pasarle el porcentaje de IGV, debera aplicar un 18%
'''

def montoIGV(monto, porcentaje=18):
    total_pagar = monto * (1+porcentaje/100)
    return total_pagar
    
monto = float(input('Ingrese el monto a pagar: '))
porcentajeIGV = float(input('Ingrese el porcentaje de IGV: '))

print(montoIGV(monto, porcentajeIGV))
print(montoIGV(monto))