def suma(a, b):
    resultado = a + b
    return resultado

#crear una funcion que imprima la tabla de cualquier número - bucle for
def tabla(num):
    for i in range(1,11):
        producto = i * num
        print(f"{num} x {i} = {producto}")
    #esta funcion no tiene ningun valor de retorno


#llamado a la funcion
numero1= 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

numero = int(input("ingrese un valor: "))
var = tabla(numero)