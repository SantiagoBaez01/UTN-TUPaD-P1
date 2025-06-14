
"""Práctico 7: Estructuras de datos complejas
Este script contiene las soluciones a las 10 actividades propuestas.
"""

def actividad_1():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    # Agregar nuevas frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera']    = 2300
    print('Actividad 1:', precios_frutas)

def actividad_2(precios_frutas):
    # Actualizar precios existentes
    to_update = {'Banana': 1330, 'Manzana': 1700, 'Melón': 2800}
    for fruta, nuevo_precio in to_update.items():
        precios_frutas[fruta] = nuevo_precio
    print('Actividad 2:', precios_frutas)
    return precios_frutas

def actividad_3(precios_frutas):
    lista_frutas = list(precios_frutas.keys())
    print('Actividad 3:', lista_frutas)

def actividad_4():
    contactos = {}
    for i in range(5):
        nombre = input(f"Nombre del contacto {i+1}: ")
        numero = input(f"Número de {nombre}: ")
        contactos[nombre] = numero
    dbusqueda = input("Ingresá el nombre a buscar: ")
    if dbusqueda in contactos:
        print(f"Teléfono de {dbusqueda}: {contactos[dbusqueda]}")
    else:
        print(f"{dbusqueda} no está en la agenda.")

def actividad_5():
    frase = input("Ingresá una frase: ")
    palabras = frase.split()
    punicas = set(palabras)
    dic_recuento = {palabra: palabras.count(palabra) for palabra in punicas}
    print("Palabras únicas:", punicas)
    print("Recuento:", dic_recuento)

def actividad_6():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Nombre del alumno {i+1}: ")
        notas = []
        for j in range(3):
            nota = float(input(f"  Nota {j+1} de {nombre}: "))
            notas.append(nota)
        alumnos[nombre] = tuple(notas)
    def promedio(tupla_notas):
        return sum(tupla_notas) / len(tupla_notas)
    for nombre, notas in alumnos.items():
        print(f"{nombre}: promedio = {promedio(notas):.2f}")

def actividad_7():
    parcial1 = {'Ana', 'Luis', 'Sofia', 'Juan'}
    parcial2 = {'Luis', 'María', 'Sofia', 'Pedro'}
    ambos = parcial1 & parcial2
    solo_uno = parcial1 ^ parcial2
    al_menos_uno = parcial1 | parcial2
    print("Actividad 7:")
    print("  Ambos parciales:", ambos)
    print("  Solo uno:", solo_uno)
    print("  Al menos uno:", al_menos_uno)

def actividad_8():
    stock = {}
    while True:
        prod = input("Producto (ENTER para salir): ")
        if not prod:
            break
        if prod in stock:
            print(f"Stock actual de {prod}: {stock[prod]}")
            cant = int(input("Cantidad a agregar: "))
            stock[prod] += cant
        else:
            cant = int(input("Producto nuevo. Ingresá cantidad inicial: "))
            stock[prod] = cant
        print("Stock actualizado:", stock)

def actividad_9():
    agenda = {('lunes', '10:00'): 'Reunión',
              ('martes', '15:00'): 'Clase de inglés'}
    dia = input("Día: ").lower()
    hora = input("Hora: ")
    clave = (dia, hora)
    if clave in agenda:
        print("Evento:", agenda[clave])
    else:
        print("No hay actividad en ese horario.")

def actividad_10():
    original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
    invertido = {capital: pais for pais, capital in original.items()}
    print('Actividad 10:', invertido)

if __name__ == "__main__":
    actividad_1()
    frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
    frutas = actividad_2(frutas)
    actividad_3(frutas)
    # actividad_4()
    # actividad_5()
    # actividad_6()
    actividad_7()
    # actividad_8()
    # actividad_9()
    actividad_10()
