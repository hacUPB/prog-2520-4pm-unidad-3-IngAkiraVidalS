## ejercicio 5
'''
Una compañía de paquetería internacional tiene servicio en algunos países según su zona. El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido.
 Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. 
 Usa la siguiente tabla para resolver el problema:
'''
print("ingrese la zona de envio. Elija un numero.")
zona = int(input("1. Norteamerica\n2. Centroamerica\n3. Suramerica\
     \n4. Europa\n5. Asia\nElija un numero: "))
if zona > 0 and zona < 6:
    peso = int(input("ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
        if zona == 1:
        total = peso * 11
        elif zona == 2:
        total = peso * 10
        elif zona == 3:
        total = peso * 12
        elif zona == 4:
        total = peso * 24
        elif zona == 5:
        total = peso * 27
        print (f"el envio de su paquete cuesta ${total}.")
    else:
        print("no se puede enviar paquetes de mas de 5 kg.")
 else:
    print("la zona ingresada no existe.")



                 