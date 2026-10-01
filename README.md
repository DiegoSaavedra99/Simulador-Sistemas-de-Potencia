# Simulador de Sistemas de Potencia — Hito 1

Proyecto del curso **EL4203 – Programación Avanzada**.

## Alcance del Hito 1

Esta entrega implementa la arquitectura orientada a objetos del simulador:

- `ElementoRed`: clase padre.
- `Generador`: clase hija con potencia máxima, potencia actual y costo operativo.
- `Carga`: clase hija que representa la demanda eléctrica.
- `LineaTransmision`: clase hija que representa una conexión de la red.
- `SistemaPotencia`: clase gestora que administra los elementos de la red.

Se aplican **herencia**, **encapsulamiento**, atributos privados, getters/setters y docstrings.

## Estructura

```text
.
├── elemento_red.py
├── generador.py
├── carga.py
├── linea_transmision.py
├── sistema_potencia.py
├── main.py
└── .gitignore
```

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

`main.py` crea un generador, una carga y una línea de transmisión, los incorpora a `SistemaPotencia` y realiza una prueba simple de encapsulamiento.
