class ElementoRed:
    """
    Clase padre que representa un elemento genérico de la red eléctrica.

    Atributos:
        id_elemento (str): Identificador único del elemento.
        nombre (str): Nombre descriptivo del elemento.
    """

    def __init__(self, id_elemento, nombre):
        self.__id = id_elemento
        self.__nombre = nombre

    def get_id(self):
        """
        Retorna el identificador del elemento.

        Returns:
            str: Identificador del elemento.
        """
        return self.__id

    def set_id(self, nuevo_id):
        """
        Modifica el identificador del elemento.

        Atributos:
            nuevo_id (str): Nuevo identificador del elemento.
        """
        self.__id = nuevo_id

    def get_nombre(self):
        """
        Retorna el nombre del elemento.

        Returns:
            str: Nombre del elemento.
        """
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        """
        Modifica el nombre del elemento.

        Atributos:
            nuevo_nombre (str): Nuevo nombre del elemento.
        """
        self.__nombre = nuevo_nombre

    def obtener_datos(self):
        """
        Retorna los datos básicos del elemento.

        Returns:
            dict: Diccionario con id y nombre.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre
        }
