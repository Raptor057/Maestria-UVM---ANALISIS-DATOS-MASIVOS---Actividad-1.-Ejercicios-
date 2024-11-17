# a) Itera de 0 a 10 usando cualquier ciclo
print("Iterar de 0 a 10:")
for i in range(11):
    print(i)

# b) Itera de 10 a 0 usando cualquier ciclo
print("\nIterar de 10 a 0:")
for i in range(10, -1, -1):
    print(i)

# c) Escribe un ciclo para obtener un triángulo
print("\nTriángulo:")
for i in range(1, 8):
    print("#" * i)

# d) Utiliza ciclos anidados para crear un cuadrado
print("\nCuadrado de #:")
for _ in range(8):
    print("# " * 8)

# e) Imprime un patrón de multiplicación
print("\nPatrón de multiplicación:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# f) Itera a través de la lista e imprime los elementos
print("\nElementos de la lista:")
for item in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(item)

# g) Imprimir solo números pares de 0 a 100
print("\nNúmeros pares de 0 a 100:")
for i in range(101):
    if i % 2 == 0:
        print(i, end=" ")
print()

# h) Imprimir solo números impares de 0 a 100
print("\nNúmeros impares de 0 a 100:")
for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")
print()
