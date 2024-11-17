# a) Crear un diccionario vacío llamado perro
perro = {}

# b) Agregar nombre, color, raza, patas y edad al diccionario de perro
perro["nombre"] = "Max"
perro["color"] = "Marrón"
perro["raza"] = "Labrador"
perro["patas"] = 4
perro["edad"] = 5

print("Diccionario de perro:", perro)

# c) Crear un diccionario de estudiantes
estudiante = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "sexo": "Masculino",
    "edad": 26,
    "estado_civil": "Soltero",
    "habilidades": ["Python", "SQL"],
    "pais": "México",
    "ciudad": "Ciudad de México",
    "direccion": "Calle Falsa 123"
}

print("Diccionario de estudiante:", estudiante)

# d) Obtener la longitud del diccionario del estudiante
longitud_estudiante = len(estudiante)
print("Longitud del diccionario de estudiante:", longitud_estudiante)

# e) Obtener el valor de habilidades y verificar el tipo de datos
habilidades = estudiante["habilidades"]
print("Habilidades:", habilidades)
print("Tipo de datos de habilidades:", type(habilidades))

# f) Modificar las habilidades agregando una o dos habilidades
estudiante["habilidades"].extend(["Java", "Docker"])
print("Habilidades modificadas:", estudiante["habilidades"])

# g) Obtener las claves del diccionario como una lista
claves_estudiante = list(estudiante.keys())
print("Claves del diccionario de estudiante:", claves_estudiante)

# h) Obtener los valores del diccionario como una lista
valores_estudiante = list(estudiante.values())
print("Valores del diccionario de estudiante:", valores_estudiante)

# i) Cambiar el diccionario a una lista de tuplas usando el método items()
tuplas_estudiante = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas_estudiante)

# j) Eliminar uno de los elementos del diccionario
estudiante.pop("estado_civil")
print("Diccionario de estudiante después de eliminar 'estado_civil':", estudiante)

# k) Eliminar uno de los diccionarios
del perro
print("El diccionario de perro ha sido eliminado.")
