import math

# Radio del círculo
radio = 30

# Cálculos
area_of_circle = math.pi * (radio ** 2)
circum_of_circle = 2 * math.pi * radio

# Imprimir resultados iniciales
print(f"Radio: {radio} metros")
print(f"Área del círculo: {area_of_circle:.2f} metros cuadrados")
print(f"Circunferencia del círculo: {circum_of_circle:.2f} metros")

# Pedir entrada al usuario
try:
    user_radio = float(input("Introduce el radio del círculo (en metros): "))
    user_area_of_circle = math.pi * (user_radio ** 2)
    print(f"El área del círculo con radio {user_radio} es: {user_area_of_circle:.2f} metros cuadrados")
except ValueError:
    print("Por favor, introduce un valor numérico válido.")
