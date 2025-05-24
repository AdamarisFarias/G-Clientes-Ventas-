"""
La clase Producto define los atributos y métodos relacionados con los productos
que se manejan en el sistema de gestión de clientes y ventas.

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        # inicializa los datos del producto
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    # Propiedades para acceder a los atributos de forma controlada
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0: # Solo permite precios positivos o cero
            self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, cantidad):
        if cantidad >= 0: # Solo permite cantidades positivas o cero
            self._stock = cantidad

    def reducir_stock(self, cantidad):
        # Reduce el stock si la cantidad es válida
        if cantidad <= self._stock:
            self._stock -= cantidad

if __name__ == "__main__":
    producto = Producto("A01", "Pera", 0.50, 100)
    print("Producto:", producto.nombre, "Precio:", producto.precio, "Stock:", producto.stock)
    producto.reducir_stock(10)
    print("Stock después de venta:", producto.stock)