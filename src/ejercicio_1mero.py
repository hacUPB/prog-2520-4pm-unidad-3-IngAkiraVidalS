
nombre = input("Por favor ingrese su nombre: ")
print("Bienvenido ", nombre)

#Calcular el indice de Masa Corporal
#IMC = peso / estatura^2

#leer estatura
estatura = input ("ingrese su estatura en metros: ")
estatura = float(estatura)
#leer peso
peso = input("ingrese su peso: ")
peso = int(peso)
#calcula imc
imc = peso / estatura ** 2
#mostrar imc
print ("Su IMC = ", imc)

#determinar si el indice de masa corporal es saludable o a tratar

#pedir el indice de masa coroporal 
imc = float (input ("ingrese su indice de masa corporal (IMC): "))

#evaluar la categoria 
if imc < 1805:
    print("bajo de peso → Requiere atención.")
elif 1805 <= imc <= 24.9:
    print("peso saludable")
elif 25 <= imc <= 29.9:
    print("sobrepeso → Requiere atención.")
else: # IMC >= 30
    print("Obesidad → Requiere atención.")


