# Archivo: BAEZ_SANTIAGO_TP-04.py

# 1) Imprimir del 0 al 100
print("Ejercicio 1:")
for i in range(0, 101):
    print(i)

# 2) Contar dígitos de un número
print("\nEjercicio 2:")
num = int(input("Ingresa un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

# 3) Suma entre dos valores, excluyéndolos
print("\nEjercicio 3:")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
menor = min(a, b)
mayor = max(a, b)
suma = sum(range(menor + 1, mayor))
print("Suma de los números entre", menor, "y", mayor, "es:", suma)

# 4) Sumar números hasta que se ingrese 0
print("\nEjercicio 4:")
total = 0
while True:
    n = int(input("Ingresa un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# 5) Juego de adivinar un número
print("\nEjercicio 5:")
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    guess = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if guess == secreto:
        print("¡Correcto! Lo adivinaste en", intentos, "intentos.")
        break

# 6) Números pares del 100 al 0 en orden decreciente
print("\nEjercicio 6:")
for i in range(100, -1, -2):
    print(i)

# 7) Sumar todos los números desde 0 hasta uno dado
print("\nEjercicio 7:")
limite = int(input("Ingresa un número entero positivo: "))
suma = sum(range(0, limite + 1))
print("Suma total:", suma)

# 8) Contar pares, impares, positivos y negativos
print("\nEjercicio 8:")
cantidad = 100  # Cambiar aquí si se desea probar con menos
pares = impares = positivos = negativos = 0
for _ in range(cantidad):
    n = int(input("Ingresa un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9) Calcular la media de 100 números
print("\nEjercicio 9:")
cantidad = 100  # Cambiar aquí si se desea probar con menos
total = 0
for _ in range(cantidad):
    n = int(input("Ingresa un número: "))
    total += n
media = total / cantidad
print("Media:", media)

# 10) Invertir los dígitos de un número
print("\nEjercicio 10:")
n = input("Ingresa un número: ")
invertido = n[::-1]
print("Número invertido:", invertido)
