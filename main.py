from src.APersona import Persona
from src.Cliente import Cliente
from src.Empleado import Empleado
from src.Producto import Producto
from src.rFactura import Factura
from src.tDetalle_Factura import DetalleFactura

def main():
    print(" Prueba del sistema de gestión de clientes y ventas \n")

    # Crea una Persona
    persona = Persona("Sebas", "1234567890", "sebas@mail.com")
    print("Persona:", persona.nombre, persona.cedula, persona.email)

    # Crea un Cliente
    cliente = Cliente("Natalia", "0987654321", "natalia@mail.com", "Mayorista")
    print("Cliente:", cliente.nombre, cliente.tipo_cliente)

    # Crea un Empleado
    empleado = Empleado("Jeremy", "1122334455", "Jeremy@mail.com", "Ventas")
    print("Empleado:", empleado.nombre, empleado.departamento)

    # Crea un Producto
    producto1 = Producto("A01", "Pera", 0.5, 100)
    producto2 = Producto("B02", "Mora", 0.3, 50)
    print("Producto 1:", producto1.nombre, "Stock:", producto1.stock)

    # Crea detalles de factura
    detalle1 = DetalleFactura(producto1, 5, producto1.precio)
    detalle2 = DetalleFactura(producto2, 10, producto2.precio)

    # Crea una factura y agrega detalles
    factura = Factura("F001", "2025-05-23", cliente)
    factura.agregar_detalle(detalle1)
    factura.agregar_detalle(detalle2)
    print("\nFactura creada para:", factura.cliente.nombre)
    print("Total de factura:", factura.calcular_total())

if __name__ == "__main__":
    main()