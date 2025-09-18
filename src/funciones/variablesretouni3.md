## Tabla de variables 
# OPCIÓN 1: Fuerza de arrastre

|variables de entrada | descripcion |
|---------------------|-------------|
| S                   |Area alar de la aeronave en m² |
| CD                  |Coeficiente de arrastre (adimensional) |
| alt                 |Altitud inicial en metros |
| V                   |Velocidad inicial en m/s |



| variables intermedias | descripcion |
|-----------------------|-------------|
|rho                    | Densidad del aire en función de la altitud (kg/m³) |
| q                     | Presión dinámica del aire (Pa) |
| D                     | Presión dinámica del aire (Pa) |
| paso                  | Incremento de tiempo en segundos (1,0 s) |         
| t                     | Contador del tiempo de simulación |




| variables de salida   | descripcion |
|-----------------------|-------------|
| estado final          | Valores actualizados de tiempo, velocidad, altitud, densidad y fuerza de arrastre en cada paso. |
| Gráfica textual       | Impresión de los resultados en pantalla (evolución de la simulación) |


# OPCIÓN 2: Carrera de despegue y verificación de VR
# Esta funcion se encarga de simular, dependiendo de nas condiciones, si el avion es capaz de alcanzar la velocidad de despegue necesaria para el vuelo


|variables de entrada | descripcion |
|---------------------|-------------|
| alt                 | Altitud del aeródromo en metros |
| S                   | Área alar de la aeronave (m²) |
| CD                  | Coeficiente de arrastre en rodaje |
| CL_to               |Coeficiente de sustentación promedio en rodaje |
| CL_máx              | Coeficiente de sustentación máximo con flaps de despegue |
| masa                | Masa total de la aeronave (kg) |
| T                   | Empuje neto total (N) |
| mu                  | Coeficiente de fricción de rodaje.|
| Lpista              | Longitud de pista disponible (m) |


| variables intermedias | descripcion |
|-----------------------|-------------|
| rho                   | Densidad del aire en función de la altitud (kg/m³) |
| W                     | Peso de la aeronave (N) |
| Vs                    | Velocidad de pérdida (velocidad de pérdida) en m/s |
| Vr                    | Velocidad de rotación en m/s (objetivo) |
| q                     | Presión dinámica (Pa) |
| D                     | Fuerza de arrastre (N) |
| L                     | Fuerza de sustentación (N) |
| N                     | Fuerza normal sobre el tren de aterrizaje (N) |
|Fr                     | Fuerza de fricción de rodaje (N) |
| Fnet                  | Fuerza neta longitudinal (N) |
| a                     | Aceleración (m/s²) |
| V                     | Velocidad actual de la aeronave (m/s) |
| x                     | Distancia recorrida en la pista (m) |
| t                     | Tiempo de simulación (s) |


| variables de salida   | descripcion |
|-----------------------|-------------|
| Estado final          | Velocidad, aceleración, distancia recorrida y fuerzas en cada paso. |
| Resultado             | Indica si la aeronave alcanzó VR dentro de la pista o no |


# OPCIÓN 3: Autonomía en espera y margen de pérdida con consumo de fuel 

|variables de entrada | descripcion |
|---------------------|-------------|
| m_fuel              | Combustible inicial disponible (kg). |
| m_reserva           | Combustible mínimo de reserva a respetar (kg). |
| FF_bajo             | Consumo bajo de combustible (0,18 kg/min). |    
| FF_medio            | Consumo medio de combustible (0,25 kg/min). |
| FF_alto             | Consumo alto de combustible (0,35 kg/min). |
| accion              | Opción seleccionada por el usuario (1=bajo, 2=medio, 3=alto, x=salir). |


| variables intermedias | descripcion |
|-----------------------|-------------|
| consumo_por_minuto    | Valor del flujo de combustible según el nivel de potencia elegido. |
| m_fuel=m_fuel - FF_x  | Actualización del combustible restante según la opción seleccionada. |
| validacion m_fuel > m_reserva | Condición para continuar la simulación o detenerla al llegar a la reserva. |
|tiempo_vuelo           | Tiempo de vuelo antes de llegar a la reserva: (m_fuel - m_reserva) / consumo_por_minuto. |


| variables de salida   | descripcion |
|-----------------------|-------------|
|Restos de combustible  | Muestra el combustible disponible en cada iteración (kg). |
| consumo_por_minuto    | Indica el consumo aplicado según la selección del usuario (kg/min). |
| timpo_vuelo           | Tiempo total de vuelo antes de llegar a la reserva (minutos). |
| Mensajes de estado    | Notificación si se alcanzó la reserva o si el usuario detuvo la simulación. |