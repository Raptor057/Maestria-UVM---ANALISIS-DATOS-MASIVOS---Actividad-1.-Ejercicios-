import math

# a) Declara una función add_two_numbers
def add_two_numbers(a, b):
    return a + b

# b) Escribe una función que calcule el área del círculo
def area_del_circulo(radio):
    return math.pi * radio * radio

# c) Escribe una función que tome un número arbitrario de argumentos y los sume todos
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números."

# d) Convierte de °C a °F
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# e) Calcula las soluciones de una ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No tiene soluciones reales."
    elif discriminant == 0:
        x = -b / (2 * a)
        return f"Tiene una solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Tiene dos soluciones: x1 = {x1}, x2 = {x2}"

# f) Imprime cada elemento de una lista
def print_list(lista):
    for elemento in lista:
        print(elemento)

# g) Devuelve el reverso de una lista
def lista_inversa(lista):
    inversa = []
    for i in range(len(lista)-1, -1, -1):
        inversa.append(lista[i])
    return inversa

# Ejemplos de uso:
if __name__ == "__main__":
    # a
    print("Suma de 5 y 3:", add_two_numbers(5, 3))

    # b
    print("Área de un círculo con radio 7:", area_del_circulo(7))

    # c
    print("Suma de 1, 2, 3:", add_all_nums(1, 2, 3))
    print("Prueba con un elemento no numérico:", add_all_nums(1, 2, "3"))

    # d
    print("Convertir 25°C a °F:", convert_celsius_to_fahrenheit(25))

    # e
    print("Soluciones de x² - 4x + 4 = 0:", solve_quadratic_eqn(1, -4, 4))
    print("Soluciones de x² + 2x + 1 = 0:", solve_quadratic_eqn(1, 2, 1))
    print("Soluciones de x² + x + 1 = 0:", solve_quadratic_eqn(1, 1, 1))

    # f
    print("Elementos de la lista ['Python', 'C++', 'Java']:")
    print_list(['Python', 'C++', 'Java'])

    # g
    print("Reversa de [1, 2, 3, 4]:", lista_inversa([1, 2, 3, 4]))
