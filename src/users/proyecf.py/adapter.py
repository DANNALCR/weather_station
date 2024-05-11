# Objeto a adaptar
class Adaptee:
    def specific_request(self):
        print("Método específico del Adaptee")

# Interfaz objetivo
class Target:
    def request(self):
        pass

# Adaptador
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

# Cliente
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.request()

// En este ejemplo, la clase
Adaptee representa el objeto que queremos adaptar,
con un método specific_request(). La clase Target define la interfaz que el cliente espera utilizar,
 con un método request(). La clase Adapter implementa la interfaz Target y contiene una instancia de Adaptee.
 Cuando el cliente llama al método request() en el adaptador,
  este reenvía la solicitud al método specific_request() del objeto Adaptee. //