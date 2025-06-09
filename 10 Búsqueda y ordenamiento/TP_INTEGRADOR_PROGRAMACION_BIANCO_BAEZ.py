def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

nombres = ["Santiago","Nicolas","Lucas","Laura","Julieta"]

print ("Lista original:", nombres)
selection_sort(nombres)
print("Lista ordenada", nombres)

nombre_buscado = input("Ingrese el nombre que desea buscar: ")

pos = busqueda_lineal(nombres,nombre_buscado)

if pos != -1:
    print(f"{nombre_buscado} fue encontrado en la posición {pos}.")
else:
    print(f"{nombre_buscado} no se encuentra en la lista.")

