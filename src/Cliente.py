"""
La clase Cliente es nuestra subclase que hereda de la superclase Persona, donde
agregaremos atributos y metodos para los clientes y ventas.

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
from src.APersona import Persona

class Cliente(Persona):
    def __init__(self, nombre, cedula, email, tipo_cliente="Minorista"):
        super().__init__(nombre, cedula, email) # Se llama a la superclase Persona
        self._tipo_cliente = tipo_cliente

    # Getter y Setter para el tipo de cliente
    @property
    def tipo_cliente(self):
        return self._tipo_cliente

    @tipo_cliente.setter
    def tipo_cliente(self, tipo):
        self._tipo_cliente = tipo

    """Este metodo debe generar una factura dependiendo del tipo de cliente:"""
    def generar_factura(self, productos, cantidades):
        if self._tipo_cliente == "Minorista":
            #Implementación para clientes minoristas
            pass
        elif self._tipo_cliente == "Mayorista":
            #Implementación para clientes mayoristas
            pass

if __name__ == "__main__":
    cliente = Cliente("Natalia", "0987654321", "natalia@mail.com")
    print("Cliente:", cliente.nombre, cliente.tipo_cliente)
    cliente.tipo_cliente = "Mayorista"
    print("Nuevo tipo de cliente:", cliente.tipo_cliente)
