from elemento_red import ElementoRed


class SistemaPotencia:
    """
    Clase gestora encargada de administrar los elementos de la red.

    Esta clase no hereda de ElementoRed, ya que no representa un componente
    físico de la red; solo administra el conjunto de elementos existentes.
    """

    def __init__(self):
        self.__elementos = []

    def get_elementos(self):
        """
        Retorna la lista de elementos del sistema.

        Returns:
            list: Lista de elementos de la red.
        """
        return self.__elementos

    def agregar_elemento(self, elemento):
        """
        Agrega un elemento al sistema de potencia.

        Atributos:
            elemento (ElementoRed): Elemento que se desea incorporar al sistema.
        """
        if isinstance(elemento, ElementoRed):
            self.__elementos.append(elemento)
        else:
            print("Error: el objeto debe pertenecer a ElementoRed.")

    def consultar_elementos(self):
        """
        Muestra los elementos almacenados en el sistema de potencia.
        """
        for elemento in self.__elementos:
            print(elemento.obtener_datos())
