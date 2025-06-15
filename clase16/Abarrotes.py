import json
lista_productos =[
  {
    "id": 1,
    "nombre": "Arroz",
    "categoria": "Granos",
    "marca": "La Campiña",
    "precio": 2.50,
    "unidad_medida": "kg",
    "stock": 100
  },
  
  {
    "id": 2,
    "nombre": "Leche Entera",
    "categoria": "Lácteos",
    "marca": "Gloria",
    "precio": 1.20,
    "unidad_medida": "litro",
    "stock": 50
  },
  {
    "id": 3,
    "nombre": "Aceite Vegetal",
    "categoria": "Aceites",
    "marca": "Primor",
    "precio": 4.00,
    "unidad_medida": "litro",
    "stock": 30
  },
  {
    "id": 4,
    "nombre": "Azúcar",
    "categoria": "Endulzantes",
    "marca": "Rubia",
    "precio": 2.00,
    "unidad_medida": "kg",
    "stock": 80
  }
]

# guardar en un archivo JSON:
with open('./products.json', 'w') as outfile:
  #convertir a JSON:
  #json.dump(diccionario que deseas guardar, ruta del archivo donde se va guardar)
  json.dump(lista_productos, outfile)