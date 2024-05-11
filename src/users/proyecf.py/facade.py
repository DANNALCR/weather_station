# Subsistema 1
class Subsystem1:
    def operation1(self):
        print("Subsystem1: Operation1")

    def operation2(self):
        print("Subsystem1: Operation2")

# Subsistema 2
class Subsystem2:
    def operation1(self):
        print("Subsystem2: Operation1")

    def operation2(self):
        print("Subsystem2: Operation2")

# Fachada
class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem1.operation2()
        self._subsystem2.operation1()
        self._subsystem2.operation2()

# Cliente
if __name__ == "__main__":
    facade = Facade()
    facade.operation()




//Subsystem1 y Subsystem2 son dos subsistemas con funcionalidades complejas.
Facade proporciona una interfaz simple que utiliza estos subsistemas para realizar una serie de operaciones.
El cliente interactúa solo con la fachada y no necesita conocer los detalles de implementación de los subsistemas.
Este patrón es útil cuando tienes un sistema complejo y deseas proporcionar una interfaz simplificada para interactuar
con él, ocultando la complejidad interna.//