# Componente base
class Component:
    def __init__(self, name):
        self.name = name

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, indent=0):
        pass

# Hoja
class Person(Component):
    def display(self, indent=0):
        print("  " * indent + f"- {self.name}")

# Composite
class Group(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print("  " * indent + f"+ {self.name}")
        for child in self.children:
            child.display(indent + 1)

# Cliente
if __name__ == "__main__":
    # Crear personas
    person1 = Person("Alice")
    person2 = Person("Bob")
    person3 = Person("Charlie")

    # Crear grupos
    group1 = Group("Familia")
    group1.add(person1)
    group1.add(person2)

    group2 = Group("Amigos")
    group2.add(person3)

    # Crear un grupo principal
    main_group = Group("Picnic en el parque")
    main_group.add(group1)
    main_group.add(group2)

    # Mostrar la estructura
    main_group.display()



#Component define la interfaz común para todos los componentes, ya sean hojas individuales (en este caso, personas)
#o grupos que contienen más personas o grupos.
#Person representa una hoja individual en la estructura. En este caso, una persona que asiste al picnic.
#Group es el componente compuesto que puede contener tanto personas individuales como otros grupos.
#El cliente crea instancias de personas y grupos, y los organiza en una estructura jerárquica. Luego,
 #muestra la estructura completa, que incluye tanto personas individuales como grupos anidados.
#Este ejemplo ilustra cómo el patrón Composite puede ser útil para modelar estructuras jerárquicas,
#como los participantes en un evento comunitario, donde hay grupos que contienen tanto a personas individuales
#como a otros grupos. 
