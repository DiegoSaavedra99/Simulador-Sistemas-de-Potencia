from generador import Generador
from sistema_potencia import SistemaPotencia
from nodo import Nodo


def main():
    """
    Prueba de que funciona bien la Tabla Hash y busqueda
    """
    print("\nPrueba de Tabla Hash:")
    print()

    nodo_1 = Nodo(
        "Barra_Quillota",
        "Barra Quillota"
    )

    nodo_2 = Nodo(
        "Barra_Charrua",
        "Barra Charrúa"
    )

    nodo_3 = Nodo(
        "Barra_AltoJahuel",
        "Barra Alto Jahuel"
    )

    sistema_nodos = SistemaPotencia()

    sistema_nodos.agregar_nodo(nodo_1)
    sistema_nodos.agregar_nodo(nodo_2)
    sistema_nodos.agregar_nodo(nodo_3)

    print("Nodos almacenados:")
    sistema_nodos.consultar_nodos()

    print("\nBuscar Barra_Charrua:")

    nodo_buscado = sistema_nodos.buscar_nodo("Barra_Charrua")

    if nodo_buscado is not None:
        print(nodo_buscado.obtener_datos())
    else:
        print("Nodo no encontrado.")


if __name__ == "__main__":
    main()