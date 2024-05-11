# Observador
class Observer:
    def update(self, news):
        pass

# Sujeto
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, news):
        for observer in self._observers:
            observer.update(news)

# Cliente
if __name__ == "__main__":
    # Definir observadores (suscriptores)
    class EmailSubscriber(Observer):
        def update(self, news):
            print("Enviando correo electrónico con noticias:", news)

    class SMSSubscriber(Observer):
        def update(self, news):
            print("Enviando SMS con noticias:", news)

    # Definir el sujeto (servicio de noticias)
    class NewsService(Subject):
        def publish_news(self, news):
            print("Publicando nuevas noticias:", news)
            self.notify(news)

    # Crear instancias de observadores
    email_subscriber = EmailSubscriber()
    sms_subscriber = SMSSubscriber()

    # Crear instancia de sujeto (servicio de noticias)
    news_service = NewsService()

    # Adjuntar observadores al sujeto
    news_service.attach(email_subscriber)
    news_service.attach(sms_subscriber)

    # Publicar noticias
    news_service.publish_news("¡Nuevas noticias disponibles!")

    # Resultado: Ambos observadores (suscriptores) son notificados y actualizados automáticamente




// Observer define una interfaz para los objetos que deben ser notificados de cambios en el sujeto.
Subject es el objeto que está siendo observado. Mantiene una lista de observadores y notifica a los observadores cuando ocurren cambios.
EmailSubscriber y SMSSubscriber son clases que implementan el comportamiento específico de los observadores.
NewsService es el sujeto concreto que publica noticias. Cuando se publican nuevas noticias, notificaautomáticamente a todos sus observadores.
Este ejemplo muestra cómo el patrón Observer se puede aplicar a un servicio de noticias por correo electrónico,
donde los usuarios se suscriben para recibir actualizaciones automáticas cuando se publican nuevas noticias.//