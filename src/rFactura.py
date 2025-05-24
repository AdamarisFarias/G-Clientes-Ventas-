"""
La clase Factura representa una factura generada en el sistema de gestión de clientes y ventas.
Contiene información sobre el cliente, los detalles de la factura y otros datos.

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
class Factura:
    def __init__(self, numero, fecha, cliente):
        # inicializa el número de factura, fecha y cliente
        self._numero = numero
        self._fecha = fecha
        self._cliente = cliente
        self._detalles = [] # Lista para almacenar los detalles de la factura

    @property
    def numero(self):
        return self._numero

    @property
    def fecha(self):
        return self._fecha

    @property
    def cliente(self):
        return self._cliente

    @property
    def detalles(self):
        return self._detalles

    def agregar_detalle(self, detalle):
        self._detalles.append(detalle)

    def calcular_total(self):
        # Calcula el total de la factura sumando los subtotales de cada detalle
        return sum(detalle.subtotal() for detalle in self._detalles)

if __name__ == "__main__":
    class DetallePrueba:
        def subtotal(self):
            return 10

    factura = Factura("F001", "2025-05-23", "Cliente Prueba")
    factura.agregar_detalle(DetallePrueba())
    factura.agregar_detalle(DetallePrueba())
    print("Total de factura:", factura.calcular_total())