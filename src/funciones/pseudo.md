## OPCIÓN 1: Fuerza de arrastre

INICIO

Definir constante:
    G = 9.81   // Gravedad (m/s^2)

FUNCIÓN opcion_1_arrastre():
    Mostrar "== Opción 1: Simulación de arrastre =="

    Leer S  (Área alar en m^2)
    Leer CD (Coeficiente de arrastre)
    Leer alt (Altitud inicial en m)
    Leer V  (Velocidad inicial en m/s)

    paso ← 1.0   // intervalo de tiempo
    t ← 0.0      // tiempo inicial

    Mostrar controles disponibles:
        a = acelerar (+5 m/s)
        d = disminuir (–5 m/s)
        m = mantener velocidad
        u = subir (+100 m)
        b = bajar (–100 m)
        x = salir

    REPETIR MIENTRAS VERDADERO:
        Calcular densidad del aire:
            rho = 1.225 * (1 - 2.25577e-5 * alt) ^ 4.256

        Calcular presión dinámica:
            q = 0.5 * rho * V^2

        Calcular fuerza de arrastre:
            D = q * S * CD

        Mostrar en pantalla:
            tiempo (t), velocidad (V), altitud (alt), densidad (rho), fuerza de arrastre (D)

        Leer acción del usuario (accion)

        SEGÚN accion HACER:
            SI "a": aumentar velocidad (V = V + 5.0)
            SI "d": disminuir velocidad (V = máx(0, V - 5.0)) // evita valores negativos
            SI "m": mantener velocidad igual
            SI "u": aumentar altitud (alt = alt + 100.0)
            SI "b": disminuir altitud (alt = máx(0, alt - 100.0)) // evita altitud negativa
            SI "x": SALIR del bucle
            EN OTRO CASO: mostrar "Opción no válida, se mantiene el estado"

        Incrementar el tiempo: t = t + paso

    FIN MIENTRAS

    Mostrar "Fin de la simulación de arrastre."
    Esperar que el usuario presione Enter para continuar

FIN FUNCIÓN

FIN


## OPCIÓN 2: Carrera de despegue y verificación de VR 

INICIO

FUNCIÓN opcion_2_carrera_despegue():

    Mostrar "== Opción 2: Carrera de despegue (alcance de VR) =="

    Leer alt        (Altitud del aeródromo en m)
    Leer S          (Área alar en m²)
    Leer CD         (Coeficiente de arrastre en rodaje)
    Leer CL_to      (CL medio durante rodaje/configuración despegue)
    Leer CL_max     (CL máximo con flaps de despegue)
    Leer masa       (Masa total de la aeronave en kg)
    Leer T          (Empuje neto total en N)
    Leer mu         (Coeficiente de fricción de rodaje)
    Leer Lpista     (Longitud de pista disponible en m)

    Calcular densidad del aire:
        rho = 1.225 * (1 - 2.25577e-5 * alt) ^ 4.256

    Calcular peso de la aeronave:
        W = masa * G

    Calcular velocidad de pérdida (stall speed):
        Vs = sqrt( (2 * W) / (rho * S * CL_max) )

    Calcular velocidad de rotación (VR):
        Vr = 1.2 * Vs

    Mostrar datos iniciales:
        rho, Vs y Vr

    Definir condiciones iniciales:
        dt = 1.0       // paso de tiempo
        V = 0.0        // velocidad inicial
        x = 0.0        // distancia recorrida
        t = 0          // tiempo inicial

    MIENTRAS (V < Vr) Y (x < Lpista):
        Calcular presión dinámica:
            q = 0.5 * rho * V^2

        Calcular fuerzas aerodinámicas:
            D = q * S * CD          // arrastre
            L = q * S * CL_to       // sustentación

        Calcular fuerza normal:
            N = W - L
            SI N < 0 → N = 0

        Calcular fricción de rodaje:
            Fr = mu * N

        Calcular fuerza neta:
            Fnet = T - D - Fr

        Calcular aceleración:
            a = Fnet / masa
            SI a < -5 → a = -5   // limitar valores extremos

        Actualizar velocidad:
            V = máx(0, V + a * dt)

        Actualizar posición:
            x = x + V * dt + 0.5 * a * dt^2

        Incrementar tiempo:
            t = t + 1

        Mostrar en pantalla: t, V, x, a, D, N, Fr

        SI (t > 120) O (a <= 0 y V < 1):
            SALIR del bucle

    FIN MIENTRAS

    Mostrar "--- Resultado ---"
    SI (V >= Vr y x <= Lpista):
        Mostrar "¡VR alcanzada!"
        Indicar velocidad, distancia y tiempo
    EN OTRO CASO:
        Mostrar "No se alcanzó VR"
        Indicar velocidad final, distancia recorrida y pista disponible

    Esperar "Presiona Enter para continuar..."

FIN FUNCIÓN

FIN

# OPCIÓN 3: Autonomía en espera y margen de pérdida con consumo de fuel 
 
 INICIO

LEER m_fuel        // Combustible inicial
LEER m_reserva     // Reserva mínima de combustible

DEFINIR FF_bajo  = 0.18
DEFINIR FF_medio = 0.25
DEFINIR FF_alto  = 0.35

MOSTRAR "Menú de consumo:"
MOSTRAR "1. Bajo consumo"
MOSTRAR "2. Consumo medio"
MOSTRAR "3. Alto consumo"
MOSTRAR "x. Salir"

MIENTRAS m_fuel > m_reserva HACER
    LEER accion

    SI accion == "1" ENTONCES
        m_fuel = m_fuel - FF_bajo
    SINO SI accion == "2" ENTONCES
        m_fuel = m_fuel - FF_medio
    SINO SI accion == "3" ENTONCES
        m_fuel = m_fuel - FF_alto
    SINO SI accion == "x" ENTONCES
        MOSTRAR "Simulación terminada por el usuario"
        SALIR DEL BUCLE
    SINO
        MOSTRAR "Opción no válida, se asume consumo medio"
        m_fuel = m_fuel - FF_medio
    FIN SI

    SI m_fuel <= m_reserva ENTONCES
        MOSTRAR "Se alcanzó la reserva mínima de", m_reserva, "kg"
        SALIR DEL BUCLE
    FIN SI

    MOSTRAR "Combustible restante:", m_fuel, "kg"
FIN MIENTRAS

// Determinar el consumo seleccionado
SI accion == "1" ENTONCES
    consumo_por_minuto = FF_bajo
SINO SI accion == "2" ENTONCES
    consumo_por_minuto = FF_medio
SINO
    consumo_por_minuto = FF_alto
FIN SI

// Calcular tiempo de vuelo antes de la reserva
tiempo_vuelo = (m_fuel - m_reserva) / consumo_por_minuto

MOSTRAR "Consumo por minuto:", consumo_por_minuto, "kg/min"
MOSTRAR "Tiempo total de vuelo antes de la reserva:", tiempo_vuelo, "minutos"

FIN
