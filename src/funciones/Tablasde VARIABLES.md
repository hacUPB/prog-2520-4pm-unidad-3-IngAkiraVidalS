1. Evitar Bird Strike con recomendación del sistema del avión

Contexto:

El avión está en aproximación y el sistema detecta un pájaro que se acerca con cierta velocidad, a una distancia inicial y con una trayectoria (arriba, abajo o frente).
El sistema de abordo analiza el riesgo y recomienda al piloto la acción más segura:

- Subir, Bajar, o Mantener altitud si no hay riesgo.
- El piloto (usuario) puede seguir o no la recomendación.

| variables de entrada | descripción |
|----------------------|-------------|
|Distancia_inicial_del_ave| distancia inicial del ave |
|Velocidad_del_ave        |velocidad del ave |
|Posición_inicial_del_ave |posicion inicial dela ave (arriba, abajo o frente → puede ser aleatoria o definida).|
|Decisión_del_piloto_en_cada_segundo | decision del piloto en cada segundo (subir, bajar, antener) |

| variables de salida  | descripción |
|----------------------|-------------|
|Recom_del_avión       |Recomendación del avión en cada segundo (“suba”, “baje”, “mantenga”).|
|Estado_del_avión      | Estado del avión después de la decisión: 
 “Impacto evitado”
- “Choque con el ave”
- “Vuelo seguro, sin riesgo” |

|Distan_restante       |  Distancia restante en cada segundo. |
|Resul_final           | Resultado final: éxito (evitó impacto) o fracaso (colisión). |

| variables intermedias| descripción |
|----------------------|-------------|
|Dist_actual           |distancia inicial – velocidad * tiempo |
|Acción_tomada_por_el_piloto | Acción tomada por el piloto (puede coincidir o no con la recomendación) |
|Verifi_del_choque     |según acción vs posición del ave y distancia |
|Estado_del_riesgo     |Estado del riesgo: alto, medio, bajo. |

|Valores constantes    | descripción |
|----------------------|-------------|
|Tiem_de_simul         |Tiempo de simulación: 10 segundos (se puede fijar). |
|Umbral de riesgo por distancia:| 
- < 100 m → riesgo alto
- 100–200 m → riesgo medio
- 200 m → sin riesgo



|Reglas de recomendación:
- Si el ave está arriba → recomendar “bajar altitud”.

- Si el ave está abajo → recomendar “subir altitud”.

- Si el ave está de frente y a < 100 m → recomendar “subir altitud”.

- Si la distancia es segura (>200 m) → “mantener altitud”. |

| variables de entrada | descripción |
|----------------------|-------------|


