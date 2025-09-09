#Tarea 
'''
Crear las siguientes tabla:
- Operadores aritmeticos
- Operadores relacionales
- Tipos de datos en python
'''

#tabala: OPERADORES ARITMETICOS
operadores_aritmeticos = [
    ["Operador", "Descripción", "Ejemplo"],
    ["+", "Suma", "9 + 8 = 17"],
    ["-", "Resta", "7 - 3 = 4"],
    ["*", "Multiplicación", "8 * 5 = 40"],
    ["/", "División", "20 / 2 = 10"],
    ["//", "División entera", "10 // 3 = 3"],
    ["%", "Módulo (residuo)", "10 % 3 = 1"],
    ["**", "Potencia", "2 ** 5 = 32"]
]

# 2) Operadores relacionales
operadores_relacionales = [
    ["Operador", "Descripción", "Ejemplo"],
    ["==", "Igual a", "5 == 5 → True"],
    ["!=", "Diferente de", "5 != 3 → True"],
    [">", "Mayor que", "7 > 3 → True"],
    ["<", "Menor que", "3 < 7 → True"],
    [">=", "Mayor o igual que", "5 >= 5 → True"],
    ["<=", "Menor o igual que", "4 <= 6 → True"]
]

# 3) Tipos de datos en Python
tipos_datos = [
    ["Tipo", "Descripción", "Ejemplo"],
    ["int", "Números enteros", "x = 10"],
    ["float", "Números decimales", "y = 3.14"],
    ["str", "Cadenas de texto", "nombre = 'Carla'"],
    ["bool", "Valores lógicos", "es_valido = True"],
    ["list", "Listas ordenadas", "[1, 2, 3]"],
    ["tuple", "Tuplas inmutables", "(1, 2, 3)"],
    ["set", "Conjuntos sin duplicados", "{1, 2, 3}"],
    ["dict", "Diccionarios clave-valor", "{'a': 1, 'b': 2}"]
]

# Función para imprimir tablas de forma bonita
def imprimir_tabla(tabla):
    for fila in tabla:
        print("{:<10} | {:<25} | {:<20}".format(*fila))
    print("-" * 60)

# Mostrar tablas
print("\n📌 OPERADORES ARITMÉTICOS")
imprimir_tabla(operadores_aritmeticos)

print("\n📌 OPERADORES RELACIONALES")
imprimir_tabla(operadores_relacionales)

print("\n📌 TIPOS DE DATOS EN PYTHON")
imprimir_tabla(tipos_datos)