from elemento_red import ElementoRed


class Generador(ElementoRed):
    """
    Clase hija que representa un generador eléctrico.

    Hereda los atributos id y nombre desde ElementoRed.

    Atributos:
        __potencia_max (float): Potencia máxima del generador.
        __costo_operativo (float): Costo operativo del generador.
        __potencia_actual (float): Potencia actualmente generada.
        id_elemento (str): Identificador del generador.
        nombre (str): Nombre del generador.
    """

    def __init__(
        self,
        id_elemento,
        nombre,
        potencia_max,
        costo_operativo,
        potencia_actual=0
    ):
        super().__init__(id_elemento, nombre)

        self.__potencia_max = potencia_max
        self.__costo_operativo = costo_operativo
        self.__potencia_actual = 0

        self.set_potencia(potencia_actual)

    def get_potencia_max(self):
        """
        Retorna la potencia máxima del generador.

        Returns:
            float: Potencia máxima.
        """
        return self.__potencia_max

    def set_potencia_max(self, nueva_potencia_max):
        """
        Modifica la potencia máxima del generador.

        Atributos:
            nueva_potencia_max (float): Nueva potencia máxima.
        """
        if nueva_potencia_max >= 0:
            self.__potencia_max = nueva_potencia_max

            if self.__potencia_actual > self.__potencia_max:
                self.__potencia_actual = self.__potencia_max
        else:
            print("Error: la potencia máxima no puede ser negativa.")

    def get_costo_operativo(self):
        """
        Retorna el costo operativo del generador.

        Returns:
            float: Costo operativo.
        """
        return self.__costo_operativo

    def set_costo_operativo(self, nuevo_costo):
        """
        Modifica el costo operativo del generador.

        Atributos:
            nuevo_costo (float): Nuevo costo operativo.
        """
        if nuevo_costo >= 0:
            self.__costo_operativo = nuevo_costo
        else:
            print("Error: el costo operativo no puede ser negativo.")

    def get_potencia(self):
        """
        Retorna la potencia actual del generador.

        Returns:
            float: Potencia actual.
        """
        return self.__potencia_actual

    def set_potencia(self, nueva_potencia):
        """
        Modifica la potencia actual del generador.

        Se verifica que la potencia cumpla la siguiente relación:

        0 <= potencia_actual <= potencia_max

        Atributos:
            nueva_potencia (float): Nueva potencia a asignar.
        """
        if 0 <= nueva_potencia <= self.__potencia_max:
            self.__potencia_actual = nueva_potencia
        else:
            print(
                "Error: la potencia debe estar entre 0 y la potencia máxima."
            )

    def modificar_potencia(self, nueva_potencia):
        """
        Modifica la potencia actual del generador.

        Atributos:
            nueva_potencia (float): Nueva potencia a asignar.
        """
        self.set_potencia(nueva_potencia)

    def obtener_datos(self):
        """
        Retorna los datos del generador.

        Returns:
            dict: Diccionario con los datos del generador.
        """
        return {
            "id": self.get_id(),
            "nombre": self.get_nombre(),
            "potencia_max": self.__potencia_max,
            "potencia_actual": self.__potencia_actual,
            "costo_operativo": self.__costo_operativo
        }
