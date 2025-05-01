# Práctico 5: Listas

# 1) Lista con múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4:", multiplos_de_4)

# 2) Lista con 5 elementos y mostrar el penúltimo
gustos = ["pizza", "música", "gatos", "viajes", "tecnología"]
print("2) Penúltimo elemento:", gustos[-2])

# 3) Lista vacía, agregar tres palabras con append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3) Lista con palabras agregadas:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"         # segundo valor (índice 1)
animales[-1] = "oso"         # último valor (índice -1)
print("4) Lista animales modificada:", animales)

# 5) Análisis del código
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina el número mayor, que es 22
print("5) Lista después de eliminar el máximo:", numeros)
# Explicación: El programa encuentra el valor máximo de la lista y lo elimina.

# 6) Números del 10 al 30 saltando de 5 en 5, mostrar los dos primeros
saltos = list(range(10, 31, 5))
print("6) Dos primeros valores:", saltos[:2])

# 7) Reemplazar valores centrales de la lista “autos”
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]  # reemplaza índice 1 y 2
print("7) Lista autos modificada:", autos)

# 8) Crear lista "dobles" con el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista dobles:", dobles)

# 9) Manipular lista anidada de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")                     # a)
compras[1][1] = "tallarines"                 # b)
compras[0].remove("pan")                     # c)
print("9) Lista de compras modificada:", compras)  # d)

# 10) Crear lista anidada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10) Lista anidada:", lista_anidada)
