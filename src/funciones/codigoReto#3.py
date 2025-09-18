#Reto Unidad 3 - Menú interactivo de problemas aeronáuticos


# -------------------- Funciones -----------------

import Funciones




# --------------------------------- MENÚ -------------------------------------

def menu():
    while True:
        print("\n================ MENÚ PRINCIPAL ================")
        print("1) Problema 1: Control de arrastre generado")
        print("2) Problema 2: Carrera de despegue")
        print("3) Problema 3: Consumo de combustible")
        print("4) Salir")
        opcion = input("Elige una opción [1-4]: ").strip()

        if opcion == "1":
            Funciones.opcion_1_arrastre()
        elif opcion == "2":
            Funciones.opcion_2_carrera_despegue()
        elif opcion == "3":
            Funciones.opcion_3_consumo_combustible()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
