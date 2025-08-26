#determinar si un número es par o impar 
#leer número
numero = int(input("ingrese un numero entero: "))
residuo = numero % 2
#si residuo es cero es par
if residuo == 0: 
    print(numero, " es par")
else:
    print(numero, "es impar")
