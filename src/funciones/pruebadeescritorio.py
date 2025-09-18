# Reto Unidad 3 - Menú interactivo de problemas aeronáuticos
# Constantes básicas
G = 9.81  # m/s^2

# -------------------- OPCIÓN 1: Fuerza de arrastre -----------------

def opcion_1_arrastre():
    print("\n=== Opción 1: Simulación de arrastre ===")
    S = float(input("Área alar S (m^2): "))
    CD = float(input("Coeficiente de arrastre CD: "))
    alt = float(input("Altitud inicial (m): "))
    V = float(input("Velocidad inicial (m/s): "))
    paso = 1.0  # s
    t = 0.0

    print("\nSimulación paso a paso. Controles:")
    print("  a = acelerar (+5 m/s), d = disminuir (-5 m/s), m = mantener")
    print("  u = subir (+100 m),    b = bajar (-100 m),    x = salir\n")

    while True:
        rho = 1.225 * (1 - 2.25577e-5 * alt) ** 4.256
        q = 0.5 * rho * V * V
        D = q * S * CD
        print(f"t={int(t):3d} s | V={V:6.1f} m/s | alt={alt:5.0f} m | rho={rho:1.3f} kg/m³ | D={D:7.1f} N")

        accion = input("Acción [a/d/m/u/b/x]: ").strip().lower()
        if accion == "a":
            V = V + 5.0
        elif accion == "d":
            V = max(0.0, V - 5.0) # Se usa la funcion max, para que v tome el valor mayor entre estos datos, de esta manera evitamos usar velocidades negativas
        elif accion == "m":
            V = V
        elif accion == "u":
            alt = alt + 100.0
        elif accion == "b":
            alt = max(0.0, alt - 100.0) # Evita usar altitudes negativas
        elif accion == "x":
            break
        else:
            print("Opción no válida. Se mantiene el estado.")
        t = t + paso #Contador

    print("Fin de la simulación de arrastre.")
    input("Presiona Enter para continuar...")