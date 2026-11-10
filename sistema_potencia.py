from elemento_red import ElementoRed
from generador import Generador


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

    def obtener_generadores(self):
        """
          Retorna únicamente los generadores almacenados en el sistema.

          Returns:
              list: Lista de objetos Generador.
         """
        generadores = []

        for elemento in self.__elementos:
            if isinstance(elemento, Generador):
                generadores.append(elemento)

        return generadores


    def ordenar_generadores_por_costo(self):
        """
        Ordena los generadores desde el menor al mayor costo operativo
        utilizando Merge Sort.

        Returns:
            list: Lista de generadores ordenados por costo operativo.
        """
        generadores = self.obtener_generadores()

        return self.__merge_sort_generadores(generadores)


    def __merge_sort_generadores(self, generadores):
        """
        Divide recursivamente la lista de generadores y posteriormente
        fusiona las partes de manera ordenada.

        Atributos:
            generadores (list): Lista de objetos Generador.

        Returns:
            list: Lista de generadores ordenada por costo operativo.
        """

        if len(generadores) <= 1:
            return generadores

        mitad = len(generadores) // 2

        izquierda = self.__merge_sort_generadores(generadores[:mitad])

        derecha = self.__merge_sort_generadores(generadores[mitad:])

        return self.__mezclar_generadores(izquierda,derecha)


    def __mezclar_generadores(self, izquierda, derecha):
        """
        Fusiona dos listas previamente ordenadas comparando
        el costo operativo de cada generador.

        Atributos:
            izquierda (list): Primera lista ordenada.
            derecha (list): Segunda lista ordenada.

        Returns:
            list: Lista fusionada y ordenada.
        """

        resultado = []

        i = 0
        j = 0

        while i < len(izquierda) and j < len(derecha):

            if (izquierda[i].get_costo_operativo()<= derecha[j].get_costo_operativo()):
                resultado.append(izquierda[i])
                i += 1

            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    def despacho_economico(self, demanda_total):
        """
        Realiza un despacho económico de energía.

        Los generadores se ordenan desde el menor al mayor costo
        operativo y se utilizan en ese orden hasta satisfacer
        la demanda total.

        Atributos:
            demanda_total (float): Demanda total que debe abastecerse.

        Returns:
            list: Lista con los generadores despachados y la potencia
            asignada a cada uno.
        """

        if demanda_total < 0:
            print("Error: la demanda no puede ser negativa.")
            return []

        generadores_ordenados = self.ordenar_generadores_por_costo()

        demanda_pendiente = demanda_total
        despacho = []

        # Reiniciar potencia de todos los generadores
        for generador in generadores_ordenados:
            generador.set_potencia(0)

        # Realizar el despacho (se parte por el mas barato segun Merge Sort)
        for generador in generadores_ordenados:

            if demanda_pendiente <= 0:
                break

            potencia_disponible = generador.get_potencia_max()
            """
            # aqui es importante porque si el generador entrega menos de lo que 
            necestiamos,se ocupa toda la potencia del generador 
            y si entraga mas de lo que necesitamos, solo entrega lo necesario
            para cumplir la demanda.
            """     
            if demanda_pendiente >= potencia_disponible:
                potencia_asignada = potencia_disponible

            else:
                potencia_asignada = demanda_pendiente

            generador.set_potencia(potencia_asignada)

            #Se guarda el resultado
            despacho.append(
                {
                    "id": generador.get_id(),
                    "costo": generador.get_costo_operativo(),
                    "potencia": potencia_asignada
                })
            # Y se actualiza la demanda pendiente.
            demanda_pendiente -= potencia_asignada

        if demanda_pendiente > 0:
            print(
                "Advertencia: la capacidad de generación no es "
                "suficiente para cubrir toda la demanda."
            )

        return despacho
