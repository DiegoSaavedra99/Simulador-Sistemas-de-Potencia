from elemento_red import ElementoRed


class Nodo(ElementoRed):
    """
    Clase que representa un nodo o barra del sistema eléctrico.

    Hereda los atributos id y nombre desde ElementoRed.

    Atributos:
        id_elemento (str): Identificador único del nodo.
        nombre (str): Nombre descriptivo del nodo.
    """

    def __init__(self, id_elemento, nombre):
        super().__init__(id_elemento, nombre)