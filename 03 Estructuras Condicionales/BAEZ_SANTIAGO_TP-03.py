import random
from statistics import mode, median, mean

# 1) Mayor de edad
def mayor_de_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Es mayor de edad")

# 2) Aprobado o desaprobado
def aprobado_desaprobado():
    nota = float(input("Ingrese su nota: "))
    print("Aprobado" if nota >= 6 else "Desaprobado")

# 3) Número par
def numero_par():
    num = int(input("Ingrese un número: "))
    print("Ha ingresado un número par" if num % 2 == 0 else "Por favor, ingrese un número par")

# 4) Categoría según la edad
def categoria_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# 5) Longitud de la contraseña
def validar_contraseña():
    contraseña = input("Ingrese una contraseña: ")
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Sesgo de la distribución
def sesgo_distribucion():
    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    if media > mediana > moda:
        print("Sesgo positivo")
    elif media < mediana < moda:
        print("Sesgo negativo")
    else:
        print("Sin sesgo")

# 7) Modificación de una frase
def modificar_frase():
    frase = input("Ingrese una frase: ")
    if frase[-1].lower() in "aeiou":
        frase += "!"
    print(frase)

# 8) Formato del nombre
def formato_nombre():
    nombre = input("Ingrese su nombre: ")
    opcion = int(input("Ingrese 1 (MAYUS), 2 (minus), 3 (Capitalizar): "))
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())

# 9) Clasificación de terremotos
def clasificar_terremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif magnitud < 4:
        print("Leve")
    elif magnitud < 5:
        print("Moderado")
    elif magnitud < 6:
        print("Fuerte")
    elif magnitud < 7:
        print("Muy fuerte")
    else:
        print("Extremo")

# 10) Estación del año
def estacion_del_anio():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día: "))
    
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes < 3 or dia <= 20)):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes < 6 or dia <= 20)):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes < 9 or dia <= 20)):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    else:
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    
    print("La estación actual es:", estacion)
