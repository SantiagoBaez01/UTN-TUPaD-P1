'''
Práctico 11: Aplicación de la Recursividad
Funciones recursivas para diferentes problemas matemáticos y de texto.
'''

def factorial(n):
    """Calcula el factorial de n (n>=0)."""
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci_recursivo(pos):
    """Devuelve el valor de la serie de Fibonacci en la posición pos (pos>=0)."""
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)


def potencia(base, exp):
    """Calcula base**exp (exp>=0) de forma recursiva."""
    if exp < 0:
        raise ValueError("El exponente debe ser no negativo.")
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)


def decimal_a_binario(n):
    """Convierte un entero decimal positivo a binario como cadena."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    resto = n % 2
    return decimal_a_binario(n // 2) + str(resto)


def es_palindromo(palabra):
    """Devuelve True si palabra es palíndromo, sin usar slicing ni reversed."""
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def suma_digitos(n):
    """Suma los dígitos de n (n>=0) sin convertir a string."""
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)


def contar_bloques(n):
    """Devuelve la suma de bloques para construir una pirámide de base n."""
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)


def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece digito en numero (ambos >=0)."""
    if numero == 0:
        return 1 if digito == 0 else 0
    cuenta = 1 if numero % 10 == digito else 0
    if numero < 10:
        return cuenta
    return cuenta + contar_digito(numero // 10, digito)


if __name__ == "__main__":
    # Ejercicio 1: factorial de 1 a n
    n = int(input("Ingresa un número para calcular factoriales hasta n: "))
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

    # Ejercicio 2: Fibonacci hasta posición p
    p = int(input("Ingresa la posición hasta donde mostrar Fibonacci: "))
    print("Serie Fibonacci:")
    for i in range(p + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")

    # Ejercicio 3: potencia
    b = int(input("Ingresa la base: "))
    e = int(input("Ingresa el exponente: "))
    print(f"{b}^{e} = {potencia(b, e)}")

    # Ejercicio 4: decimal a binario
    d = int(input("Ingresa un número decimal para convertir a binario: "))
    print(f"Representación binaria de {d}: {decimal_a_binario(d)}")

    # Ejercicio 5: palíndromo
    palabra = input("Ingresa una palabra para verificar palíndromo: ").strip().lower()
    print(f"¿'{palabra}' es palíndromo? {es_palindromo(palabra)}")

    # Ejercicio 6: suma de dígitos
    num = int(input("Ingresa un número para sumar sus dígitos: "))
    print(f"Suma de dígitos de {num}: {suma_digitos(num)}")

    # Ejercicio 7: contar bloques
    base = int(input("Ingresa la cantidad de bloques en la base de la pirámide: "))
    print(f"Total de bloques necesarios: {contar_bloques(base)}")

    # Ejercicio 8: contar digito
    numero = int(input("Ingresa un número para contar dígitos: "))
    dig = int(input("Ingresa el dígito a contar: "))
    print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces en {numero}.")
