'''
1
12
123
1234
12345

i                       j
1  hasta n              1 hasta 1
              
'''
numero = int(input("ingrese el numero entero positivo: "))

for i in range(1, numero + 1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

