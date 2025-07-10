def sumaProducto(p, inicio, fin):
    if inicio == fin:
        return inicio*p
    return (inicio*p)+sumaProducto(p, inicio+1, fin)

n = float(input("Input n: "))
p = float(input("Input p: "))

print("Output:", sumaProducto(p, 1, n))
