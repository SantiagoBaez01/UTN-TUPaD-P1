import random

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

def juego_adivinanza():
    print("Bienvenido al Juego de Adivinanza en Binario")
    print("Elige el tipo de desafío:")
    print("1. De Binario a Decimal")
    print("2. De Decimal a Binario")

    opcion = input("Ingresa 1 o 2: ")

    numero = random.randint(0, 31)  # Número aleatorio entre 0 y 31

    if opcion == "1":
        binario = decimal_a_binario(numero)
        print(f"\n¿Qué número decimal representa este binario?: {binario}")
        respuesta = input("Tu respuesta: ")
        if respuesta.isdigit() and int(respuesta) == numero:
            print("¡Correcto! 🎉")
        else:
            print(f"Incorrecto. La respuesta correcta era: {numero}")

    elif opcion == "2":
        print(f"\n¿Qué número binario representa este decimal?: {numero}")
        respuesta = input("Tu respuesta (sin 0b): ")
        if respuesta == decimal_a_binario(numero):
            print("¡Correcto! 🎉")
        else:
            print(f"Incorrecto. La respuesta correcta era: {decimal_a_binario(numero)}")

    else:
        print("Opción no válida.")

juego_adivinanza()