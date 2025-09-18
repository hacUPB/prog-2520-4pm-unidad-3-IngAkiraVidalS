# opcion 1
INICIO
    Definir G ← 9.81        // gravedad (m/s²)
FIN

INICIO FUNCIÓN opcion_1_arrastre
    Mostrar "=== Opción 1: Simulación de arrastre ==="

    Leer S          // área alar (m²)
    Leer CD         // coeficiente de arrastre
    Leer alt        // altitud inicial (m)
    Leer V          // velocidad inicial (m/s)

    paso ← 1.0
    t ← 0.0

    Mostrar controles: a=acelerar, d=disminuir, m=mantener, u=subir, b=bajar, x=salir

    MIENTRAS VERDADERO HACER
        rho ← 1.225 * (1 − 2.25577e−5 * alt) ^ 4.256    // densidad ISA aprox.
        q   ← 0.5 * rho * V^2                           // presión dinámica
        D   ← q * S * CD                                // arrastre

        Mostrar t, V, alt, rho, D

        Leer accion
        SI accion = "a" ENTONCES
            V ← V + 5
        SINO SI accion = "d" ENTONCES
            V ← máx(0, V − 5)                           // evita V negativa
        SINO SI accion = "m" ENTONCES
            (sin cambio)
        SINO SI accion = "u" ENTONCES
            alt ← alt + 100
        SINO SI accion = "b" ENTONCES
            alt ← máx(0, alt − 100)                     // evita alt negativa
        SINO SI accion = "x" ENTONCES
            SALIR DEL BUCLE
        SINO
            Mostrar "Opción no válida"

        t ← t + paso
    FIN MIENTRAS

    Mostrar "Fin de la simulación de arrastre"
    Esperar Enter
FIN FUNCIÓN

# opcion 2
INICIO FUNCIÓN opcion_2_carrera_despegue
    Mostrar "=== Opción 2: Carrera de despegue (alcance de VR) ==="

    Leer alt, S, CD, CL_to, CL_max, masa, T, mu, Lpista

    rho ← 1.225 * (1 − 2.25577e−5 * alt) ^ 4.256
    W   ← masa * G
    Vs  ← √( (2 * W) / (rho * S * CL_max) )
    Vr  ← 1.2 * Vs
    Mostrar rho, Vs, Vr

    dt ← 1
    V ← 0           // velocidad
    x ← 0           // distancia
    t ← 0           // tiempo

    MIENTRAS (V < Vr) Y (x < Lpista) HACER
        q  ← 0.5 * rho * V^2
        D  ← q * S * CD
        L  ← q * S * CL_to
        N  ← W − L
        SI N < 0 ENTONCES N ← 0

        Fr   ← mu * N
        Fnet ← T − D − Fr
        a    ← Fnet / masa
        SI a < −5 ENTONCES a ← −5

        V ← máx(0, V + a * dt)
        x ← x + V * dt + 0.5 * a * dt^2
        t ← t + 1

        Mostrar t, V, x, a, D, Fr

        SI (t > 120) O ((a ≤ 0) Y (V < 1)) ENTONCES
            SALIR DEL BUCLE
    FIN MIENTRAS

    Mostrar "--- Resultado ---"
    SI (V ≥ Vr) Y (x ≤ Lpista) ENTONCES
        Mostrar "¡VR alcanzada!", V, x, t
    SINO
        Mostrar "No se alcanzó VR", V, x, Lpista

    Esperar Enter
FIN FUNCIÓN

# opcion 3
INICIO FUNCIÓN opcion_3_consumo_combustible
    Mostrar "=== Opción 3: Consumo de combustible ==="

    Leer m_fuel        // combustible inicial (kg)
    Leer m_reserva     // reserva mínima (kg)

    FF_bajo  ← 0.18    // kg/min
    FF_medio ← 0.25
    FF_alto  ← 0.35

    Mostrar menú: 1=bajo, 2=medio, 3=alto, x=salir

    MIENTRAS m_fuel > m_reserva HACER
        Leer accion

        SI accion = "1" ENTONCES
            m_fuel ← m_fuel − FF_bajo
        SINO SI accion = "2" ENTONCES
            m_fuel ← m_fuel − FF_medio
        SINO SI accion = "3" ENTONCES
            m_fuel ← m_fuel − FF_alto
        SINO SI accion = "x" ENTONCES
            Mostrar "Simulación terminada por el usuario"
            SALIR DEL BUCLE
        SINO
            Mostrar "Opción no válida, se asume consumo medio"
            m_fuel ← m_fuel − FF_medio
        FIN SI

        SI m_fuel ≤ m_reserva ENTONCES
            Mostrar "Se alcanzó la reserva mínima", m_reserva, "kg"
            SALIR DEL BUCLE
        FIN SI

        Mostrar "Combustible restante:", m_fuel, "kg"

        // guardar consumo usado en este minuto (para reporte final)
        SI accion = "1" ENTONCES
            consumo_por_minuto ← FF_bajo
        SINO SI accion = "2" ENTONCES
            consumo_por_minuto ← FF_medio
        SINO
            consumo_por_minuto ← FF_alto
        FIN SI

        Mostrar "Consumo por minuto:", consumo_por_minuto, "kg/min"
    FIN MIENTRAS

    tiempo_vuelo ← (m_fuel − m_reserva) / consumo_por_minuto
    Mostrar "Tiempo total de vuelo antes de la reserva:", tiempo_vuelo, "min"

    Esperar Enter
FIN FUNCIÓN

INICIO FUNCIÓN menu
    MIENTRAS VERDADERO HACER
        Mostrar "=== MENÚ PRINCIPAL ==="
        Mostrar "1) Arrastre"
        Mostrar "2) Carrera de despegue"
        Mostrar "3) Consumo de combustible"
        Mostrar "4) Salir"

        Leer opcion

        SI opcion = "1" ENTONCES
            Llamar opcion_1_arrastre
        SINO SI opcion = "2" ENTONCES
            Llamar opcion_2_carrera_despegue
        SINO SI opcion = "3" ENTONCES
            Llamar opcion_3_consumo_combustible
        SINO SI opcion = "4" ENTONCES
            Mostrar "¡Hasta luego!"
            SALIR DEL BUCLE
        SINO
            Mostrar "Opción inválida"
        FIN SI
    FIN MIENTRAS
FIN FUNCIÓN

INICIO PROGRAMA
    Llamar menu
FIN PROGRAMA