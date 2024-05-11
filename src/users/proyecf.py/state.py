# Estado
class State:
    def go(self):
        pass

# Estados concretos
class GreenState(State):
    def go(self):
        return "Avanzar"

class YellowState(State):
    def go(self):
        return "Prepararse para detenerse"

class RedState(State):
    def go(self):
        return "Detenerse"

# Contexto
class TrafficLight:
    def __init__(self):
        self._state = GreenState()

    def change_state(self, state):
        self._state = state

    def request(self):
        return self._state.go()

# Cliente
if __name__ == "__main__":
    traffic_light = TrafficLight()

    print("Estado actual:", traffic_light.request())

    # Cambiar a estado amarillo
    traffic_light.change_state(YellowState())
    print("Estado actual:", traffic_light.request())

    # Cambiar a estado rojo
    traffic_light.change_state(RedState())
    print("Estado actual:", traffic_light.request())



#State define una interfaz para todos los estados posibles del semáforo.
#GreenState, YellowState y RedState son clases que implementan comportamientos específicos para cada estado.
#TrafficLight es el contexto que contiene un estado interno y proporciona una interfaz para cambiar ese estado.
#El cliente crea una instancia de TrafficLight y solicita el estado actual. Luego, cambia el estado del semáforo
#y solicita el nuevo estado.
#Este ejemplo muestra cómo el patrón State se puede aplicar para modelar el comportamiento de un semáforo de tráfico,
#donde el semáforo cambia su estado en respuesta a eventos externos.//