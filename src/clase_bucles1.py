numero = 1
while numero <= 5:
    print(numero)
    numero += 1      #numero = numero + 1

#imprimir los numeros pares entre el 20 y 80 

numero = 20   # empezamos en 20

while numero <= 80:   # condición hasta 80
    print(numero)     # imprime el número actual
    numero += 2       # sumamos de 2 en 2 porque son pares

#imprimir los numeros impares entre 90 y 61, en orden descente 



#solicitar dos numeros al usuario e imprimir los numeros impares entre ellos

#solicitar dos numeros al usuario 
inicio = int (input("ingrese el primer numero: "))
fin= int(input("Ingrese el segundo número: "))

# asegurarnos de que inicio sea el menor
if inicio > fin:
    inicio, fin = fin, inicio

# imprimir los números impares entre ellos
while inicio <= fin:
    if inicio % 2 != 0:   # si el número es impar
        print(inicio)
    inicio += 1



#imprimir los multiplos de 7 ntre 0 y 100 

numero = 0 

while numero <= 100:
    if numero % 7 == 0:
        print(numero)
    numero += 1



#solicitaar un numero al usuario e imprimir su tabla de multiplicar hasta 15

# solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# imprimir la tabla de multiplicar hasta 15
i = 1
while i <= 15:
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}")
    i += 1
    


