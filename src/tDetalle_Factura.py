"""
La clase Detalle_Factura representa un detalle de la factura, incluyendo el producto,
la cantidad y el precio unitario.

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
class DetalleFactura:
    def __init__(self, producto, cantidad, precio_unitario):
        # recibe un producto, la cantidad y el precio unitario
        self._producto = producto
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio_unitario(self):
        return self._precio_unitario

    def subtotal(self):
        # Calcula el subtotal multiplicando cantidad por precio unitario
        return self._cantidad * self._precio_unitario

if __name__ == "__main__":
    detalle = DetalleFactura("Manzana", 5, 0.5)
    print("Subtotal del detalle:", detalle.subtotal())