#Funciones codigo
# Constantes básicas
G = 9.81  # m/s^2
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

# -------- OPCIÓN 2: Carrera de despegue y verificación de VR -----
#Esta funcion se encarga de simular, dependiendo de nas condiciones, si el avion es capaz de alcanzar la velocidad de despegue necesaria para el vuelo

def opcion_2_carrera_despegue():
    print("\n=== Opción 2: Carrera de despegue (alcance de VR) ===")
    alt = float(input("Altitud del aeródromo (m): "))
    S = float(input("Área alar S (m^2): "))
    CD = float(input("CD en rodaje (aprox. 0.03–0.08): "))
    CL_to = float(input("CL medio durante rodaje (config. despegue): "))
    CL_max = float(input("CL_max (con flaps de despegue): "))
    masa = float(input("Masa total (kg): "))
    T = float(input("Empuje neto total T (N): "))
    mu = float(input("Coef. fricción de rodaje μ (0.02–0.04 asfalto): "))
    Lpista = float(input("Longitud de pista disponible (m): "))

    rho = 1.225 * (1 - 2.25577e-5 * alt) ** 4.256
    W = masa * G
    Vs = (2.0 * W / (rho * S * CL_max)) ** 0.5
    Vr = 1.2 * Vs

    print(f"\nDensidad: {rho:0.3f} kg/m³ | Vs={Vs:0.1f} m/s | Vr objetivo={Vr:0.1f} m/s")
    print("Simulación con Δt=1 s. Se imprime cada paso.")

    dt = 1.0
    V = 0.0
    x = 0.0
    t = 0

    while V < Vr and x < Lpista:
        q = 0.5 * rho * V * V
        D = q * S * CD
        L = q * S * CL_to
        N = W - L
        if N < 0.0:
            N = 0.0
        Fr = mu * N
        Fnet = T - D - Fr
        a = Fnet / masa

        if a < -5.0:
            a = -5.0  # Evitar valores absurdos por datos extremos
        V = max(0.0, V + a * dt)
        x = x + V * dt + 0.5 * a * dt * dt
        t = t + 1

        print(f"t={t:2d}s | V={V:6.1f} m/s | x={x:7.1f} m | a={a:5.2f} m/s² | D={D:6.0f} N | Fr={Fr:6.0f} N")
        # Si se hacen mas de 120 simulaciones y el avion aun no llega a VR, por mas que intente no llegará a la velocidad necesaria
        if t > 120 or (a <= 0.0 and V < 1.0):
            break

    print("\n--- Resultado ---")
    if V >= Vr and x <= Lpista:
        print(f"¡VR alcanzada! V={V:0.1f} m/s en x={x:0.1f} m, tiempo={t} s")
    else:
        print(f"No se alcanzó VR. V={V:0.1f} m/s, distancia recorrida={x:0.1f} m (pista={Lpista:0.0f} m)")
    input("Presiona Enter para continuar...")

# -- OPCIÓN 3: Autonomía en espera y margen de pérdida con consumo de fuel ---

def opcion_3_consumo_combustible():
    print("\n=== Opción 3: Consumo de combustible ===")
    m_fuel = float(input("Combustible inicial (kg): "))  # Combustible inicial
    m_reserva = float(input("Reserva mínima a respetar (kg): "))  # Reserva mínima de combustible
    FF_bajo = 0.18  # Consumo bajo (kg/min)
    FF_medio = 0.25  # Consumo medio (kg/min)
    FF_alto = 0.35  # Consumo alto (kg/min)

    print("\nElige el nivel de potencia:")
    print("1) Bajo consumo")
    print("2) Consumo medio")
    print("3) Alto consumo")
    print("x) Salir")

    # Bucle para simular el consumo de combustible minuto a minuto
    while m_fuel > m_reserva:
        accion = input("Selecciona opción [1/2/3/x]: ").strip().lower()

        if accion == "1":
            m_fuel -= FF_bajo  # Disminuir combustible según el consumo bajo
        elif accion == "2":
            m_fuel -= FF_medio  # Disminuir combustible según el consumo medio
        elif accion == "3":
            m_fuel -= FF_alto  # Disminuir combustible según el consumo alto
        elif accion == "x":
            print("Simulación terminada por el usuario.")
            break
        else:
            print("Opción no válida. Se asume consumo medio.")
            m_fuel -= FF_medio

        if m_fuel <= m_reserva:
            print(f"\n¡Se alcanzó la reserva mínima de {m_reserva} kg!")
            break

        print(f"\nCombustible restante: {m_fuel:.1f} kg")
        if accion == '1':
            consumo_por_minuto = FF_bajo
        elif accion == '2':
            consumo_por_minuto = FF_medio
        else:
            consumo_por_minuto = FF_alto

        # Imprimimos el resultado con el consumo elegido
        print(f"Consumo por minuto: {consumo_por_minuto} kg/min")

    # Ahora calculamos el tiempo total de vuelo usando el consumo correspondiente
    tiempo_vuelo = (m_fuel - m_reserva) / consumo_por_minuto

    # Imprimimos el resultado
    print(f"\nTiempo total de vuelo antes de la reserva: {tiempo_vuelo:.1f} minutos")

    input("\nPresiona Enter para continuar...")