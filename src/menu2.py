# utilizamos una variable tipo booleana -> una bandera
control = True

while control == True:
    print("1. entradas\n2. platos fuertes\n3. bebidas\n4. postres\n5. Salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1:
            print("1. patacon con hogao ")
            print("2. ceviche de chicharron ")
            print("3. totopos con carne y pollo ")
        case 2:
            print("1. Slomito ")
            print("2. hamburguesa ")
            print("3. sushi ")
        case 3:
            print("1. Limonada ")
            print("2. jugos naturales ")
            print("3. cerveza ")
        case 4:
            print("1. tres leches ")
            print("2. tiramisu ")
            print("3. torta de chocolate ")
        case 5:
            control= False
        case _:
            print("opcion no valida")
