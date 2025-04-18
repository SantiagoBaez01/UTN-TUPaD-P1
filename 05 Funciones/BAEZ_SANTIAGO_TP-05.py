import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que saluda al usuario por su nombre
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Funciones para calcular área y perímetro del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar del número dado
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que realiza operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero"
    return (suma, resta, multiplicacion, division)

# 8. Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 10. Función para calcular el promedio de 3 números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# === PROGRAMA PRINCIPAL ===
# 1
imprimir_hola_mundo()

# 2
nombre = input("\nIngresá tu nombre: ")
print(saludar_usuario(nombre))

# 3
nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4
radio = float(input("\nIngresá el radio de un círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5
segundos = int(input("\nIngresá cantidad de segundos: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")

# 6
numero = int(input("\nIngresá un número para su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7
a = float(input("\nIngresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# 8
peso = float(input("\nIngresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

# 9
celsius = float(input("\nTemperatura en Celsius: "))
print(f"Equivale a {celsius_a_fahrenheit(celsius):.2f}°F")

# 10
a = float(input("\nPrimer nota: "))
b = float(input("Segunda nota: "))
c = float(input("Tercera nota: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
