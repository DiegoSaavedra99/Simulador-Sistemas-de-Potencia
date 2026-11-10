from generador import Generador
from sistema_potencia import SistemaPotencia


def main():
    """
    Prueba del algoritmo de ordenamiento y despacho económico.
    """

    generador_1 = Generador(
        "G1",
        "Generador 1",
        100,
        25,
        0
    )

    generador_2 = Generador(
        "G2",
        "Generador 2",
        80,
        15,
        0
    )

    generador_3 = Generador(
        "G3",
        "Generador 3",
        120,
        40,
        0
    )

    generador_4 = Generador(
        "G4",
        "Generador 4",
        60,
        10,
        0
    )

    sistema = SistemaPotencia()

    sistema.agregar_elemento(generador_1)
    sistema.agregar_elemento(generador_2)
    sistema.agregar_elemento(generador_3)
    sistema.agregar_elemento(generador_4)

    print("Generadores ordenados por costo:")

    generadores_ordenados = sistema.ordenar_generadores_por_costo()

    for generador in generadores_ordenados:
        print(
            generador.get_id(),
            generador.get_costo_operativo()
        )

    print("\nDespacho económico:")

    demanda_total = 180

    despacho = sistema.despacho_economico(
        demanda_total
    )

    print(f"Demanda total: {demanda_total} MW")

    for unidad in despacho:
        print(
            unidad["id"],
            "- Costo:",
            unidad["costo"],
            "- Potencia:",
            unidad["potencia"],
            "MW"
        )


if __name__ == "__main__":
    main()