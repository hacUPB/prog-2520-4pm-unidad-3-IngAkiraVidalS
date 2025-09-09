## Menú Interactivo de Problemas Aeronáuticos para el reto de la unidad 3

'''
1. Evitar Bird Strike con recomendación del sistema del avión

Contexto:

El avión está en aproximación y el sistema detecta un pájaro que se acerca con cierta velocidad, a una distancia inicial y con una trayectoria (arriba, abajo o frente).
El sistema de abordo analiza el riesgo y recomienda al piloto la acción más segura:

- Subir, Bajar, o Mantener altitud si no hay riesgo.
- El piloto (usuario) puede seguir o no la recomendación.

Dinámica:

1. El pájaro comienza a una distancia inicial (ej. 500 m) y avanza con una velocidad dada.

2. En cada segundo:

- Se recalcula la distancia (fórmula: distancia – velocidad).
- El sistema indica la posición del ave (arriba, abajo, frente).
- Una función de recomendación sugiere la maniobra más segura.
- El piloto decide si seguir o no la recomendación.

3. Condicionales:

- Si la distancia llega a 0 y el piloto tomó la decisión incorrecta → impacto.
- Si el piloto sigue la recomendación → choque evitado.
- Si el pájaro pasa de largo sin riesgo → éxito.

4. El bucle continúa hasta que:
- Se cumplan los 10 segundos.
* O si ocurre un choque.

Elementos técnicos:
- Bucle *for*: simula segundo a segundo.

- Condicionales if: determinan si el pájaro representa un riesgo.

- Función 1: recomendar_maniobra(posicion, distancia, velocidad) → sugiere subir, bajar o mantener.

- Función 2: 
verificar_choque(posicion, accion, distancia) → determina si hubo choque o no.

Ejemplo de recomendación:

- Si el pájaro está de frente y la distancia < 100 m → recomendar “subir altitud”.
- Si el pájaro está arriba → recomendar “bajar altitud”.
- Si el pájaro está abajo → recomendar “subir altitud”.
- Si la distancia > 200 m → “mantener altitud, sin riesgo”.
'''

'''
 Evitar Bird Strike con recomendación del sistema del avión

Contexto:

El avión está en aproximación y el sistema detecta un pájaro que se acerca con cierta velocidad, a una distancia inicial y con una trayectoria (arriba, abajo o frente).
El sistema de abordo analiza el riesgo y recomienda al piloto la acción más segura:

- Subir, Bajar, o Mantener altitud si no hay riesgo.
- El piloto (usuario) puede seguir o no la recomendación.

Dinámica:

1. El pájaro comienza a una distancia inicial (ej. 500 m) y avanza con una velocidad dada.

2. En cada segundo:

- Se recalcula la distancia (fórmula: distancia – velocidad).
- El sistema indica la posición del ave (arriba, abajo, frente).
- Una función de recomendación sugiere la maniobra más segura.
- El piloto decide si seguir o no la recomendación.

3. Condicionales:

- Si la distancia llega a 0 y el piloto tomó la decisión incorrecta → impacto.
- Si el piloto sigue la recomendación → choque evitado.
- Si el pájaro pasa de largo sin riesgo → éxito.

4. El bucle continúa hasta que:
- Se cumplan los 10 segundos.
* O si ocurre un choque.

Elementos técnicos:
- Bucle *for*: simula segundo a segundo.

- Condicionales if: determinan si el pájaro representa un riesgo.

- Función 1: recomendar_maniobra(posicion, distancia, velocidad) → sugiere subir, bajar o mantener.

- Función 2: 
verificar_choque(posicion, accion, distancia) → determina si hubo choque o no.

Ejemplo de recomendación:

- Si el pájaro está de frente y la distancia < 100 m → recomendar “subir altitud”.
- Si el pájaro está arriba → recomendar “bajar altitud”.
- Si el pájaro está abajo → recomendar “subir altitud”.
- Si la distancia > 200 m → “mantener altitud, sin riesgo”.
 1. Valores de entrada (datos que da el usuario o el sistema al inicio):

- Distancia inicial del ave (ej. 500 m).

- Velocidad del ave (ej. 50 m/s).

- Posición inicial del ave (arriba, abajo o frente → puede ser aleatoria o definida).

- Decisión del piloto en cada segundo (subir, bajar, mantener).

2. Valores de salida (lo que el programa muestra):

- Recomendación del avión en cada segundo (“suba”, “baje”, “mantenga”).

- Estado del avión después de la decisión:
- “Impacto evitado”
- “Choque con el ave”
- “Vuelo seguro, sin riesgo”

- Distancia restante en cada segundo.

- Resultado final: éxito (evitó impacto) o fracaso (colisión).

3. Valores intermedios (se calculan durante la ejecución):

- Distancia actual (distancia inicial – velocidad * tiempo).

- Acción tomada por el piloto (puede coincidir o no con la recomendación).

- Verificación del choque (según acción vs posición del ave y distancia).

Estado del riesgo: alto, medio, bajo.

4. Valores constantes (no cambian durante la ejecución):

Tiempo de simulación: 10 segundos (se puede fijar).

Umbral de riesgo por distancia:

- < 100 m → riesgo alto
- 100–200 m → riesgo medio
- 200 m → sin riesgo

- Reglas de recomendación:

- Si el ave está arriba → recomendar “bajar altitud”.

- Si el ave está abajo → recomendar “subir altitud”.

- Si el ave está de frente y a < 100 m → recomendar “subir altitud”.

- Si la distancia es segura (>200 m) → “mantener altitud”.
'''

