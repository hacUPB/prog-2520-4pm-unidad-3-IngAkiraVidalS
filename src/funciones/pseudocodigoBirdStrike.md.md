1. Bird Strike:
```
Inicio
    leer  distancia, velocidad y posición del ave
  Mientras distancia > 0 y no hay impacto:
    Reducir distancia según velocidad
    Dar recomendación según posición del ave
    Pedir decisión del piloto
    Si la decisión coincide con la recomendación:
      Mostrar “vuelo seguro”
    Sino:
      Si posición es “frente” y distancia < 50:
        Mostrar “choque con el ave”
        Terminar simulación
    Si distancia == 0:
      Mostrar “el ave ya pasó sin impacto”
 Fin
 ```