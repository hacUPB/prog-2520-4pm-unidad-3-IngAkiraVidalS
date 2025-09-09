print(10 > 5)
print("hola"!= "mundo")
print (3.14 <= 4.5)
nombre ="juan"
print(nombre == "juan")
print (nombre == "juan" and 10 < 4)

## Ejercicio 2
'''
Resuelve el siguiente problema usando el condicional simple.

Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.
'''

comptra = int(input(ingrese el valor de la compra>> "))
if compra < 100000:
    envio = 9000
total = compra + envio 
print(f"El total de la compra es {total}")


##ejercicio 5

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 26:
        if edad <= 18:
            etapa = "Adolescencia"
        if edad > 14:
            etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    print(f"Tu etapa del ciclo de vida es: {etapa}")
else:
    print("La edad ingresada no es válida.")


