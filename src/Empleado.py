"""
La clase Empleado es nuestra subclase que hereda de la superclase Persona, donde
agregaremos atributos y metodos para los empleados.

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
from src.APersona import Persona

class Empleado(Persona):
    def __init__(self, nombre, cedula, email, departamento):
        super().__init__(nombre, cedula, email)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, valor):
        self._departamento = valor

    def generar_factura(self, productos, cantidades):
        #Implementación del metodo generar_factura() para empleados."""
        pass

if __name__ == "__main__":
    empleado = Empleado("Jeremy", "1122334455", "Jeremy@mail.com", "Ventas")
    print("Empleado:", empleado.nombre, "Departamento:", empleado.departamento)
    empleado.departamento = "Contabilidad"
    print("Nuevo departamento:", empleado.departamento)