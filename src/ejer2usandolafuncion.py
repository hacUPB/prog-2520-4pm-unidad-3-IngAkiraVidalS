## Escribe un programa que solicite al usuario ingresar un número entero positivo n. 
# Luego, utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n.
#  Finalmente, muestra el resultado de la suma en pantalla.

n = int(input("ingrese un numero entero positivo: "))
acumulador = 0
for i in range(0, n+1): 
    if i % 2 == 0:
        acumulador += i #acumulador tipo de variable: acumulador

print(f"la suma de los pares hasta {n} es {acumulador}")