'''

2. ALCULO DE SUSTENTACION EN DESPEGUE 
Simular el despegue de un avión durante 15 segundos,
permitiendo al usuario modificar el ángulo de ataque en cada segundo. 
Se calcula la fuerza de sustentación en cada ciclo.

Valores de entrada (ingresados por el usuario)
Velocidad inicial del avión (v) → en m/s

Superficie alar (S) → en m²

Ángulo de ataque inicial (α) → en grados

Decisión por segundo → aumentar, disminuir o mantener el ángulo de ataque

Valores de salida (mostrados al usuario)
Sustentación calculada en cada segundo (L) → en Newtons

Ángulo de ataque actualizado

Coeficiente de sustentación (C_L)

Mensaje final con resumen del despegue (por ejemplo, si logró suficiente sustentación)

Valores intermedios (calculados durante el proceso)
C_L (coeficiente de sustentación) → se calcula como C_L = 0.1 × ángulo_de_ataque

Velocidad (v) → puede mantenerse constante o variar si lo decides

Tiempo actual → contador de segundos (1 a 15)

Valores constantes (definidos en el código)
ρ (densidad del aire) = 1.225 kg/m³

Duración de la simulación = 15 segundos

Incremento/disminución del ángulo = ±1 grado por segundo (puedes ajustar)

'''

'''

3. Simulación de gestión de combustible con pérdida de motor

Un avión bimotor está en vuelo de crucero con cierta cantidad de combustible.

De repente, uno de los motores falla y el consumo cambia:

- Con dos motores, el consumo es mayor (pero el avión mantiene mejor velocidad).

- Con un motor, el consumo es menor, pero el avión vuela más lento (más tiempo para llegar).

El piloto debe decidir en cada ciclo (minuto de vuelo) si mantiene el empuje, lo reduce o lo aumenta para administrar el combustible y llegar al destino.

1. Valores de entrada (datos iniciales o elegidos por el usuario):

- Cantidad inicial de combustible (ej. 1000 kg).

- Distancia al destino (ej. 500 km).

- Estado inicial de motores: ambos funcionando.

Decisión del piloto por minuto: empuje bajo, medio o alto.

2. Valores de salida (lo que el programa muestra):

- Combustible restante en cada ciclo.
- Motores en operación (2 motores / 1 motor).
- Velocidad de avance (depende de empuje y número de motores).
- Distancia restante al destino.
- Mensajes:
- “Vuelo exitoso: llegó al destino”
- “Fallo: se quedó sin combustible”
- “Vuelo forzado: motor falló en medio del trayecto”

3. Valores intermedios (se recalculan en cada iteración):

- Consumo de combustible por minuto (según empuje y número de motores).

- Distancia recorrida por minuto (depende de empuje y motores).

- Estado de riesgo (si el combustible está bajo o no alcanza para llegar).

- Tiempo transcurrido (minutos de vuelo).

4. Valores constantes (no cambian durante la ejecución):

- Duración máxima de la simulación: hasta llegar o quedarse sin combustible.

- Consumo aproximado por empuje con 2 motores:
- Bajo: 20 kg/min
- Medio: 40 kg/min
- Alto: 60 kg/min

- Consumo con 1 motor:
- Bajo: 15 kg/min
- Medio: 25 kg/min
- Alto: 35 kg/min

-Velocidad de avance (km/min):
- Con 2 motores: bajo 5 km/min, medio 10 km/min, alto 15 km/min.

- Con 1 motor: bajo 3 km/min, medio 6 km/min, alto 9 km/min.

Momento de falla de motor: puede ser aleatorio o fijado (ej. minuto 3)

'''

'''

4. SIMULACION DE NAVEGACION INERCIAL (INS)

El sistema INS permite a una aeronave calcular su posición, velocidad y orientación sin depender de señales externas,
 usando acelerómetros y giróscopos. En esta simulación, 
 el usuario controla la aceleración y dirección del avión, y el sistema estima su posición en cada segundo.

 Valores de entrada (usuario)
Posición inicial (x, y) → en kilómetros

Velocidad inicial (km/h)

Aceleración por segundo (km/h²) → el usuario decide si aumenta, disminuye o mantiene

Dirección de vuelo → norte, sur, este, oeste (se traduce en vectores)

Valores de salida (consola)
Posición actual (x, y)

Velocidad actual

Trayectoria estimada

Mensaje final con distancia total recorrida

Valores intermedios
Velocidad actual → actualizada cada segundo según aceleración

Desplazamiento por segundo → calculado como velocidad / 3600 (para convertir a km/s)

Dirección vectorial → norte = (0,1), sur = (0,-1), este = (1,0), oeste = (-1,0)

Valores constantes
Duración de simulación = 10 segundos

Factor de conversión = 1 hora = 3600 segundos

Unidad de distancia = kilómetros

'''