'''
funcion: menu
parametros de entrada: ninguno
Ejecucion: imprimir en la panta 4 opciones diferentes. Solicitar que se elija una opcion y la guarda en una variable.
valor de retorno: opcion elegida
'''

def menu():
    print("seleccione una opcion: ")
    print("1. Encabezado: ")
    print("2. porcenttaje: ")
    print("3. mesaje : ")
    print("4. salir: ")
    opcion= int(input("ingrese el numero de la opcion deseada: "))
    return opcion 

def encabezado(mensaje):
    print("Nombre: Akira Vial Sanchez")
    print("programa de pregrado: Ingenieria Aeronautica: ")
    print(mensaje)


def porcentaje(valor1, valor2):
    print("")

eleccion = menu()
match(eleccion):
    case 1:
        Encabezado(mensaje)
        #imprimir informacion sobre ustedes 
        #parametro: mensaje que se imprime dentro de la funcion
    case 2:
        pass 
        #parametro 1: valor total
        #parametro 2: porcentaje
        #retorno: valor del porcentaje
    case 3: 
        pass
        #no recibe ningun parámetro y no devuelve un resultado
        #imprime en la pantalla un mensaje de cierre de programa 