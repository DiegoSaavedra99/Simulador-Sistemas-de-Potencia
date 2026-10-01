from elemento_red import ElementoRed


class Carga(ElementoRed):
    """
    Clase hija que representa una carga eléctrica.

    Hereda los atributos id y nombre desde ElementoRed.

    Atributos:
        __demanda (float): Demanda eléctrica de la carga.
        id_elemento (str): Identificador de la carga.
        nombre (str): Nombre de la carga.
    """

    def __init__(self, id_elemento, nombre, demanda):
        super().__init__(id_elemento, nombre)

        self.__demanda = 0
        self.set_demanda(demanda)

    def get_demanda(self):
        """
        Retorna la demanda de la carga.

        Returns:
            float: Demanda eléctrica.
        """
        return self.__demanda

    def set_demanda(self, nueva_demanda):
        """
        Modifica la demanda de la carga.

        Atributos:
            nueva_demanda (float): Nueva demanda eléctrica.
        """
        if nueva_demanda >= 0:
            self.__demanda = nueva_demanda
        else:
            print("Error: la demanda no puede ser negativa.")

    def obtener_demanda(self):
        """
        Retorna la demanda actual de la carga.

        Returns:
            float: Demanda eléctrica.
        """
        return self.__demanda

    def obtener_datos(self):
        """
        Retorna los datos de la carga.

        Returns:
            dict: Diccionario con los datos de la carga.
        """
        return {
            "id": self.get_id(),
            "nombre": self.get_nombre(),
            "demanda": self.__demanda
        }
