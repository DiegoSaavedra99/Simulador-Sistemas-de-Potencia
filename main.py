from carga import Carga
from generador import Generador
from linea_transmision import LineaTransmision
from sistema_potencia import SistemaPotencia


def main():
    """
    Ejecuta una prueba básica de las clases implementadas en el Hito 1.
    """
    print("Se cargan los datos a los elementos del sistema")
    print()

    generador_1 = Generador(
        "G1",
        "Generador 1",
        100,
        25,
        60
    )

    carga_1 = Carga(
        "C1",
        "Carga 1",
        50
    )

    linea_1 = LineaTransmision(
        "L1",
        "Linea 1",
        "Barra 1",
        "Barra 2",
        0.1
    )

    sistema = SistemaPotencia()

    sistema.agregar_elemento(generador_1)
    sistema.agregar_elemento(carga_1)
    sistema.agregar_elemento(linea_1)

    sistema.consultar_elementos()
    print()

    print("Prueba de encapsulamiento:")
    print()

    print("Potencia inicial:")
    print(generador_1.get_potencia())

    print("\nIntentando asignar 120 MW:")
    generador_1.set_potencia(120)

    print("\nPotencia después del intento:")
    print(generador_1.get_potencia())


if __name__ == "__main__":
    main()
