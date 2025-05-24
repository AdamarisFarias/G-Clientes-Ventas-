"""
La clase Persona es nuestra superclase, donde definiremos atributos
   y metodos a todas las personas en el sistema Gestión de clientes y ventas

Miembros del grupo: Farias Moya Adamaris
                    Chuisaca Villacis Milena
                    Moncayo Ríos Niurka
                    González Rodriguez Angie
                    Aquilar Preciado Anthony
                    """
class Persona:
    def __init__(self, nombre, cedula, email):
        self._nombre = nombre
        self._cedula = cedula
        self._email = email

    # Getter y Setter del nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    # Getter y Setter de la cédula
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        self._cedula = valor

    # Getter y Setter del email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

if __name__ == "__main__":
    persona = Persona("Sebas", "1234567890", "sebas@mail.com")
    print("Nombre:", persona.nombre)
    print("Cédula:", persona.cedula)
    print("Email:", persona.email)