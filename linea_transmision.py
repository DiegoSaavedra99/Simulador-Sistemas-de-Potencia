from elemento_red import ElementoRed


class LineaTransmision(ElementoRed):
    """
    Clase hija que representa una línea de transmisión.

    También hereda los atributos id y nombre desde ElementoRed.

    Atributos:
        __origen (str): Punto de origen de la línea.
        __destino (str): Punto de destino de la línea.
        __reactancia (float): Reactancia de la línea.
        id_elemento (str): Identificador de la línea.
        nombre (str): Nombre de la línea.
    """

    def __init__(
        self,
        id_elemento,
        nombre,
        origen,
        destino,
        reactancia
    ):
        super().__init__(id_elemento, nombre)

        self.__origen = origen
        self.__destino = destino
        self.__reactancia = 0

        self.set_reactancia(reactancia)

    def get_origen(self):
        """
        Retorna el origen de la línea.

        Returns:
            str: Identificador del punto de origen.
        """
        return self.__origen

    def set_origen(self, nuevo_origen):
        """
        Modifica el origen de la línea.

        Atributos:
            nuevo_origen (str): Nuevo punto de origen.
        """
        self.__origen = nuevo_origen

    def get_destino(self):
        """
        Retorna el destino de la línea.

        Returns:
            str: Identificador del punto de destino.
        """
        return self.__destino

    def set_destino(self, nuevo_destino):
        """
        Modifica el destino de la línea.

        Atributos:
            nuevo_destino (str): Nuevo punto de destino.
        """
        self.__destino = nuevo_destino

    def get_reactancia(self):
        """
        Retorna la reactancia de la línea.

        Returns:
            float: Reactancia de la línea.
        """
        return self.__reactancia

    def set_reactancia(self, nueva_reactancia):
        """
        Modifica la reactancia de la línea.

        Atributo:
            nueva_reactancia (float): Nueva reactancia.
        """
        if nueva_reactancia > 0:
            self.__reactancia = nueva_reactancia
        else:
            print("Error: la reactancia debe ser mayor que cero.")

    def obtener_datos(self):
        """
        Retorna los datos de la línea de transmisión.

        Returns:
            dict: Diccionario con los datos de la línea.
        """
        return {
            "id": self.get_id(),
            "nombre": self.get_nombre(),
            "origen": self.__origen,
            "destino": self.__destino,
            "reactancia": self.__reactancia
        }
